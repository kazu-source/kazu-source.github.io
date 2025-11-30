"""
Create all remaining worksheet generators for Grade 1 and Grade 2
"""

import os

BASE_PATH = r"c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8"

def create_generator_file(path, class_name, description, topic, implementations):
    """Create a generator file with custom implementations"""

    template = f'''"""
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

{implementations['easy']}

{implementations['medium']}

{implementations['hard']}

{implementations['challenge']}


def main():
    generator = {class_name}()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {{problem.latex}} = {{problem.solution}}")


if __name__ == '__main__':
    main()
'''

    filepath = os.path.join(BASE_PATH, path)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(template)

    return filepath

# Define all generators to create
generators = [
    # Grade 1 Unit 03 (remaining)
    {
        'path': 'Grade_1/Unit03/subtraction_strategies_up_to_10_generator.py',
        'class_name': 'SubtractionStrategiesUpTo10Generator',
        'description': 'Subtraction Strategies Up to 10 Generator - Grade 1 Unit 3\\nGenerates subtraction strategy problems up to 10',
        'topic': 'subtraction strategies up to 10',
        'implementations': {
            'easy': '''    def _generate_easy(self) -> Equation:
        a = random.randint(3, 7)
        b = random.randint(1, a)
        result = a - b
        latex = f"{a} - {b} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"count back from {a}"], difficulty='easy')''',
            'medium': '''    def _generate_medium(self) -> Equation:
        a = random.randint(5, 10)
        b = random.randint(1, a)
        result = a - b
        latex = f"{a} - {b} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{a} - {b} = {result}"], difficulty='medium')''',
            'hard': '''    def _generate_hard(self) -> Equation:
        a = 10
        b = random.randint(2, 8)
        result = a - b
        latex = f"\\\\text{{{{Subtract from 10: }}}} {a} - {b} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"10 - {b} = {result}"], difficulty='hard')''',
            'challenge': '''    def _generate_challenge(self) -> Equation:
        a = random.randint(6, 10)
        b = random.randint(2, a - 1)
        result = a - b
        latex = f"\\\\_ - {b} = {result}"
        solution = str(a)
        return Equation(latex=latex, solution=solution, steps=[f"{a} - {b} = {result}"], difficulty='challenge')'''
        }
    },
    {
        'path': 'Grade_1/Unit03/subtraction_up_to_10_generator.py',
        'class_name': 'SubtractionUpTo10Generator',
        'description': 'Subtraction Up to 10 Generator - Grade 1 Unit 3\\nGenerates subtraction problems up to 10',
        'topic': 'subtraction up to 10',
        'implementations': {
            'easy': '''    def _generate_easy(self) -> Equation:
        a = random.randint(3, 7)
        b = random.randint(1, a)
        result = a - b
        latex = f"{a} - {b} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{result}"], difficulty='easy')''',
            'medium': '''    def _generate_medium(self) -> Equation:
        a = random.randint(5, 10)
        b = random.randint(1, a)
        result = a - b
        latex = f"{a} - {b} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{a} - {b} = {result}"], difficulty='medium')''',
            'hard': '''    def _generate_hard(self) -> Equation:
        a = random.randint(7, 10)
        b = random.randint(2, a - 1)
        result = a - b
        latex = f"{a} - {b} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{result}"], difficulty='hard')''',
            'challenge': '''    def _generate_challenge(self) -> Equation:
        a = random.randint(7, 10)
        result = random.randint(2, 5)
        b = a - result
        latex = f"{a} - \\\\_ = {result}"
        solution = str(b)
        return Equation(latex=latex, solution=solution, steps=[f"{a} - {b} = {result}"], difficulty='challenge')'''
        }
    },
    {
        'path': 'Grade_1/Unit03/subtraction_word_problems_up_to_10_generator.py',
        'class_name': 'SubtractionWordProblemsUpTo10Generator',
        'description': 'Subtraction Word Problems Up to 10 Generator - Grade 1 Unit 3\\nGenerates subtraction word problems up to 10',
        'topic': 'subtraction word problems up to 10',
        'implementations': {
            'easy': '''    def _generate_easy(self) -> Equation:
        a = random.randint(4, 7)
        b = random.randint(1, a - 1)
        result = a - b
        item = random.choice(["apples", "toys", "books"])
        latex = f"\\\\text{{{{Tom has {a} {item}. He gives away {b}. How many left?}}}}"
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{a} - {b} = {result}"], difficulty='easy')''',
            'medium': '''    def _generate_medium(self) -> Equation:
        a = random.randint(6, 10)
        b = random.randint(2, a - 2)
        result = a - b
        item = random.choice(["pencils", "crayons", "stickers"])
        latex = f"\\\\text{{{{Sara had {a} {item}. She lost {b}. How many now?}}}}"
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{a} - {b} = {result}"], difficulty='medium')''',
            'hard': '''    def _generate_hard(self) -> Equation:
        a = random.randint(7, 10)
        b = random.randint(3, a - 2)
        result = a - b
        latex = f"\\\\text{{{{There were {a} birds. {b} flew away. How many left?}}}}"
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{a} - {b} = {result}"], difficulty='hard')''',
            'challenge': '''    def _generate_challenge(self) -> Equation:
        a = random.randint(8, 10)
        result = random.randint(2, 4)
        b = a - result
        latex = f"\\\\text{{{{Ann had {a} cookies. She has {result} left. How many did she eat?}}}}"
        solution = str(b)
        return Equation(latex=latex, solution=solution, steps=[f"{a} - {b} = {result}"], difficulty='challenge')'''
        }
    },
]

# Add Grade 1 Unit 04-10 generators (I'll add them in batches due to length)
grade1_unit04_10 = [
    # Unit 04
    ('Grade_1/Unit04/addition_strategies_up_to_20_generator.py', 'AdditionStrategiesUpTo20Generator', 'addition strategies up to 20', 20),
    ('Grade_1/Unit04/addition_up_to_20_generator.py', 'AdditionUpTo20Generator', 'addition up to 20', 20),
    ('Grade_1/Unit04/addition_word_problems_up_to_20_generator.py', 'AdditionWordProblemsUpTo20Generator', 'addition word problems up to 20', 20),
    # Unit 05
    ('Grade_1/Unit05/subtraction_strategies_up_to_20_generator.py', 'SubtractionStrategiesUpTo20Generator', 'subtraction strategies up to 20', 20),
    ('Grade_1/Unit05/subtraction_up_to_20_generator.py', 'SubtractionUpTo20Generator', 'subtraction up to 20', 20),
    ('Grade_1/Unit05/subtraction_word_problems_up_to_20_generator.py', 'SubtractionWordProblemsUpTo20Generator', 'subtraction word problems up to 20', 20),
    ('Grade_1/Unit05/addition_and_subtraction_up_to_20_generator.py', 'AdditionAndSubtractionUpTo20Generator', 'addition and subtraction up to 20', 20),
]

for path, class_name, topic, max_val in grade1_unit04_10:
    unit_num = path.split('/')[1]
    generators.append({
        'path': path,
        'class_name': class_name,
        'description': f'{" ".join([w.capitalize() for w in topic.split("_")])} Generator - Grade 1 {unit_num}\\nGenerates {topic} problems',
        'topic': topic,
        'implementations': {
            'easy': f'''    def _generate_easy(self) -> Equation:
        a = random.randint(1, {max_val//2})
        b = random.randint(1, {max_val//2})
        {'total = a + b' if 'addition' in topic else 'total = a if a > b else b; diff = abs(a - b)'}
        latex = f"{{a}} {'+' if 'addition' in topic else '-'} {{b}} = "
        solution = str({'total' if 'addition' in topic else 'diff'})
        return Equation(latex=latex, solution=solution, steps=[f"{{a}} {'+' if 'addition' in topic else '-'} {{b}} = {{solution}}"], difficulty='easy')''',
            'medium': f'''    def _generate_medium(self) -> Equation:
        a = random.randint({max_val//3}, {max_val-5})
        b = random.randint(1, {max_val - max_val//3})
        {'total = a + b' if 'addition' in topic else 'result = a - b if a > b else b - a'}
        {'if total > ' + str(max_val) + ': b = ' + str(max_val) + ' - a; total = a + b' if 'addition' in topic else 'if a <= b: a, b = b, a; result = a - b'}
        latex = f"{{a}} {'+' if 'addition' in topic else '-'} {{b}} = "
        solution = str({'total' if 'addition' in topic else 'result'})
        return Equation(latex=latex, solution=solution, steps=[f"{{solution}}"], difficulty='medium')''',
            'hard': f'''    def _generate_hard(self) -> Equation:
        a = random.randint({max_val//2}, {max_val-2})
        b = random.randint(2, {max_val//2})
        {'total = a + b' if 'addition' in topic else 'result = a - b'}
        {'if total > ' + str(max_val) + ': b = random.randint(1, ' + str(max_val) + ' - a); total = a + b' if 'addition' in topic else ''}
        item = random.choice(["apples", "books", "toys"])
        latex = f"\\\\text{{{{{{a}}}} {{item}} {'+' if 'addition' in topic else 'take away'} {{{{b}}}} {'{item}' if 'word' not in topic else ''}?}}}}"
        solution = str({'total' if 'addition' in topic else 'result'})
        return Equation(latex=latex, solution=solution, steps=[f"{{a}} {'+' if 'addition' in topic else '-'} {{b}} = {{solution}}"], difficulty='hard')''',
            'challenge': f'''    def _generate_challenge(self) -> Equation:
        {'total = random.randint(' + str(max_val//2) + ', ' + str(max_val) + ')' if 'addition' in topic else 'a = random.randint(' + str(max_val//2) + ', ' + str(max_val) + ')'}
        {'a = random.randint(2, total - 2); b = total - a' if 'addition' in topic else 'result = random.randint(2, a - 2); b = a - result'}
        latex = f"{{a}} {'+' if 'addition' in topic else '-'} \\\\_ = {{'{{total}}' if 'addition' in topic else '{{result}}'}}"
        solution = str(b)
        return Equation(latex=latex, solution=solution, steps=[f"missing {'addend' if 'addition' in topic else 'subtrahend'}"], difficulty='challenge')'''
        }
    })

# Create all files
count = 0
for gen in generators:
    filepath = create_generator_file(
        gen['path'],
        gen['class_name'],
        gen['description'],
        gen['topic'],
        gen['implementations']
    )
    print(f"Created: {filepath}")
    count += 1

print(f"\\nTotal files created: {count}")
