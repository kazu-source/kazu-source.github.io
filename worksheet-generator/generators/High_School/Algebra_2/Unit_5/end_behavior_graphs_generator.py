"""
End Behavior of Graphs Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class EndBehaviorGraphsGenerator:
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
                a = random.randint(1, 5)
                b = random.randint(-10, 10)
                latex = f"\\text{{Describe end behavior of }} f(x) = {a}x + {b}"
                solution = f"\\text{{As }} x \\to \\infty, f(x) \\to \\infty; \\text{{ as }} x \\to -\\infty, f(x) \\to -\\infty"
                steps = [f"Linear with positive slope", f"Both ends go to infinity in opposite directions"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
                a = random.randint(1, 4)
                sign = random.choice([1, -1])
                a = a * sign
                latex = f"\\text{{End behavior of }} f(x) = {a}x^2"
                if a > 0:
                    solution = f"\\text{{Both ends: }} \\to +\\infty"
                else:
                    solution = f"\\text{{Both ends: }} \\to -\\infty"
                steps = [f"Even degree, leading coefficient {a}", f"Both ends go to {'positive' if a > 0 else 'negative'} infinity"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
                a = random.choice([1, -1]) * random.randint(1, 3)
                latex = f"\\text{{End behavior of }} f(x) = {a}x^3"
                if a > 0:
                    solution = f"\\text{{As }} x \\to -\\infty, y \\to -\\infty; \\text{{ as }} x \\to \\infty, y \\to \\infty"
                else:
                    solution = f"\\text{{As }} x \\to -\\infty, y \\to \\infty; \\text{{ as }} x \\to \\infty, y \\to -\\infty"
                steps = [f"Odd degree, leading coef {a}", f"Opposite end behaviors"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
                a = random.randint(1, 3)
                n = random.randint(4, 6)
                latex = f"\\text{{End behavior of }} f(x) = -{a}x^{{{n}}} + 100x^{{{n-1}}}"
                solution = f"\\text{{Dominated by }} -x^{{{n}}}, \\text{{ both ends }} \\to -\\infty"
                steps = [f"Highest degree term: -{a}x^{n}", f"Even degree, negative coefficient", f"Both ends to -infinity"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = EndBehaviorGraphsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
