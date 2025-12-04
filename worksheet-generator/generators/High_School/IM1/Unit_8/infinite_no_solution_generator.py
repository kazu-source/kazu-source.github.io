"""
Infinite No Solution Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class InfiniteNoSolutionGenerator:
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
        m = random.randint(2, 6)
        b1 = random.randint(3, 10)
        b2 = b1 + random.randint(2, 5)

        latex = f"\\text{{How many solutions: }} y = {m}x + {b1}, y = {m}x + {b2}?"
        solution = "No solution"
        steps = ["Same slope, different y-intercepts", "Lines are parallel", "Answer: No solution"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        m = random.randint(2, 6)
        b = random.randint(3, 10)

        latex = f"\\text{{How many solutions: }} y = {m}x + {b}, y = {m}x + {b}?"
        solution = "Infinitely many solutions"
        steps = ["Same slope, same y-intercept", "Lines are identical", "Answer: Infinitely many solutions"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 4)
        c1 = random.randint(10, 20)
        c2 = c1 + random.randint(3, 8)

        latex = f"\\text{{How many solutions: }} {a}x + {b}y = {c1}, {a}x + {b}y = {c2}?"
        solution = "No solution"
        steps = ["Same coefficients, different constants", "Lines are parallel", "Answer: No solution"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(2, 4)
        c = random.randint(10, 25)
        k = random.randint(2, 4)

        latex = f"\\text{{How many solutions: }} {a}x + {b}y = {c}, {a*k}x + {b*k}y = {c*k}?"
        solution = "Infinitely many solutions"
        steps = [f"Second equation is {k} times the first", "Same line", "Answer: Infinitely many solutions"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = InfiniteNoSolutionGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
