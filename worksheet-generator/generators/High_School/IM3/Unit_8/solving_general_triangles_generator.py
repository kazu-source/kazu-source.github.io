"""
Solving General Triangles Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SolvingGeneralTrianglesGenerator:
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
        # ASA case
        A = random.randint(40, 70)
        B = random.randint(40, 70)
        c = random.randint(8, 15)

        latex = f"\\text{{Solve triangle: }} \\angle A = {A}°, \\angle B = {B}°, c = {c}"
        solution = f"Find C = {180-A-B}°, use law of sines for a and b"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # SAS case
        a = random.randint(8, 15)
        b = random.randint(8, 15)
        C = random.randint(50, 100)

        latex = f"\\text{{Solve triangle: }} a = {a}, b = {b}, \\angle C = {C}°"
        solution = "Use law of cosines for c, then law of sines for angles"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # SSS case
        a = random.randint(8, 15)
        b = random.randint(8, 15)
        c = random.randint(8, 15)

        latex = f"\\text{{Solve triangle: }} a = {a}, b = {b}, c = {c}"
        solution = "Use law of cosines for all three angles"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Application problem
        d = random.randint(100, 200)
        A = random.randint(30, 60)
        B = random.randint(30, 60)

        latex = f"\\text{{Two observers {d}m apart see object at angles {A}° and {B}°. Find distance to object.}}"
        solution = "Set up triangle and use law of sines"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = SolvingGeneralTrianglesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
