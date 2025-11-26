"""Histograms Generator - Grade 6 Unit 11"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class HistogramsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        bins = ["0-10", "11-20", "21-30"]
        freqs = [random.randint(2, 8) for _ in range(3)]
        total = sum(freqs)
        latex = f"\\text{{Histogram bins: {bins[0]}({freqs[0]}), {bins[1]}({freqs[1]}), {bins[2]}({freqs[2]}). Total?}}"
        return Equation(latex=latex, solution=str(total), steps=[f"Sum: {total}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        bins = ["0-5", "6-10", "11-15"]
        freqs = [random.randint(3, 10) for _ in range(3)]
        max_bin = bins[freqs.index(max(freqs))]
        latex = f"\\text{{Histogram: {bins[0]}({freqs[0]}), {bins[1]}({freqs[1]}), {bins[2]}({freqs[2]}). Which bin has most?}}"
        return Equation(latex=latex, solution=max_bin, steps=[f"{max_bin} has {max(freqs)}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        bins = ["10-20", "21-30", "31-40", "41-50"]
        freqs = [random.randint(2, 7) for _ in range(4)]
        latex = f"\\text{{How many values in 10-30 range? Bins: {bins[0]}({freqs[0]}), {bins[1]}({freqs[1]}), {bins[2]}({freqs[2]}), {bins[3]}({freqs[3]})}}"
        return Equation(latex=latex, solution=str(freqs[0] + freqs[1]), steps=[f"{freqs[0]} + {freqs[1]} = {freqs[0] + freqs[1]}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        bins = ["0-10", "11-20", "21-30"]
        freqs = [random.randint(4, 12) for _ in range(3)]
        total = sum(freqs)
        percent = round(freqs[0] / total * 100)
        latex = f"\\text{{Bins: {bins[0]}({freqs[0]}), {bins[1]}({freqs[1]}), {bins[2]}({freqs[2]}). Percent in first bin?}}"
        return Equation(latex=latex, solution=f"{percent}\\%", steps=[f"{freqs[0]}/{total} \\approx {percent}\\%"], difficulty='challenge')

def main():
    gen = HistogramsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
