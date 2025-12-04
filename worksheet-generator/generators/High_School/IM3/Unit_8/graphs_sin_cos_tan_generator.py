"""
Graphs of Sin, Cos, and Tan Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class GraphsSinCosTanGenerator:
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
        # Amplitude
        a = random.randint(2, 5)

        latex = f"\\text{{Find amplitude of }} y = {a}\\sin(x)"
        solution = f"{a}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Period
        b = random.randint(2, 4)

        latex = f"\\text{{Find period of }} y = \\cos({b}x)"
        solution = f"\\frac{{2\\pi}}{{{b}}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Phase shift and vertical shift
        c = random.randint(1, 5)
        d = random.randint(1, 5)

        latex = f"\\text{{Describe transformations: }} y = \\sin(x - {c}) + {d}"
        solution = f"Phase shift right {c}, vertical shift up {d}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complete analysis
        a = random.randint(2, 4)
        b = random.randint(2, 4)
        c = random.randint(1, 5)
        d = random.randint(1, 5)

        latex = f"\\text{{Analyze }} y = {a}\\sin({b}(x - {c})) + {d}: \\text{{ amplitude, period, shifts}}"
        solution = f"Amplitude: {a}, Period: \\frac{{2\\pi}}{{{b}}}, Right {c}, Up {d}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = GraphsSinCosTanGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
