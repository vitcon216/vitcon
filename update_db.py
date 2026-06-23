import json
import glob
import re

# Read database.json
with open('database.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

# Create a mapping from id to explanation
explanations = {}

# Read all markdown files
md_files = glob.glob('giai_thich_*.md')
for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by "**Câu"
    blocks = content.split('**Câu')
    for block in blocks[1:]:
        # block looks like " 1 (q_194): ...\nĐáp án đúng: C\nGiải thích: ....\n- Loại A...\n"
        match = re.search(r'\((q_\d+)\)', block)
        if match:
            q_id = match.group(1)
            # Find the explanation part (everything after Đáp án đúng: X)
            exp_match = re.search(r'Đáp án đúng: [A-D]\n(.*)', block, flags=re.DOTALL)
            if exp_match:
                exp_text = exp_match.group(1).strip()
                # Remove trailing newlines and next question markers if any
                exp_text = exp_text.split('\n\n**Câu')[0].strip()
                
                # Convert markdown newlines to HTML breaks for simple rendering
                html_exp = exp_text.replace('\n', '<br/>')
                # Make the "Giải thích:" bold
                html_exp = html_exp.replace('Giải thích:', '<strong>Giải thích:</strong>')
                # Make the "- Loại A..." bold
                html_exp = re.sub(r'- (Loại [A-D][^:]*:)', r'- <strong>\1</strong>', html_exp)
                
                explanations[q_id] = html_exp

# Update db
updated_count = 0
for q in db.get('revision', []):
    if q['id'] in explanations:
        q['detailed_explanation'] = explanations[q['id']]
        updated_count += 1

for q in db.get('mockTest', []):
    if q['id'] in explanations:
        q['detailed_explanation'] = explanations[q['id']]
        updated_count += 1

print(f"Updated {updated_count} questions.")

# Save back to database.json
with open('database.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=2)
