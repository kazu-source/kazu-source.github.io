"""
Horizontal Vertical Lines Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class HorizontalVerticalLinesGenerator:
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
        k = random.randint(-8, 8)

        latex = f"\\text{{What is the equation of a horizontal line through }} y = {k}?"
        solution = f"y = {k}"
        steps = ["Horizontal lines have form y = k", f"Answer: y = {k}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        k = random.randint(-8, 8)

        latex = f"\\text{{What is the equation of a vertical line through }} x = {k}?"
        solution = f"x = {k}"
        steps = ["Vertical lines have form x = k", f"Answer: x = {k}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        x_val = random.randint(-6, 6)
        y_val = random.randint(-6, 6)

        line_type = random.choice(['horizontal', 'vertical'])
        if line_type == 'horizontal':
            latex = f"\\text{{Write the equation of the horizontal line through }} ({x_val}, {y_val})"
            solution = f"y = {y_val}"
            steps = ["Horizontal line has constant y-value", f"Answer: y = {y_val}"]
        else:
            latex = f"\\text{{Write the equation of the vertical line through }} ({x_val}, {y_val})"
            solution = f"x = {x_val}"
            steps = ["Vertical line has constant x-value", f"Answer: x = {x_val}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        k = random.randint(-5, 5)

        latex = f"\\text{{What is the slope of the line }} y = {k}?"
        solution = "0"
        steps = [f"y = {k} is a horizontal line", "Horizontal lines have slope 0", "Answer: 0"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = HorizontalVerticalLinesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
