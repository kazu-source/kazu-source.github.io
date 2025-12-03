"""
Refactor K-2 generators to remove difficulty levels.
For K-2, the skill itself defines the complexity, so difficulty levels are redundant.
"""

import re
import os
from pathlib import Path


def refactor_generator_file(file_path: Path) -> bool:
    """
    Refactor a generator file to remove difficulty levels.
    Returns True if successful, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Step 1: Update docstring to mention no difficulty levels
        # Find the module docstring and add a note
        module_docstring_match = re.search(r'^"""(.*?)"""', content, re.DOTALL)
        if module_docstring_match:
            old_docstring = module_docstring_match.group(0)
            docstring_content = module_docstring_match.group(1).strip()
            # Add note about no difficulty levels if not already present
            if 'difficulty' not in docstring_content.lower():
                new_docstring = f'"""\n{docstring_content}\nNote: K-2 generators do not use difficulty levels.\n"""'
                content = content.replace(old_docstring, new_docstring, 1)

        # Step 2: Update generate_worksheet method signature and body
        # Pattern to match the generate_worksheet method
        gen_worksheet_pattern = r'''def generate_worksheet\(self, difficulty: str, num_problems: int\) -> List\[Equation\]:
        problems = \[\]
        for _ in range\(num_problems\):
            problem = self\._generate_problem\(difficulty\)
            problems\.append\(problem\)
        return problems'''

        new_gen_worksheet = '''def generate_worksheet(self, difficulty: str = None, num_problems: int = 8) -> List[Equation]:
        """Generate worksheet problems. Note: difficulty parameter is ignored for K-2."""
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem()
            problems.append(problem)
        return problems'''

        content = re.sub(gen_worksheet_pattern, new_gen_worksheet, content)

        # Step 3: Extract _generate_easy content and create new _generate_problem
        # Find the _generate_easy method
        easy_pattern = r'def _generate_easy\(self\) -> Equation:(.*?)(?=\n    def _|\n\ndef |\nclass |\Z)'
        easy_match = re.search(easy_pattern, content, re.DOTALL)

        if easy_match:
            easy_body = easy_match.group(1)
            # Remove difficulty='easy' from Equation constructor
            easy_body = re.sub(r",\s*difficulty=['\"]easy['\"]", "", easy_body)
            easy_body = re.sub(r"difficulty=['\"]easy['\"],\s*", "", easy_body)

            new_generate_problem = f"def _generate_problem(self) -> Equation:{easy_body}"
        else:
            print(f"  Warning: Could not find _generate_easy in {file_path}")
            return False

        # Step 4: Remove the old _generate_problem routing method
        old_routing_pattern = r'''def _generate_problem\(self, difficulty: str\) -> Equation:
        if difficulty == 'easy':
            return self\._generate_easy\(\)
        elif difficulty == 'medium':
            return self\._generate_medium\(\)
        elif difficulty == 'hard':
            return self\._generate_hard\(\)
        else:
            return self\._generate_challenge\(\)'''

        content = re.sub(old_routing_pattern, new_generate_problem, content)

        # Step 5: Remove _generate_easy, _generate_medium, _generate_hard, _generate_challenge methods
        for diff in ['easy', 'medium', 'hard', 'challenge']:
            pattern = rf'\n    def _generate_{diff}\(self\) -> Equation:.*?(?=\n    def _|\n\ndef |\nclass |\Z)'
            content = re.sub(pattern, '', content, flags=re.DOTALL)

        # Step 6: Update main() function if it exists
        # Replace difficulty-specific calls in main()
        content = re.sub(
            r"generator\.generate_worksheet\(['\"]easy['\"],\s*(\d+)\)",
            r"generator.generate_worksheet(num_problems=\1)",
            content
        )
        content = re.sub(
            r"generator\.generate_worksheet\(['\"]medium['\"],\s*(\d+)\)",
            r"generator.generate_worksheet(num_problems=\1)",
            content
        )
        content = re.sub(
            r'print\("Easy:"\)',
            'print("Problems:")',
            content
        )
        content = re.sub(
            r'print\("\\nMedium:"\).*?print\(f"  \{problem\.latex\}.*?\n',
            '',
            content,
            flags=re.DOTALL
        )

        # Clean up any double blank lines
        content = re.sub(r'\n{3,}', '\n\n', content)

        # Only write if content changed
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        else:
            return False

    except Exception as e:
        print(f"  Error processing {file_path}: {e}")
        return False


def main():
    """Refactor all K-2 generators."""
    base_path = Path("generators/K_8")

    grades = ["Kindergarten", "Grade_1", "Grade_2"]

    total_files = 0
    successful = 0
    failed = []

    for grade in grades:
        grade_path = base_path / grade
        if not grade_path.exists():
            print(f"Warning: {grade_path} does not exist")
            continue

        print(f"\n{'='*60}")
        print(f"Refactoring {grade}")
        print('='*60)

        # Find all generator files
        generator_files = list(grade_path.glob("**/*_generator.py"))

        for gen_file in sorted(generator_files):
            total_files += 1
            relative_path = gen_file.relative_to(base_path)
            print(f"  [{total_files}] {relative_path}...", end=" ")

            if refactor_generator_file(gen_file):
                print("[OK]")
                successful += 1
            else:
                print("[SKIPPED/FAILED]")
                failed.append(str(relative_path))

    print(f"\n{'='*60}")
    print("REFACTORING COMPLETE")
    print('='*60)
    print(f"Total files: {total_files}")
    print(f"Successful: {successful}")
    print(f"Failed/Skipped: {len(failed)}")

    if failed:
        print("\nFailed files:")
        for f in failed:
            print(f"  - {f}")


if __name__ == "__main__":
    main()
