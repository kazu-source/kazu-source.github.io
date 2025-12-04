"""
Properties of Exponents - Addition and Subtraction Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PropertiesExponentsAddSubGenerator:
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
                base = random.randint(2, 5)
                exp1 = random.randint(2, 6)
                exp2 = random.randint(2, 6)
                latex = f"{base}^{{{exp1}}} + {base}^{{{exp2}}}"
                val1 = base ** exp1
                val2 = base ** exp2
                solution = f"{val1 + val2}"
                steps = [f"Calculate: {base}^{exp1} = {val1}", f"Calculate: {base}^{exp2} = {val2}", f"Sum: {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
                base = random.randint(2, 4)
                exp = random.randint(3, 6)
                coef = random.randint(2, 5)
                latex = f"{coef} \\cdot {base}^{{{exp}}} + {base}^{{{exp}}}"
                solution = f"{coef + 1} \\cdot {base}^{{{exp}}}"
                steps = [f"Factor out {base}^{exp}", f"= ({coef} + 1) \\cdot {base}^{exp}", f"= {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
                a = random.randint(2, 5)
                n = random.randint(3, 6)
                latex = f"2 \\cdot {a}^{{{n+1}}} - 3 \\cdot {a}^{{{n}}}"
                solution = f"{a}^{{{n}}}(2 \\cdot {a} - 3)"
                steps = [f"Factor out {a}^{n}", f"= {a}^{n}(2 \\cdot {a} - 3)", f"Result: {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
                base = random.randint(2, 4)
                n = random.randint(2, 5)
                latex = f"{base}^{{{n+2}}} + {base}^{{{n+1}}} + {base}^{{{n}}}"
                solution = f"{base}^{{{n}}}({base}^2 + {base} + 1)"
                steps = [f"Factor out {base}^{n}", f"= {base}^{n}({base}^2 + {base} + 1)", f"Result: {solution}"]
                return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = PropertiesExponentsAddSubGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
