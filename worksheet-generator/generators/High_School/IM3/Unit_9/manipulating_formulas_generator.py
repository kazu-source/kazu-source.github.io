"""
Manipulating Formulas Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ManipulatingFormulasGenerator:
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
        # Solve for variable in linear equation
        latex = "\\text{Solve for } w: P = 2l + 2w"
        solution = "w = \\frac{P - 2l}{2}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Solve for variable with exponents
        latex = "\\text{Solve for } r: A = \\pi r^2"
        solution = "r = \\sqrt{\\frac{A}{\\pi}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Solve for variable in rational equation
        latex = "\\text{Solve for } t: d = \\frac{1}{2}at^2 + v_0t"
        solution = "\\text{Use quadratic formula to solve for } t"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complex formula manipulation
        latex = "\\text{Solve for } h: V = \\frac{1}{3}\\pi r^2 h"
        solution = "h = \\frac{3V}{\\pi r^2}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = ManipulatingFormulasGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
