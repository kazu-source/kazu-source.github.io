"""
Domain and Range of Exponential and Logarithmic Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class DomainRangeExponentialLogarithmicGenerator:
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
        a = random.randint(2, 5)

        latex = f"\\text{{Find the domain of }} f(x) = {a}^x."
        solution = "(-\\infty, \\infty)"
        steps = [
            "\\text{Exponential functions are defined for all real numbers}",
            "\\text{Domain: } (-\\infty, \\infty)"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 5)

        latex = f"\\text{{Find the range of }} f(x) = {a}^x."
        solution = "(0, \\infty)"
        steps = [
            f"\\text{{Exponential }} {a}^x \\text{{ is always positive}}",
            "\\text{As } x \\to -\\infty, f(x) \\to 0",
            "\\text{As } x \\to \\infty, f(x) \\to \\infty",
            "\\text{Range: } (0, \\infty)"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\text{Find the domain of } f(x) = \\log(x)."
        solution = "(0, \\infty)"
        steps = [
            "\\text{Logarithm requires positive argument}",
            "x > 0",
            "\\text{Domain: } (0, \\infty)"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 5)

        latex = f"\\text{{Find domain and range of }} f(x) = \\log(x - {a})."
        solution = f"Domain: ({a}, \\infty), Range: (-\\infty, \\infty)"
        steps = [
            f"x - {a} > 0 \\Rightarrow x > {a}",
            f"\\text{{Domain: }} ({a}, \\infty)",
            "\\text{Range of log is all reals}",
            "\\text{Range: } (-\\infty, \\infty)"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = DomainRangeExponentialLogarithmicGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
