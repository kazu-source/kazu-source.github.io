"""
Introduction to Logarithms Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class IntroLogarithmsGenerator:
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
        # Simple logarithm evaluation
        base = random.choice([2, 3, 5, 10])
        exp = random.randint(1, 4)
        value = base ** exp

        latex = f"\\log_{{{base}}} {value}"
        solution = f"{exp}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Convert between exponential and logarithmic form
        base = random.choice([2, 3, 4, 5])
        exp = random.randint(2, 4)
        value = base ** exp

        latex = f"\\text{{Write in logarithmic form: }} {base}^{{{exp}}} = {value}"
        solution = f"\\log_{{{base}}} {value} = {exp}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Solve simple logarithmic equation
        base = random.choice([2, 3, 5])
        exp = random.randint(2, 4)
        value = base ** exp

        latex = f"\\text{{Solve: }} \\log_{{{base}}} x = {exp}"
        solution = f"x = {value}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # More complex logarithm
        base = random.choice([2, 3, 4])
        exp = random.randint(-3, -1)
        value_num = 1
        value_den = base ** (-exp)

        latex = f"\\log_{{{base}}} \\frac{{1}}{{{value_den}}}"
        solution = f"{exp}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = IntroLogarithmsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
