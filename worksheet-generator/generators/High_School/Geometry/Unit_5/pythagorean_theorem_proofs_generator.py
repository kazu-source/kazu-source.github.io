"""
Pythagorean Theorem Proofs Generator
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class PythagoreanTheoremProofsGenerator:
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
        latex = "\\text{State the Pythagorean Theorem.}"
        solution = "a² + b² = c² for right triangles"
        steps = ["\\text{In a right triangle with legs } a, b \\text{ and hypotenuse } c:",
                "a^2 + b^2 = c^2"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a, b = 3, 4
        c = 5
        latex = f"\\text{{Verify Pythagorean theorem for }} a={a}, b={b}, c={c}."
        solution = f"{a}² + {b}² = {c}²"
        steps = [f"{a}^2 + {b}^2 = {a**2} + {b**2} = {a**2 + b**2}",
                f"{c}^2 = {c**2}", f"\\text{{Therefore }} {a}^2 + {b}^2 = {c}^2 \\checkmark"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\text{Prove Pythagorean theorem using four congruent right triangles in a square.}"
        solution = "Rearrangement proof showing c² = a² + b²"
        steps = ["\\text{Arrange 4 triangles (legs } a, b) \\text{ in square of side } a+b",
                "\\text{Inner space forms square of side } c",
                "\\text{Area of large square: } (a+b)^2 = a^2 + 2ab + b^2",
                "\\text{Also equals: } 4 \\cdot \\frac{1}{2}ab + c^2 = 2ab + c^2",
                "\\text{Therefore: } a^2 + 2ab + b^2 = 2ab + c^2",
                "\\text{Simplifying: } a^2 + b^2 = c^2"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Prove the Pythagorean theorem using similar triangles (altitude to hypotenuse).}"
        solution = "Use geometric mean relationships"
        steps = ["\\text{Draw altitude } h \\text{ from right angle to hypotenuse}",
                "\\text{Creates similar triangles: whole ~ left part ~ right part}",
                "\\text{From similarity: } a^2 = c \\cdot m \\text{ and } b^2 = c \\cdot n",
                "\\text{where hypotenuse } c = m + n",
                "a^2 + b^2 = c \\cdot m + c \\cdot n = c(m+n) = c \\cdot c = c^2"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = PythagoreanTheoremProofsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
