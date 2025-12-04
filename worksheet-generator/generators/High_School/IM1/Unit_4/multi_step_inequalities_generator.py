"""
Multi-Step Inequalities Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class MultiStepInequalitiesGenerator:
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
        b = random.randint(1, 10)
        c = random.randint(15, 30)

        latex = f"{a}x + {b} < {c}"
        solution = f"x < {(c - b) // a}"
        steps = [f"Subtract {b} from both sides", f"{a}x < {c - b}", f"Divide by {a}", f"x < {(c - b) // a}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(3, 8)
        b = random.randint(2, 10)
        c = random.randint(1, 15)

        latex = f"{a}x - {b} \\geq {c}"
        solution = f"x \\geq {(c + b) // a}"
        steps = [f"Add {b} to both sides", f"{a}x \\geq {c + b}", f"Divide by {a}", f"x \\geq {(c + b) // a}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(3, 7)
        b = random.randint(2, 8)
        c = random.randint(1, 10)

        latex = f"-{a}x + {b} > {c}"
        solution = f"x < {(b - c) // a}"
        steps = [f"Subtract {b} from both sides", f"-{a}x > {c - b}", f"Divide by -{a} (FLIP sign)", f"x < {(b - c) // a}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 6)
        c = random.randint(1, 5)
        d = random.randint(1, 4)
        e = random.randint(10, 25)

        # a(bx + c) - dx <= e
        left_x = a * b - d
        left_c = a * c
        x_val = (e - left_c) // left_x if left_x > 0 else 0

        latex = f"{a}({b}x + {c}) - {d}x \\leq {e}"
        solution = f"x \\leq {x_val}"
        steps = [f"Distribute: {a * b}x + {a * c} - {d}x \\leq {e}", f"Combine: {left_x}x + {left_c} \\leq {e}", f"Subtract {left_c}: {left_x}x \\leq {e - left_c}", f"Divide by {left_x}", f"x \\leq {x_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = MultiStepInequalitiesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
