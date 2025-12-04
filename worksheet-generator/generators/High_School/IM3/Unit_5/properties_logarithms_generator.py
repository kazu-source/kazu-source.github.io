"""
Properties of Logarithms Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PropertiesLogarithmsGenerator:
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
        # Product rule
        a = random.randint(2, 9)
        b = random.randint(2, 9)

        latex = f"\\text{{Simplify: }} \\log({a}) + \\log({b})"
        solution = f"\\log({a*b})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Quotient rule
        a = random.randint(10, 99)
        b = random.randint(2, 9)

        latex = f"\\text{{Simplify: }} \\log({a}) - \\log({b})"
        solution = f"\\log\\left(\\frac{{{a}}}{{{b}}}\\right)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Power rule
        a = random.randint(2, 9)
        n = random.randint(2, 5)

        latex = f"\\text{{Simplify: }} \\log({a}^{{{n}}})"
        solution = f"{n}\\log({a})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Combined properties
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        n = random.randint(2, 4)

        latex = f"\\text{{Expand: }} \\log\\left(\\frac{{{a}^{{{n}}}}}{{{b}}}\\right)"
        solution = f"{n}\\log({a}) - \\log({b})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = PropertiesLogarithmsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
