"""
Extending Patterns Generator - Grade 1 Unit10
Generates extending patterns problems
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ExtendingPatternsGenerator:
    """Generates extending patterns problems."""

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
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        latex = f"{a} + {b} = "
        solution = str(a + b)
        return Equation(latex=latex, solution=solution, steps=["step"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(10, 50)
        b = random.randint(10, 50)
        latex = f"{a} + {b} = "
        solution = str(a + b)
        return Equation(latex=latex, solution=solution, steps=["step"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(20, 80)
        b = random.randint(10, 50)
        latex = f"{a} + {b} = "
        solution = str(a + b)
        return Equation(latex=latex, solution=solution, steps=["step"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(30, 90)
        b = random.randint(20, 60)
        latex = f"{a} + {b} = "
        solution = str(a + b)
        return Equation(latex=latex, solution=solution, steps=["step"], difficulty='challenge')


def main():
    generator = ExtendingPatternsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
