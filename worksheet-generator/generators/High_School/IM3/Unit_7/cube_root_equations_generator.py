"""
Cube Root Equations Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class CubeRootEquationsGenerator:
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
        # Simple cube root
        a = random.randint(1, 5)

        latex = f"\\sqrt[3]{{x}} = {a}"
        solution = f"x = {a**3}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Cube root with addition inside
        a = random.randint(1, 9)
        b = random.randint(1, 5)

        latex = f"\\sqrt[3]{{x + {a}}} = {b}"
        solution = f"x = {b**3 - a}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Cube root with subtraction
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\sqrt[3]{{x - {a}}} = {b}"
        solution = f"x = {b**3 + a}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Cube root with coefficient
        a = random.randint(2, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)

        latex = f"{a}\\sqrt[3]{{x}} + {b} = {c}"
        solution = f"x = \\left(\\frac{{{c - b}}}{{{a}}}\\right)^3"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = CubeRootEquationsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
