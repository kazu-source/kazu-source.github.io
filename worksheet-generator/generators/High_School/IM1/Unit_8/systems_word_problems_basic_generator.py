"""
Systems Word Problems Basic Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SystemsWordProblemsBasicGenerator:
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
        total = random.randint(15, 30)
        x_val = random.randint(5, 12)
        y_val = total - x_val

        latex = f"\\text{{Two numbers sum to {total}. One is {x_val}. Find the other.}}"
        solution = f"{y_val}"
        steps = [f"x + y = {total}", f"x = {x_val}", f"y = {total} - {x_val} = {y_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        total_items = random.randint(20, 40)
        x_val = random.randint(8, 18)
        y_val = total_items - x_val
        diff = abs(x_val - y_val)

        latex = f"\\text{{Total items: {total_items}. Difference: {diff}. Find each quantity.}}"
        solution = f"x = {max(x_val, y_val)}, y = {min(x_val, y_val)}"
        steps = [f"x + y = {total_items}", f"x - y = {diff}", f"Solve: x = {max(x_val, y_val)}, y = {min(x_val, y_val)}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x_val = random.randint(10, 20)
        y_val = random.randint(8, 15)
        total = x_val + y_val
        twice_diff = 2 * x_val - y_val

        latex = f"\\text{{Sum is {total}. Twice first minus second is {twice_diff}. Find both.}}"
        solution = f"x = {x_val}, y = {y_val}"
        steps = [f"x + y = {total}", f"2x - y = {twice_diff}", f"Solve system", f"x = {x_val}, y = {y_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        length = random.randint(15, 25)
        width = random.randint(8, 14)
        perimeter = 2 * (length + width)

        latex = f"\\text{{Rectangle perimeter is {perimeter}. Length is {length - width} more than width. Find dimensions.}}"
        solution = f"Length: {length}, Width: {width}"
        steps = [f"2L + 2W = {perimeter}", f"L = W + {length - width}", f"Solve: L = {length}, W = {width}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SystemsWordProblemsBasicGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
