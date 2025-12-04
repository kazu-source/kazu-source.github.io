"""
Representing Quantitative Data with Histograms and Stem Plots Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class RepresentingQuantitativeHistogramsStemGenerator:
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
        # Histogram bin counts
        bins = ["0-10", "10-20", "20-30", "30-40"]
        counts = [random.randint(5, 15) for _ in range(4)]

        question = f"\\text{{Histogram bins and frequencies:}}\\\\"\
                   f"\\text{{{bins[0]}: {counts[0]}, {bins[1]}: {counts[1]}, {bins[2]}: {counts[2]}, {bins[3]}: {counts[3]}}}\\\\"\
                   f"\\text{{(a) How many data values total?}}\\\\"\
                   f"\\text{{(b) Which bin has the most data?}}"

        total = sum(counts)
        max_count = max(counts)
        max_bin = bins[counts.index(max_count)]

        solution = f"(a) {total}, (b) {max_bin}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Stem plot data
        stems_20s = [random.randint(0, 9) for _ in range(3)]
        stems_30s = [random.randint(0, 9) for _ in range(5)]
        stems_40s = [random.randint(0, 9) for _ in range(2)]

        question = f"\\text{{Stem-and-leaf plot:}}\\\\"\
                   f"\\text{{2 | {' '.join(map(str, sorted(stems_20s)))}}}\\\\"\
                   f"\\text{{3 | {' '.join(map(str, sorted(stems_30s)))}}}\\\\"\
                   f"\\text{{4 | {' '.join(map(str, sorted(stems_40s)))}}}\\\\"\
                   f"\\text{{(a) How many values in the 30s?}}\\\\"\
                   f"\\text{{(b) What is the smallest value?}}\\\\"\
                   f"\\text{{(c) What is the largest value?}}"

        count_30s = len(stems_30s)
        smallest = 20 + min(stems_20s)
        largest = 40 + max(stems_40s)

        solution = f"(a) {count_30s}, (b) {smallest}, (c) {largest}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Histogram with relative frequency
        bins = ["50-60", "60-70", "70-80", "80-90", "90-100"]
        counts = [8, 15, 22, 18, 7]
        total = sum(counts)

        question = f"\\text{{Test score histogram:}}\\\\"\
                   f"\\text{{50-60: {counts[0]}, 60-70: {counts[1]}, 70-80: {counts[2]}, 80-90: {counts[3]}, 90-100: {counts[4]}}}\\\\"\
                   f"\\text{{(a) Convert to relative frequencies}}\\\\"\
                   f"\\text{{(b) What percent scored 80 or above?}}\\\\"\
                   f"\\text{{(c) Describe the shape of the distribution.}}"

        rel_freqs = [round(c/total, 3) for c in counts]
        percent_80_plus = round(((counts[3] + counts[4])/total) * 100, 1)

        # Determine shape
        peak_index = counts.index(max(counts))
        if peak_index <= 1:
            shape = "skewed right"
        elif peak_index >= 3:
            shape = "skewed left"
        else:
            shape = "approximately symmetric"

        solution = f"(a) {', '.join(map(str, rel_freqs))}, (b) {percent_80_plus}\\%, (c) {shape}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Split stem plot
        question = f"\\text{{A split stem-and-leaf plot uses two lines per stem:}}\\\\"\
                   f"\\text{{2L | 1 2 3 4 (leaves 0-4)}}\\\\"\
                   f"\\text{{2H | 5 7 8 9 (leaves 5-9)}}\\\\"\
                   f"\\text{{3L | 0 1 3}}\\\\"\
                   f"\\text{{3H | 6 8 9 9}}\\\\"\
                   f"\\text{{(a) List all data values}}\\\\"\
                   f"\\text{{(b) Why use a split stem plot?}}\\\\"\
                   f"\\text{{(c) Find the median}}\\\\"\
                   f"\\text{{(d) Identify any repeated values}}"

        data = [21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 33, 36, 38, 39, 39]
        median = data[len(data)//2]

        solution = f"(a) {', '.join(map(str, data))}, "\
                   f"(b) Better resolution when data clusters in few stems, "\
                   f"(c) Median = {median}, "\
                   f"(d) 39 appears twice"

        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = RepresentingQuantitativeHistogramsStemGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
