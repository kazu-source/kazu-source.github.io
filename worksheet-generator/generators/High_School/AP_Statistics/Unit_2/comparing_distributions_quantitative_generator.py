"""
Comparing Distributions of Quantitative Data Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ComparingDistributionsQuantitativeGenerator:
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
        # Two simple datasets
        data_a = [12, 14, 15, 16, 18]
        data_b = [20, 22, 24, 25, 28]

        question = f"\\text{{Group A: {', '.join(map(str, data_a))}}}\\\\"\
                   f"\\text{{Group B: {', '.join(map(str, data_b))}}}\\\\"\
                   f"\\text{{Which group has the higher center?}}"

        median_a = sorted(data_a)[len(data_a)//2]
        median_b = sorted(data_b)[len(data_b)//2]

        solution = f"Group B (median {median_b} vs {median_a})"

        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Two datasets with different spreads
        data_1 = sorted([random.randint(40, 60) for _ in range(10)])
        data_2 = sorted([random.randint(45, 55) for _ in range(10)])

        question = f"\\text{{Class 1: {', '.join(map(str, data_1))}}}\\\\"\
                   f"\\text{{Class 2: {', '.join(map(str, data_2))}}}\\\\"\
                   f"\\text{{Compare the distributions using center and spread.}}"

        median_1 = data_1[len(data_1)//2]
        median_2 = data_2[len(data_2)//2]
        range_1 = max(data_1) - min(data_1)
        range_2 = max(data_2) - min(data_2)

        solution = f"Centers are similar (Class 1 median: {median_1}, Class 2 median: {median_2}); "\
                   f"Class 1 has greater spread (range {range_1} vs {range_2})"

        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Parallel box plots comparison
        group1_min = 20
        group1_q1 = 30
        group1_med = 40
        group1_q3 = 50
        group1_max = 60

        group2_min = 35
        group2_q1 = 42
        group2_med = 48
        group2_q3 = 55
        group2_q3 = 62

        question = f"\\text{{Box plot summaries:}}\\\\"\
                   f"\\text{{Group 1: Min={group1_min}, Q1={group1_q1}, Med={group1_med}, Q3={group1_q3}, Max={group1_max}}}\\\\"\
                   f"\\text{{Group 2: Min={group2_min}, Q1={group2_q1}, Med={group2_med}, Q3={group2_q3}, Max=62}}\\\\"\
                   f"\\text{{(a) Which group has higher center?}}\\\\"\
                   f"\\text{{(b) Which has greater variability (use IQR)?}}\\\\"\
                   f"\\text{{(c) Write a complete comparison.}}"

        iqr1 = group1_q3 - group1_q1
        iqr2 = 62 - group2_q1

        solution = f"(a) Group 2 (median 48 vs 40), "\
                   f"(b) Group 1 has greater variability (IQR {iqr1} vs {iqr2-group2_q3}), "\
                   f"(c) Group 2 has higher center but Group 1 has more spread; both roughly symmetric"

        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Three groups comparison
        question = f"\\text{{Histograms for three treatment groups show:}}\\\\"\
                   f"\\text{{Group A: Symmetric, centered at 50, range 40-60}}\\\\"\
                   f"\\text{{Group B: Skewed right, median 45, range 35-70}}\\\\"\
                   f"\\text{{Group C: Skewed left, median 55, range 40-65}}\\\\"\
                   f"\\text{{(a) Rank groups by center (use appropriate measure)}}\\\\"\
                   f"\\text{{(b) Which group has most variability?}}\\\\"\
                   f"\\text{{(c) For which group(s) is mean likely different from median?}}\\\\"\
                   f"\\text{{(d) Write a complete 3-4 sentence comparison of all three groups.}}"

        solution = f"(a) Group C (median 55), Group A (center 50), Group B (median 45), "\
                   f"(b) Group B (largest range), "\
                   f"(c) Groups B and C (skewed distributions), "\
                   f"(d) Group C has the highest center with median 55, followed by Group A at 50 and Group B at 45. "\
                   f"Group B shows the most variability with range of 35 and right skewness. "\
                   f"Group A is symmetric while Groups B and C are skewed in opposite directions. "\
                   f"All groups have overlapping values between 40-60."

        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = ComparingDistributionsQuantitativeGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
