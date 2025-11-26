"""
Pythagorean Theorem Proofs Generator - Grade 8 Unit 5
Generates problems about understanding and verifying Pythagorean theorem
Example: Verify that 5, 12, 13 forms a Pythagorean triple.
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class PythagoreanTheoremProofsGenerator:
    """Generates Pythagorean theorem proofs problems."""

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
        triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17)]
        a, b, c = random.choice(triples)

        latex = f"\\text{{Verify that }} {a}, {b}, {c} \\text{{ is a Pythagorean triple.}}"
        solution = f"\\text{{Yes: }} {a}^2 + {b}^2 = {c}^2"
        steps = [
            f"{a}^2 + {b}^2 = {a**2} + {b**2} = {a**2 + b**2}",
            f"{c}^2 = {c**2}",
            f"{a**2 + b**2} = {c**2} \\checkmark"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Not a Pythagorean triple
        a, b = random.randint(4, 8), random.randint(6, 10)
        c = a + b - 1  # Definitely not c²

        latex = f"\\text{{Is }} {a}, {b}, {c} \\text{{ a Pythagorean triple?}}"
        solution = f"\\text{{No}}"
        steps = [
            f"{a}^2 + {b}^2 = {a**2} + {b**2} = {a**2 + b**2}",
            f"{c}^2 = {c**2}",
            f"{a**2 + b**2} \\neq {c**2}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Determine if triangle is right triangle
        triples = [(3, 4, 5), (5, 12, 13), (7, 24, 25)]
        a, b, c = random.choice(triples)

        # Randomly permute to test understanding
        sides = [a, b, c]
        random.shuffle(sides)

        latex = f"\\text{{Is a triangle with sides }} {sides[0]}, {sides[1]}, {sides[2]} \\text{{ a right triangle?}}"
        solution = "\\text{Yes}"
        steps = [
            f"\\text{{Check if }} {max(sides)}^2 = {sorted(sides)[0]}^2 + {sorted(sides)[1]}^2",
            f"{max(sides)**2} = {sorted(sides)[0]**2 + sorted(sides)[1]**2}",
            solution
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        k = random.randint(2, 5)
        a, b, c = 3 * k, 4 * k, 5 * k

        latex = f"\\text{{Prove }} {a}, {b}, {c} \\text{{ is a Pythagorean triple.}}"
        solution = f"\\text{{Yes, it's }} 3 \\times {k}, 4 \\times {k}, 5 \\times {k}"
        steps = [
            f"{a}^2 + {b}^2 = {a**2} + {b**2} = {a**2 + b**2}",
            f"{c}^2 = {c**2}",
            f"\\text{{Equal, so it's a Pythagorean triple}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    generator = PythagoreanTheoremProofsGenerator()
    print("Easy:")
    for problem in generator.generate_worksheet('easy', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
