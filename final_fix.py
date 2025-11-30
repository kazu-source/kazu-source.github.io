"""
Final comprehensive fix based on manual testing.
"""

import os
import re

def fix_file(filepath):
    """Fix brace errors."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # Fix 1: \\text{{{{ {VAR}}}} -> \\text{{ {VAR} }}
        # This handles the common pattern where 4 braces should be 2
        content = re.sub(r'\\text\{\{\{\{ (\{[^}]+\})\}\}\}\}', r'\\text{{ \1 }}', content)

        # Fix 2: \\text{{{{ {VAR}s}}}} -> \\text{{ {VAR}s }}
        content = re.sub(r'\\text\{\{\{\{ (\{[^}]+\}s)\}\}\}\}', r'\\text{{ \1 }}', content)

        # Fix 3: \\text{{{{ {VAR}.}}}  -> \\text{{ {VAR}. }}
        content = re.sub(r'\\text\{\{\{\{ (\{[^}]+\}[.?!,])\}\}\}\}', r'\\text{{ \1 }}', content)

        # Fix 4: Pattern without leading space: \\text{{{{{VAR}}}}} -> \\text{{{VAR}}}
        content = re.sub(r'\\text\{\{\{(\{[^}]+\})\}\}\}', r'\\text{{\1}}', content)

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
                    print(f"Fixed: {os.path.basename(filepath)}")

print(f"\nFixed {fixed}/{total} files")
