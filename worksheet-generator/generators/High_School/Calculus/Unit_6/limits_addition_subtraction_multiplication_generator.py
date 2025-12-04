"""
Limits with Addition Subtraction and Multiplication Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class LimitsAdditionSubtractionMultiplicationGenerator:
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
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(2, 4)

        latex = f"\\text{{Evaluate }} \\lim_{{x \\to {c}}} ({a}x + {b})."
        result = a * c + b
        solution = f"{result}"
        steps = [
            f"\\text{{Substitute }} x = {c}:",
            f"= {a}({c}) + {b}",
            f"= {result}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(1, 4)
        b = random.randint(1, 4)
        c = random.randint(2, 4)

        latex = f"\\text{{Evaluate }} \\lim_{{x \\to {c}}} (x^2 + {a}x - {b})."
        result = c**2 + a*c - b
        solution = f"{result}"
        steps = [
            f"= {c}^2 + {a}({c}) - {b}",
            f"= {c**2} + {a*c} - {b}",
            f"= {result}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        c = random.randint(2, 4)

        latex = f"\\text{{Evaluate }} \\lim_{{x \\to {c}}} x(x+1)."
        result = c * (c + 1)
        solution = f"{result}"
        steps = [
            f"= {c}({c}+1)",
            f"= {c} \\cdot {c+1}",
            f"= {result}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Evaluate } \\lim_{x \\to 2} (x^3 - 3x^2 + 2x)."
        solution = "0"
        steps = [
            "= 2^3 - 3(2)^2 + 2(2)",
            "= 8 - 12 + 4",
            "= 0"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = LimitsAdditionSubtractionMultiplicationGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
