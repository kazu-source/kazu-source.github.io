"""
Expressions Part of Equation Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ExpressionsPartOfEquationGenerator:
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
        a = random.randint(2, 9)
        b = random.randint(1, 12)
        c = random.randint(1, 15)

        latex = f"\\text{{How many expressions are in: }} {a}x + {b} = {c}?"
        solution = "2"
        steps = [f"Left side: {a}x + {b} (expression 1)", f"Right side: {c} (expression 2)", "Answer: 2 expressions"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 8)
        b = random.randint(1, 10)
        c = random.randint(1, 12)
        d = random.randint(1, 9)

        latex = f"\\text{{True or False: Every equation contains at least two expressions}}"
        solution = "True"
        steps = ["An equation has form: expression = expression", "Both sides of = are expressions", "Answer: True"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 7)
        b = random.randint(1, 9)
        c = random.randint(1, 10)
        d = random.randint(1, 12)

        latex = f"\\text{{List the two main expressions in: }} {a}({b}x + {c}) = {d}"
        solution = f"{a}({b}x + {c}) and {d}"
        steps = [f"Left side of =: {a}({b}x + {c})", f"Right side of =: {d}", "These are the two main expressions"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(1, 8)
        c = random.randint(1, 7)
        d = random.randint(2, 5)
        e = random.randint(1, 9)

        latex = f"\\text{{In }} {a}x + {b} = {c}x - {d}\\text{{, identify the expressions on each side and write a new equation with different expressions}}"
        solution = f"Left: {a}x + {b}, Right: {c}x - {d}; New equation (answers vary): {e}x = {b}"
        steps = [f"Original left expression: {a}x + {b}", f"Original right expression: {c}x - {d}", "New equation can use any valid expressions"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = ExpressionsPartOfEquationGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
