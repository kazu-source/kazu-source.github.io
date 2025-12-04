"""
Evaluating Expressions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class EvaluatingExpressionsGenerator:
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
        a = random.randint(2, 8)
        b = random.randint(1, 12)
        x_val = random.randint(1, 5)
        result = a * x_val + b

        latex = f"\\text{{Evaluate }} {a}x + {b} \\text{{ when }} x = {x_val}"
        solution = f"{result}"
        steps = [f"Substitute x = {x_val}", f"{a}({x_val}) + {b}", f"{a * x_val} + {b}", f"= {result}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 7)
        b = random.randint(1, 10)
        c = random.randint(1, 8)
        x_val = random.randint(2, 6)
        result = a * x_val - b * x_val + c

        latex = f"\\text{{Evaluate }} {a}x - {b}x + {c} \\text{{ when }} x = {x_val}"
        solution = f"{result}"
        steps = [f"Substitute x = {x_val}", f"{a}({x_val}) - {b}({x_val}) + {c}", f"{a * x_val} - {b * x_val} + {c}", f"= {result}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(1, 8)
        c = random.randint(2, 5)
        x_val = random.randint(2, 5)
        y_val = random.randint(1, 6)
        result = a * x_val + b * y_val - c

        latex = f"\\text{{Evaluate }} {a}x + {b}y - {c} \\text{{ when }} x = {x_val}, y = {y_val}"
        solution = f"{result}"
        steps = [f"Substitute x = {x_val}, y = {y_val}", f"{a}({x_val}) + {b}({y_val}) - {c}", f"{a * x_val} + {b * y_val} - {c}", f"= {result}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 6)
        c = random.randint(1, 7)
        d = random.randint(1, 8)
        x_val = random.randint(2, 4)
        inner = b * x_val - c
        result = a * inner + d

        latex = f"\\text{{Evaluate }} {a}({b}x - {c}) + {d} \\text{{ when }} x = {x_val}"
        solution = f"{result}"
        steps = [f"Substitute x = {x_val}", f"{a}({b}({x_val}) - {c}) + {d}", f"{a}({b * x_val} - {c}) + {d}", f"{a}({inner}) + {d}", f"{a * inner} + {d}", f"= {result}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = EvaluatingExpressionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
