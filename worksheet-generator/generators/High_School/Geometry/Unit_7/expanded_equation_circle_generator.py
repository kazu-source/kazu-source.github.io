"""
Expanded Equation of a Circle Generator
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ExpandedEquationCircleGenerator:
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
        h, k = random.randint(2, 6), random.randint(2, 6)
        r_sq = random.choice([16, 25, 36])
        expanded_const = h**2 + k**2 - r_sq
        latex = f"\\text{{Expand: }} (x - {h})^2 + (y - {k})^2 = {r_sq}."
        solution = f"x² - {2*h}x + y² - {2*k}y + {expanded_const} = 0"
        steps = [f"x^2 - {2*h}x + {h**2} + y^2 - {2*k}y + {k**2} = {r_sq}",
                f"x^2 + y^2 - {2*h}x - {2*k}y + {h**2 + k**2 - r_sq} = 0"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Convert from expanded to standard
        h, k = random.randint(-4, 4), random.randint(-4, 4)
        r_sq = random.choice([9, 16, 25])
        D = -2 * h
        E = -2 * k
        F = h**2 + k**2 - r_sq
        latex = f"\\text{{Convert to standard form: }} x^2 + y^2 {D:+d}x {E:+d}y {F:+d} = 0."
        solution = f"(x - {h})² + (y - {k})² = {r_sq}"
        steps = [f"\\text{{Complete the square for x and y}}",
                f"(x^2 {D:+d}x) + (y^2 {E:+d}y) = {-F}",
                f"(x - {h})^2 + (y - {k})^2 = {r_sq}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        h, k = random.randint(-5, 5), random.randint(-5, 5)
        r = random.randint(4, 8)
        r_sq = r**2
        D = -2 * h
        E = -2 * k
        F = h**2 + k**2 - r_sq
        latex = f"\\text{{Find center and radius: }} x^2 + y^2 {D:+d}x {E:+d}y {F:+d} = 0."
        solution = f"Center ({h},{k}), radius {r}"
        steps = [f"\\text{{Complete the square:}}",
                f"(x - {h})^2 + (y - {k})^2 = {r_sq}",
                f"\\text{{Center: }} ({h},{k}), \\text{{ radius: }} {r}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # General form with coefficient
        a = random.choice([2, 4])
        h, k = random.randint(-3, 3), random.randint(-3, 3)
        r = random.randint(3, 6)
        r_sq = r**2
        D = -2 * a * h
        E = -2 * a * k
        F = a * (h**2 + k**2 - r_sq)
        latex = f"\\text{{Find center and radius: }} {a}x^2 + {a}y^2 {D:+d}x {E:+d}y {F:+d} = 0."
        solution = f"Center ({h},{k}), radius {r}"
        steps = [f"\\text{{Divide by }} {a}: x^2 + y^2 {D//a:+d}x {E//a:+d}y {F//a:+d} = 0",
                f"\\text{{Complete the square:}}",
                f"(x - {h})^2 + (y - {k})^2 = {r_sq}",
                f"\\text{{Center: }} ({h},{k}), \\text{{ radius: }} {r}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = ExpandedEquationCircleGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
