"""
Quadratic Systems Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class QuadraticSystemsGenerator:
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
        # Linear and quadratic
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\begin{{cases}} y = x^2 \\\\ y = {a}x + {b} \\end{{cases}}"
        solution = "Substitute and solve quadratic equation"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Circle and line
        r = random.randint(2, 5)
        m = random.randint(1, 3)

        latex = f"\\begin{{cases}} x^2 + y^2 = {r**2} \\\\ y = {m}x \\end{{cases}}"
        solution = f"Substitute and solve for intersection points"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Two parabolas
        a = random.randint(1, 3)
        b = random.randint(1, 5)

        latex = f"\\begin{{cases}} y = x^2 \\\\ y = {a}x^2 + {b} \\end{{cases}}"
        solution = f"Set equal: x^2 = {a}x^2 + {b}, solve for x"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Ellipse and line
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        m = random.randint(1, 3)

        latex = f"\\begin{{cases}} \\frac{{x^2}}{{{a**2}}} + \\frac{{y^2}}{{{b**2}}} = 1 \\\\ y = {m}x \\end{{cases}}"
        solution = "Substitute and solve for intersection points"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = QuadraticSystemsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
