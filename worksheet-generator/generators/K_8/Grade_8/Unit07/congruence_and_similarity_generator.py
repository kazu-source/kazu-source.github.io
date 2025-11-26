"""
Congruence and Similarity Generator - Grade 8 Unit 7
Generates problems about congruent and similar figures
Example: Are two triangles congruent or similar?
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class CongruenceAndSimilarityGenerator:
    """Generates congruence and similarity problems."""

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
        latex = "\\text{Congruent figures have the same shape and size. True or False?}"
        solution = "\\text{True}"
        steps = [solution]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        k = random.randint(2, 4)
        side1 = random.randint(3, 8)
        side2 = k * side1

        latex = f"\\text{{Triangle 1 has side }} {side1}. \\text{{ Triangle 2 has corresponding side }} {side2}. \\text{{ Are they similar?}}"
        solution = f"\\text{{Yes, scale factor }} k = {k}"
        steps = [
            f"k = \\frac{{{side2}}}{{{side1}}} = {k}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        angles1 = [50, 60, 70]
        angles2 = [50, 60, 70]

        latex = f"\\text{{Triangle 1 has angles }} {angles1[0]}°, {angles1[1]}°, {angles1[2]}°. \\text{{ Triangle 2 has angles }} {angles2[0]}°, {angles2[1]}°, {angles2[2]}°. \\text{{ Similar?}}"
        solution = "\\text{Yes, corresponding angles equal}"
        steps = [
            "\\text{Angles are equal}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        side = random.randint(5, 10)
        k = random.randint(2, 4)
        new_side = side * k

        latex = f"\\text{{If two similar figures have scale factor }} {k}, \\text{{ and one side is }} {side}, \\text{{ find corresponding side.}}"
        solution = f"{new_side}"
        steps = [
            f"{k} \\times {side} = {new_side}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = CongruenceAndSimilarityGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
