"""
Solving Systems Graphing Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SolvingSystemsGraphingGenerator:
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
        x_val = random.randint(1, 4)
        y_val = random.randint(2, 6)

        m1 = random.randint(1, 3)
        b1 = y_val - m1 * x_val

        m2 = random.randint(-3, -1)
        b2 = y_val - m2 * x_val

        latex = f"\\text{{Solve by graphing: }} y = {m1}x + {b1}, y = {m2}x + {b2}"
        solution = f"({x_val}, {y_val})"
        steps = [f"Graph both lines", f"Lines intersect at ({x_val}, {y_val})", f"Answer: ({x_val}, {y_val})"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x_val = random.randint(2, 5)
        y_val = random.randint(3, 8)

        m1 = random.randint(1, 4)
        b1 = y_val - m1 * x_val

        m2 = -m1
        b2 = y_val - m2 * x_val

        latex = f"\\text{{Solve by graphing: }} y = {m1}x + {b1}, y = {m2}x + {b2}"
        solution = f"({x_val}, {y_val})"
        steps = [f"Line 1: slope {m1}, y-int {b1}", f"Line 2: slope {m2}, y-int {b2}", f"Intersection: ({x_val}, {y_val})"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x_val = random.randint(1, 4)
        y_val = random.randint(2, 7)

        a1 = random.randint(1, 3)
        b1 = random.randint(1, 2)
        c1 = a1 * x_val + b1 * y_val

        a2 = random.randint(2, 4)
        b2 = random.randint(1, 3)
        c2 = a2 * x_val + b2 * y_val

        latex = f"\\text{{Solve by graphing: }} {a1}x + {b1}y = {c1}, {a2}x + {b2}y = {c2}"
        solution = f"({x_val}, {y_val})"
        steps = [f"Find intercepts for each equation", f"Graph both lines", f"Intersection: ({x_val}, {y_val})"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = f"\\text{{What does the solution to a system represent on a graph?}}"
        solution = "The point where the two lines intersect"
        steps = ["Each equation is a line", "Solution satisfies both equations", "Answer: The intersection point of the lines"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SolvingSystemsGraphingGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
