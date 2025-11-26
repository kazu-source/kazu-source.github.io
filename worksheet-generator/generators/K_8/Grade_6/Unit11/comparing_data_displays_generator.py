"""Comparing Data Displays Generator - Grade 6 Unit 11"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class ComparingDataDisplaysGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        displays = ["dot plot", "bar graph", "histogram", "box plot"]
        best = random.choice(["histogram", "dot plot"])
        latex = f"\\text{{Best display for showing distribution of test scores?}}"
        return Equation(latex=latex, solution=best, steps=[f"{best} shows distribution well"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        latex = f"\\text{{Which shows median, quartiles, and outliers: histogram or box plot?}}"
        return Equation(latex=latex, solution="Box plot", steps=["Box plot shows 5-number summary"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        data_a = sorted([random.randint(10, 40) for _ in range(7)])
        data_b = sorted([random.randint(15, 45) for _ in range(7)])
        median_a, median_b = data_a[3], data_b[3]
        higher = "Dataset A" if median_a > median_b else "Dataset B"
        latex = f"\\text{{Which has higher median? A: median={median_a}, B: median={median_b}}}"
        return Equation(latex=latex, solution=higher, steps=[f"{higher} has higher median"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        latex = f"\\text{{Explain when to use histogram vs box plot for displaying data.}}"
        return Equation(latex=latex, solution="Histogram: frequency distribution; Box plot: quartiles and outliers", steps=["Different purposes"], difficulty='challenge')

def main():
    gen = ComparingDataDisplaysGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
