"""
Graphical Representations of Summary Statistics Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class GraphicalRepresentationsSummaryStatisticsGenerator:
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
        min_val, q1, med, q3, max_val = 10, 20, 30, 40, 50
        question = f"\\text{{Box plot shows: Min={min_val}, Q1={q1}, Med={med}, Q3={q3}, Max={max_val}}}\\\\"\
                   f"\\text{{What is the IQR?}}"
        solution = f"IQR = {q3 - q1}"
        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        min_val, q1, med, q3, max_val = 15, 25, 35, 50, 60
        question = f"\\text{{Five-number summary: {min_val}, {q1}, {med}, {q3}, {max_val}}}\\\\"\
                   f"\\text{{(a) Which quarter of data has most variability?}}\\\\"\
                   f"\\text{{(b) Calculate IQR}}"
        q4_spread = max_val - q3
        solution = f"(a) Q4 (from {q3} to {max_val}, spread of {q4_spread}), (b) IQR = {q3-q1}"
        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        question = f"\\text{{Box plot A: symmetric with IQR=20}}\\\\"\
                   f"\\text{{Box plot B: right-skewed with IQR=20}}\\\\"\
                   f"\\text{{(a) How do they differ visually?}}\\\\"\
                   f"\\text{{(b) What does skewness tell about mean vs median?}}"
        solution = "(a) B has longer right whisker/tail; median not centered in box, "\
                   "(b) Right-skewed: mean > median due to high outliers"
        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        question = f"\\text{{Create a box plot from: 5,7,8,10,12,15,18,20,22,25,30}}\\\\"\
                   f"\\text{{(a) Find five-number summary}}\\\\"\
                   f"\\text{{(b) Check for outliers using 1.5xIQR rule}}\\\\"\
                   f"\\text{{(c) Describe the shape}}"
        data = [5,7,8,10,12,15,18,20,22,25,30]
        solution = "(a) Min=5, Q1=8.5, Med=15, Q3=21, Max=30, (b) Bounds: -10.25 to 39.75, no outliers, (c) Slight right skew"
        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = GraphicalRepresentationsSummaryStatisticsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
