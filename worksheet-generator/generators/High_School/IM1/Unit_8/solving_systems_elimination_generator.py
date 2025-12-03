"""
Solving Systems by Elimination Generator
Creates problems about solving systems of equations using elimination
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class SolvingSystemsEliminationGenerator:
    """Generates systems of equations problems for elimination method."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _format_equation(self, a, b, c):
        """Format ax + by = c nicely"""
        parts = []
        if a == 1:
            parts.append("x")
        elif a == -1:
            parts.append("-x")
        else:
            parts.append(f"{a}x")

        if b == 1:
            parts.append("+ y")
        elif b == -1:
            parts.append("- y")
        elif b > 0:
            parts.append(f"+ {b}y")
        else:
            parts.append(f"- {abs(b)}y")

        return f"{parts[0]} {parts[1]} = {c}"

    def _generate_easy(self) -> Equation:
        """Coefficients already set up for direct elimination"""
        x = random.randint(-5, 5)
        y = random.randint(-5, 5)

        # Create system where one variable cancels directly
        a1 = random.randint(1, 4)
        b1 = random.randint(1, 4)
        a2 = random.randint(1, 4)
        b2 = -b1  # Opposite coefficients for y

        c1 = a1 * x + b1 * y
        c2 = a2 * x + b2 * y

        eq1 = self._format_equation(a1, b1, c1)
        eq2 = self._format_equation(a2, b2, c2)

        latex = f"\\text{{Solve by elimination: }} \\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}"
        solution = f"({x}, {y})"

        steps = [
            f"\\text{{Add the equations to eliminate y:}}",
            f"{a1 + a2}x = {c1 + c2}",
            f"x = {x}",
            f"\\text{{Substitute into first equation: }} {a1}({x}) + {b1}y = {c1}",
            f"{b1}y = {c1 - a1*x}",
            f"y = {y}",
            f"\\text{{Solution: }} ({x}, {y})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Requires multiplying one equation before eliminating"""
        x = random.randint(-5, 5)
        y = random.randint(-5, 5)

        # Create system where one equation needs to be multiplied
        a1 = random.randint(1, 3)
        b1 = random.randint(1, 3)
        mult = random.randint(2, 3)
        a2 = random.randint(1, 4)
        b2 = b1 * mult  # b2 is a multiple of b1

        c1 = a1 * x + b1 * y
        c2 = a2 * x + b2 * y

        eq1 = self._format_equation(a1, b1, c1)
        eq2 = self._format_equation(a2, b2, c2)

        latex = f"\\text{{Solve by elimination: }} \\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}"
        solution = f"({x}, {y})"

        steps = [
            f"\\text{{Multiply first equation by }} {mult}: {self._format_equation(a1*mult, b1*mult, c1*mult)}",
            f"\\text{{Subtract to eliminate y:}}",
            f"{a1*mult - a2}x = {c1*mult - c2}",
            f"x = {x}",
            f"\\text{{Substitute to find }} y = {y}",
            f"\\text{{Solution: }} ({x}, {y})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Requires multiplying both equations"""
        x = random.randint(-4, 4)
        y = random.randint(-4, 4)

        # Create system where both need multiplying
        a1 = random.randint(2, 4)
        b1 = random.randint(2, 4)
        a2 = random.randint(2, 4)
        b2 = random.randint(2, 4)

        # Make sure they're not too easy
        while b1 == b2 or b1 == -b2 or a1 == a2:
            a1 = random.randint(2, 4)
            b1 = random.randint(2, 4)
            a2 = random.randint(2, 4)
            b2 = random.randint(2, 4)

        c1 = a1 * x + b1 * y
        c2 = a2 * x + b2 * y

        eq1 = self._format_equation(a1, b1, c1)
        eq2 = self._format_equation(a2, b2, c2)

        # Find LCM for elimination
        from math import gcd
        lcm_b = abs(b1 * b2) // gcd(abs(b1), abs(b2))
        mult1 = lcm_b // abs(b1)
        mult2 = lcm_b // abs(b2)

        latex = f"\\text{{Solve by elimination: }} \\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}"
        solution = f"({x}, {y})"

        steps = [
            f"\\text{{Multiply equation 1 by }} {mult1} \\text{{ and equation 2 by }} {mult2}",
            f"\\text{{to get matching coefficients for y}}",
            f"\\text{{Then add or subtract to eliminate y}}",
            f"\\text{{Solve for x, then substitute to find y}}",
            f"\\text{{Solution: }} ({x}, {y})"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Word problems or special cases"""
        problem_type = random.choice(['word_problem', 'special'])

        if problem_type == 'word_problem':
            # Create a word problem
            x = random.randint(2, 8)
            y = random.randint(2, 8)

            problems = [
                {
                    "context": f"Adult tickets cost $12 and child tickets cost $8. The total tickets sold was {x + y} and total revenue was ${12*x + 8*y}.",
                    "question": "How many of each type were sold?",
                    "var1": "adult tickets",
                    "var2": "child tickets",
                    "eq1": f"a + c = {x + y}",
                    "eq2": f"12a + 8c = {12*x + 8*y}"
                },
                {
                    "context": f"The sum of two numbers is {x + y} and their difference is {abs(x - y)}.",
                    "question": "Find the two numbers.",
                    "var1": "larger number",
                    "var2": "smaller number",
                    "eq1": f"x + y = {x + y}",
                    "eq2": f"x - y = {abs(x - y)}"
                }
            ]

            prob = random.choice(problems)
            latex = f"\\text{{{prob['context']} {prob['question']}}}"

            if "Adult" in prob["context"]:
                solution = f"\\text{{{x} adult, {y} child}}"
            else:
                solution = f"\\text{{{max(x,y)} and {min(x,y)}}}"

            steps = [
                f"\\text{{Let variables represent the unknowns}}",
                f"\\text{{Set up equations: }} {prob['eq1']} \\text{{ and }} {prob['eq2']}",
                f"\\text{{Use elimination to solve}}",
                f"\\text{{Solution: }} {solution}"
            ]

        else:
            # Special cases
            case_type = random.choice(['infinite', 'no_solution'])

            if case_type == 'infinite':
                a = random.randint(1, 3)
                b = random.randint(1, 3)
                c = random.randint(1, 10)
                mult = random.randint(2, 3)

                eq1 = self._format_equation(a, b, c)
                eq2 = self._format_equation(a * mult, b * mult, c * mult)

                latex = f"\\text{{Solve: }} \\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}"
                solution = "\\text{Infinitely many solutions}"

                steps = [
                    f"\\text{{Notice equation 2 is equation 1 multiplied by }} {mult}",
                    f"\\text{{The equations represent the same line}}",
                    f"\\text{{Infinitely many solutions}}"
                ]

            else:
                a = random.randint(1, 3)
                b = random.randint(1, 3)
                c1 = random.randint(1, 10)
                c2 = c1 + random.randint(1, 5)  # Different constant
                mult = random.randint(2, 3)

                eq1 = self._format_equation(a, b, c1)
                eq2 = self._format_equation(a * mult, b * mult, c2 * mult)

                latex = f"\\text{{Solve: }} \\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}"
                solution = "\\text{No solution}"

                steps = [
                    f"\\text{{The left sides are proportional but right sides are not}}",
                    f"\\text{{The lines are parallel (same slope, different y-intercept)}}",
                    f"\\text{{No solution - the lines never intersect}}"
                ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = SolvingSystemsEliminationGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
