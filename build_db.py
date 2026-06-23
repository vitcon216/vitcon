import os
import re
import json
import docx
from pypdf import PdfReader

# Mapping from chapters/topics to their question PDFs and answer DOCXs
mapping = [
    {
        "chapter": 1,
        "topic": "Tổng quan Kiến trúc phần mềm",
        "pdf": "CÂU HỎI ÔN TẬP CHƯƠNG 1.pdf",
        "docx": "Dap_an_On_tap_Kien_truc_Phan_mem.docx"
    },
    {
        "chapter": 2,
        "topic": "Kiến trúc ống và lọc",
        "pdf": "2.1. Kiến trúc ống và lọc.pdf",
        "docx": "Dap_an_Kien_truc_Ong_va_Loc.docx"
    },
    {
        "chapter": 2,
        "topic": "Kiến trúc hướng sự kiện",
        "pdf": "2.2. Kiến trúc hướng sự kiện.pdf",
        "docx": "Dap_an_Kien_truc_Huong_su_kien.docx"
    },
    {
        "chapter": 2,
        "topic": "Kiến trúc phân lớp",
        "pdf": "2.3. Kiến trúc phân lớp.pdf",
        "docx": "Dap_an_Kien_truc_Phan_lop.docx"
    },
    {
        "chapter": 2,
        "topic": "Kiến trúc gọi và trả lời",
        "pdf": "2.4. Kiến trúc gọi và trả lời.pdf",
        "docx": "Dap_an_Kien_truc_Goi_va_Tra_loi.docx"
    },
    {
        "chapter": 2,
        "topic": "Kiến trúc hướng đối tượng",
        "pdf": "2.5. Kiến trúc hướng đối tượng.pdf",
        "docx": "Dap_an_Kien_truc_Huong_doi_tuong.docx"
    },
    {
        "chapter": 2,
        "topic": "Kiến trúc hướng dịch vụ",
        "pdf": "2.6. Kiến trúc hướng dịch vụ.pdf",
        "docx": "Dap_an_Kien_truc_Huong_dich_vu_Updated.docx"
    },
    {
        "chapter": 3,
        "topic": "Thiết kế kiến trúc phần mềm P1",
        "pdf": "Chương 3_P1_Thiết kế kiến trúc phần mềm.pdf",
        "docx": "Dap_an_Trac_nghiem_Chuong3_P1.docx"
    },
    {
        "chapter": 3,
        "topic": "Thiết kế kiến trúc phần mềm P2",
        "pdf": "Chương 3_P2_Thiết kế kiến trúc phần mềm.pdf",
        "docx": "Dap_an_Trac_nghiem_Chuong3_P2.docx"
    },
    {
        "chapter": 4,
        "topic": "Thiết kế mẫu",
        "pdf": "Chương 4_Thiết kế mẫu.pdf",
        "docx": "Dap_an_Trac_nghiem_Chuong4_Thiet_ke_mau (1).docx"
    }
]

def read_pdf_text(file_path):
    try:
        reader = PdfReader(file_path)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        # normalize spaces
        text = text.replace('\r\n', '\n')
        # sometimes lines break in the middle of a sentence in PDF, we try to merge them carefully later
        return text
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def read_docx_lines(file_path):
    try:
        doc = docx.Document(file_path)
        return [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

def parse_questions_from_text(text):
    # Regex to find questions like "1. What is... \n A. ... \n B. ... \n C. ... \n D. ..."
    # This might be tricky because of newlines in middle of text.
    # Let's split by regex matching question number
    question_pattern = re.compile(r'(?m)^(\d+)\.\s+(.*?)(?=(?:\n\d+\.\s+)|\Z)', re.DOTALL)
    
    questions = []
    matches = question_pattern.findall(text)
    for match in matches:
        q_num = match[0]
        q_body = match[1]
        
        # Now find options A, B, C, D
        # Option pattern
        option_pattern = re.compile(r'(?m)^([A-D])\.\s+(.*?)(?=(?:\n[A-D]\.\s+)|\Z)', re.DOTALL)
        options_matches = option_pattern.findall(q_body)
        
        if not options_matches:
            # Let's try splitting by A., B., C., D. inline if they are not at the start of a line
            option_pattern_inline = re.compile(r'([A-D])\.\s+(.*?)(?=(?:[A-D]\.\s+)|\Z)', re.DOTALL)
            # We need to find the start of A.
            a_idx = q_body.find('A. ')
            if a_idx != -1:
                q_text = q_body[:a_idx].strip()
                opts_text = q_body[a_idx:]
                options_matches = option_pattern_inline.findall(opts_text)
            else:
                q_text = q_body.strip()
        else:
            # Question text is before the first option
            first_opt_idx = q_body.find(f'{options_matches[0][0]}. ')
            if first_opt_idx != -1:
                q_text = q_body[:first_opt_idx].strip()
            else:
                q_text = q_body.split('\nA.')[0].strip()
                
        # Clean up newlines in question text and options
        q_text = q_text.replace('\n', ' ').strip()
        q_text = re.sub(r'\s+', ' ', q_text)
        
        options = []
        for opt_label, opt_text in options_matches:
            opt_text = opt_text.replace('\n', ' ').strip()
            opt_text = re.sub(r'\s+', ' ', opt_text)
            options.append(f"{opt_label}. {opt_text}")
            
        if len(options) > 0:
            questions.append({
                "q_num": q_num,
                "question": q_text,
                "options": options
            })
            
    return questions

def parse_answers_from_lines(lines):
    answers = {}
    ans_pattern = re.compile(r'^(\d+)\.\s+([A-D])\s*\((.*?)\)')
    ans_pattern2 = re.compile(r'^(\d+)\.\s+([A-D])\s*-(.*)')
    for line in lines:
        match = ans_pattern.search(line)
        if match:
            q_num = match.group(1)
            ans = match.group(2)
            exp = match.group(3).strip()
            answers[q_num] = {"correctAnswer": ans, "explanation": exp}
        else:
            match2 = ans_pattern2.search(line)
            if match2:
                q_num = match2.group(1)
                ans = match2.group(2)
                exp = match2.group(3).strip()
                answers[q_num] = {"correctAnswer": ans, "explanation": exp}
            else:
                # Some answers might just be "1. B"
                basic_pattern = re.compile(r'^(\d+)\.\s+([A-D])$')
                match3 = basic_pattern.search(line)
                if match3:
                    answers[match3.group(1)] = {"correctAnswer": match3.group(2), "explanation": ""}
    return answers

all_questions = []
id_counter = 1

for item in mapping:
    print(f"Processing Chapter {item['chapter']}: {item['topic']}")
    pdf_text = read_pdf_text(item["pdf"])
    docx_lines = read_docx_lines(item["docx"])
    
    questions = parse_questions_from_text(pdf_text)
    answers = parse_answers_from_lines(docx_lines)
    
    for q in questions:
        q_num = q["q_num"]
        if q_num in answers:
            ans_data = answers[q_num]
            all_questions.append({
                "id": f"q_{id_counter}",
                "chapter": item["chapter"],
                "topic": item["topic"],
                "question": q["question"],
                "options": q["options"],
                "correctAnswer": ans_data["correctAnswer"],
                "explanation": ans_data["explanation"]
            })
            id_counter += 1
        else:
            print(f"Warning: Missing answer for Chapter {item['chapter']} {item['topic']} Question {q_num}")

# Now parse dethithu.docx
print("Processing dethithu.docx")
dethi_lines = read_docx_lines("dethithu.docx")
dethi_text = "\n".join(dethi_lines)
mock_questions = parse_questions_from_text(dethi_text)

# Match mock questions to all_questions to find correct answers
dethi_output = []
mock_id_counter = 1
for mq in mock_questions:
    # Try to find a matching question in all_questions
    mq_text_clean = re.sub(r'\W+', '', mq["question"].lower())
    matched = False
    for aq in all_questions:
        aq_text_clean = re.sub(r'\W+', '', aq["question"].lower())
        # check if they are very similar (e.g. 90% overlap)
        if mq_text_clean in aq_text_clean or aq_text_clean in mq_text_clean:
            dethi_output.append({
                "id": f"mock_{mock_id_counter}",
                "question": mq["question"],
                "options": mq["options"],
                "correctAnswer": aq["correctAnswer"],
                "explanation": aq["explanation"],
                "sourceTopic": aq["topic"],
                "sourceChapter": aq["chapter"]
            })
            matched = True
            break
            
    if not matched:
        print(f"Could not find answer for mock question {mq['q_num']}: {mq['question']}")
        # Fallback without answer
        dethi_output.append({
            "id": f"mock_{mock_id_counter}",
            "question": mq["question"],
            "options": mq["options"],
            "correctAnswer": "",
            "explanation": "",
            "sourceTopic": "",
            "sourceChapter": ""
        })
    mock_id_counter += 1

output_data = {
    "revision": all_questions,
    "mockTest": dethi_output
}

with open("database.json", "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print("Saved successfully to database.json")
