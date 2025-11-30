"""
Addition Strategies Up To 20 Generator - Grade 1 Unit04
Generates addition strategies up to 20 problems
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class AdditionStrategiesUpTo20Generator:
    """Generates addition strategies up to 20 problems."""

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
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        result = a + b if 'addition' in 'addition strategies up to 20' or 'add' in 'addition strategies up to 20' else max(a, b) - min(a, b)
        latex = f"{a} + {b} = " if 'add' in 'addition strategies up to 20' else f"{max(a, b)} - {min(a, b)} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{solution}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(5, 15)
        b = random.randint(5, 15)
        result = a + b if 'addition' in 'addition strategies up to 20' or 'add' in 'addition strategies up to 20' else max(a, b) - min(a, b)
        if result > 20 and ('add' in 'addition strategies up to 20' or 'addition' in 'addition strategies up to 20'):
            b = 20 - a
            result = a + b
        latex = f"{a} + {b} = " if 'add' in 'addition strategies up to 20' else f"{max(a, b)} - {min(a, b)} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{solution}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(8, 18)
        b = random.randint(2, 12)
        if 'add' in 'addition strategies up to 20' or 'addition' in 'addition strategies up to 20':
            if a + b > 20:
                b = 20 - a
            result = a + b
            latex = f"{a} + {b} = "
        else:
            if a < b:
                a, b = b, a
            result = a - b
            latex = f"{a} - {b} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{result}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        if 'add' in 'addition strategies up to 20' or 'addition' in 'addition strategies up to 20':
            total = random.randint(10, 20)
            a = random.randint(5, total - 5)
            b = total - a
            latex = f"{a} + \_ = {total}"
            solution = str(b)
        else:
            a = random.randint(10, 20)
            b = random.randint(2, 10)
            result = a - b
            latex = f"{a} - \_ = {result}"
            solution = str(b)
        return Equation(latex=latex, solution=solution, steps=[f"missing number"], difficulty='challenge')


def main():
    generator = AdditionStrategiesUpTo20Generator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
