"""
Review of Graphs Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ReviewOfGraphsGenerator:
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
                func_type = random.choice(['linear', 'quadratic'])
                if func_type == 'linear':
                    a = random.randint(1, 5)
                    b = random.randint(-5, 5)
                    latex = f"\\text{{Identify: }} y = {a}x + {b}"
                    solution = "\\text{Linear function}"
                else:
                    a = random.randint(1, 4)
                    latex = f"\\text{{Identify: }} y = x^2 + {a}"
                    solution = "\\text{Quadratic function}"
                steps = ["Identify function type", f"Answer: {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
                func = random.choice(['absolute', 'rational', 'cubic'])
                if func == 'absolute':
                    latex = "\\text{Identify: } y = |x|"
                    solution = "\\text{Absolute value function, V-shaped}"
                elif func == 'rational':
                    latex = "\\text{Identify: } y = \\frac{1}{x}"
                    solution = "\\text{Rational function, hyperbola}"
                else:
                    latex = "\\text{Identify: } y = x^3"
                    solution = "\\text{Cubic function, S-shaped}"
                steps = ["Analyze function form", f"Answer: {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
                a = random.randint(2, 5)
                b = random.randint(1, 4)
                latex = f"\\text{{Key features of }} f(x) = {a}(x - {b})^2 - {a}"
                solution = f"\\text{{Vertex: ({b}, -{a}), axis of symmetry: x = {b}, opens up}}"
                steps = [f"Vertex form", f"Vertex: ({b}, -{a})", f"Axis: x = {b}", "Opens upward"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
                a = random.randint(1, 3)
                b = random.randint(1, 4)
                c = random.randint(1, 4)
                latex = f"\\text{{Domain and range of }} f(x) = \\sqrt{{{a}x + {b}}} + {c}"
                solution = f"\\text{{Domain: }} x \\geq -{b}/{a}, \\text{{ Range: }} y \\geq {c}"
                steps = [f"Square root requires {a}x + {b} >= 0", f"Domain: x >= -{b}/{a}", f"Range: y >= {c}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = ReviewOfGraphsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
