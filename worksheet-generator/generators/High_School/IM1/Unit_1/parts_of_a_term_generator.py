"""
Parts of a Term Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class PartsOfATermGenerator:
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
        problem_type = random.choice(['coefficient', 'variable', 'constant'])

        if problem_type == 'coefficient':
            coef = random.randint(2, 12)
            var = random.choice(['x', 'y', 'a', 'b'])
            latex = f"\\text{{What is the coefficient in }} {coef}{var}?"
            solution = f"{coef}"
            steps = [f"The coefficient is the number multiplied by the variable", f"Answer: {coef}"]
        elif problem_type == 'variable':
            coef = random.randint(2, 9)
            var = random.choice(['x', 'y', 'n', 'm'])
            latex = f"\\text{{What is the variable in }} {coef}{var}?"
            solution = f"{var}"
            steps = [f"The variable is the letter in the term", f"Answer: {var}"]
        else:
            const = random.randint(1, 20)
            latex = f"\\text{{Is }} {const} \\text{{ a constant or a variable?}}"
            solution = "constant"
            steps = ["A constant is a number without a variable", "Answer: constant"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        problem_type = random.choice(['identify_all', 'coefficient_with_negative'])

        if problem_type == 'identify_all':
            coef = random.randint(2, 15)
            var = random.choice(['x', 'y', 'z'])
            latex = f"\\text{{Identify the coefficient and variable in }} {coef}{var}"
            solution = f"coefficient: {coef}, variable: {var}"
            steps = [f"Coefficient is {coef}", f"Variable is {var}"]
        else:
            coef = random.randint(2, 12)
            var = random.choice(['x', 'y', 'a'])
            latex = f"\\text{{What is the coefficient in }} -{coef}{var}?"
            solution = f"-{coef}"
            steps = ["The coefficient includes the sign", f"Answer: -{coef}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        problem_type = random.choice(['multiple_terms', 'implied_coefficient'])

        if problem_type == 'multiple_terms':
            c1 = random.randint(2, 9)
            c2 = random.randint(2, 9)
            const = random.randint(1, 15)
            latex = f"\\text{{List all coefficients in }} {c1}x + {c2}y - {const}"
            solution = f"{c1}, {c2}"
            steps = [f"Coefficient of x is {c1}", f"Coefficient of y is {c2}", f"{const} is a constant term, not a coefficient"]
        else:
            var = random.choice(['x', 'y', 'a', 'b'])
            latex = f"\\text{{What is the coefficient in }} {var}?"
            solution = "1"
            steps = [f"When no number is written, the coefficient is 1", f"Answer: 1"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        c1 = random.randint(2, 8)
        c2 = random.randint(2, 8)
        c3 = random.randint(2, 8)
        const = random.randint(5, 20)
        latex = f"\\text{{In }} {c1}x^2 - {c2}y + z + {const}\\text{{, identify all coefficients and constants}}"
        solution = f"coefficients: {c1}, -{c2}, 1; constant: {const}"
        steps = [f"Coefficient of x^2 is {c1}", f"Coefficient of y is -{c2}", f"Coefficient of z is 1", f"Constant term is {const}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = PartsOfATermGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
