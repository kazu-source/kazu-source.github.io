"""Evaluating Expressions Word Problems Generator - Grade 6 Unit 6"""
import random
from typing import List
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation

class EvaluatingExpressionsWordProblemsGenerator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)
    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]
    def _generate_problem(self, difficulty: str) -> Equation:
        return getattr(self, f'_generate_{difficulty}')()
    def _generate_easy(self) -> Equation:
        cost, num = random.randint(3, 8), random.randint(4, 10)
        total = cost * num
        latex = f"\\text{{Tickets cost }}\\${cost}\\text{{ each. Total cost for }}{num}\\text{{ tickets?}}"
        return Equation(latex=latex, solution=f"\\${total}", steps=[f"{cost} \\times {num} = {total}"], difficulty='easy')
    def _generate_medium(self) -> Equation:
        rate, hours, base = random.randint(10, 20), random.randint(3, 8), random.randint(20, 50)
        total = rate * hours + base
        latex = f"\\text{{Pay: }}\\${rate}\\text{{/hour + }}\\${base}\\text{{ base. Total for }}{hours}\\text{{ hours?}}"
        return Equation(latex=latex, solution=f"\\${total}", steps=[f"{rate}({hours}) + {base} = {total}"], difficulty='medium')
    def _generate_hard(self) -> Equation:
        length, width = random.randint(5, 15), random.randint(3, 10)
        perimeter = 2 * (length + width)
        latex = f"\\text{{Rectangle: length }}{length}\\text{{, width }}{width}\\text{{. Perimeter?}}"
        return Equation(latex=latex, solution=str(perimeter), steps=[f"2({length} + {width}) = {perimeter}"], difficulty='hard')
    def _generate_challenge(self) -> Equation:
        rate1, rate2, time = random.randint(40, 60), random.randint(30, 50), random.randint(2, 5)
        distance = (rate1 + rate2) * time
        latex = f"\\text{{Two cars at }}{rate1}\\text{{ and }}{rate2}\\text{{ mph for }}{time}\\text{{ hrs. Total distance?}}"
        return Equation(latex=latex, solution=f"{distance} miles", steps=[f"({rate1}+{rate2}) \\times {time} = {distance}"], difficulty='challenge')

def main():
    gen = EvaluatingExpressionsWordProblemsGenerator()
    for d in ['easy', 'medium', 'hard', 'challenge']:
        for p in gen.generate_worksheet(d, 2): print(f"  {p.latex}")
if __name__ == '__main__': main()
