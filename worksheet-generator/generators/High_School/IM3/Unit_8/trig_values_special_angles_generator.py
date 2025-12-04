"""
Trigonometric Values of Special Angles Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class TrigValuesSpecialAnglesGenerator:
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
        # Basic special angles - sin
        values = {
            0: "0",
            30: "\\frac{1}{2}",
            45: "\\frac{\\sqrt{2}}{2}",
            60: "\\frac{\\sqrt{3}}{2}",
            90: "1"
        }

        angle = random.choice([0, 30, 45, 60, 90])

        latex = f"\\sin({angle}°)"
        solution = values[angle]

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Cosine of special angles
        values = {
            0: "1",
            30: "\\frac{\\sqrt{3}}{2}",
            45: "\\frac{\\sqrt{2}}{2}",
            60: "\\frac{1}{2}",
            90: "0"
        }

        angle = random.choice([0, 30, 45, 60, 90])

        latex = f"\\cos({angle}°)"
        solution = values[angle]

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Tangent of special angles
        values = {
            0: "0",
            30: "\\frac{\\sqrt{3}}{3}",
            45: "1",
            60: "\\sqrt{3}",
            90: "\\text{undefined}"
        }

        angle = random.choice([0, 30, 45, 60, 90])

        latex = f"\\tan({angle}°)"
        solution = values[angle]

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Special angles in other quadrants
        ref = random.choice([30, 45, 60])
        quad = random.randint(2, 4)

        if quad == 2:
            angle = 180 - ref
        elif quad == 3:
            angle = 180 + ref
        else:
            angle = 360 - ref

        func = random.choice(['sin', 'cos', 'tan'])

        latex = f"\\{func}({angle}°)"
        solution = f"Use reference angle {ref}° and quadrant {quad} signs"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = TrigValuesSpecialAnglesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
