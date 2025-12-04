"""
Greatest Common Factor Generator
"""
import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class GreatestCommonFactorGenerator:
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
        # Two terms with common factor
        gcf = random.randint(2, 6)
        a = random.randint(2, 8)
        b = random.randint(2, 8)

        term1 = gcf * a
        term2 = gcf * b

        latex = f"\\text{{Factor: }} {term1}x + {term2}"
        solution = f"{gcf}({a}x + {b})"
        steps = [
            f"Find GCF of {term1} and {term2}",
            f"GCF = {gcf}",
            f"Factor out {gcf}: {gcf}({a}x + {b})",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Three terms with common factor
        gcf = random.randint(2, 5)
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        c = random.randint(1, 8)

        term1 = gcf * a
        term2 = gcf * b
        term3 = gcf * c

        latex = f"\\text{{Factor: }} {term1}x^2 + {term2}x + {term3}"
        solution = f"{gcf}({a}x^2 + {b}x + {c})"
        steps = [
            f"Find GCF of {term1}, {term2}, and {term3}",
            f"GCF = {gcf}",
            f"Divide each term by {gcf}",
            f"{term1}/{gcf} = {a}, {term2}/{gcf} = {b}, {term3}/{gcf} = {c}",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Terms with variable GCF
        gcf_coef = random.randint(2, 6)
        gcf_power = random.randint(1, 3)
        a = random.randint(2, 6)
        b = random.randint(2, 6)

        power1 = gcf_power + random.randint(1, 2)
        power2 = gcf_power + random.randint(0, 2)

        coef1 = gcf_coef * a
        coef2 = gcf_coef * b

        latex = f"\\text{{Factor: }} {coef1}x^{{{power1}}} + {coef2}x^{{{power2}}}"
        solution = f"{gcf_coef}x^{{{gcf_power}}}({a}x^{{{power1-gcf_power}}} + {b}x^{{{power2-gcf_power}}})"
        steps = [
            f"Find GCF of coefficients: {math.gcd(coef1, coef2)}",
            f"Find lowest power of x: x^{{{gcf_power}}}",
            f"GCF = {gcf_coef}x^{{{gcf_power}}}",
            f"Factor out: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Multiple variables with GCF
        gcf_coef = random.randint(2, 5)
        a = random.randint(2, 6)
        b = random.randint(2, 6)
        c = random.randint(2, 6)

        x_pow = random.randint(1, 2)
        y_pow = random.randint(1, 2)

        coef1 = gcf_coef * a
        coef2 = gcf_coef * b
        coef3 = gcf_coef * c

        latex = f"\\text{{Factor: }} {coef1}x^{{{x_pow+1}}}y^{{{y_pow+1}}} + {coef2}x^{{{x_pow}}}y^{{{y_pow+1}}} + {coef3}x^{{{x_pow}}}y^{{{y_pow}}}"
        solution = f"{gcf_coef}x^{{{x_pow}}}y^{{{y_pow}}}({a}xy + {b}y + {c})"
        steps = [
            f"Find GCF of coefficients: {gcf_coef}",
            f"Find lowest power of x: x^{{{x_pow}}}",
            f"Find lowest power of y: y^{{{y_pow}}}",
            f"GCF = {gcf_coef}x^{{{x_pow}}}y^{{{y_pow}}}",
            f"Solution: {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = GreatestCommonFactorGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
