"""
Evaluate Logarithms Using Properties Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class EvaluateLogarithmsPropertiesGenerator:
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
        base = random.choice([2, 3, 5])

        latex = f"\\text{{Evaluate: }} \\log_{{{base}}}({base}^2) + \\log_{{{base}}}({base}^3)"
        solution = "5"
        steps = [
            f"\\log_{{{base}}}({base}^2) = 2",
            f"\\log_{{{base}}}({base}^3) = 3",
            "2 + 3 = 5"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        base = random.choice([2, 3])
        val1 = base ** 3
        val2 = base ** 2

        latex = f"\\text{{Evaluate: }} \\log_{{{base}}}({val1}) - \\log_{{{base}}}({val2})"
        solution = "1"
        steps = [
            f"= \\log_{{{base}}}\\left(\\frac{{{val1}}}{{{val2}}}\\right)",
            f"= \\log_{{{base}}}({base})",
            "= 1"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\text{Evaluate: } \\log_2(8) + \\log_2(4) - \\log_2(16)"
        solution = "1"
        steps = [
            "\\log_2(8) = 3",
            "\\log_2(4) = 2",
            "\\log_2(16) = 4",
            "3 + 2 - 4 = 1"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Evaluate: } 2\\log_3(9) + \\log_3(27) - \\log_3(3)"
        solution = "6"
        steps = [
            "2\\log_3(9) = 2(2) = 4",
            "\\log_3(27) = 3",
            "\\log_3(3) = 1",
            "4 + 3 - 1 = 6"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = EvaluateLogarithmsPropertiesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
