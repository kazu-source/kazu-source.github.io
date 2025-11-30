"""
Place Value Tens And Ones Generator - Grade 1 Unit06
Generates place value tens and ones problems
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PlaceValueTensAndOnesGenerator:
    """Generates place value tens and ones problems."""

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
        tens = random.randint(1, 5)
        ones = random.randint(0, 9)
        num = tens * 10 + ones
        latex = f"\\text{{{tens} tens and {ones} ones = ?}}"
        solution = str(num)
        return Equation(latex=latex, solution=solution, steps=[f"{tens} × 10 + {ones} = {num}"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        num = random.randint(20, 79)
        tens = num // 10
        ones = num % 10
        latex = f"\\text{{How many tens in {num}?}}"
        solution = str(tens)
        return Equation(latex=latex, solution=solution, steps=[f"{num} = {tens} tens, {ones} ones"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        num = random.randint(30, 99)
        tens = num // 10
        ones = num % 10
        latex = f"\\text{{What is {num} in tens and ones?}}"
        solution = f"{tens} tens {ones} ones"
        return Equation(latex=latex, solution=solution, steps=[f"{tens} tens, {ones} ones"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        tens = random.randint(2, 9)
        ones = random.randint(0, 9)
        num = tens * 10 + ones
        latex = f"{tens} \\text{{ tens }} {ones} \\text{{ ones}} = \\_"
        solution = str(num)
        return Equation(latex=latex, solution=solution, steps=[f"{num}"], difficulty='challenge')


def main():
    generator = PlaceValueTensAndOnesGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
