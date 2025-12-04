"""
Modeling with Function Combination Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ModelingFunctionCombinationGenerator:
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
        # Simple function addition
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\text{{If }} f(x) = {a}x \\text{{ and }} g(x) = {b}\\text{{, find }} (f+g)(x)"
        solution = f"{a}x + {b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Function composition
        a = random.randint(2, 5)
        b = random.randint(1, 5)

        latex = f"\\text{{If }} f(x) = {a}x + {b} \\text{{ and }} g(x) = x^2\\text{{, find }} f(g(x))"
        solution = f"{a}x^2 + {b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Product of functions
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        c = random.randint(1, 5)

        latex = f"\\text{{If }} f(x) = {a}x + {b} \\text{{ and }} g(x) = {c}x\\text{{, find }} (f \\cdot g)(x)"
        solution = f"{a*c}x^2 + {b*c}x"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Complex composition
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"\\text{{If }} f(x) = x^2 + {a} \\text{{ and }} g(x) = {b}x\\text{{, find }} g(f(x))"
        solution = f"{b}(x^2 + {a}) = {b}x^2 + {a*b}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = ModelingFunctionCombinationGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
