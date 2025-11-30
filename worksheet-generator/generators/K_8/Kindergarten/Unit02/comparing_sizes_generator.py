"""
Comparing Sizes Generator - Kindergarten Unit 2
Generates problems about comparing sizes (bigger, smaller, same size)
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ComparingSizesGenerator:
    """Generates comparing sizes problems."""

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
        obj1 = random.choice(['ball', 'box', 'car'])
        obj2 = random.choice(['ball', 'box', 'car'])
        latex = f"\\text{{Which is bigger: a big {obj1} or a small {obj2}?}}"
        solution = f"big {obj1}"
        return Equation(latex=latex, solution=solution, steps=["bigger object"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        obj = random.choice(['apple', 'book', 'chair', 'tree'])
        latex = f"\\text{{Circle the smaller {obj}}}"
        solution = f"smaller {obj}"
        return Equation(latex=latex, solution=solution, steps=["smaller"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        obj1 = random.choice(['elephant', 'dog', 'cat'])
        obj2 = random.choice(['mouse', 'ant', 'bird'])
        comparisons = [
            (f"Which is bigger: {obj1} or {obj2}?", obj1),
            (f"Which is smaller: {obj1} or {obj2}?", obj2)
        ]
        question, answer = random.choice(comparisons)
        latex = f"\\text{{{question}}}"
        solution = answer
        return Equation(latex=latex, solution=solution, steps=[answer], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        sizes = ['small', 'medium', 'large']
        obj = random.choice(['circle', 'square', 'triangle'])
        latex = f"\\text{{Put these in order from smallest to largest: large {obj}, small {obj}, medium {obj}}}"
        solution = f"small, medium, large"
        return Equation(latex=latex, solution=solution, steps=["order by size"], difficulty='challenge')


def main():
    generator = ComparingSizesGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
