"""
Representing Quantitative Data with Dot Plots Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class RepresentingQuantitativeDotPlotsGenerator:
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
        # Small dataset
        data = sorted([random.randint(1, 10) for _ in range(8)])

        question = f"\\text{{Test scores: {', '.join(map(str, data))}}}\\\\"\
                   f"\\text{{(a) What is the minimum value?}}\\\\"\
                   f"\\text{{(b) What is the maximum value?}}\\\\"\
                   f"\\text{{(c) How many data points are there?}}"

        solution = f"(a) {min(data)}, (b) {max(data)}, (c) {len(data)}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Dataset with mode
        base = [random.randint(10, 20) for _ in range(6)]
        mode_val = random.randint(15, 18)
        data = sorted(base + [mode_val, mode_val, mode_val])

        question = f"\\text{{Number of hours studied: {', '.join(map(str, data))}}}\\\\"\
                   f"\\text{{(a) Identify the mode}}\\\\"\
                   f"\\text{{(b) What is the range?}}\\\\"\
                   f"\\text{{(c) Describe the shape (symmetric, skewed left, skewed right)}}"

        mode = mode_val
        range_val = max(data) - min(data)

        # Determine shape
        median = sorted(data)[len(data)//2]
        mean_val = sum(data) / len(data)
        if abs(mean_val - median) < 1:
            shape = "approximately symmetric"
        elif mean_val > median:
            shape = "skewed right"
        else:
            shape = "skewed left"

        solution = f"(a) {mode}, (b) {range_val}, (c) {shape}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Two datasets to compare
        data1 = sorted([random.randint(50, 70) for _ in range(10)])
        data2 = sorted([random.randint(60, 90) for _ in range(10)])

        question = f"\\text{{Class A scores: {', '.join(map(str, data1))}}}\\\\"\
                   f"\\text{{Class B scores: {', '.join(map(str, data2))}}}\\\\"\
                   f"\\text{{(a) Which class has the higher median?}}\\\\"\
                   f"\\text{{(b) Which class has greater variability?}}\\\\"\
                   f"\\text{{(c) Compare the centers and spreads.}}"

        median1 = sorted(data1)[len(data1)//2]
        median2 = sorted(data2)[len(data2)//2]
        range1 = max(data1) - min(data1)
        range2 = max(data2) - min(data2)

        higher_median = "Class B" if median2 > median1 else "Class A"
        greater_var = "Class B" if range2 > range1 else "Class A"

        solution = f"(a) {higher_median} (median {max(median1, median2)} vs {min(median1, median2)}), "\
                   f"(b) {greater_var} (range {max(range1, range2)} vs {min(range1, range2)}), "\
                   f"(c) Class B has higher center and greater spread"

        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Gap in data
        lower_group = [random.randint(10, 20) for _ in range(6)]
        upper_group = [random.randint(35, 45) for _ in range(4)]
        data = sorted(lower_group + upper_group)

        question = f"\\text{{Data values: {', '.join(map(str, data))}}}\\\\"\
                   f"\\text{{(a) Identify any gaps in the distribution}}\\\\"\
                   f"\\text{{(b) Are there any potential outliers?}}\\\\"\
                   f"\\text{{(c) What might explain this distribution pattern?}}\\\\"\
                   f"\\text{{(d) Calculate the median. Is it representative of the data?}}"

        gap_start = max(lower_group)
        gap_end = min(upper_group)
        median = sorted(data)[len(data)//2]

        solution = f"(a) Gap between {gap_start} and {gap_end}, "\
                   f"(b) Upper values ({min(upper_group)}-{max(upper_group)}) could be outliers, "\
                   f"(c) Possibly two distinct groups or measurement errors, "\
                   f"(d) Median = {median}, not very representative due to bimodal distribution"

        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = RepresentingQuantitativeDotPlotsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
