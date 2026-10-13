"""Transcribe downloaded audio with faster-whisper (GPU) as files appear.

Runs until audio/.done_downloading exists AND every audio file is transcribed.
Resumable: skips audio files that already have a transcript.
"""
import json
import re
import site
import sys
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
AUDIO = BASE / "audio"
OUT = BASE / "transcripts"
LOGS = BASE / "logs"
OUT.mkdir(exist_ok=True)
LOGS.mkdir(exist_ok=True)

# Make pip-installed cuBLAS/cuDNN DLLs findable by ctranslate2
import os
for sp in site.getsitepackages():
    for sub in ("nvidia/cublas/bin", "nvidia/cudnn/bin"):
        p = Path(sp) / sub
        if p.is_dir():
            os.add_dll_directory(str(p))
            os.environ["PATH"] = str(p) + os.pathsep + os.environ["PATH"]

from faster_whisper import WhisperModel  # noqa: E402

videos = {v["index"]: v for v in json.loads((BASE / "videos.json").read_text(encoding="utf-8"))}


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOGS / "transcribe.log", "a", encoding="utf-8") as f:
        f.write(line + "\n")


def load_model():
    for device, ctype in (("cuda", "float16"), ("cuda", "int8_float16"), ("cpu", "int8")):
        try:
            m = WhisperModel("large-v3", device=device, compute_type=ctype)
            log(f"model loaded: large-v3 on {device}/{ctype}")
            return m
        except Exception as e:
            log(f"load failed on {device}/{ctype}: {e}")
    raise RuntimeError("could not load whisper model on any backend")


def safe_name(s, maxlen=70):
    s = re.sub(r'[<>:"/\\|?*\n\r]+', "", s).strip()
    return s[:maxlen].rstrip(" .")


model = load_model()
done_flag = AUDIO / ".done_downloading"
processed = set()

while True:
    audio_files = sorted(
        f for f in AUDIO.iterdir()
        if f.suffix.lower() in (".m4a", ".webm", ".opus", ".mp3") and f.name not in processed
    )
    worked = False
    for f in audio_files:
        idx = int(f.name.split("_")[0])
        v = videos.get(idx, {"title": f.stem, "url": ""})
        out_path = OUT / f"{idx:03d} - {safe_name(v['title'])}.txt"
        if out_path.exists() and out_path.stat().st_size > 0:
            processed.add(f.name)
            continue
        worked = True
        log(f"transcribing [{idx}] {v['title'][:60]}")
        t0 = time.time()
        try:
            segments, info = model.transcribe(str(f), vad_filter=True, beam_size=5, language="en")
            texts = [seg.text.strip() for seg in segments]
        except Exception as e:
            log(f"[{idx}] FAILED: {e}")
            processed.add(f.name)
            continue
        body = "\n".join(texts)
        header = f"TITLE: {v['title']}\nURL: {v['url']}\nDURATION: {getattr(info, 'duration', 0):.0f}s\n{'=' * 60}\n\n"
        out_path.write_text(header + body, encoding="utf-8")
        processed.add(f.name)
        log(f"[{idx}] done in {time.time() - t0:.0f}s ({getattr(info, 'duration', 0):.0f}s audio)")

    if done_flag.exists() and not worked:
        remaining = [
            f for f in AUDIO.iterdir()
            if f.suffix.lower() in (".m4a", ".webm", ".opus", ".mp3") and f.name not in processed
        ]
        if not remaining:
            break
    if not worked:
        time.sleep(30)

(OUT / ".done_transcribing").write_text("done", encoding="utf-8")
n = len(list(OUT.glob("*.txt")))
log(f"ALL DONE. {n} transcripts written.")
