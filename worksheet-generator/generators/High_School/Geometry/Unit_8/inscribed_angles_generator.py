"""
Inscribed Angles Generator
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class InscribedAnglesGenerator:
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
        central = random.randint(60, 140)
        inscribed = central / 2
        latex = f"\\text{{Central angle measures }} {central}^\\circ. \\text{{ Find inscribed angle intercepting same arc.}}"
        solution = f"{inscribed}°"
        steps = ["\\text{Inscribed Angle Theorem: inscribed angle = } \\frac{1}{2} \\text{ central angle}",
                f"= \\frac{{{central}}}{{2}} = {inscribed}^\\circ"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        inscribed = random.randint(30, 80)
        central = 2 * inscribed
        latex = f"\\text{{Inscribed angle measures }} {inscribed}^\\circ. \\text{{ Find central angle intercepting same arc.}}"
        solution = f"{central}°"
        steps = ["\\text{Central angle = } 2 \\times \\text{ inscribed angle}",
                f"= 2 \\times {inscribed}^\\circ = {central}^\\circ"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        arc = random.randint(100, 180)
        inscribed = arc / 2
        latex = f"\\text{{An inscribed angle intercepts an arc of }} {arc}^\\circ. \\text{{ Find the inscribed angle.}}"
        solution = f"{inscribed}°"
        steps = ["\\text{Inscribed angle = } \\frac{1}{2} \\text{ intercepted arc}",
                f"= \\frac{{{arc}}}{{2}} = {inscribed}^\\circ"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = "\\text{Prove: An angle inscribed in a semicircle is a right angle.}"
        solution = "Inscribed angle = (1/2)(180°) = 90°"
        steps = ["\\text{Semicircle forms an arc of } 180^\\circ",
                "\\text{Inscribed angle = } \\frac{1}{2} \\times 180^\\circ = 90^\\circ",
                "\\text{Therefore, angle inscribed in semicircle is always a right angle}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    gen = InscribedAnglesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
