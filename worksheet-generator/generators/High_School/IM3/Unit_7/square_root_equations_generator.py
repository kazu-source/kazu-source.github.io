"""
Square Root Equations Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SquareRootEquationsGenerator:
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
        # Simple square root
        a = random.randint(1, 20)

        latex = f"\\sqrt{{x}} = {a}"
        solution = f"x = {a**2}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Square root with addition inside
        a = random.randint(1, 9)
        b = random.randint(1, 9)

        latex = f"\\sqrt{{x + {a}}} = {b}"
        solution = f"x = {b**2 - a}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Square root with addition outside
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(6, 15)

        latex = f"\\sqrt{{x}} + {a} = {c}"
        solution = f"x = {(c - a)**2}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Two square roots
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\sqrt{{x + {a}}} = \\sqrt{{x}} + {b}"
        solution = f"\\text{{Square both sides and solve}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = SquareRootEquationsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
