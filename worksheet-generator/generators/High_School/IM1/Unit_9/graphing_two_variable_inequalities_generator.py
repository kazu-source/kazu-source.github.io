"""
Graphing Two Variable Inequalities Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class GraphingTwoVariableInequalitiesGenerator:
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
        m = random.randint(1, 4)
        b = random.randint(-5, 5)

        latex = f"\\text{{Graph }} y > {m}x + {b}"
        solution = f"Dashed line y = {m}x + {b}, shade above"
        steps = [f"Draw dashed line: y = {m}x + {b}", "Use dashed line for > (not equal)", "Shade above the line (y > means above)"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        m = random.randint(1, 4)
        b = random.randint(-6, 6)

        latex = f"\\text{{Graph }} y \\leq {m}x + {b}"
        solution = f"Solid line y = {m}x + {b}, shade below"
        steps = [f"Draw solid line: y = {m}x + {b}", "Use solid line for ≤ (includes equal)", "Shade below the line (y ≤ means below/on)"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        c = random.randint(10, 25)

        latex = f"\\text{{Graph }} {a}x + {b}y < {c}"
        solution = f"Dashed line {a}x + {b}y = {c}, shade below"
        steps = [f"Rewrite as y < ...", f"Draw dashed line: {a}x + {b}y = {c}", "Shade appropriate region"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        x_val = random.randint(1, 5)
        y_val = random.randint(2, 8)
        m = random.randint(1, 3)
        b = random.randint(-4, 4)

        result = y_val - (m * x_val + b)
        is_solution = result > 0

        latex = f"\\text{{Is }} ({x_val}, {y_val}) \\text{{ a solution to }} y > {m}x + {b}?"
        if is_solution:
            solution = "Yes"
            steps = [f"Test: {y_val} > {m}({x_val}) + {b}", f"{y_val} > {m * x_val + b}", "Answer: Yes"]
        else:
            solution = "No"
            steps = [f"Test: {y_val} > {m}({x_val}) + {b}", f"{y_val} \\not> {m * x_val + b}", "Answer: No"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = GraphingTwoVariableInequalitiesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
