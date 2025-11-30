"""
Comparing Lengths Generator - Kindergarten Unit 9
Generates problems about comparing lengths
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ComparingLengthsGenerator:
    """Generates comparing lengths problems."""

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
        obj1 = random.choice(['pencil', 'stick', 'ribbon'])
        obj2 = random.choice(['crayon', 'twig', 'string'])
        latex = f"\\text{{Which is longer: a {obj1} or a {obj2}?}}"
        solution = obj1
        return Equation(latex=latex, solution=solution, steps=["compare lengths"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        obj = random.choice(['line', 'rope', 'path'])
        latex = f"\\text{{This {obj} is 5 blocks long. Is it long or short?}}"
        solution = "depends on comparison"
        return Equation(latex=latex, solution=solution, steps=["relative measurement"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        len1 = random.randint(3, 8)
        len2 = random.randint(3, 8)
        while len1 == len2:
            len2 = random.randint(3, 8)
        longer = max(len1, len2)
        latex = f"\\text{{Line A is {len1} blocks. Line B is {len2} blocks. Which is longer?}}"
        solution = f"Line {'A' if len1 > len2 else 'B'}"
        return Equation(latex=latex, solution=solution, steps=[f"{longer} blocks"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        len1 = random.randint(4, 7)
        len2 = random.randint(4, 7)
        len3 = random.randint(4, 7)
        lengths = sorted([len1, len2, len3])
        latex = f"\\text{{Order by length: A={len1}, B={len2}, C={len3} blocks}}"
        solution = "shortest to longest"
        return Equation(latex=latex, solution=solution, steps=["order lengths"], difficulty='challenge')


def main():
    generator = ComparingLengthsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
