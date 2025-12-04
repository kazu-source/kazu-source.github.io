"""
Modeling with Rational Functions Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ModelingRationalFunctionsGenerator:
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
        # Average speed problem
        d = random.randint(100, 500)

        latex = f"\\text{{Write function for time to travel {d} miles at speed }} v"
        solution = f"t(v) = \\frac{{{d}}}{{v}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Average cost
        fixed = random.randint(1000, 5000)
        variable = random.randint(10, 50)

        latex = f"\\text{{Average cost per item: fixed cost \\${fixed}, variable \\${variable} per item. Write }} C(x)"
        solution = f"C(x) = \\frac{{{fixed} + {variable}x}}{{x}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Concentration problem
        initial = random.randint(10, 50)
        add = random.randint(5, 20)

        latex = f"\\text{{{initial}L at 20% solution. Add }} x \\text{{L water. Write concentration function}}"
        solution = f"C(x) = \\frac{{0.2 \\cdot {initial}}}{{{initial} + x}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Work rate problem
        a = random.randint(4, 10)
        b = random.randint(4, 10)

        latex = f"\\text{{Person A completes job in {a} hrs, Person B in {b} hrs. Time working together?}}"
        solution = f"t = \\frac{{{a*b}}}{{{a+b}}} \\text{{ hours}}"

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')

def main():
    gen = ModelingRationalFunctionsGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
