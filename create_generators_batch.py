"""
Batch create all remaining worksheet generators
"""

import os

BASE_PATH = r"c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8"

# Template for generators
TEMPLATE = '''"""
{description}
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class {class_name}:
    """Generates {topic} problems."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
{easy_impl}
        return Equation(latex=latex, solution=solution, steps=[step], difficulty='easy')

    def _generate_medium(self) -> Equation:
{medium_impl}
        return Equation(latex=latex, solution=solution, steps=[step], difficulty='medium')

    def _generate_hard(self) -> Equation:
{hard_impl}
        return Equation(latex=latex, solution=solution, steps=[step], difficulty='hard')

    def _generate_challenge(self) -> Equation:
{challenge_impl}
        return Equation(latex=latex, solution=solution, steps=[step], difficulty='challenge')


def main():
    generator = {class_name}()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {{problem.latex}} = {{problem.solution}}")


if __name__ == '__main__':
    main()
'''

generators_to_create = [
    # Grade 1 Unit 02 (remaining)
    {
        'path': 'Grade_1/Unit02/addition_up_to_10_generator.py',
        'class_name': 'AdditionUpTo10Generator',
        'description': 'Addition Up to 10 Generator - Grade 1 Unit 2\\nGenerates addition problems with sums up to 10',
        'topic': 'addition up to 10',
        'easy_impl': '        a = random.randint(1, 5)\\n        b = random.randint(1, 5)\\n        total = a + b\\n        latex = f"{a} + {b} = "\\n        solution = str(total)\\n        step = f"{a} + {b} = {total}"',
        'medium_impl': '        a = random.randint(3, 7)\\n        b = random.randint(1, 10 - a)\\n        total = a + b\\n        latex = f"{a} + {b} = "\\n        solution = str(total)\\n        step = f"{total}"',
        'hard_impl': '        a = random.randint(4, 8)\\n        b = random.randint(1, 10 - a)\\n        total = a + b\\n        latex = f"{a} + {b} = "\\n        solution = str(total)\\n        step = f"{a} + {b} = {total}"',
        'challenge_impl': '        total = random.randint(6, 10)\\n        a = random.randint(2, total - 2)\\n        b = total - a\\n        latex = f"{a} + \\\\_ = {total}"\\n        solution = str(b)\\n        step = f"missing addend: {b}"'
    },
    {
        'path': 'Grade_1/Unit02/addition_word_problems_up_to_10_generator.py',
        'class_name': 'AdditionWordProblemsUpTo10Generator',
        'description': 'Addition Word Problems Up to 10 Generator - Grade 1 Unit 2\\nGenerates addition word problems with sums up to 10',
        'topic': 'addition word problems up to 10',
        'easy_impl': '        a = random.randint(1, 4)\\n        b = random.randint(1, 5)\\n        total = a + b\\n        item = random.choice(["apples", "toys", "books"])\\n        latex = f"\\\\text{{{{Tom has {a} {item}. He gets {b} more. How many now?}}}}"\\n        solution = str(total)\\n        step = f"{a} + {b} = {total}"',
        'medium_impl': '        a = random.randint(2, 6)\\n        b = random.randint(2, 8)\\n        total = a + b\\n        if total > 10:\\n            b = 10 - a\\n            total = a + b\\n        latex = f"\\\\text{{{{Sara has {a} crayons. Ben has {b} crayons. How many total?}}}}"\\n        solution = str(total)\\n        step = f"{a} + {b} = {total}"',
        'hard_impl': '        total = random.randint(7, 10)\\n        a = random.randint(3, total - 2)\\n        b = total - a\\n        latex = f"\\\\text{{{{There are {total} birds. {a} are red. How many are blue?}}}}"\\n        solution = str(b)\\n        step = f"{total} - {a} = {b}"',
        'challenge_impl': '        a = random.randint(2, 5)\\n        b = random.randint(2, 5)\\n        c = random.randint(1, 3)\\n        total = a + b + c\\n        if total > 10:\\n            c = 1\\n            total = a + b + c\\n        latex = f"\\\\text{{{{Ann has {a} pencils, Bob has {b}, and Cal has {c}. How many total?}}}}"\\n        solution = str(total)\\n        step = f"{a} + {b} + {c} = {total}"'
    },
]

# Create files
for gen in generators_to_create:
    filepath = os.path.join(BASE_PATH, gen['path'])
    content = TEMPLATE.format(**gen)

    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, 'w') as f:
        f.write(content)

    print(f"Created: {filepath}")

print(f"\\nCreated {len(generators_to_create)} files")
