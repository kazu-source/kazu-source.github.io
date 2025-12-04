"""
Checking Answer Plugin Logic Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class CheckingAnswerPluginLogicGenerator:
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
        x_val = random.randint(3, 8)
        y_val = random.randint(2, 7)
        c = 2 * x_val + y_val

        latex = f"\\text{{Verify }} ({x_val}, {y_val}) \\text{{ solves }} 2x + y = {c}"
        solution = "Yes, it works"
        steps = [f"Substitute: 2({x_val}) + {y_val}", f"= {2 * x_val} + {y_val}", f"= {c} ✓"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        x_val = random.randint(2, 6)
        y_val = random.randint(3, 8)

        c1 = x_val + y_val
        c2 = 3 * x_val - y_val

        latex = f"\\text{{Verify }} ({x_val}, {y_val}) \\text{{ in }} x + y = {c1}, 3x - y = {c2}"
        solution = "Yes, both work"
        steps = [f"First: {x_val} + {y_val} = {c1} ✓", f"Second: 3({x_val}) - {y_val} = {3*x_val} - {y_val} = {c2} ✓", "Solution verified"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x_val = random.randint(4, 9)
        y_val = random.randint(2, 6)
        wrong_y = y_val + random.randint(1, 3)

        c1 = 2 * x_val + y_val
        c2 = x_val - wrong_y

        latex = f"\\text{{Does }} ({x_val}, {wrong_y}) \\text{{ solve }} 2x + y = {c1}, x - y = {c2}?"
        solution = "No"
        steps = [f"First: 2({x_val}) + {wrong_y} = {2*x_val + wrong_y} ≠ {c1}", "First equation fails", "Answer: No"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        latex = f"\\text{{Why is it important to check your solution in the original equations?}}"
        solution = "To verify no errors were made during solving"
        steps = ["Algebra mistakes can happen", "Checking confirms the solution is correct", "Both equations must be satisfied"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = CheckingAnswerPluginLogicGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
