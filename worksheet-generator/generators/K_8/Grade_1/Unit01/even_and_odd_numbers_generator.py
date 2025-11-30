"""
Even and Odd Numbers Generator - Grade 1 Unit 1
Generates problems about identifying even and odd numbers
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class EvenAndOddNumbersGenerator:
    """Generates even and odd numbers problems."""

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
        num = random.randint(1, 10)
        latex = f"\\text{{Is }} {num} \\text{{ even or odd?}}"
        solution = "even" if num % 2 == 0 else "odd"
        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='easy')

    def _generate_medium(self) -> Equation:
        num = random.randint(10, 30)
        latex = f"\\text{{Is }} {num} \\text{{ even or odd?}}"
        solution = "even" if num % 2 == 0 else "odd"
        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='medium')

    def _generate_hard(self) -> Equation:
        nums = random.sample(range(1, 20), 5)
        even_nums = [str(n) for n in nums if n % 2 == 0]
        latex = f"\\text{{Circle the even numbers: }} {', '.join(map(str, nums))}"
        solution = ', '.join(even_nums) if even_nums else "none"
        return Equation(latex=latex, solution=solution, steps=["find even numbers"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        start = random.randint(10, 20)
        even_or_odd = random.choice(['even', 'odd'])
        next_num = start + (2 if start % 2 == 0 else 1) if even_or_odd == 'even' else start + (1 if start % 2 == 0 else 2)
        if even_or_odd == 'even' and start % 2 != 0:
            next_num = start + 1
        elif even_or_odd == 'odd' and start % 2 == 0:
            next_num = start + 1
        else:
            next_num = start + 2
        latex = f"\\text{{What is the next {even_or_odd} number after }} {start}?"
        solution = str(next_num)
        return Equation(latex=latex, solution=solution, steps=[f"next {even_or_odd}"], difficulty='challenge')


def main():
    generator = EvenAndOddNumbersGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
