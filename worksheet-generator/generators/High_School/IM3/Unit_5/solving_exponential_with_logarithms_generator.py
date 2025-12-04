"""
Solving Exponential Equations with Logarithms Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SolvingExponentialWithLogarithmsGenerator:
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
        # Simple exponential equation
        base = random.choice([2, 3, 5])
        value = random.randint(10, 50)

        latex = f"{base}^x = {value}"
        solution = f"x = \\log_{{{base}}} {value} = \\frac{{\\ln {value}}}{{\\ln {base}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Exponential with coefficient
        base = random.choice([2, 3, 5])
        coef = random.randint(2, 9)
        value = random.randint(20, 100)

        latex = f"{coef} \\cdot {base}^x = {value}"
        solution = f"x = \\log_{{{base}}} \\frac{{{value}}}{{{coef}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Exponential with addition
        base = random.choice([2, 3, 5])
        k = random.randint(1, 5)
        value = random.randint(20, 100)

        latex = f"{base}^{{x+{k}}} = {value}"
        solution = f"x = \\log_{{{base}}} {value} - {k}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complex exponential equation
        base = random.choice([2, 3])
        k = random.randint(2, 5)
        value = random.randint(50, 200)

        latex = f"{base}^{{{k}x}} = {value}"
        solution = f"x = \\frac{{\\log_{{{base}}} {value}}}{{{k}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = SolvingExponentialWithLogarithmsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
