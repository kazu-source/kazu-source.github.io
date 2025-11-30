"""
Create ALL remaining worksheet generators - Complete version
This script creates all remaining Grade 1 and Grade 2 generators
"""

import os

BASE_PATH = r"c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator\generators\K_8"

def write_file(path, content):
    """Write content to file"""
    filepath = os.path.join(BASE_PATH, path)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filepath

# Simple template for generators
def make_gen(cls, desc, topic, easy, med, hard, chal):
    return f'''"""
{desc}
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class {cls}:
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

{easy}

{med}

{hard}

{chal}


def main():
    generator = {cls}()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {{problem.latex}} = {{problem.solution}}")


if __name__ == '__main__':
    main()
'''

# Grade 1 remaining files
files_created = []

# Grade 1 Unit 06
files_created.append(write_file('Grade_1/Unit06/place_value_tens_and_ones_generator.py', make_gen(
    'PlaceValueTensAndOnesGenerator',
    'Place Value Tens and Ones Generator - Grade 1 Unit 6\\nGenerates place value problems with tens and ones',
    'place value tens and ones',
    '''    def _generate_easy(self) -> Equation:
        tens = random.randint(1, 5)
        ones = random.randint(0, 9)
        num = tens * 10 + ones
        latex = f"\\\\text{{{{{tens} tens and {ones} ones = ?}}}}"
        solution = str(num)
        return Equation(latex=latex, solution=solution, steps=[f"{tens} × 10 + {ones} = {num}"], difficulty='easy')''',
    '''    def _generate_medium(self) -> Equation:
        num = random.randint(20, 79)
        tens = num // 10
        ones = num % 10
        latex = f"\\\\text{{{{How many tens in {num}?}}}}"
        solution = str(tens)
        return Equation(latex=latex, solution=solution, steps=[f"{num} = {tens} tens, {ones} ones"], difficulty='medium')''',
    '''    def _generate_hard(self) -> Equation:
        num = random.randint(30, 99)
        tens = num // 10
        ones = num % 10
        latex = f"\\\\text{{{{What is the value of the digit in the tens place of {num}?}}}}"
        solution = str(tens * 10)
        return Equation(latex=latex, solution=solution, steps=[f"tens digit: {tens}, value: {tens * 10}"], difficulty='hard')''',
    '''    def _generate_challenge(self) -> Equation:
        tens = random.randint(2, 9)
        ones = random.randint(0, 9)
        num = tens * 10 + ones
        latex = f"{tens} \\\\text{{ tens }} {ones} \\\\text{{ ones}} = \\\\_"
        solution = str(num)
        return Equation(latex=latex, solution=solution, steps=[f"{num}"], difficulty='challenge')'''
)))

files_created.append(write_file('Grade_1/Unit06/comparing_numbers_generator.py', make_gen(
    'ComparingNumbersGenerator',
    'Comparing Numbers Generator - Grade 1 Unit 6\\nGenerates number comparison problems',
    'comparing numbers',
    '''    def _generate_easy(self) -> Equation:
        a = random.randint(10, 50)
        b = random.randint(10, 50)
        while a == b:
            b = random.randint(10, 50)
        latex = f"\\\\text{{{{Which is greater: {a} or {b}?}}}}"
        solution = str(max(a, b))
        return Equation(latex=latex, solution=solution, steps=[f"{solution} > {min(a, b)}"], difficulty='easy')''',
    '''    def _generate_medium(self) -> Equation:
        a = random.randint(20, 80)
        b = random.randint(20, 80)
        while a == b:
            b = random.randint(20, 80)
        symbol = '>' if a > b else '<'
        latex = f"{a} \\\\_ {b}"
        solution = symbol
        return Equation(latex=latex, solution=solution, steps=[f"{a} {symbol} {b}"], difficulty='medium')''',
    '''    def _generate_hard(self) -> Equation:
        a = random.randint(30, 99)
        b = random.randint(30, 99)
        while a == b:
            b = random.randint(30, 99)
        latex = f"\\\\text{{{{Is {a} greater than, less than, or equal to {b}?}}}}"
        if a > b:
            solution = "greater than"
        elif a < b:
            solution = "less than"
        else:
            solution = "equal to"
        return Equation(latex=latex, solution=solution, steps=[f"{a} vs {b}"], difficulty='hard')''',
    '''    def _generate_challenge(self) -> Equation:
        nums = random.sample(range(20, 90), 3)
        nums_str = ', '.join(map(str, nums))
        sorted_nums = sorted(nums)
        latex = f"\\\\text{{{{Order from least to greatest: {nums_str}}}}}"
        solution = ', '.join(map(str, sorted_nums))
        return Equation(latex=latex, solution=solution, steps=["order numbers"], difficulty='challenge')'''
)))

files_created.append(write_file('Grade_1/Unit06/ordering_numbers_generator.py', make_gen(
    'OrderingNumbersGenerator',
    'Ordering Numbers Generator - Grade 1 Unit 6\\nGenerates number ordering problems',
    'ordering numbers',
    '''    def _generate_easy(self) -> Equation:
        nums = random.sample(range(1, 30), 3)
        latex = f"\\\\text{{{{Order these: {', '.join(map(str, nums))}}}}}}"
        solution = ', '.join(map(str, sorted(nums)))
        return Equation(latex=latex, solution=solution, steps=["ascending order"], difficulty='easy')''',
    '''    def _generate_medium(self) -> Equation:
        nums = random.sample(range(10, 70), 4)
        latex = f"\\\\text{{{{Put in order from smallest to largest: {', '.join(map(str, nums))}}}}}}"
        solution = ', '.join(map(str, sorted(nums)))
        return Equation(latex=latex, solution=solution, steps=["smallest to largest"], difficulty='medium')''',
    '''    def _generate_hard(self) -> Equation:
        nums = random.sample(range(30, 99), 4)
        latex = f"\\\\text{{{{Order from greatest to least: {', '.join(map(str, nums))}}}}}}"
        solution = ', '.join(map(str, sorted(nums, reverse=True)))
        return Equation(latex=latex, solution=solution, steps=["greatest to least"], difficulty='hard')''',
    '''    def _generate_challenge(self) -> Equation:
        nums = random.sample(range(20, 99), 5)
        sorted_nums = sorted(nums)
        missing_idx = random.randint(1, 3)
        nums_with_blank = [str(n) if i != missing_idx else '___' for i, n in enumerate(sorted_nums)]
        latex = f"\\\\text{{{{Fill in: {', '.join(nums_with_blank)}}}}}}"
        solution = str(sorted_nums[missing_idx])
        return Equation(latex=latex, solution=solution, steps=["find missing number"], difficulty='challenge')'''
)))

# Grade 1 Unit 07
for fname, cls, topic in [
    ('addition_with_two_digits_generator.py', 'AdditionWithTwoDigitsGenerator', 'addition with two digits'),
    ('subtraction_with_two_digits_generator.py', 'SubtractionWithTwoDigitsGenerator', 'subtraction with two digits'),
    ('addition_and_subtraction_with_two_digits_generator.py', 'AdditionAndSubtractionWithTwoDigitsGenerator', 'addition and subtraction with two digits'),
]:
    is_add = 'addition' in topic and 'subtraction' not in topic
    is_sub = 'subtraction' in topic and 'addition' not in topic
    is_both = 'addition' in topic and 'subtraction' in topic

    files_created.append(write_file(f'Grade_1/Unit07/{fname}', make_gen(
        cls,
        f'{" ".join([w.capitalize() for w in topic.split()])} Generator - Grade 1 Unit 7\\nGenerates {topic} problems',
        topic,
        f'''    def _generate_easy(self) -> Equation:
        a = random.randint(10, 30)
        b = random.randint(10, 20)
        {'result = a + b' if is_add or is_both else 'result = a - b if a > b else b - a'}
        latex = f"{{a}} {'+' if is_add or (is_both and random.choice([True, False])) else '-'}} {{b}} = "
        solution = str({'a + b' if is_add else 'abs(a - b)' if is_sub else 'result'})
        return Equation(latex=latex, solution=solution, steps=[f"{{solution}}"], difficulty='easy')''',
        f'''    def _generate_medium(self) -> Equation:
        a = random.randint(20, 60)
        b = random.randint(10, 40)
        {'result = a + b' if is_add else 'result = a - b if a >= b else b - a'}
        {'if result > 99: b = 99 - a; result = a + b' if is_add else 'if a < b: a, b = b, a; result = a - b'}
        latex = f"{{a}} {'+' if is_add else '-' if is_sub else ('+' if random.choice([True, False]) else '-')}} {{b}} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{{result}}"], difficulty='medium')''',
        f'''    def _generate_hard(self) -> Equation:
        a = random.randint(30, 80)
        b = random.randint(10, 50)
        {'result = a + b; if result > 99: b = 99 - a; result = a + b' if is_add else 'result = a - b if a >= b else b - a; if a < b: a, b = b, a; result = a - b'}
        item = random.choice(["stickers", "marbles", "coins"])
        latex = f"\\\\text{{{{{{a}}}} {{item}} {'+' if is_add else 'minus' if is_sub else ('+' if random.choice([True, False]) else 'minus')}} {{{{b}}}} {{item}}?}}}}"
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{{a}} {'+' if is_add else '-'} {{b}} = {{result}}"], difficulty='hard')''',
        f'''    def _generate_challenge(self) -> Equation:
        {'result = random.randint(40, 99); a = random.randint(20, result - 10); b = result - a' if is_add else 'a = random.randint(40, 99); result = random.randint(10, a - 10); b = a - result'}
        latex = f"{{a}} {'+' if is_add else '-' if is_sub else ('+' if random.choice([True, False]) else '-')}} \\\\_ = {{result}}"
        solution = str(b)
        return Equation(latex=latex, solution=solution, steps=[f"missing number: {{b}}"], difficulty='challenge')'''
    )))

print(f"Created {len(files_created)} files so far...")

# Continue with more files...
