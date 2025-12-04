"""
Pythagorean Identity Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PythagoreanIdentityGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy': return self._generate_easy()
        elif difficulty == 'medium': return self._generate_medium()
        elif difficulty == 'hard': return self._generate_hard()
        else: return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        # Verify identity
        latex = "\\text{Verify: } \\sin^2(\\theta) + \\cos^2(\\theta) = 1"
        solution = "This is the fundamental Pythagorean identity"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Find sin given cos
        cos_values = {
            "\\frac{3}{5}": "\\frac{4}{5}",
            "\\frac{4}{5}": "\\frac{3}{5}",
            "\\frac{5}{13}": "\\frac{12}{13}",
            "\\frac{12}{13}": "\\frac{5}{13}"
        }

        cos_val, sin_val = random.choice(list(cos_values.items()))

        latex = f"\\text{{If }} \\cos(\\theta) = {cos_val} \\text{{ (Quadrant I), find }} \\sin(\\theta)"
        solution = sin_val

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Find cos given sin in different quadrant
        sin_val = random.choice(["\\frac{3}{5}", "\\frac{4}{5}", "\\frac{5}{13}"])
        quad = random.choice([2, 3, 4])

        latex = f"\\text{{If }} \\sin(\\theta) = {sin_val} \\text{{ (Quadrant {quad}), find }} \\cos(\\theta)"
        solution = "Use Pythagorean identity, apply quadrant sign"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Simplify using identity
        expressions = [
            ("1 - \\sin^2(\\theta)", "\\cos^2(\\theta)"),
            ("1 - \\cos^2(\\theta)", "\\sin^2(\\theta)"),
            ("\\sin^2(\\theta) + \\cos^2(\\theta) + 1", "2")
        ]

        expr, result = random.choice(expressions)

        latex = f"\\text{{Simplify: }} {expr}"
        solution = result

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = PythagoreanIdentityGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
