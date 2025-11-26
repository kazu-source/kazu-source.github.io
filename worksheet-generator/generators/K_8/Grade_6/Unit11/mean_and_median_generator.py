"""Mean and Median Generator - Grade 6 Unit 11"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class MeanAndMedianGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        data = [random.randint(1, 10) for _ in range(5)]
        mean = sum(data) / len(data)
        latex = f"\\text{{Find mean: {', '.join(map(str, data))}}}"
        return Equation(latex=latex, solution=str(round(mean, 1)), steps=[f"Sum/{len(data)} = {round(mean, 1)}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        data = sorted([random.randint(1, 20) for _ in range(5)])
        median = data[len(data)//2]
        latex = f"\\text{{Find median: {', '.join(map(str, data))}}}"
        return Equation(latex=latex, solution=str(median), steps=[f"Middle value: {median}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        data = sorted([random.randint(5, 30) for _ in range(6)])
        median = (data[2] + data[3]) / 2
        latex = f"\\text{{Find median: {', '.join(map(str, data))}}}"
        return Equation(latex=latex, solution=str(median), steps=[f"({data[2]} + {data[3]})/2 = {median}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        data = [random.randint(10, 50) for _ in range(7)]
        mean = sum(data) / len(data)
        median = sorted(data)[3]
        latex = f"\\text{{Data: {', '.join(map(str, data))}. Find mean and median.}}"
        return Equation(latex=latex, solution=f"Mean: {round(mean, 1)}, Median: {median}", steps=[f"Mean = {round(mean, 1)}, Median = {median}"], difficulty='challenge')

def main():
    gen = MeanAndMedianGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
