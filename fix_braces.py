"""
Script to fix LaTeX f-string brace errors in worksheet generator files.
The issue: f-strings with \\text{{{{...}}}}} have 5 closing braces when they should have 4.
"""

import re
import os
import sys

def fix_braces_in_file(filepath):
    """Fix brace errors in a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        lines = content.split('\n')
        fixed_lines = []

        for line in lines:
            fixed_line = line

            # Check if line contains f" and \\text
            if ('f"' in line or "f'" in line) and '\\text{' in line:
                # Pattern 1: Fix }}}}} (5 closes) -> }}}} (4 closes)
                # This fixes: f"\\text{{{{literal}}}}} -> f"\\text{{{{literal}}}}"
                fixed_line = re.sub(r'(?<!})}}}}}(?!})', r'}}}}', fixed_line)

                # Pattern 2: Fix \\text{{{{ {var}}}} -> \\text{{ {var} }}
                # The {{{{ creates {{ in output (4 braces -> 2 literal braces)
                # But we want { in output (2 braces -> 1 literal brace)
                # So replace {{{{ with {{ and }}}} with }}
                # But be careful - only when it's followed by a variable substitution
                fixed_line = re.sub(r'\\text\{\{\{\{( \{[^}]+\} )\}\}\}\}', r'\\text{{\1}}', fixed_line)

            fixed_lines.append(fixed_line)

        content = '\n'.join(fixed_lines)

        # Check if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    """Process all Python files in specified directories."""
    base_path = r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8'

    grades = ['Kindergarten', 'Grade_1', 'Grade_2', 'Grade_5', 'Grade_6', 'Grade_8']

    files_fixed = 0
    files_processed = 0

    for grade in grades:
        grade_path = os.path.join(base_path, grade)
        if not os.path.exists(grade_path):
            continue

        # Walk through all subdirectories
        for root, dirs, files in os.walk(grade_path):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    filepath = os.path.join(root, file)
                    files_processed += 1
                    if fix_braces_in_file(filepath):
                        files_fixed += 1
                        print(f"Fixed: {filepath}")

    print(f"\nProcessed {files_processed} files, fixed {files_fixed} files.")

if __name__ == '__main__':
    main()
