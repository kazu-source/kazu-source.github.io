"""
Effects of Linear Transformations on Shape Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class EffectsLinearTransformationsShapeGenerator:
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
        question = f"\\text{{A distribution is skewed right. If we add 10 to each value,}}\\\\"\
                   f"\\text{{what happens to the shape?}}"

        solution = "Shape stays skewed right (adding constant preserves shape)"

        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        question = f"\\text{{A symmetric distribution has mean 50 and std dev 5.}}\\\\"\
                   f"\\text{{Transform: y = 2x - 10. Describe new distribution's shape.}}"

        solution = "Still symmetric (linear transformations preserve shape)"

        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        question = f"\\text{{Distribution is bimodal with peaks at 20 and 40.}}\\\\"\
                   f"\\text{{Transform: y = 3x + 5}}\\\\"\
                   f"\\text{{(a) Where are the new peaks?}}\\\\"\
                   f"\\text{{(b) Is it still bimodal?}}"

        peak1_new = 3 * 20 + 5
        peak2_new = 3 * 40 + 5

        solution = f"(a) Peaks at {peak1_new} and {peak2_new}, (b) Yes, still bimodal"

        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        question = f"\\text{{Explain why linear transformations y = ax + b (a > 0) preserve shape}}\\\\"\
                   f"\\text{{but y = x^2 does not. Use the concept of relative positions.}}"

        solution = "Linear transformations multiply all distances by same factor |a| and shift by b, "\
                   "preserving relative positions. Nonlinear transformations like x^2 change relative "\
                   "distances (e.g., gap from 1 to 2 becomes gap from 1 to 4), distorting shape"

        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = EffectsLinearTransformationsShapeGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
