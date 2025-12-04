"""
Law of Cosines Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class LawOfCosinesGenerator:
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
        # Find side given SAS
        b = random.randint(5, 12)
        c = random.randint(5, 12)
        A = random.randint(40, 80)

        latex = f"\\text{{Given }} b = {b}, c = {c}, \\angle A = {A}°\\text{{, find }} a"
        solution = f"a^2 = {b}^2 + {c}^2 - 2({b})({c})\\cos({A}°)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Find angle given SSS
        a = random.randint(5, 10)
        b = random.randint(5, 10)
        c = random.randint(5, 10)

        latex = f"\\text{{Given }} a = {a}, b = {b}, c = {c}\\text{{, find }} \\angle C"
        solution = f"\\cos(C) = \\frac{{{a}^2 + {b}^2 - {c}^2}}{{2({a})({b})}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Complete triangle given SAS
        a = random.randint(8, 15)
        b = random.randint(8, 15)
        C = random.randint(50, 100)

        latex = f"\\text{{Given }} a = {a}, b = {b}, \\angle C = {C}°\\text{{, find }} c \\text{{ and other angles}}"
        solution = f"c^2 = {a}^2 + {b}^2 - 2({a})({b})\\cos({C}°)"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Application problem
        a = random.randint(10, 20)
        b = random.randint(10, 20)
        c = random.randint(10, 20)

        latex = f"\\text{{Triangle with sides }} {a}, {b}, {c}\\text{{. Find largest angle.}}"
        solution = "Largest angle opposite longest side, use law of cosines"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = LawOfCosinesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
