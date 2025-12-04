"""
Convert Radians to Degrees Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation
import math

class ConvertRadiansDegreesGenerator:
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
        angles = [30, 45, 60, 90, 120, 135, 150, 180]
        deg = random.choice(angles)

        latex = f"\\text{{Convert }} {deg}^\\circ \\text{{ to radians.}}"
        # Calculate radians in terms of pi
        rad_num = deg
        rad_den = 180
        from math import gcd
        g = gcd(rad_num, rad_den)
        rad_num //= g
        rad_den //= g

        if rad_den == 1:
            solution = f"{rad_num}\\pi"
        else:
            solution = f"\\frac{{{rad_num}\\pi}}{{{rad_den}}}"

        steps = [
            f"\\text{{Use: }} \\theta_{{rad}} = \\theta_{{deg}} \\cdot \\frac{{\\pi}}{{180}}",
            f"= {deg} \\cdot \\frac{{\\pi}}{{180}}",
            f"= {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Radians to degrees
        fractions = [(1,6), (1,4), (1,3), (1,2), (2,3), (3,4), (5,6)]
        num, den = random.choice(fractions)

        latex = f"\\text{{Convert }} \\frac{{{num}\\pi}}{{{den}}} \\text{{ to degrees.}}"
        degrees = (num * 180) // den
        solution = f"{degrees}^\\circ"

        steps = [
            f"\\text{{Use: }} \\theta_{{deg}} = \\theta_{{rad}} \\cdot \\frac{{180}}{{\\pi}}",
            f"= \\frac{{{num}\\pi}}{{{den}}} \\cdot \\frac{{180}}{{\\pi}}",
            f"= \\frac{{{num} \\cdot 180}}{{{den}}} = {degrees}^\\circ"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        deg = random.randint(1, 360)

        latex = f"\\text{{Convert }} {deg}^\\circ \\text{{ to radians (exact form).}}"

        from math import gcd
        g = gcd(deg, 180)
        num = deg // g
        den = 180 // g

        if den == 1:
            solution = f"{num}\\pi"
        else:
            solution = f"\\frac{{{num}\\pi}}{{{den}}}"

        steps = [
            f"{deg}^\\circ \\cdot \\frac{{\\pi}}{{180}}",
            f"= \\frac{{{deg}\\pi}}{{180}}",
            f"= {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Multiple conversions
        deg1, deg2 = random.randint(30, 90), random.randint(120, 180)

        latex = f"\\text{{Convert }} {deg1}^\\circ \\text{{ and }} {deg2}^\\circ \\text{{ to radians, then find their sum.}}"

        total_deg = deg1 + deg2
        from math import gcd
        g = gcd(total_deg, 180)
        num = total_deg // g
        den = 180 // g

        solution = f"\\frac{{{num}\\pi}}{{{den}}}"

        steps = [
            f"{deg1}^\\circ = \\frac{{{deg1}\\pi}}{{180}}",
            f"{deg2}^\\circ = \\frac{{{deg2}\\pi}}{{180}}",
            f"\\text{{Sum: }} \\frac{{{deg1 + deg2}\\pi}}{{180}} = {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = ConvertRadiansDegreesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
