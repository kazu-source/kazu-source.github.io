"""
More on Mean and Median Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class MoreMeanMedianGenerator:
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
        data = sorted([random.randint(10, 30) for _ in range(5)])
        outlier = random.randint(70, 90)
        data_with_outlier = sorted(data + [outlier])

        question = f"\\text{{Data without outlier: {', '.join(map(str, data))}}}\\\\"\
                   f"\\text{{Data with outlier: {', '.join(map(str, data_with_outlier))}}}\\\\"\
                   f"\\text{{Which measure of center changes more: mean or median?}}"

        mean1 = round(sum(data) / len(data), 1)
        mean2 = round(sum(data_with_outlier) / len(data_with_outlier), 1)
        median1 = data[len(data)//2]
        median2 = data_with_outlier[len(data_with_outlier)//2]

        mean_change = abs(mean2 - mean1)
        median_change = abs(median2 - median1)

        solution = f"Mean changes more ({mean1} to {mean2}, change of {mean_change}) than median ({median1} to {median2}, change of {median_change})"

        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        n = 6
        data = [random.randint(20, 40) for _ in range(n-1)]
        target_mean = random.randint(30, 35)

        question = f"\\text{{Data: {', '.join(map(str, data))}, x}}\\\\"\
                   f"\\text{{If the mean is {target_mean}, find x.}}"

        sum_needed = target_mean * n
        x = sum_needed - sum(data)

        solution = f"x = {x}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        data = sorted([random.randint(25, 45) for _ in range(8)])

        question = f"\\text{{Data: {', '.join(map(str, data))}}}\\\\"\
                   f"\\text{{(a) Find mean and median}}\\\\"\
                   f"\\text{{(b) Remove the largest value. Find new mean and median.}}\\\\"\
                   f"\\text{{(c) Which changed by a larger percentage?}}"

        mean1 = round(sum(data) / len(data), 2)
        median1 = (data[3] + data[4]) / 2

        data2 = data[:-1]
        mean2 = round(sum(data2) / len(data2), 2)
        median2 = data2[len(data2)//2]

        mean_pct_change = round(abs((mean2 - mean1) / mean1) * 100, 2)
        median_pct_change = round(abs((median2 - median1) / median1) * 100, 2)

        solution = f"(a) Mean = {mean1}, Median = {median1}, "\
                   f"(b) New mean = {mean2}, New median = {median2}, "\
                   f"(c) Mean changed {mean_pct_change}\\%, median changed {median_pct_change}\\%"

        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Resistance to outliers
        question = f"\\text{{Two datasets:}}\\\\"\
                   f"\\text{{Dataset A: 10, 12, 15, 18, 20}}\\\\"\
                   f"\\text{{Dataset B: 10, 12, 15, 18, 100}}\\\\"\
                   f"\\text{{(a) Calculate mean and median for both}}\\\\"\
                   f"\\text{{(b) Define 'resistant statistic'}}\\\\"\
                   f"\\text{{(c) Is median resistant? Is mean resistant? Support with data.}}"

        data_a = [10, 12, 15, 18, 20]
        data_b = [10, 12, 15, 18, 100]

        mean_a = sum(data_a) / len(data_a)
        mean_b = sum(data_b) / len(data_b)
        median_a = 15
        median_b = 15

        solution = f"(a) A: mean={mean_a}, median={median_a}; B: mean={mean_b}, median={median_b}, "\
                   f"(b) Resistant statistic: not strongly affected by outliers/extreme values, "\
                   f"(c) Median is resistant (stayed at 15); mean is not resistant (changed from {mean_a} to {mean_b})"

        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = MoreMeanMedianGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
