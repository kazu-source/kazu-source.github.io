"""
Comparing Sizes Measurement Generator - Kindergarten Unit 9
Generates problems about comparing sizes using measurement concepts
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ComparingSizesMeasurementGenerator:
    """Generates comparing sizes using measurement problems."""

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
        obj1 = random.choice(['elephant', 'bus', 'house'])
        obj2 = random.choice(['mouse', 'toy', 'book'])
        latex = f"\\text{{Which is heavier: {obj1} or {obj2}?}}"
        solution = obj1
        return Equation(latex=latex, solution=solution, steps=["compare weights"], difficulty='easy')

    def _generate_medium(self) -> Equation:
        container1 = random.choice(['cup', 'bottle'])
        container2 = random.choice(['bucket', 'pool'])
        latex = f"\\text{{Which holds more water: {container1} or {container2}?}}"
        solution = container2
        return Equation(latex=latex, solution=solution, steps=["compare capacity"], difficulty='medium')

    def _generate_hard(self) -> Equation:
        weight1 = random.randint(2, 5)
        weight2 = random.randint(2, 5)
        while weight1 == weight2:
            weight2 = random.randint(2, 5)
        latex = f"\\text{{Box A weighs {weight1} blocks. Box B weighs {weight2} blocks. Which is heavier?}}"
        solution = f"Box {'A' if weight1 > weight2 else 'B'}"
        return Equation(latex=latex, solution=solution, steps=["compare weights"], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        sizes = ['small', 'medium', 'large']
        obj = random.choice(['box', 'bag', 'container'])
        latex = f"\\text{{Order these {obj}es by how much they can hold: large, small, medium}}"
        solution = "small, medium, large"
        return Equation(latex=latex, solution=solution, steps=["order by capacity"], difficulty='challenge')


def main():
    generator = ComparingSizesMeasurementGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex} = {problem.solution}")
    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex} = {problem.solution}")


if __name__ == '__main__':
    main()
