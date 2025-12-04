"""
Introduction to Factoring Quadratics Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class IntroFactoringQuadraticsGenerator:
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
        # Simple GCF factoring
        gcf = random.randint(2, 6)
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        coef_x2 = gcf * a
        coef_x = gcf * b

        latex = f"\\text{{Factor: }} {coef_x2}x^2 + {coef_x}x"
        solution = f"{gcf}x({a}x + {b})"
        steps = [
            f"Find GCF of {coef_x2}x² and {coef_x}x",
            f"GCF = {gcf}x",
            f"Factor out {gcf}x:",
            f"{coef_x2}x² ÷ {gcf}x = {a}x",
            f"{coef_x}x ÷ {gcf}x = {b}",
            f"Answer: {gcf}x({a}x + {b})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        # GCF from all three terms
        gcf = random.randint(2, 5)
        a = random.randint(1, 4)
        b = random.randint(1, 6)
        c = random.randint(1, 6)

        coef_x2 = gcf * a
        coef_x = gcf * b
        coef_const = gcf * c

        latex = f"\\text{{Factor: }} {coef_x2}x^2 + {coef_x}x + {coef_const}"
        solution = f"{gcf}({a}x^2 + {b}x + {c})"
        steps = [
            f"Find GCF of {coef_x2}, {coef_x}, and {coef_const}",
            f"GCF = {gcf}",
            f"Factor out {gcf}:",
            f"{coef_x2}x² ÷ {gcf} = {a}x²",
            f"{coef_x}x ÷ {gcf} = {b}x",
            f"{coef_const} ÷ {gcf} = {c}",
            f"Answer: {gcf}({a}x² + {b}x + {c})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Factor with variables in GCF
        gcf_coef = random.randint(2, 4)
        gcf_power = random.randint(2, 3)
        a = random.randint(1, 4)
        b = random.randint(1, 5)
        c = random.randint(1, 5)

        highest_power = gcf_power + 2

        latex = f"\\text{{Factor: }} {gcf_coef * a}x^{highest_power} + {gcf_coef * b}x^{gcf_power + 1} + {gcf_coef * c}x^{gcf_power}"
        solution = f"{gcf_coef}x^{gcf_power}({a}x^2 + {b}x + {c})"
        steps = [
            f"Find GCF of coefficients: {gcf_coef * a}, {gcf_coef * b}, {gcf_coef * c}",
            f"GCF of coefficients = {gcf_coef}",
            f"Lowest power of x is x^{gcf_power}",
            f"GCF = {gcf_coef}x^{gcf_power}",
            f"Factor out {gcf_coef}x^{gcf_power}:",
            f"{gcf_coef}x^{gcf_power}({a}x² + {b}x + {c})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Negative GCF
        gcf = random.randint(2, 5)
        a = random.randint(1, 4)
        b = random.randint(1, 5)
        c = random.randint(1, 5)

        coef_x2 = -gcf * a
        coef_x = -gcf * b
        coef_const = -gcf * c

        latex = f"\\text{{Factor: }} {coef_x2}x^2 {coef_x:+}x {coef_const:+}"
        solution = f"-{gcf}({a}x^2 + {b}x + {c})"
        steps = [
            f"All terms are negative, factor out -{gcf}",
            f"{coef_x2}x² ÷ (-{gcf}) = {a}x²",
            f"{coef_x}x ÷ (-{gcf}) = {b}x",
            f"{coef_const} ÷ (-{gcf}) = {c}",
            f"Answer: -{gcf}({a}x² + {b}x + {c})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = IntroFactoringQuadraticsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
