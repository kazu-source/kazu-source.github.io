"""
Proofs About Inscribed Shapes Generator
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ProofsInscribedShapesGenerator:
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
        latex = "\\text{State the Inscribed Angle Theorem.}"
        solution = "Inscribed angle = (1/2) × central angle"
        steps = ["\\text{An inscribed angle is half the central angle}",
                "\\text{that subtends the same arc}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        latex = "\\text{Prove: Opposite angles of an inscribed quadrilateral are supplementary.}"
        solution = "Sum of arcs = 360°, so angles sum to 180°"
        steps = ["\\text{Let quadrilateral ABCD be inscribed in circle}",
                "\\angle A \\text{ intercepts arc BCD}, \\angle C \\text{ intercepts arc DAB}",
                "\\text{Arc BCD + arc DAB} = 360^\\circ",
                "\\angle A + \\angle C = \\frac{1}{2}(360^\\circ) = 180^\\circ"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        latex = "\\text{Prove: An angle inscribed in a semicircle is a right angle.}"
        solution = "Angle = (1/2)(180°) = 90°"
        steps = ["\\text{Let angle } \\angle ABC \\text{ be inscribed in semicircle}",
                "\\text{Arc AC is a semicircle = } 180^\\circ",
                "\\text{By Inscribed Angle Theorem:}",
                "\\angle ABC = \\frac{1}{2} \\times 180^\\circ = 90^\\circ"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Prove: Angles inscribed in same arc are congruent.}"
        solution = "Both equal half the intercepted arc"
        steps = ["\\text{Let } \\angle ABC \\text{ and } \\angle ADC \\text{ intercept same arc AC}",
                "\\text{Both angles are inscribed angles}",
                "\\angle ABC = \\frac{1}{2} \\times \\text{arc AC}",
                "\\angle ADC = \\frac{1}{2} \\times \\text{arc AC}",
                "\\text{Therefore } \\angle ABC = \\angle ADC"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = ProofsInscribedShapesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
