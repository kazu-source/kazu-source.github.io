"""
Pythagorean Theorem Generator - Grade 8 Unit 5
Generates problems using the Pythagorean theorem
Example: Find the hypotenuse if legs are 3 and 4.
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PythagoreanTheoremGenerator:
    """Generates Pythagorean theorem problems."""

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
        # Pythagorean triples
        triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (6, 8, 10)]
        a, b, c = random.choice(triples)

        latex = f"\\text{{Find the hypotenuse if legs are }} {a} \\text{{ and }} {b}."
        solution = f"c = {c}"
        steps = [
            f"a^2 + b^2 = c^2",
            f"{a}^2 + {b}^2 = c^2",
            f"{a**2} + {b**2} = c^2",
            f"c = {c}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17)]
        a, b, c = random.choice(triples)

        # Find leg given hypotenuse and other leg
        latex = f"\\text{{Find leg }} b \\text{{ if }} a = {a} \\text{{ and }} c = {c}."
        solution = f"b = {b}"
        steps = [
            f"{a}^2 + b^2 = {c}^2",
            f"{a**2} + b^2 = {c**2}",
            f"b^2 = {c**2 - a**2}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(5, 12)
        b = random.randint(5, 12)
        c = math.sqrt(a**2 + b**2)

        latex = f"\\text{{Find hypotenuse (to nearest tenth) if legs are }} {a} \\text{{ and }} {b}."
        solution = f"c \\approx {c:.1f}"
        steps = [
            f"{a}^2 + {b}^2 = c^2",
            f"{a**2 + b**2} = c^2",
            f"c = \\sqrt{{{a**2 + b**2}}}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Scaled Pythagorean triple
        scale = random.randint(2, 4)
        base_a, base_b, base_c = 3, 4, 5
        a, b, c = scale * base_a, scale * base_b, scale * base_c

        latex = f"\\text{{A right triangle has legs }} {a} \\text{{ and }} {b}. \\text{{ Find the hypotenuse.}}"
        solution = f"c = {c}"
        steps = [
            f"{a}^2 + {b}^2 = c^2",
            f"{a**2} + {b**2} = c^2",
            f"{a**2 + b**2} = c^2",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = PythagoreanTheoremGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
