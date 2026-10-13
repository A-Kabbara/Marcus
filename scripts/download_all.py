"""Download audio-only for all videos in videos.json via yt-dlp.

Resumable: uses a download archive + skips existing files. Writes
audio/.done_downloading when finished and logs/download_status.json throughout.
"""
import json
import subprocess
import sys
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
AUDIO = BASE / "audio"
LOGS = BASE / "logs"
AUDIO.mkdir(exist_ok=True)
LOGS.mkdir(exist_ok=True)

videos = json.loads((BASE / "videos.json").read_text(encoding="utf-8"))
status_path = LOGS / "download_status.json"
status = {"ok": [], "failed": [], "total": len(videos)}
if status_path.exists():
    status = json.loads(status_path.read_text(encoding="utf-8"))


def save_status():
    status_path.write_text(json.dumps(status, indent=2), encoding="utf-8")


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOGS / "download.log", "a", encoding="utf-8") as f:
        f.write(line + "\n")


for v in videos:
    idx, url, title = v["index"], v["url"], v["title"]
    vid = url.split("v=")[-1]
    existing = list(AUDIO.glob(f"{idx:03d}_*.m4a")) + list(AUDIO.glob(f"{idx:03d}_*.webm")) + list(AUDIO.glob(f"{idx:03d}_*.opus")) + list(AUDIO.glob(f"{idx:03d}_*.mp3"))
    if existing or vid in status["ok"]:
        if vid not in status["ok"]:
            status["ok"].append(vid)
            save_status()
        continue
    log(f"[{idx}/{len(videos)}] downloading: {title[:60]}")
    attempts = 0
    while attempts < 3:
        attempts += 1
        r = subprocess.run(
            [
                sys.executable, "-m", "yt_dlp",
                "-f", "bestaudio[ext=m4a]/bestaudio",
                "-o", str(AUDIO / f"{idx:03d}_{vid}.%(ext)s"),
                "--no-playlist",
                "--retries", "10",
                "--fragment-retries", "10",
                "--sleep-requests", "1",
                "--no-progress",
                url,
            ],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        if r.returncode == 0:
            status["ok"].append(vid)
            if vid in status["failed"]:
                status["failed"].remove(vid)
            save_status()
            log(f"[{idx}] OK")
            break
        log(f"[{idx}] attempt {attempts} failed: {(r.stderr or '')[-300:]}")
        time.sleep(20 * attempts)
    else:
        if vid not in status["failed"]:
            status["failed"].append(vid)
        save_status()
    time.sleep(4)  # be polite between videos

(AUDIO / ".done_downloading").write_text("done", encoding="utf-8")
log(f"DONE. ok={len(status['ok'])} failed={len(status['failed'])}")
