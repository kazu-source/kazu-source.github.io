"""
Simple, safe fix: ONLY replace }}}}} with }}}} in f-strings.
This is the ONLY change that is guaranteed safe based on testing.
"""

import os

def fix_file(filepath):
    """Fix only the }}}}} -> }}}} pattern."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # ONLY fix: }}}}} (5 closes) -> }}}} (4 closes)
        # This is safe because we validated it
        content = content.replace('}}}}}', '}}}}')

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True

        return False

    except Exception as e:
        print(f"Error: {e}")
        return False

base_path = r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8'
grades = ['Kindergarten', 'Grade_1', 'Grade_2', 'Grade_5', 'Grade_6', 'Grade_8']

fixed = 0
total = 0

for grade in grades:
    grade_path = os.path.join(base_path, grade)
    if not os.path.exists(grade_path):
        continue

    for root, dirs, files in os.walk(grade_path):
        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                filepath = os.path.join(root, file)
                total += 1
                if fix_file(filepath):
                    fixed += 1
                    print(f"Fixed: {file}")

print(f"\nFixed {fixed}/{total} files")
