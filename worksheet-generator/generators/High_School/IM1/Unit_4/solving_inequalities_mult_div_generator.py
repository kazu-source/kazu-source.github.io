"""
Solving Inequalities Mult/Div Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class SolvingInequalitiesMultDivGenerator:
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
        a = random.randint(2, 8)
        b = random.randint(2, 12)
        c = a * b

        latex = f"{a}x < {c}"
        solution = f"x < {b}"
        steps = [f"Divide both sides by {a}", f"Inequality sign stays the same (dividing by positive)", f"x < \\frac{{{c}}}{{{a}}}", f"x < {b}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(3, 15)

        latex = f"\\frac{{x}}{{{a}}} \\geq {b}"
        solution = f"x \\geq {a * b}"
        steps = [f"Multiply both sides by {a}", f"Inequality sign stays the same (multiplying by positive)", f"x \\geq {a} \\cdot {b}", f"x \\geq {a * b}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 8)
        b = random.randint(2, 10)
        c = a * b

        latex = f"-{a}x > {c}"
        solution = f"x < -{b}"
        steps = [f"Divide both sides by -{a}", f"FLIP the inequality sign (dividing by negative)", f"x < \\frac{{{c}}}{{-{a}}}", f"x < -{b}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 6)
        b = random.randint(2, 8)

        latex = f"\\frac{{x}}{{-{a}}} \\leq {b}"
        solution = f"x \\geq -{a * b}"
        steps = [f"Multiply both sides by -{a}", f"FLIP the inequality sign (multiplying by negative)", f"x \\geq -{a} \\cdot {b}", f"x \\geq -{a * b}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = SolvingInequalitiesMultDivGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
