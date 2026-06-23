import os
import json
from pypdf import PdfReader

def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

files_to_read = [
    "CÂU HỎI ÔN TẬP CHƯƠNG 1.pdf",
    "2.1. Kiến trúc ống và lọc.pdf",
    "dethithu.docx" # I want to read all of dethithu to see if it has answers
]

data = {}
for f in files_to_read:
    print(f"Reading {f}...")
    try:
        if f.endswith('.pdf'):
            text = read_pdf(f)
            data[f] = text[:2000] # First 2000 chars for pdf preview
        elif f.endswith('.docx'):
            import docx
            doc = docx.Document(f)
            full_text = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
            data[f] = "\n".join(full_text) # all text for dethithu
    except Exception as e:
        print(f"Failed to read {f}: {e}")

with open("extracted_pdf_preview.json", "w", encoding="utf-8") as out_f:
    json.dump(data, out_f, ensure_ascii=False, indent=2)
print("Saved preview to extracted_pdf_preview.json")
