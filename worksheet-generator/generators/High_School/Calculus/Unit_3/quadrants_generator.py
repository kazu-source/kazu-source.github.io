"""
Quadrants Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class QuadrantsGenerator:
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
        angles = [
            (30, "I"), (45, "I"), (60, "I"),
            (120, "II"), (135, "II"), (150, "II"),
            (210, "III"), (225, "III"), (240, "III"),
            (300, "IV"), (315, "IV"), (330, "IV")
        ]
        deg, quad = random.choice(angles)

        latex = f"\\text{{In which quadrant is }} {deg}^\\circ?"
        solution = f"Quadrant {quad}"
        steps = [
            f"{deg}^\\circ \\text{{ is between }} {(int(quad) if quad.isdigit() else {'I':0,'II':90,'III':180,'IV':270}[quad])}^\\circ \\text{{ and }} {(int(quad) if quad.isdigit() else {'I':90,'II':180,'III':270,'IV':360}[quad])}^\\circ" if quad in ['I','II','III','IV'] else "",
            f"\\text{{Quadrant }} {quad}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        fractions = [
            ("\\frac{\\pi}{6}", "I"), ("\\frac{\\pi}{4}", "I"), ("\\frac{\\pi}{3}", "I"),
            ("\\frac{2\\pi}{3}", "II"), ("\\frac{3\\pi}{4}", "II"), ("\\frac{5\\pi}{6}", "II"),
            ("\\frac{7\\pi}{6}", "III"), ("\\frac{5\\pi}{4}", "III"), ("\\frac{4\\pi}{3}", "III"),
            ("\\frac{5\\pi}{3}", "IV"), ("\\frac{7\\pi}{4}", "IV"), ("\\frac{11\\pi}{6}", "IV")
        ]
        angle, quad = random.choice(fractions)

        latex = f"\\text{{In which quadrant is }} {angle}?"
        solution = f"Quadrant {quad}"
        steps = [
            f"{angle} \\text{{ in radians}}",
            f"\\text{{Quadrant }} {quad}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        angle = random.randint(361, 720)
        normalized = angle % 360

        if 0 < normalized < 90:
            quad = "I"
        elif 90 < normalized < 180:
            quad = "II"
        elif 180 < normalized < 270:
            quad = "III"
        else:
            quad = "IV"

        latex = f"\\text{{In which quadrant is }} {angle}^\\circ?"
        solution = f"Quadrant {quad}"
        steps = [
            f"{angle}^\\circ - 360^\\circ = {normalized}^\\circ",
            f"\\text{{Quadrant }} {quad}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        angle = -(random.randint(30, 330))
        normalized = angle % 360

        if 0 < normalized < 90:
            quad = "I"
        elif 90 < normalized < 180:
            quad = "II"
        elif 180 < normalized < 270:
            quad = "III"
        else:
            quad = "IV"

        latex = f"\\text{{In which quadrant is }} {angle}^\\circ?"
        solution = f"Quadrant {quad}"
        steps = [
            f"\\text{{Negative angle: rotate clockwise}}",
            f"{angle}^\\circ + 360^\\circ = {normalized}^\\circ",
            f"\\text{{Quadrant }} {quad}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = QuadrantsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
