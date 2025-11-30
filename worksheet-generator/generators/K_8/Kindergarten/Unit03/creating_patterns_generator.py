"""
Creating Patterns Generator - Kindergarten Unit 3
Generates problems about creating simple patterns
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class CreatingPatternsGenerator:
    """Generates creating patterns problems."""

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
        elem1, elem2 = random.choice([('red', 'blue'), ('A', 'B'), ('●', '○')])
        latex = f"\\text{{Make a pattern using {elem1} and {elem2}}}"
        solution = f"{elem1}, {elem2}, {elem1}, {elem2}"
        return Equation(latex=latex, solution=solution, steps=["AB pattern"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        elems = random.choice([
            ('●', '●', '○'),
            ('A', 'A', 'B'),
            ('red', 'red', 'blue')
        ])
        latex = f"\\text{{Create a pattern with: {elems[0]}, {elems[1]}, {elems[2]}}}"
        solution = f"{elems[0]}, {elems[1]}, {elems[2]}, {elems[0]}, {elems[1]}, {elems[2]}"
        return Equation(latex=latex, solution=solution, steps=["AAB pattern"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        items = random.choice([
            ['circles', 'squares'],
            ['red blocks', 'blue blocks'],
            ['stars', 'hearts']
        ])
        latex = f"\\text{{Make your own pattern using {items[0]} and {items[1]}}}"
        solution = "Student creates pattern"
        return Equation(latex=latex, solution=solution, steps=["various patterns"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        elem1 = random.choice(['A', '●', '1'])
        elem2 = random.choice(['B', '○', '2'])
        elem3 = random.choice(['C', '△', '3'])
        latex = f"\\text{{Create an ABC pattern using {elem1}, {elem2}, and {elem3}}}"
        solution = f"{elem1}, {elem2}, {elem3}, {elem1}, {elem2}, {elem3}"
        return Equation(latex=latex, solution=solution, steps=["ABC pattern"], difficulty='challenge')


def main():
    generator = CreatingPatternsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
