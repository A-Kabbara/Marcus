"""Extract text from the foundational .docx files in the Ads folder -> foundational-docs/*.txt"""
import re
import zipfile
from pathlib import Path

ADS = Path(r"C:\N8N\Agency\Vanguard Digital\Ads")
OUT = ADS / "Markus URL" / "foundational-docs"
OUT.mkdir(exist_ok=True)


def docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml").decode("utf-8")
    xml = xml.replace("</w:p>", "\n").replace("<w:tab/>", "\t").replace("<w:br/>", "\n")
    text = re.sub(r"<[^>]+>", "", xml)
    for ent, ch in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&apos;", "'")):
        text = text.replace(ent, ch)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


for docx in ADS.glob("*.docx"):
    out = OUT / (docx.stem + ".txt")
    try:
        out.write_text(docx_text(docx), encoding="utf-8")
        print(f"OK  {docx.name} -> {out.name} ({out.stat().st_size} bytes)")
    except Exception as e:
        print(f"ERR {docx.name}: {e}")
