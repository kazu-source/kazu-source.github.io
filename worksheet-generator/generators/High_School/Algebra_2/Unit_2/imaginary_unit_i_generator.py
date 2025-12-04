"""
Imaginary Unit i Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class ImaginaryUnitIGenerator:
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
        power = random.choice([2, 3, 4])

        if power == 2:
            latex = f"i^2 = ?"
            solution = "-1"
            steps = ["By definition, i^2 = -1"]
        elif power == 3:
            latex = f"i^3 = ?"
            solution = "-i"
            steps = [
                "i^3 = i^2 \\cdot i",
                "= (-1) \\cdot i",
                "= -i"
            ]
        else:
            latex = f"i^4 = ?"
            solution = "1"
            steps = [
                "i^4 = (i^2)^2",
                "= (-1)^2",
                "= 1"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        power = random.randint(5, 12)
        remainder = power % 4

        results = {0: "1", 1: "i", 2: "-1", 3: "-i"}
        solution = results[remainder]

        latex = f"i^{{{power}}} = ?"
        steps = [
            f"Divide exponent by 4: {power} = 4({power//4}) + {remainder}",
            f"i^{{{power}}} = (i^4)^{{{power//4}}} \\cdot i^{{{remainder}}}",
            f"= 1^{{{power//4}}} \\cdot i^{{{remainder}}}",
            f"= i^{{{remainder}}} = {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        problem_type = random.choice(['high_power', 'negative_power'])

        if problem_type == 'high_power':
            power = random.randint(20, 50)
            remainder = power % 4
            results = {0: "1", 1: "i", 2: "-1", 3: "-i"}
            solution = results[remainder]

            latex = f"i^{{{power}}} = ?"
            steps = [
                f"{power} \\div 4 = {power//4} \\text{{ remainder }} {remainder}",
                f"i^{{{power}}} = (i^4)^{{{power//4}}} \\cdot i^{{{remainder}}}",
                f"= 1 \\cdot i^{{{remainder}}} = {solution}"
            ]
        else:
            power = random.randint(5, 15)
            remainder = power % 4
            # For negative powers: i^(-n) = 1/i^n
            results = {0: "1", 1: "-i", 2: "-1", 3: "i"}
            solution = results[remainder]

            latex = f"i^{{-{power}}} = ?"
            steps = [
                f"i^{{-{power}}} = \\frac{{1}}{{i^{{{power}}}}}",
                f"i^{{{power}}} has remainder {remainder} when divided by 4",
                f"1/i^{{{power}}} = 1/{results[(4-remainder)%4]} = {solution}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        problem_type = random.choice(['sum_powers', 'product_powers'])

        if problem_type == 'sum_powers':
            p1 = random.randint(6, 15)
            p2 = random.randint(6, 15)

            r1 = p1 % 4
            r2 = p2 % 4
            results = {0: 1, 1: 'i', 2: -1, 3: '-i'}

            latex = f"i^{{{p1}}} + i^{{{p2}}} = ?"
            val1 = results[r1]
            val2 = results[r2]

            # Simplified calculation
            if isinstance(val1, int) and isinstance(val2, int):
                solution = str(val1 + val2)
            elif val1 == val2:
                solution = f"2{val1}" if val1 not in [1, -1] else str(2*val1)
            else:
                solution = f"{val1} + {val2}"

            steps = [
                f"i^{{{p1}}} = i^{{{r1}}} = {val1}",
                f"i^{{{p2}}} = i^{{{r2}}} = {val2}",
                f"Sum: {val1} + {val2} = {solution}"
            ]
        else:
            p1 = random.randint(5, 12)
            p2 = random.randint(5, 12)
            total = p1 + p2
            remainder = total % 4
            results = {0: "1", 1: "i", 2: "-1", 3: "-i"}
            solution = results[remainder]

            latex = f"i^{{{p1}}} \\cdot i^{{{p2}}} = ?"
            steps = [
                f"i^{{{p1}}} \\cdot i^{{{p2}}} = i^{{{p1}+{p2}}}",
                f"= i^{{{total}}}",
                f"{total} = 4({total//4}) + {remainder}",
                f"i^{{{total}}} = {solution}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = ImaginaryUnitIGenerator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\n{d.upper()}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {p.latex}\n  Sol: {p.solution}\n")

if __name__ == '__main__': main()
