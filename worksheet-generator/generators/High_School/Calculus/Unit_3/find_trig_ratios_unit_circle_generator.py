"""
Find Trigonometric Ratios Using Unit Circle Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class FindTrigRatiosUnitCircleGenerator:
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
        special_angles = {
            "0": {"sin": "0", "cos": "1", "tan": "0"},
            "\\frac{\\pi}{6}": {"sin": "\\frac{1}{2}", "cos": "\\frac{\\sqrt{3}}{2}", "tan": "\\frac{\\sqrt{3}}{3}"},
            "\\frac{\\pi}{4}": {"sin": "\\frac{\\sqrt{2}}{2}", "cos": "\\frac{\\sqrt{2}}{2}", "tan": "1"},
            "\\frac{\\pi}{3}": {"sin": "\\frac{\\sqrt{3}}{2}", "cos": "\\frac{1}{2}", "tan": "\\sqrt{3}"},
            "\\frac{\\pi}{2}": {"sin": "1", "cos": "0", "tan": "\\text{undefined}"}
        }

        angle = random.choice(list(special_angles.keys()))
        func = random.choice(['sin', 'cos', 'tan'])

        latex = f"\\text{{Find }} \\{func}({angle})."
        solution = special_angles[angle][func]
        steps = [
            f"\\text{{Using unit circle at }} {angle}:",
            f"\\{func}({angle}) = {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        angles_q2 = {
            "\\frac{2\\pi}{3}": {"sin": "\\frac{\\sqrt{3}}{2}", "cos": "-\\frac{1}{2}"},
            "\\frac{3\\pi}{4}": {"sin": "\\frac{\\sqrt{2}}{2}", "cos": "-\\frac{\\sqrt{2}}{2}"},
            "\\frac{5\\pi}{6}": {"sin": "\\frac{1}{2}", "cos": "-\\frac{\\sqrt{3}}{2}"}
        }

        angle = random.choice(list(angles_q2.keys()))
        func = random.choice(['sin', 'cos'])

        latex = f"\\text{{Find }} \\{func}({angle})."
        solution = angles_q2[angle][func]
        steps = [
            f"\\text{{Quadrant II angle}}",
            f"\\{func}({angle}) = {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        angles_q3 = {
            "\\frac{7\\pi}{6}": {"sin": "-\\frac{1}{2}", "cos": "-\\frac{\\sqrt{3}}{2}"},
            "\\frac{5\\pi}{4}": {"sin": "-\\frac{\\sqrt{2}}{2}", "cos": "-\\frac{\\sqrt{2}}{2}"},
            "\\frac{4\\pi}{3}": {"sin": "-\\frac{\\sqrt{3}}{2}", "cos": "-\\frac{1}{2}"}
        }

        angle = random.choice(list(angles_q3.keys()))
        func = random.choice(['sin', 'cos'])

        latex = f"\\text{{Find }} \\{func}({angle})."
        solution = angles_q3[angle][func]
        steps = [
            f"\\text{{Quadrant III angle}}",
            f"\\text{{Both sin and cos are negative}}",
            f"\\{func}({angle}) = {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        angles_q4 = {
            "\\frac{5\\pi}{3}": {"sin": "-\\frac{\\sqrt{3}}{2}", "cos": "\\frac{1}{2}"},
            "\\frac{7\\pi}{4}": {"sin": "-\\frac{\\sqrt{2}}{2}", "cos": "\\frac{\\sqrt{2}}{2}"},
            "\\frac{11\\pi}{6}": {"sin": "-\\frac{1}{2}", "cos": "\\frac{\\sqrt{3}}{2}"}
        }

        angle = random.choice(list(angles_q4.keys()))
        func = random.choice(['sin', 'cos', 'tan'])

        if func == 'tan':
            sin_val = angles_q4[angle]['sin']
            cos_val = angles_q4[angle]['cos']
            solution = f"\\frac{{{sin_val}}}{{{cos_val}}}"
        else:
            solution = angles_q4[angle][func]

        latex = f"\\text{{Find }} \\{func}({angle})."
        steps = [
            f"\\text{{Quadrant IV angle}}",
            f"\\{func}({angle}) = {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = FindTrigRatiosUnitCircleGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
