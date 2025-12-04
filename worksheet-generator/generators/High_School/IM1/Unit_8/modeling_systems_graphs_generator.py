"""
Modeling Systems Graphs Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ModelingSystemsGraphsGenerator:
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
        rate1 = random.randint(40, 70)
        fee1 = random.randint(20, 50)

        latex = f"\\text{{Company A: \\${fee1} + \\${rate1}/hour. Write the equation.}}"
        solution = f"y = {rate1}x + {fee1}"
        steps = [f"Rate: {rate1}", f"Initial fee: {fee1}", f"y = {rate1}x + {fee1}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        rate1 = random.randint(50, 80)
        fee1 = random.randint(25, 60)
        rate2 = random.randint(40, 70)
        fee2 = random.randint(40, 90)

        if rate1 == rate2:
            rate2 += 10

        latex = f"\\text{{A: \\${fee1} + \\${rate1}/hr, B: \\${fee2} + \\${rate2}/hr. Write system.}}"
        solution = f"y = {rate1}x + {fee1}, y = {rate2}x + {fee2}"
        steps = [f"Company A: y = {rate1}x + {fee1}", f"Company B: y = {rate2}x + {fee2}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        rate1 = random.randint(50, 75)
        fee1 = random.randint(20, 50)
        rate2 = random.randint(35, 60)
        fee2 = random.randint(60, 100)

        if rate1 <= rate2:
            rate1 = rate2 + 10

        hours = (fee2 - fee1) / (rate1 - rate2)

        latex = f"\\text{{Plumber A: \\${fee1} + \\${rate1}/hr. Plumber B: \\${fee2} + \\${rate2}/hr. When equal?}}"
        solution = f"{hours:.1f} \\text{{ hours}}"
        steps = [f"{rate1}x + {fee1} = {rate2}x + {fee2}", f"Solve for x", f"x = {hours:.1f} hours"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        initial1 = random.randint(100, 200)
        rate1 = random.randint(10, 25)
        initial2 = random.randint(50, 150)
        rate2 = random.randint(20, 40)

        if initial1 <= initial2:
            initial1 = initial2 + 50
        if rate1 >= rate2:
            rate2 = rate1 + 10

        weeks = (initial1 - initial2) / (rate2 - rate1)

        latex = f"\\text{{Account A: \\${initial1}, saves \\${rate1}/wk. Account B: \\${initial2}, saves \\${rate2}/wk. When equal?}}"
        solution = f"{weeks:.1f} \\text{{ weeks}}"
        steps = [f"A: y = {rate1}x + {initial1}", f"B: y = {rate2}x + {initial2}", f"Set equal and solve", f"x = {weeks:.1f} weeks"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = ModelingSystemsGraphsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
