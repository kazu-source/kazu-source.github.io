"""Shape of Data Distributions Generator - Grade 6 Unit 11"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class ShapeOfDataDistributionsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        shapes = ["symmetric", "skewed left", "skewed right", "uniform"]
        shape = random.choice(shapes)
        latex = f"\\text{{Define '{shape}' distribution.}}"
        descriptions = {
            "symmetric": "Mirror image around center",
            "skewed left": "Tail on left side",
            "skewed right": "Tail on right side",
            "uniform": "All values equally frequent"
        }
        return Equation(latex=latex, solution=descriptions[shape], steps=[descriptions[shape]], difficulty='easy')
    def _generate_medium(self) -> Equation:
        latex = f"\\text{{If mean > median, distribution is likely?}}"
        return Equation(latex=latex, solution="Skewed right", steps=["Mean pulled by high values"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        latex = f"\\text{{If mean < median, distribution is likely?}}"
        return Equation(latex=latex, solution="Skewed left", steps=["Mean pulled by low values"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        data = [random.randint(20, 30) for _ in range(5)] + [random.randint(60, 80)]
        mean = sum(data) / len(data)
        median = sorted(data)[len(data)//2]
        shape = "Skewed right" if mean > median else ("Skewed left" if mean < median else "Symmetric")
        latex = f"\\text{{Data: {', '.join(map(str, data))}. Describe distribution shape.}}"
        return Equation(latex=latex, solution=shape, steps=[f"Mean={round(mean,1)}, Median={median}, Shape: {shape}"], difficulty='challenge')

def main():
    gen = ShapeOfDataDistributionsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
