"""
Describing Distribution of Quantitative Data Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class DescribingDistributionQuantitativeGenerator:
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
        # Simple symmetric data
        data = [12, 14, 15, 16, 16, 17, 18, 20]

        question = f"\\text{{Data: {', '.join(map(str, data))}}}\\\\"\
                   f"\\text{{Describe the shape: symmetric, skewed left, or skewed right?}}"

        mean_val = sum(data) / len(data)
        median = sorted(data)[len(data)//2]

        if abs(mean_val - median) < 0.5:
            solution = "Approximately symmetric (mean and median are close)"
        elif mean_val > median:
            solution = "Skewed right (mean > median)"
        else:
            solution = "Skewed left (mean < median)"

        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Dataset with outlier
        base = [random.randint(20, 30) for _ in range(8)]
        outlier = random.randint(55, 70)
        data = sorted(base + [outlier])

        question = f"\\text{{Ages: {', '.join(map(str, data))}}}\\\\"\
                   f"\\text{{(a) Identify any outliers}}\\\\"\
                   f"\\text{{(b) Describe the shape}}\\\\"\
                   f"\\text{{(c) Describe center and spread in context}}"

        mean_val = round(sum(data) / len(data), 1)
        median = sorted(data)[len(data)//2]
        range_val = max(data) - min(data)

        solution = f"(a) {outlier} is an outlier (far from other values), "\
                   f"(b) Skewed right due to outlier, "\
                   f"(c) Center: median age is {median} years; Spread: range is {range_val} years"

        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Histogram description
        bins = ["0-5", "5-10", "10-15", "15-20", "20-25"]
        counts = [3, 8, 12, 7, 2]

        question = f"\\text{{Histogram of wait times (minutes):}}\\\\"\
                   f"\\text{{0-5: {counts[0]}, 5-10: {counts[1]}, 10-15: {counts[2]}, 15-20: {counts[3]}, 20-25: {counts[4]}}}\\\\"\
                   f"\\text{{Describe the distribution using SOCS (Shape, Outliers, Center, Spread).}}"

        total = sum(counts)
        peak_index = counts.index(max(counts))

        # Approximate center
        approx_median_bin = bins[2]

        # Shape
        if peak_index <= 1:
            shape = "skewed right"
        elif peak_index >= 3:
            shape = "skewed left"
        else:
            shape = "approximately symmetric"

        solution = f"Shape: {shape} with peak at {bins[peak_index]}; "\
                   f"Outliers: none apparent; "\
                   f"Center: median appears to be in 10-15 minute range; "\
                   f"Spread: ranges from 0 to 25 minutes"

        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Bimodal distribution
        question = f"\\text{{A histogram shows two distinct peaks:}}\\\\"\
                   f"\\text{{one around 20-30 and another around 50-60.}}\\\\"\
                   f"\\text{{(a) What is this distribution called?}}\\\\"\
                   f"\\text{{(b) Why might this occur in real data?}}\\\\"\
                   f"\\text{{(c) Is the mean or median more appropriate for describing center?}}\\\\"\
                   f"\\text{{(d) Give an example context where this might occur.}}"

        solution = f"(a) Bimodal distribution, "\
                   f"(b) Data may come from two distinct groups or populations, "\
                   f"(c) Neither is very useful; describe each mode separately, "\
                   f"(d) Example: heights of mixed-gender group, ages at a family reunion (children and adults)"

        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = DescribingDistributionQuantitativeGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
