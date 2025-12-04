"""
Systems of Inequalities Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SystemsOfInequalitiesGenerator:
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
        a = random.randint(3, 8)
        b = random.randint(5, 12)

        latex = f"\\text{{Graph the system: }} y > {a}, x < {b}"
        solution = f"Horizontal line at y={a} (shade above), vertical line at x={b} (shade left)"
        steps = [f"y > {a}: horizontal dashed line, shade above", f"x < {b}: vertical dashed line, shade left", "Solution is overlap region"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        m1 = random.randint(1, 3)
        b1 = random.randint(-4, 4)
        m2 = random.randint(-3, -1)
        b2 = random.randint(-4, 4)

        latex = f"\\text{{Graph the system: }} y \\geq {m1}x + {b1}, y < {m2}x + {b2}"
        solution = f"Graph both lines, shade overlap"
        steps = [f"First: solid line y = {m1}x + {b1}, shade above", f"Second: dashed line y = {m2}x + {b2}, shade below", "Solution is where shadings overlap"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x_val = random.randint(2, 6)
        y_val = random.randint(3, 8)
        m1 = random.randint(1, 3)
        b1 = y_val - m1 * x_val - random.randint(1, 3)
        m2 = random.randint(-3, -1)
        b2 = y_val - m2 * x_val + random.randint(1, 3)

        test1 = y_val > m1 * x_val + b1
        test2 = y_val < m2 * x_val + b2

        latex = f"\\text{{Is }} ({x_val}, {y_val}) \\text{{ a solution to }} y > {m1}x + {b1}, y < {m2}x + {b2}?"
        if test1 and test2:
            solution = "Yes"
            steps = [f"Test first: {y_val} > {m1 * x_val + b1}", f"Test second: {y_val} < {m2 * x_val + b2}", "Both true, Answer: Yes"]
        else:
            solution = "No"
            steps = [f"Test both inequalities", "At least one fails", "Answer: No"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 5)
        c1 = random.randint(15, 30)
        c2 = random.randint(10, 25)

        latex = f"\\text{{Graph: }} {a}x + {b}y \\leq {c1}, x + y \\geq {c2}"
        solution = "Graph both lines, find overlap region"
        steps = [f"Convert to slope-intercept form", f"Graph each inequality", "Solution is overlap of shaded regions"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SystemsOfInequalitiesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
