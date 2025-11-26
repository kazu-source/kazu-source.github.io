"""Box Plots Generator - Grade 6 Unit 11"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class BoxPlotsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        data = sorted([random.randint(10, 50) for _ in range(7)])
        min_val, max_val, median = data[0], data[-1], data[3]
        latex = f"\\text{{For box plot: min, max, median from: {', '.join(map(str, data))}}}"
        return Equation(latex=latex, solution=f"Min={min_val}, Max={max_val}, Median={median}", steps=[f"Min={min_val}, Max={max_val}, Median={median}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        data = sorted([random.randint(15, 70) for _ in range(9)])
        five_num = f"{data[0]}, {data[2]}, {data[4]}, {data[6]}, {data[8]}"
        latex = f"\\text{{Find 5-number summary for: {', '.join(map(str, data))}}}"
        return Equation(latex=latex, solution=five_num, steps=[f"Min, Q1, Median, Q3, Max: {five_num}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        min_val, q1, median, q3, max_val = 20, 35, 50, 65, 80
        range_val = max_val - min_val
        iqr = q3 - q1
        latex = f"\\text{{Box plot: Min={min_val}, Q1={q1}, Med={median}, Q3={q3}, Max={max_val}. Find range and IQR.}}"
        return Equation(latex=latex, solution=f"Range={range_val}, IQR={iqr}", steps=[f"Range={range_val}, IQR={iqr}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        min_val, q1, median, q3, max_val = random.randint(10, 20), random.randint(25, 35), random.randint(40, 50), random.randint(55, 65), random.randint(70, 90)
        latex = f"\\text{{Interpret: Does box plot show outliers if Min={min_val}, Q1={q1}, Med={median}, Q3={q3}, Max={max_val}?}}"
        iqr = q3 - q1
        lower_fence = q1 - 1.5 * iqr
        upper_fence = q3 + 1.5 * iqr
        has_outliers = "Yes" if (min_val < lower_fence or max_val > upper_fence) else "No"
        return Equation(latex=latex, solution=has_outliers, steps=[f"IQR={iqr}, Fences: {round(lower_fence,1)}-{round(upper_fence,1)}, Outliers: {has_outliers}"], difficulty='challenge')

def main():
    gen = BoxPlotsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
