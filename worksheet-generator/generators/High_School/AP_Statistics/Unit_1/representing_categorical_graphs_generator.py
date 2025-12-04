"""
Representing Categorical Data with Graphs Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class RepresentingCategoricalGraphsGenerator:
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
        categories = ["Red", "Blue", "Green", "Yellow"]
        counts = [random.randint(10, 40) for _ in range(4)]
        total = sum(counts)

        question = f"\\text{{Survey results for favorite color:}}\\\\"\
                   f"\\text{{Red: {counts[0]}, Blue: {counts[1]}, Green: {counts[2]}, Yellow: {counts[3]}}}\\\\"\
                   f"\\text{{What percentage chose Blue?}}"

        percentage = round((counts[1] / total) * 100, 1)
        solution = f"{percentage}\\%"

        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        categories = ["A", "B", "C", "D", "E"]
        counts = sorted([random.randint(15, 50) for _ in range(5)], reverse=True)
        total = sum(counts)

        question = f"\\text{{Grade distribution: A:{counts[0]}, B:{counts[1]}, C:{counts[2]}, D:{counts[3]}, E:{counts[4]}}}\\\\"\
                   f"\\text{{(a) Which grade is the mode?}}\\\\"\
                   f"\\text{{(b) What percentage received an A or B?}}"

        percentage = round(((counts[0] + counts[1]) / total) * 100, 1)
        solution = f"(a) A (highest frequency), (b) {percentage}\\%"

        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        sports = ["Soccer", "Basketball", "Baseball", "Tennis"]
        counts = [random.randint(20, 60) for _ in range(4)]
        total = sum(counts)

        question = f"\\text{{Preferred sport survey (n={total}):}}\\\\"\
                   f"\\text{{Soccer: {counts[0]}, Basketball: {counts[1]}, Baseball: {counts[2]}, Tennis: {counts[3]}}}\\\\"\
                   f"\\text{{(a) Create a relative frequency table}}\\\\"\
                   f"\\text{{(b) Which sport should get displayed with the largest wedge in a pie chart?}}"

        max_count = max(counts)
        max_sport = sports[counts.index(max_count)]

        rel_freqs = [round(c/total, 3) for c in counts]
        solution = f"(a) Soccer: {rel_freqs[0]}, Basketball: {rel_freqs[1]}, Baseball: {rel_freqs[2]}, Tennis: {rel_freqs[3]}, (b) {max_sport}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        categories = ["Category A", "Category B", "Category C", "Category D"]
        percentages = [25, 35, 20, 20]
        total = random.randint(200, 400)

        question = f"\\text{{A pie chart shows: A(25\\%), B(35\\%), C(20\\%), D(20\\%). Total n={total}.}}\\\\"\
                   f"\\text{{(a) How many individuals are in Category B?}}\\\\"\
                   f"\\text{{(b) What angle (in degrees) does Category A occupy in the pie chart?}}\\\\"\
                   f"\\text{{(c) Is a bar chart or pie chart more appropriate for this data? Explain.}}"

        count_b = int(total * 0.35)
        angle_a = int(360 * 0.25)

        solution = f"(a) {count_b} individuals, (b) {angle_a} degrees, (c) Either is appropriate; "\
                   f"pie chart emphasizes parts of whole, bar chart shows frequencies clearly"

        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = RepresentingCategoricalGraphsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
