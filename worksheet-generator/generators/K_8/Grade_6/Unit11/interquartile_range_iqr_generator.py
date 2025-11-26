"""Interquartile Range IQR Generator - Grade 6 Unit 11"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class InterquartileRangeIqrGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        data = sorted([random.randint(10, 50) for _ in range(7)])
        q1, q3 = data[1], data[5]
        iqr = q3 - q1
        latex = f"\\text{{Data: {', '.join(map(str, data))}. Find IQR (Q3 - Q1).}}"
        return Equation(latex=latex, solution=str(iqr), steps=[f"Q1={q1}, Q3={q3}, IQR={iqr}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        data = sorted([random.randint(15, 60) for _ in range(9)])
        q1, q3 = data[2], data[6]
        iqr = q3 - q1
        latex = f"\\text{{Find IQR: {', '.join(map(str, data))}}}"
        return Equation(latex=latex, solution=str(iqr), steps=[f"Q1={q1}, Q3={q3}, IQR={iqr}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        data = sorted([random.randint(20, 80) for _ in range(11)])
        q1, q3 = data[2], data[8]
        iqr = q3 - q1
        latex = f"\\text{{Calculate IQR for: {', '.join(map(str, data[:6]))}...}}"
        return Equation(latex=latex, solution=str(iqr), steps=[f"Q1={q1}, Q3={q3}, IQR={iqr}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        data = sorted([random.randint(10, 100) for _ in range(13)])
        q1, q2, q3 = data[3], data[6], data[9]
        iqr = q3 - q1
        latex = f"\\text{{Find Q1, Q2 (median), Q3, and IQR for dataset (n=13).}}"
        return Equation(latex=latex, solution=f"Q1={q1}, Q2={q2}, Q3={q3}, IQR={iqr}", steps=[f"Q1={q1}, Q2={q2}, Q3={q3}, IQR={iqr}"], difficulty='challenge')

def main():
    gen = InterquartileRangeIqrGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
