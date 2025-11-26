"""
Pythagorean Theorem Application Generator - Grade 8 Unit 5
Generates word problems applying the Pythagorean theorem
Example: A ladder is 10 ft long and 6 ft from wall. How high does it reach?
"""

import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PythagoreanTheoremApplicationGenerator:
    """Generates Pythagorean theorem application problems."""

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
        triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13)]
        a, b, c = random.choice(triples)

        latex = f"\\text{{A ladder is }} {c} \\text{{ ft long. It's }} {a} \\text{{ ft from the wall. How high does it reach?}}"
        solution = f"{b} \\text{{ ft}}"
        steps = [
            f"{a}^2 + h^2 = {c}^2",
            f"{a**2} + h^2 = {c**2}",
            f"h^2 = {c**2 - a**2}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        width = random.randint(6, 12)
        height = random.randint(8, 16)
        diagonal = math.sqrt(width**2 + height**2)

        latex = f"\\text{{A TV screen is }} {width} \\text{{ in wide and }} {height} \\text{{ in tall. Find the diagonal (nearest tenth).}}"
        solution = f"{diagonal:.1f} \\text{{ in}}"
        steps = [
            f"{width}^2 + {height}^2 = d^2",
            f"{width**2 + height**2} = d^2",
            f"d = \\sqrt{{{width**2 + height**2}}}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        base = random.randint(10, 20)
        height = random.randint(15, 25)
        distance = math.sqrt(base**2 + height**2)

        latex = f"\\text{{A kite is }} {height} \\text{{ m high. The string forms a right triangle with base }} {base} \\text{{ m. Find string length.}}"
        solution = f"{distance:.1f} \\text{{ m}}"
        steps = [
            f"{base}^2 + {height}^2 = L^2",
            f"{base**2 + height**2} = L^2",
            f"L = \\sqrt{{{base**2 + height**2}}}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        side = random.randint(8, 15)
        diagonal = side * math.sqrt(2)

        latex = f"\\text{{A square has side length }} {side}. \\text{{ Find the diagonal (exact answer).}}"
        solution = f"{side}\\sqrt{{2}}"
        steps = [
            f"{side}^2 + {side}^2 = d^2",
            f"{2 * side**2} = d^2",
            f"d = \\sqrt{{{2 * side**2}}} = {side}\\sqrt{{2}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = PythagoreanTheoremApplicationGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
