"""
Radians Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class RadiansGenerator:
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
        # Convert simple degrees to radians
        degrees = random.choice([30, 45, 60, 90, 120, 135, 150, 180])

        conversions = {
            30: "\\frac{\\pi}{6}",
            45: "\\frac{\\pi}{4}",
            60: "\\frac{\\pi}{3}",
            90: "\\frac{\\pi}{2}",
            120: "\\frac{2\\pi}{3}",
            135: "\\frac{3\\pi}{4}",
            150: "\\frac{5\\pi}{6}",
            180: "\\pi"
        }

        latex = f"\\text{{Convert to radians: }} {degrees}°"
        solution = conversions[degrees]

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Convert radians to degrees
        radians = {
            "\\frac{\\pi}{6}": 30,
            "\\frac{\\pi}{4}": 45,
            "\\frac{\\pi}{3}": 60,
            "\\frac{2\\pi}{3}": 120,
            "\\frac{3\\pi}{4}": 135
        }

        rad, deg = random.choice(list(radians.items()))

        latex = f"\\text{{Convert to degrees: }} {rad}"
        solution = f"{deg}°"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Less common conversions
        degrees = random.choice([210, 225, 240, 270, 300, 315, 330, 360])

        conversions = {
            210: "\\frac{7\\pi}{6}",
            225: "\\frac{5\\pi}{4}",
            240: "\\frac{4\\pi}{3}",
            270: "\\frac{3\\pi}{2}",
            300: "\\frac{5\\pi}{3}",
            315: "\\frac{7\\pi}{4}",
            330: "\\frac{11\\pi}{6}",
            360: "2\\pi"
        }

        latex = f"\\text{{Convert to radians: }} {degrees}°"
        solution = conversions[degrees]

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Arc length or sector area
        r = random.randint(3, 10)
        theta_deg = random.choice([60, 90, 120])
        theta_conversions = {60: "\\frac{\\pi}{3}", 90: "\\frac{\\pi}{2}", 120: "\\frac{2\\pi}{3}"}

        latex = f"\\text{{Find arc length: }} r = {r}, \\theta = {theta_deg}°"
        solution = f"s = {r} \\cdot {theta_conversions[theta_deg]}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = RadiansGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
