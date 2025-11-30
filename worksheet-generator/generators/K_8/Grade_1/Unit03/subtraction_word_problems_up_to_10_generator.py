"""
Subtraction Word Problems Up to 10 Generator - Grade 1 Unit 3\nGenerates subtraction word problems up to 10
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class SubtractionWordProblemsUpTo10Generator:
    """Generates subtraction word problems up to 10 problems."""

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
        a = random.randint(4, 7)
        b = random.randint(1, a - 1)
        result = a - b
        item = random.choice(["apples", "toys", "books"])
        latex = f"\\text{{{{Tom has {a} {item}. He gives away {b}. How many left?}}}}"
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{a} - {b} = {result}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(6, 10)
        b = random.randint(2, a - 2)
        result = a - b
        item = random.choice(["pencils", "crayons", "stickers"])
        latex = f"\\text{{{{Sara had {a} {item}. She lost {b}. How many now?}}}}"
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{a} - {b} = {result}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(7, 10)
        b = random.randint(3, a - 2)
        result = a - b
        latex = f"\\text{{{{There were {a} birds. {b} flew away. How many left?}}}}"
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{a} - {b} = {result}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(8, 10)
        result = random.randint(2, 4)
        b = a - result
        latex = f"\\text{{{{Ann had {a} cookies. She has {result} left. How many did she eat?}}}}"
        solution = str(b)
        return Equation(latex=latex, solution=solution, steps=[f"{a} - {b} = {result}"], difficulty='challenge')


def main():
    generator = SubtractionWordProblemsUpTo10Generator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
