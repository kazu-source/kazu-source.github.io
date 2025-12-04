"""
Modeling with Multiple Variables Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ModelingMultipleVariablesGenerator:
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
        # Function of multiple variables
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\text{{If }} f(x,y) = {a}x + {b}y\\text{{, find }} f(2,3)"
        solution = f"{2*a + 3*b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Surface area or volume formula
        latex = "\\text{Write surface area of rectangular prism: length } l\\text{, width } w\\text{, height } h"
        solution = "SA = 2(lw + lh + wh)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Optimization with constraints
        latex = "\\text{Maximize } A = xy \\text{ subject to } 2x + 2y = 100"
        solution = "\\text{Substitute } y = 50 - x\\text{, then maximize}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complex multivariable function
        latex = "\\text{If } V = \\frac{1}{3}\\pi r^2 h\\text{, express } r \\text{ in terms of } V \\text{ and } h"
        solution = "r = \\sqrt{\\frac{3V}{\\pi h}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = ModelingMultipleVariablesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
