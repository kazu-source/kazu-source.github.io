"""
Measuring Center of Quantitative Data Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class MeasuringCenterQuantitativeGenerator:
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
        data = [random.randint(10, 50) for _ in range(7)]

        question = f"\\text{{Data: {', '.join(map(str, data))}}}\\\\"\
                   f"\\text{{Find the mean.}}"

        mean_val = round(sum(data) / len(data), 2)

        solution = f"\\bar{{x}} = {mean_val}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        data = sorted([random.randint(15, 45) for _ in range(9)])

        question = f"\\text{{Data: {', '.join(map(str, data))}}}\\\\"\
                   f"\\text{{(a) Find the median}}\\\\"\
                   f"\\text{{(b) Find the mean}}"

        median = data[len(data)//2]
        mean_val = round(sum(data) / len(data), 2)

        solution = f"(a) Median = {median}, (b) Mean = {mean_val}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        data = sorted([random.randint(20, 40) for _ in range(10)])

        question = f"\\text{{Data: {', '.join(map(str, data))}}}\\\\"\
                   f"\\text{{(a) Calculate mean and median}}\\\\"\
                   f"\\text{{(b) Which is a better measure of center? Why?}}\\\\"\
                   f"\\text{{(c) If the largest value doubled, how would mean and median change?}}"

        median = (data[4] + data[5]) / 2
        mean_val = round(sum(data) / len(data), 2)

        new_data = data[:-1] + [data[-1] * 2]
        new_mean = round(sum(new_data) / len(new_data), 2)

        solution = f"(a) Mean = {mean_val}, Median = {median}, "\
                   f"(b) Similar values suggest symmetric data - either is appropriate, "\
                   f"(c) Mean would increase to {new_mean}, median stays {median}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Weighted mean
        scores = [85, 90, 78, 92]
        weights = [20, 30, 25, 25]

        question = f"\\text{{Course grades with weights:}}\\\\"\
                   f"\\text{{Exam 1: {scores[0]} (20\\%), Exam 2: {scores[1]} (30\\%)}}\\\\"\
                   f"\\text{{Exam 3: {scores[2]} (25\\%), Final: {scores[3]} (25\\%)}}\\\\"\
                   f"\\text{{(a) Calculate the weighted mean}}\\\\"\
                   f"\\text{{(b) Why not use the simple mean?}}\\\\"\
                   f"\\text{{(c) If weights were equal, what would the mean be?}}"

        weighted_sum = sum(s * w for s, w in zip(scores, weights))
        weighted_mean = round(weighted_sum / sum(weights), 2)
        simple_mean = round(sum(scores) / len(scores), 2)

        solution = f"(a) Weighted mean = {weighted_mean}, "\
                   f"(b) Different weights reflect different importance of exams, "\
                   f"(c) Simple mean = {simple_mean}"

        return Equation(latex=question, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = MeasuringCenterQuantitativeGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
