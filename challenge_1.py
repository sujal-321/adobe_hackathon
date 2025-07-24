import fitz  # PyMuPDF
import json
import os
from pathlib import Path

def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = ""
    max_font_size = 0

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    text = span["text"].strip()
                    size = span["size"]
                    if not text or len(text) < 2:
                        continue
                    if size > max_font_size:
                        max_font_size = size
                        title = text
                    level = None
                    if size >= 18:
                        level = "H1"
                    elif size >= 14:
                        level = "H2"
                    elif size >= 12:
                        level = "H3"
                    if level:
                        outline.append({
                            "level": level,
                            "text": text,
                            "page": page_num
                        })
    return {"title": title, "outline": outline}

def main():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    os.makedirs(output_dir, exist_ok=True)

    for pdf_file in input_dir.glob("*.pdf"):
        output = extract_outline_from_pdf(pdf_file)
        output_file = output_dir / f"{pdf_file.stem}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
