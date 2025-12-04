"""
Unit Circle Introduction Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class UnitCircleIntroGenerator:
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
        # Basic quadrantal angles
        angles = [(0, 1, 0), (90, 0, 1), (180, -1, 0), (270, 0, -1)]
        angle, x, y = random.choice(angles)

        latex = f"\\text{{On unit circle, find coordinates at }} {angle}°"
        solution = f"({x}, {y})"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # 30-60-90 and 45-45-90 angles
        angles = {
            30: "(\\frac{\\sqrt{3}}{2}, \\frac{1}{2})",
            45: "(\\frac{\\sqrt{2}}{2}, \\frac{\\sqrt{2}}{2})",
            60: "(\\frac{1}{2}, \\frac{\\sqrt{3}}{2})"
        }
        angle = random.choice([30, 45, 60])

        latex = f"\\text{{Find coordinates on unit circle at }} {angle}°"
        solution = angles[angle]

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Reference angles
        quad = random.randint(2, 4)
        ref = random.choice([30, 45, 60])

        if quad == 2:
            angle = 180 - ref
        elif quad == 3:
            angle = 180 + ref
        else:
            angle = 360 - ref

        latex = f"\\text{{Find reference angle for }} {angle}°"
        solution = f"{ref}°"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Coordinates in different quadrants
        angle = random.choice([120, 135, 150, 210, 225, 240, 300, 315, 330])

        latex = f"\\text{{Find exact coordinates on unit circle at }} {angle}°"
        solution = "Use reference angle and quadrant signs"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = UnitCircleIntroGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
