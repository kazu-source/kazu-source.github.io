"""
Shapes Generator - Grade 2 Unit08
Generates shapes problems
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ShapesGenerator:
    """Generates shapes problems."""

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
        result = a + b
        latex = f"{a} + {b} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{a} + {b} = {result}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(10, 50)
        b = random.randint(10, 50)
        result = a + b
        latex = f"{a} + {b} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{result}"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(30, 100)
        b = random.randint(20, 100)
        result = a + b
        latex = f"{a} + {b} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{result}"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(50, 200)
        b = random.randint(50, 200)
        result = a + b
        latex = f"{a} + {b} = "
        solution = str(result)
        return Equation(latex=latex, solution=solution, steps=[f"{result}"], difficulty='challenge')


def main():
    generator = ShapesGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
