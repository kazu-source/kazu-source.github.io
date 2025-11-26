"""Dot Plots and Frequency Tables Generator - Grade 6 Unit 11"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class DotPlotsAndFrequencyTablesGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        data = [random.randint(1, 5) for _ in range(10)]
        most_common = max(set(data), key=data.count)
        freq = data.count(most_common)
        latex = f"\\text{{Data: {', '.join(map(str, data))}. Most frequent value?}}"
        return Equation(latex=latex, solution=str(most_common), steps=[f"{most_common} appears {freq} times"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        data = [random.randint(1, 6) for _ in range(12)]
        latex = f"\\text{{Data: {', '.join(map(str, data))}. How many data points?}}"
        return Equation(latex=latex, solution=str(len(data)), steps=[f"Count: {len(data)}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        values = [2, 3, 4, 5]
        freqs = [random.randint(1, 5) for _ in range(4)]
        total = sum(freqs)
        latex = f"\\text{{Frequency table: }} {values[0]}({freqs[0]}), {values[1]}({freqs[1]}), {values[2]}({freqs[2]}), {values[3]}({freqs[3]})\\text{{. Total data points?}}"
        return Equation(latex=latex, solution=str(total), steps=[f"Sum frequencies: {total}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        data = [random.randint(1, 10) for _ in range(15)]
        range_val = max(data) - min(data)
        latex = f"\\text{{Data range (max - min) for: {', '.join(map(str, data[:8]))}...}}"
        return Equation(latex=latex, solution=str(range_val), steps=[f"Range = {max(data)} - {min(data)} = {range_val}"], difficulty='challenge')

def main():
    gen = DotPlotsAndFrequencyTablesGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
