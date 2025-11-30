"""
Test script to verify all generator files import successfully.
"""

import os
import sys
import importlib.util

def test_import(filepath):
    """Try to import a Python file and return success/error."""
    try:
        spec = importlib.util.spec_from_file_location("test_module", filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return True, None
    except Exception as e:
        return False, str(e)

def main():
    base_path = r'c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8'

    grades = ['Kindergarten', 'Grade_1', 'Grade_2', 'Grade_5', 'Grade_6', 'Grade_8']

    total_files = 0
    passed_files = 0
    failed_files = []

    for grade in grades:
        grade_path = os.path.join(base_path, grade)
        if not os.path.exists(grade_path):
            continue

        # Walk through all subdirectories
        for root, dirs, files in os.walk(grade_path):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    filepath = os.path.join(root, file)
                    total_files += 1

                    success, error = test_import(filepath)
                    if success:
                        passed_files += 1
                        print(f"[OK] {filepath}")
                    else:
                        failed_files.append((filepath, error))
                        print(f"[FAIL] {filepath}")
                        print(f"  Error: {error}")

    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"Total files tested: {total_files}")
    print(f"Passed: {passed_files}")
    print(f"Failed: {len(failed_files)}")

    if failed_files:
        print(f"\nFailed files:")
        for filepath, error in failed_files:
            print(f"  - {filepath}")
            print(f"    {error}")
    else:
        print(f"\nAll files passed!")

if __name__ == '__main__':
    main()
