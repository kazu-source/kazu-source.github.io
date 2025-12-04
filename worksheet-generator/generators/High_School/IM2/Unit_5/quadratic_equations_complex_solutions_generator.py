"""
Quadratic Equations with Complex Solutions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation
import math

class QuadraticEquationsComplexSolutionsGenerator:
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
        k = random.choice([1, 4, 9, 16])
        latex = f"\\text{{Solve: }} x^2 + {k} = 0"
        solution = f"x = \\pm {int(math.sqrt(k))}i"
        steps = [
            f"x² = -{k}",
            f"x = ±√(-{k})",
            f"x = ±√{k} · i",
            f"x = ±{int(math.sqrt(k))}i"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = 1
        b = random.randint(1, 6)
        c = random.randint(b**2 + 1, 20)
        disc = b**2 - 4*a*c
        latex = f"\\text{{Solve: }} x^2 + {2*b}x + {c} = 0"
        sqrt_disc = int(math.sqrt(abs(disc)))
        solution = f"x = {-b} \\pm {sqrt_disc}i"
        steps = [
            f"Use quadratic formula",
            f"Discriminant: {2*b}² - 4(1)({c}) = {disc}",
            f"x = \\frac{{-{2*b} \\pm \\sqrt{{{disc}}}}}{{2}}",
            f"x = \\frac{{-{2*b} \\pm {sqrt_disc}i}}{{2}}",
            f"x = {-b} \\pm {sqrt_disc}i"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(1, 3)
        b = random.randint(1, 5)
        c = random.randint(10, 20)
        disc = b**2 - 4*a*c
        latex = f"\\text{{Solve: }} {a}x^2 + {b}x + {c} = 0"
        solution = f"x = \\frac{{-{b} \\pm \\sqrt{{{disc}}}i}}{{{2*a}}}"
        steps = [
            f"Discriminant: {b}² - 4({a})({c}) = {disc}",
            "Since discriminant < 0, complex solutions",
            f"x = \\frac{{-{b} \\pm \\sqrt{{{abs(disc)}}}i}}{{{2*a}}}"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        h = random.randint(-3, 3)
        k = random.randint(1, 9)
        a = random.randint(1, 3)
        latex = f"\\text{{Solve: }} {a}(x {'-' if h < 0 else '+'} {abs(h)})^2 + {k} = 0"
        sqrt_k_over_a = math.sqrt(k / a)
        solution = f"x = {h} \\pm {sqrt_k_over_a:.2f}i"
        steps = [
            f"(x {'-' if h < 0 else '+'} {abs(h)})² = -{k}/{a}",
            f"x {'-' if h < 0 else '+'} {abs(h)} = \\pm \\sqrt{{-{k}/{a}}}",
            f"x {'-' if h < 0 else '+'} {abs(h)} = \\pm {sqrt_k_over_a:.2f}i",
            f"x = {h} \\pm {sqrt_k_over_a:.2f}i"
        ]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = QuadraticEquationsComplexSolutionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
