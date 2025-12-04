"""
Convert Between Exponential and Logarithmic Forms Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ConvertExponentialLogarithmicGenerator:
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
        result = base ** exp

        latex = f"\\text{{Convert to logarithmic form: }} {base}^{{{exp}}} = {result}"
        solution = f"\\log_{{{base}}}({result}) = {exp}"
        steps = [
            f"\\text{{Form: }} b^y = x \\Leftrightarrow \\log_b(x) = y",
            f"\\log_{{{base}}}({result}) = {exp}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        base = random.randint(2, 5)
        x = random.randint(10, 50)
        y = random.randint(2, 4)

        latex = f"\\text{{Convert to exponential form: }} \\log_{{{base}}}({x}) = {y}"
        solution = f"{base}^{{{y}}} = {x}"
        steps = [
            f"\\text{{Form: }} \\log_b(x) = y \\Leftrightarrow b^y = x",
            f"{base}^{{{y}}} = {x}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        base = random.randint(2, 4)
        exp = random.randint(2, 3)

        latex = f"\\text{{Convert to logarithmic form: }} {base}^{{{exp}}} = x"
        solution = f"\\log_{{{base}}}(x) = {exp}"
        steps = [
            f"{base}^{{{exp}}} = x",
            f"\\log_{{{base}}}(x) = {exp}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Convert to exponential form: } \\ln(x) = 5"
        solution = "e^5 = x"
        steps = [
            "\\ln(x) = \\log_e(x) = 5",
            "e^5 = x"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = ConvertExponentialLogarithmicGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
