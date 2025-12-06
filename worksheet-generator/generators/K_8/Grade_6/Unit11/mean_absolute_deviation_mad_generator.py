"""Mean Absolute Deviation MAD Generator - Grade 6 Unit 11"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class MeanAbsoluteDeviationMadGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        data = [random.randint(5, 15) for _ in range(5)]
        mean = sum(data) / len(data)
        deviations = [abs(x - mean) for x in data]
        mad = sum(deviations) / len(deviations)
        latex = f"\\text{{Find MAD for: {', '.join(map(str, data))}}}"
        dev_strs = [f"|{x} - {round(mean,1)}| = {round(abs(x - mean),1)}" for x in data]
        steps = [
            f"\\text{{Mean}} = \\frac{{{' + '.join(map(str, data))}}}{{{len(data)}}} = {round(mean,1)}",
            f"\\text{{Deviations: }}" + ", ".join(dev_strs),
            f"\\text{{MAD}} = \\frac{{{' + '.join([str(round(d,1)) for d in deviations])}}}{{{len(deviations)}}} = {round(mad,1)}"
        ]
        return Equation(latex=latex, solution=str(round(mad, 1)), steps=steps, difficulty='easy')
    def _generate_medium(self) -> Equation:
        data = [random.randint(10, 30) for _ in range(6)]
        mean = sum(data) / len(data)
        deviations = [abs(x - mean) for x in data]
        mad = sum(deviations) / len(deviations)
        latex = f"\\text{{Calculate MAD: {', '.join(map(str, data))}}}"
        dev_strs = [f"|{x} - {round(mean,1)}| = {round(abs(x - mean),1)}" for x in data]
        steps = [
            f"\\text{{Mean}} = \\frac{{{' + '.join(map(str, data))}}}{{{len(data)}}} = {round(mean,1)}",
            f"\\text{{Deviations: }}" + ", ".join(dev_strs),
            f"\\text{{MAD}} = {round(mad,1)}"
        ]
        return Equation(latex=latex, solution=str(round(mad, 1)), steps=steps, difficulty='medium')
    def _generate_hard(self) -> Equation:
        data1 = [random.randint(20, 30) for _ in range(5)]
        mean1 = sum(data1) / len(data1)
        dev1 = [abs(x - mean1) for x in data1]
        mad1 = sum(dev1) / len(dev1)
        data2 = [random.randint(15, 35) for _ in range(5)]
        mean2 = sum(data2) / len(data2)
        dev2 = [abs(x - mean2) for x in data2]
        mad2 = sum(dev2) / len(dev2)
        more_spread = "Dataset A" if mad1 > mad2 else "Dataset B"
        latex = f"\\text{{Which has more variability? A: {', '.join(map(str, data1))} or B: {', '.join(map(str, data2))}}}"
        steps = [
            f"\\text{{Dataset A: Mean}} = {round(mean1,1)}, \\text{{MAD}} = {round(mad1,1)}",
            f"\\text{{Dataset B: Mean}} = {round(mean2,1)}, \\text{{MAD}} = {round(mad2,1)}",
            f"\\text{{Higher MAD means more spread: {more_spread}}}"
        ]
        return Equation(latex=latex, solution=more_spread, steps=steps, difficulty='hard')
    def _generate_challenge(self) -> Equation:
        data = [random.randint(25, 75) for _ in range(7)]
        mean = sum(data) / len(data)
        deviations = [abs(x - mean) for x in data]
        mad = sum(deviations) / len(deviations)
        latex = f"\\text{{Find mean and MAD for: {', '.join(map(str, data))}}}"
        dev_strs = [f"|{x} - {round(mean,1)}|" for x in data]
        steps = [
            f"\\text{{Mean}} = \\frac{{{' + '.join(map(str, data))}}}{{{len(data)}}} = {round(mean,1)}",
            f"\\text{{Deviations: }}" + " + ".join(dev_strs),
            f"\\text{{MAD}} = {round(mad,1)}"
        ]
        return Equation(latex=latex, solution=f"Mean={round(mean,1)}, MAD={round(mad,1)}", steps=steps, difficulty='challenge')

def main():
    gen = MeanAbsoluteDeviationMadGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
