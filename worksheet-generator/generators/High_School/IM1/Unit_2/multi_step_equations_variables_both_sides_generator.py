"""
Multi-Step Equations Variables Both Sides Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class MultiStepEquationsVariablesBothSidesGenerator:
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
        a = random.randint(4, 8)
        b = random.randint(2, 6)
        c = random.randint(5, 12)
        d = random.randint(1, 8)

        x_val = (c - d) // (a - b)

        latex = f"{a}x + {d} = {b}x + {c}"
        solution = f"x = {x_val}"
        steps = [f"Subtract {b}x from both sides", f"{a - b}x + {d} = {c}", f"Subtract {d} from both sides", f"{a - b}x = {c - d}", f"Divide by {a - b}", f"x = {x_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 6)
        c = random.randint(1, 5)
        d = random.randint(3, 8)
        e = random.randint(10, 25)

        # a(bx + c) = dx + e
        left_x = a * b
        left_c = a * c
        x_val = (e - left_c) // (left_x - d)

        latex = f"{a}({b}x + {c}) = {d}x + {e}"
        solution = f"x = {x_val}"
        steps = [f"Distribute: {left_x}x + {left_c} = {d}x + {e}", f"Subtract {d}x: {left_x - d}x + {left_c} = {e}", f"Subtract {left_c}: {left_x - d}x = {e - left_c}", f"Divide by {left_x - d}", f"x = {x_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(2, 5)
        c = random.randint(1, 4)
        d = random.randint(2, 4)
        e = random.randint(2, 5)
        f = random.randint(1, 4)

        # a(bx + c) = d(ex - f)
        left_x = a * b
        left_c = a * c
        right_x = d * e
        right_c = -d * f

        x_val = (right_c - left_c) // (left_x - right_x)

        latex = f"{a}({b}x + {c}) = {d}({e}x - {f})"
        solution = f"x = {x_val}"
        steps = [f"Distribute left: {left_x}x + {left_c}", f"Distribute right: {right_x}x - {d * f}", f"{left_x}x + {left_c} = {right_x}x - {d * f}", f"Subtract {right_x}x: {left_x - right_x}x + {left_c} = -{d * f}", f"Subtract {left_c}: {left_x - right_x}x = {right_c - left_c}", f"x = {x_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(2, 4)
        c = random.randint(1, 3)
        d = random.randint(2, 4)
        e = random.randint(2, 4)
        f = random.randint(1, 3)
        g = random.randint(1, 5)

        # a(bx + c) + g = d(ex - f)
        left_x = a * b
        left_c = a * c + g
        right_x = d * e
        right_c = -d * f

        x_val = (right_c - left_c) // (left_x - right_x) if (left_x - right_x) != 0 else 1

        latex = f"{a}({b}x + {c}) + {g} = {d}({e}x - {f})"
        solution = f"x = {x_val}"
        steps = [f"Distribute: {left_x}x + {a * c} + {g} = {right_x}x - {d * f}", f"Simplify left: {left_x}x + {left_c} = {right_x}x - {d * f}", f"Subtract {right_x}x: {left_x - right_x}x + {left_c} = -{d * f}", f"Solve for x", f"x = {x_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = MultiStepEquationsVariablesBothSidesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
