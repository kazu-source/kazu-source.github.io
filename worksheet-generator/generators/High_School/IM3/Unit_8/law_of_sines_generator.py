"""
Law of Sines Generator
"""
import random
from typing import List
import sys
import os
import math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class LawOfSinesGenerator:
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
        # Find side given two angles and one side
        A = random.randint(30, 80)
        B = random.randint(30, 80)
        a = random.randint(5, 15)

        latex = f"\\text{{Given }} \\angle A = {A}°, \\angle B = {B}°, a = {a}\\text{{, find }} b"
        solution = f"b = \\frac{{{a} \\sin({B}°)}}{{\\sin({A}°)}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Find angle given two sides and one angle
        A = random.randint(30, 60)
        a = random.randint(5, 15)
        b = random.randint(5, 15)

        latex = f"\\text{{Given }} \\angle A = {A}°, a = {a}, b = {b}\\text{{, find }} \\angle B"
        solution = f"\\sin(B) = \\frac{{{b} \\sin({A}°)}}{{{a}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Complete triangle given AAS
        A = random.randint(40, 70)
        B = random.randint(40, 70)
        C = 180 - A - B
        a = random.randint(8, 15)

        latex = f"\\text{{Given }} \\angle A = {A}°, \\angle B = {B}°, a = {a}\\text{{, find }} b \\text{{ and }} c"
        solution = f"\\angle C = {C}°, \\text{{ use law of sines for }} b \\text{{ and }} c"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Ambiguous case (SSA)
        A = random.randint(30, 50)
        a = random.randint(8, 12)
        b = random.randint(10, 15)

        latex = f"\\text{{Given }} \\angle A = {A}°, a = {a}, b = {b}\\text{{, how many triangles?}}"
        solution = "Check if ambiguous case applies (SSA)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = LawOfSinesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
