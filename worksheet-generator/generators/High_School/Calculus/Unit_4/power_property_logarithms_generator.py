"""
Power Property of Logarithms Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PowerPropertyLogarithmsGenerator:
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
        base = random.randint(2, 5)
        exp = random.randint(2, 4)
        k = random.randint(2, 4)

        latex = f"\\text{{Simplify: }} \\log_{{{base}}}(x^{{{k}}})"
        solution = f"{k}\\log_{{{base}}}(x)"
        steps = [
            f"\\text{{Power property: }} \\log_b(x^k) = k\\log_b(x)",
            f"\\log_{{{base}}}(x^{{{k}}}) = {k}\\log_{{{base}}}(x)"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        base = random.randint(2, 4)
        k1 = random.randint(2, 4)
        k2 = random.randint(2, 4)

        latex = f"\\text{{Simplify: }} {k1}\\log_{{{base}}}(x) + {k2}\\log_{{{base}}}(x)"
        result = k1 + k2
        solution = f"{result}\\log_{{{base}}}(x)"
        steps = [
            f"{k1}\\log_{{{base}}}(x) + {k2}\\log_{{{base}}}(x)",
            f"= {result}\\log_{{{base}}}(x)"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        base = random.randint(2, 4)
        k = random.randint(2, 4)

        latex = f"\\text{{Expand: }} \\log_{{{base}}}(x^{{{k}}}y^2)"
        solution = f"{k}\\log_{{{base}}}(x) + 2\\log_{{{base}}}(y)"
        steps = [
            f"\\log_{{{base}}}(x^{{{k}}}y^2) = \\log_{{{base}}}(x^{{{k}}}) + \\log_{{{base}}}(y^2)",
            f"= {k}\\log_{{{base}}}(x) + 2\\log_{{{base}}}(y)"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Simplify: } 3\\ln(x) - 2\\ln(x) + \\ln(x^4)"
        solution = "5\\ln(x)"
        steps = [
            "3\\ln(x) - 2\\ln(x) + 4\\ln(x)",
            "= (3 - 2 + 4)\\ln(x)",
            "= 5\\ln(x)"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = PowerPropertyLogarithmsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
