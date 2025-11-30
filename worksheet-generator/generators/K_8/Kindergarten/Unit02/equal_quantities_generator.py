"""
Equal Quantities Generator - Kindergarten Unit 2
Generates problems about recognizing equal quantities
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class EqualQuantitiesGenerator:
    """Generates equal quantities problems."""

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
        num = random.randint(1, 5)
        latex = f"\\text{{Are these the same? }} {num} \\text{{ and }} {num}"
        solution = "Yes"
        return Equation(latex=latex, solution=solution, steps=[f"{num} = {num}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        num1 = random.randint(1, 10)
        num2 = random.choice([num1, num1 + random.randint(1, 3)])
        if num1 == num2:
            latex = f"\\text{{Are }} {num1} \\text{{ and }} {num2} \\text{{ equal?}}"
            solution = "Yes"
        else:
            latex = f"\\text{{Are }} {num1} \\text{{ and }} {num2} \\text{{ equal?}}"
            solution = "No"
        return Equation(latex=latex, solution=solution, steps=[f"{num1} {'=' if num1 == num2 else '≠'} {num2}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        num = random.randint(3, 8)
        item1 = random.choice(['red balls', 'blue cars', 'green blocks'])
        item2 = random.choice(['yellow balls', 'red cars', 'blue blocks'])
        latex = f"\\text{{There are }} {num} \\text{{ {item1} and }} {num} \\text{{ {item2}. Are they equal?}}"
        solution = "Yes"
        return Equation(latex=latex, solution=solution, steps=[f"{num} = {num}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        num1 = random.randint(5, 12)
        num2 = random.randint(5, 12)
        latex = f"{num1} = {num2} \\text{{ True or False?}}"
        solution = "True" if num1 == num2 else "False"
        return Equation(latex=latex, solution=solution, steps=[f"{num1} {'=' if num1 == num2 else '≠'} {num2}"], difficulty='challenge')


def main():
    generator = EqualQuantitiesGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
