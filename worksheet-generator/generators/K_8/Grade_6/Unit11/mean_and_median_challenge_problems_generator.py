"""Mean and Median Challenge Problems Generator - Grade 6 Unit 11"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class MeanAndMedianChallengeProblemsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        data = [random.randint(5, 15) for _ in range(4)]
        total = sum(data)
        target_mean = random.randint(10, 20)
        needed = target_mean * 5 - total
        latex = f"\\text{{Data: {', '.join(map(str, data))}. What 5th value gives mean {target_mean}?}}"
        return Equation(latex=latex, solution=str(needed), steps=[f"5×{target_mean} - {total} = {needed}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        data = [random.randint(10, 30) for _ in range(5)]
        mean_val = sum(data) / len(data)
        outlier = random.randint(60, 100)
        new_mean = (sum(data) + outlier) / 6
        latex = f"\\text{{Data mean is {round(mean_val, 1)}. Adding {outlier} changes mean how much?}}"
        return Equation(latex=latex, solution=f"{round(new_mean - mean_val, 1)}", steps=[f"New mean - old mean = {round(new_mean - mean_val, 1)}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        data = sorted([random.randint(10, 40) for _ in range(5)])
        median = data[2]
        new_val = median + random.randint(5, 15)
        new_data = sorted(data + [new_val])
        new_median = (new_data[2] + new_data[3]) / 2
        latex = f"\\text{{Data: {', '.join(map(str, data))}. Adding {new_val}, new median?}}"
        return Equation(latex=latex, solution=str(new_median), steps=[f"New median = {new_median}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        data = [random.randint(15, 35) for _ in range(6)]
        mean_val = sum(data) / len(data)
        latex = f"\\text{{Data: {', '.join(map(str, data))}. Removing largest value changes mean by how much?}}"
        new_mean = (sum(data) - max(data)) / 5
        change = abs(new_mean - mean_val)
        return Equation(latex=latex, solution=f"{round(change, 1)}", steps=[f"Change = {round(change, 1)}"], difficulty='challenge')

def main():
    gen = MeanAndMedianChallengeProblemsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
