import os
import json
import docx

def read_docx(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        if para.text.strip():
            full_text.append(para.text.strip())
    return "\n".join(full_text)

files_to_read = [
    "dethithu.docx",
    "Dap_an_Trac_nghiem_Chuong3_P1.docx",
    "Dap_an_Trac_nghiem_Chuong3_P2.docx",
    "Dap_an_Trac_nghiem_Chuong4_Thiet_ke_mau (1).docx",
    "Dap_an_Kien_truc_Goi_va_Tra_loi.docx",
    "Dap_an_Kien_truc_Huong_dich_vu_Updated.docx",
    "Dap_an_Kien_truc_Huong_doi_tuong.docx",
    "Dap_an_Kien_truc_Huong_su_kien.docx",
    "Dap_an_Kien_truc_Ong_va_Loc.docx",
    "Dap_an_Kien_truc_Phan_lop.docx",
    "Dap_an_On_tap_Kien_truc_Phan_mem.docx"
]

data = {}
for f in files_to_read:
    print(f"Reading {f}...")
    try:
        text = read_docx(f)
        data[f] = text[:1000] # Just first 1000 chars for inspection
    except Exception as e:
        print(f"Failed to read {f}: {e}")

with open("extracted_preview.json", "w", encoding="utf-8") as out_f:
    json.dump(data, out_f, ensure_ascii=False, indent=2)
print("Saved preview to extracted_preview.json")
