"""
Solving Systems Substitution Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SolvingSystemsSubstitutionGenerator:
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
        x_val = random.randint(2, 6)
        y_val = random.randint(1, 5)
        a = random.randint(2, 5)
        c = a * x_val + y_val

        latex = f"\\text{{Solve: }} y = {x_val}, {a}x + y = {c}"
        solution = f"x = {x_val}, y = {y_val}"
        steps = [f"Substitute y = {x_val} into second equation", f"{a}x + {x_val} = {c}", f"{a}x = {c - x_val}", f"x = {(c - x_val)//a}", f"Actually y={x_val} so x must make it work", f"Solution: x = {x_val}, y = {y_val}"]

        # Fix logic
        x_val = random.randint(2, 6)
        y_val = random.randint(1, 5)
        a = random.randint(2, 5)
        c = a * x_val + y_val

        latex = f"\\text{{Solve: }} x = {x_val}, {a}x + y = {c}"
        solution = f"x = {x_val}, y = {y_val}"
        steps = [f"Substitute x = {x_val} into second equation", f"{a}({x_val}) + y = {c}", f"{a*x_val} + y = {c}", f"y = {y_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x_val = random.randint(2, 6)
        y_val = random.randint(1, 5)
        m = random.randint(2, 5)
        b = y_val - m * x_val
        a = random.randint(2, 4)
        c = a * x_val + y_val

        latex = f"\\text{{Solve: }} y = {m}x + {b}, {a}x + y = {c}"
        solution = f"x = {x_val}, y = {y_val}"
        steps = [f"Substitute y = {m}x + {b} into second equation", f"{a}x + ({m}x + {b}) = {c}", f"{a+m}x + {b} = {c}", f"{a+m}x = {c-b}", f"x = {x_val}, y = {y_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x_val = random.randint(2, 5)
        y_val = random.randint(3, 8)

        a1 = random.randint(2, 4)
        b1 = random.randint(1, 3)
        c1 = a1 * x_val + b1 * y_val

        a2 = random.randint(1, 3)
        c2 = a2 * x_val + y_val

        latex = f"\\text{{Solve: }} {a2}x + y = {c2}, {a1}x + {b1}y = {c1}"
        solution = f"x = {x_val}, y = {y_val}"
        steps = [f"Solve first for y: y = {c2} - {a2}x", f"Substitute into second equation", f"Solve for x, then find y", f"x = {x_val}, y = {y_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        x_val = random.randint(3, 7)
        y_val = random.randint(2, 6)

        a1 = random.randint(2, 4)
        b1 = random.randint(2, 4)
        c1 = a1 * x_val + b1 * y_val

        a2 = random.randint(2, 5)
        b2 = random.randint(1, 3)
        c2 = a2 * x_val + b2 * y_val

        latex = f"\\text{{Solve: }} {a1}x + {b1}y = {c1}, {a2}x + {b2}y = {c2}"
        solution = f"x = {x_val}, y = {y_val}"
        steps = [f"Solve first equation for x or y", f"Substitute into second equation", f"Solve the resulting equation", f"x = {x_val}, y = {y_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SolvingSystemsSubstitutionGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
