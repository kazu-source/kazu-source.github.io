"""
Evaluating After Simplifying Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class EvaluatingAfterSimplifyingGenerator:
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
        a = random.randint(2, 7)
        b = random.randint(1, 6)
        c = random.randint(1, 8)
        x_val = random.randint(2, 5)

        combined = a + b
        result = combined * x_val + c

        latex = f"\\text{{Simplify then evaluate }} {a}x + {b}x + {c} \\text{{ when }} x = {x_val}"
        solution = f"{result}"
        steps = [f"Simplify: {a}x + {b}x = {combined}x", f"Expression: {combined}x + {c}", f"Substitute x = {x_val}", f"{combined}({x_val}) + {c} = {combined*x_val} + {c} = {result}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(2, 7)
        c = random.randint(1, 5)
        d = random.randint(1, 8)
        x_val = random.randint(2, 4)

        x_coef = a + b
        const = c + d
        result = x_coef * x_val + const

        latex = f"\\text{{Simplify then evaluate }} {a}x + {c} + {b}x + {d} \\text{{ when }} x = {x_val}"
        solution = f"{result}"
        steps = [f"Combine x: {a}x + {b}x = {x_coef}x", f"Combine constants: {c} + {d} = {const}", f"Simplified: {x_coef}x + {const}", f"Substitute x = {x_val}: {x_coef}({x_val}) + {const} = {result}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 6)
        c = random.randint(1, 5)
        d = random.randint(1, 4)
        e = random.randint(1, 7)
        x_val = random.randint(2, 4)

        x2_coef = a + c
        x1_coef = b
        result = x2_coef * (x_val ** 2) + x1_coef * x_val + (d + e)

        latex = f"\\text{{Simplify then evaluate }} {a}x^2 + {b}x + {c}x^2 + {d} + {e} \\text{{ when }} x = {x_val}"
        solution = f"{result}"
        steps = [f"Combine x^2: {a}x^2 + {c}x^2 = {x2_coef}x^2", f"Combine constants: {d} + {e} = {d+e}", f"Simplified: {x2_coef}x^2 + {b}x + {d+e}", f"Substitute x = {x_val}: {x2_coef}({x_val}^2) + {b}({x_val}) + {d+e} = {result}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(2, 5)
        c = random.randint(1, 4)
        d = random.randint(1, 6)
        x_val = random.randint(2, 3)

        # a(bx + c) + dx
        distributed_x = a * b + d
        distributed_c = a * c
        result = distributed_x * x_val + distributed_c

        latex = f"\\text{{Simplify then evaluate }} {a}({b}x + {c}) + {d}x \\text{{ when }} x = {x_val}"
        solution = f"{result}"
        steps = [f"Distribute: {a}({b}x + {c}) = {a*b}x + {a*c}", f"Add {d}x: {a*b}x + {d}x = {distributed_x}x", f"Simplified: {distributed_x}x + {distributed_c}", f"Substitute x = {x_val}: {distributed_x}({x_val}) + {distributed_c} = {result}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = EvaluatingAfterSimplifyingGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
