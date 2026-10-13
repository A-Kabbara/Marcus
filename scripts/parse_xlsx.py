"""Parse 'Mark Builds Brands - YouTube Videos.xlsx' -> videos.json (no external deps)."""
import json
import re
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
XLSX = BASE / "Mark Builds Brands - YouTube Videos.xlsx"
OUT = BASE / "videos.json"


def col_letters(ref: str) -> str:
    return re.match(r"([A-Z]+)", ref).group(1)


def main():
    with zipfile.ZipFile(XLSX) as z:
        shared = re.findall(
            r"<si>(?:<t[^>]*>)?(.*?)(?:</t>)?</si>",
            z.read("xl/sharedStrings.xml").decode("utf-8"),
            re.S,
        )
        # unescape basic XML entities
        def unesc(s):
            return (
                s.replace("&amp;", "&")
                .replace("&lt;", "<")
                .replace("&gt;", ">")
                .replace("&quot;", '"')
                .replace("&apos;", "'")
            )

        shared = [unesc(re.sub(r"<[^>]+>", "", s)) for s in shared]
        sheet = z.read("xl/worksheets/sheet1.xml").decode("utf-8")

    videos = []
    for row_xml in re.findall(r"<row[^>]*>(.*?)</row>", sheet, re.S):
        cells = {}
        for ref, ctype, val in re.findall(
            r'<c r="([A-Z]+\d+)"(?:[^>]*t="([^"]*)")?[^>]*>(?:<v>(.*?)</v>)?', row_xml
        ):
            if val == "":
                continue
            text = shared[int(val)] if ctype == "s" else val
            cells[col_letters(ref)] = text
        title, url = cells.get("A", ""), cells.get("B", "")
        if url.startswith("http"):
            videos.append({"index": len(videos) + 1, "title": title, "url": url})

    OUT.write_text(json.dumps(videos, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(videos)} videos to {OUT}")


if __name__ == "__main__":
    main()
