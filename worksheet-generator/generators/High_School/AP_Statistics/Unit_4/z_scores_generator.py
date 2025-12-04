"""
Z-Scores Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ZScoresGenerator:
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
        mean = random.randint(70, 90)
        std = random.randint(5, 15)
        x = mean + random.randint(-2, 2) * std
        z = round((x - mean) / std, 2)
        question = f"\\text{{Mean}} = {mean}, \\text{{SD}} = {std}, x = {x}. \\text{{ Find the z-score.}}"
        solution = f"z = {z}"
        steps = [
            f"z = \\frac{{x - \\mu}}{{\\sigma}}",
            f"z = \\frac{{{x} - {mean}}}{{{std}}}",
            f"z = {z}"
        ]
        return Equation(latex=question, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        score = random.randint(90, 130)
        mean = 100
        std = 15
        z = round((score - mean) / std, 2)
        question = f"\\text{{Score}} = {score}, \\text{{mean}} = {mean}, \\text{{SD}} = {std}. \\text{{ Calculate and interpret the z-score.}}"
        interpretation = "above" if z > 0 else "below"
        solution = f"z = {z}, \\text{{score is }} {abs(z)} \\text{{ standard deviations {interpretation} the mean}}"
        steps = [
            f"z = \\frac{{x - \\mu}}{{\\sigma}} = \\frac{{{score} - {mean}}}{{{std}}} = {z}",
            f"\\text{{Since z = {z}, the score is {abs(z)} SDs {interpretation} the mean}}"
        ]
        return Equation(latex=question, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        sat_score = random.randint(480, 600)
        act_score = random.randint(20, 32)
        question = f"\\text{{SAT}} = {sat_score} \\text{{ (mean=500, SD=100)}}, \\text{{ACT}} = {act_score} \\text{{ (mean=21, SD=5)}}. \\text{{ Which is relatively better?}}"
        z_sat = round((sat_score - 500) / 100, 2)
        z_act = round((act_score - 21) / 5, 2)
        better = "SAT" if z_sat > z_act else "ACT"
        solution = f"\\text{{SAT z}} = {z_sat}, \\text{{ACT z}} = {z_act}. \\text{{{better} is relatively better (higher z-score)}}"
        steps = [
            f"z_{{SAT}} = \\frac{{{sat_score} - 500}}{{100}} = {z_sat}",
            f"z_{{ACT}} = \\frac{{{act_score} - 21}}{{5}} = {z_act}",
            f"\\text{{{better} has the higher z-score, so it is relatively better}}"
        ]
        return Equation(latex=question, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        data = [random.randint(10, 30) for _ in range(5)]
        data.sort()
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        std = variance ** 0.5
        z_scores = [round((x - mean) / std, 2) for x in data]
        question = f"\\text{{Data: }} {data}. \\text{{ (a) Find z-scores for all values. (b) What is the mean and SD of the z-scores?}}"
        solution = f"\\text{{Z-scores: }} {z_scores}. \\text{{ Mean of z-scores = 0, SD of z-scores = 1}}"
        steps = [
            f"\\text{{Mean}} = {round(mean, 2)}, \\text{{SD}} = {round(std, 2)}",
            f"\\text{{Z-scores: }} {z_scores}",
            f"\\text{{Property: Standardized data always has mean = 0 and SD = 1}}"
        ]
        return Equation(latex=question, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = ZScoresGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
