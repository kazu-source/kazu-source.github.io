"""
Measuring Variability of Quantitative Data Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class MeasuringVariabilityQuantitativeGenerator:
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
        data = sorted([random.randint(10, 50) for _ in range(6)])

        question = f"\\text{{Data: {', '.join(map(str, data))}}}\\\\"\
                   f"\\text{{Find the range.}}"

        range_val = max(data) - min(data)

        solution = f"\\text{{Range}} = {range_val}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        data = sorted([random.randint(20, 60) for _ in range(8)])

        question = f"\\text{{Data: {', '.join(map(str, data))}}}\\\\"\
                   f"\\text{{(a) Find Q1, Q2 (median), and Q3}}\\\\"\
                   f"\\text{{(b) Find the IQR}}"

        q2 = (data[3] + data[4]) / 2
        q1 = (data[1] + data[2]) / 2
        q3 = (data[5] + data[6]) / 2
        iqr = q3 - q1

        solution = f"(a) Q_1 = {q1}, Q_2 = {q2}, Q_3 = {q3}, (b) IQR = {iqr}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        data = sorted([random.randint(15, 45) for _ in range(10)])

        question = f"\\text{{Data: {', '.join(map(str, data))}}}\\\\"\
                   f"\\text{{(a) Calculate the five-number summary}}\\\\"\
                   f"\\text{{(b) Calculate the IQR}}\\\\"\
                   f"\\text{{(c) Determine outlier boundaries using 1.5×IQR rule}}"

        min_val = min(data)
        max_val = max(data)
        q2 = (data[4] + data[5]) / 2
        q1 = (data[2] + data[3]) / 2
        q3 = (data[7] + data[8]) / 2
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        solution = f"(a) Min={min_val}, Q1={q1}, Med={q2}, Q3={q3}, Max={max_val}, "\
                   f"(b) IQR={iqr}, (c) Lower bound={lower_bound}, Upper bound={upper_bound}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        data = [12, 15, 18, 20, 22, 25, 28]

        question = f"\\text{{Data: {', '.join(map(str, data))}}}\\\\"\
                   f"\\text{{(a) Calculate the standard deviation}}\\\\"\
                   f"\\text{{(b) If each value increases by 5, what happens to std dev?}}\\\\"\
                   f"\\text{{(c) If each value doubles, what happens to std dev?}}"

        mean_val = sum(data) / len(data)
        variance = sum((x - mean_val)**2 for x in data) / (len(data) - 1)
        std_dev = round(variance ** 0.5, 2)

        solution = f"(a) s ≈ {std_dev}, (b) Std dev stays same (adding constant doesn't change spread), "\
                   f"(c) Std dev doubles to ≈ {round(std_dev * 2, 2)}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = MeasuringVariabilityQuantitativeGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
