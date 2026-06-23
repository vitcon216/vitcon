import json
import glob
import re

# Read database.json
with open('database.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# Create a mapping from id to explanation and correct answer
updates = {}

# Read all markdown files
md_files = glob.glob('giai_thich_*.md')
for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    blocks = content.split('**Câu')
    for block in blocks[1:]:
        match = re.search(r'\((q_\d+)\)', block)
        if match:
            q_id = match.group(1)
            
            # Find the correct answer
            ans_match = re.search(r'Đáp án đúng:\s*([A-D])', block)
            if not ans_match:
                continue
            correct_ans = ans_match.group(1)
            
            # Find the explanation part
            exp_match = re.search(r'Đáp án đúng:\s*[A-D]\n(.*)', block, flags=re.DOTALL)
            if exp_match:
                exp_text = exp_match.group(1).strip()
                exp_text = exp_text.split('\n\n**Câu')[0].strip()
                
                html_exp = exp_text.replace('\n', '<br/>')
                html_exp = html_exp.replace('Giải thích:', '<strong>Giải thích:</strong>')
                html_exp = re.sub(r'- (Loại [A-D][^:]*:)', r'- <strong>\1</strong>', html_exp)
                
                updates[q_id] = {
                    'correctAnswer': correct_ans,
                    'detailed_explanation': html_exp
                }

updated_count = 0
for q in db.get('revision', []):
    if q['id'] in updates:
        q['correctAnswer'] = updates[q['id']]['correctAnswer']
        q['detailed_explanation'] = updates[q['id']]['detailed_explanation']
        updated_count += 1

for q in db.get('mockTest', []):
    if q['id'] in updates:
        q['correctAnswer'] = updates[q['id']]['correctAnswer']
        q['detailed_explanation'] = updates[q['id']]['detailed_explanation']
        updated_count += 1

print(f"Updated {updated_count} questions with correct answers and explanations.")

with open('database.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)
