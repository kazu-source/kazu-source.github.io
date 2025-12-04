"""
Number of Solutions Inequalities Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class NumberOfSolutionsInequalitiesGenerator:
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
        a = random.randint(1, 10)

        latex = f"\\text{{How many solutions does }} x > {a} \\text{{ have?}}"
        solution = "Infinitely many"
        steps = ["Any number greater than {a} works", "There are infinitely many such numbers", "Answer: Infinitely many"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 8)
        b = random.randint(1, 12)
        c = random.randint(10, 25)

        latex = f"\\text{{How many solutions does }} {a}x + {b} \\leq {c} \\text{{ have?}}"
        solution = "Infinitely many"
        steps = ["This is a linear inequality", "Linear inequalities have infinitely many solutions", "Answer: Infinitely many"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 8)
        b = random.randint(5, 15)

        latex = f"\\text{{Name three solutions to }} x < {b}"
        examples = [b - 1, b - 2, b - 3]
        solution = f"{examples[0]}, {examples[1]}, {examples[2]}"
        steps = [f"Any number less than {b} works", f"Examples: {examples[0]}, {examples[1]}, {examples[2]}", "Many other answers possible"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 7)

        latex = f"\\text{{Compare: How many solutions does }} x = {a} \\text{{ vs }} x > {a} \\text{{ have?}}"
        solution = f"x = {a} has 1 solution; x > {a} has infinitely many"
        steps = [f"Equation x = {a} has exactly one solution", f"Inequality x > {a} has infinitely many solutions", "Inequalities generally have more solutions than equations"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = NumberOfSolutionsInequalitiesGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
