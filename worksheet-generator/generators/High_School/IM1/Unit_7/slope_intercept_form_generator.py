"""
Slope-Intercept Form Generator
Creates problems about y = mx + b form
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class SlopeInterceptFormGenerator:
    """Generates slope-intercept form problems."""

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

    def _format_equation(self, m, b):
        """Format y = mx + b nicely"""
        if m == 0:
            return f"y = {b}"
        elif m == 1:
            m_part = "x"
        elif m == -1:
            m_part = "-x"
        else:
            m_part = f"{m}x"

        if b == 0:
            return f"y = {m_part}"
        elif b > 0:
            return f"y = {m_part} + {b}"
        else:
            return f"y = {m_part} - {abs(b)}"

    def _generate_easy(self) -> Equation:
        """Identify slope and y-intercept from equation"""
        m = random.randint(-5, 5)
        b = random.randint(-10, 10)

        eq = self._format_equation(m, b)

        problem_type = random.choice(['slope', 'intercept', 'both'])

        if problem_type == 'slope':
            latex = f"\\text{{What is the slope of }} {eq}?"
            solution = str(m)
            steps = [
                f"\\text{{In }} y = mx + b, m \\text{{ is the slope}}",
                f"\\text{{Slope}} = {m}"
            ]
        elif problem_type == 'intercept':
            latex = f"\\text{{What is the y-intercept of }} {eq}?"
            solution = str(b)
            steps = [
                f"\\text{{In }} y = mx + b, b \\text{{ is the y-intercept}}",
                f"\\text{{y-intercept}} = {b}"
            ]
        else:
            latex = f"\\text{{Identify the slope and y-intercept of }} {eq}."
            solution = f"m = {m}, b = {b}"
            steps = [
                f"\\text{{Compare to }} y = mx + b",
                f"\\text{{Slope }} m = {m}",
                f"\\text{{y-intercept }} b = {b}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Write equation given slope and y-intercept or a point"""
        problem_type = random.choice(['from_m_b', 'from_point'])

        if problem_type == 'from_m_b':
            m = random.randint(-4, 4)
            b = random.randint(-8, 8)

            latex = f"\\text{{Write the equation of a line with slope }} {m} \\text{{ and y-intercept }} {b}."
            solution = self._format_equation(m, b)

            steps = [
                f"\\text{{Use }} y = mx + b",
                f"\\text{{Substitute }} m = {m}, b = {b}",
                f"{solution}"
            ]
        else:
            # Given slope and one point
            m = random.randint(-3, 3)
            while m == 0:
                m = random.randint(-3, 3)
            x1 = random.randint(1, 5)
            # Calculate b such that point is on line
            b = random.randint(-8, 8)
            y1 = m * x1 + b

            latex = f"\\text{{Write the equation of a line with slope }} {m} \\text{{ passing through }} ({x1}, {y1})."
            solution = self._format_equation(m, b)

            steps = [
                f"\\text{{Use }} y = mx + b \\text{{ with }} m = {m}",
                f"\\text{{Substitute the point: }} {y1} = {m}({x1}) + b",
                f"{y1} = {m * x1} + b",
                f"b = {y1} - {m * x1} = {b}",
                f"\\text{{Equation: }} {solution}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Write equation from two points or convert from standard form"""
        problem_type = random.choice(['two_points', 'from_standard'])

        if problem_type == 'two_points':
            # Choose points that give integer slope
            x1 = random.randint(-3, 3)
            y1 = random.randint(-5, 5)
            dx = random.randint(1, 4)
            m = random.randint(-3, 3)
            while m == 0:
                m = random.randint(-3, 3)
            dy = m * dx

            x2 = x1 + dx
            y2 = y1 + dy

            b = y1 - m * x1

            latex = f"\\text{{Write the equation of the line through }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})."
            solution = self._format_equation(m, b)

            steps = [
                f"\\text{{Find slope: }} m = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}} = \\frac{{{dy}}}{{{dx}}} = {m}",
                f"\\text{{Use point-slope with }} ({x1}, {y1}):",
                f"y - {y1} = {m}(x - {x1})",
                f"y = {m}x - {m * x1} + {y1}",
                f"y = {m}x + {b}",
                f"\\text{{or }} {solution}"
            ]
        else:
            # Convert from standard form Ax + By = C
            a = random.randint(1, 5)
            b_coef = random.randint(1, 5)
            c = random.randint(-15, 15)

            # y = (-a/b)x + c/b
            # For integer m and b, we need a and c divisible by b_coef
            a = random.randint(1, 4) * b_coef
            c = random.randint(-5, 5) * b_coef

            m = -a // b_coef
            b = c // b_coef

            latex = f"\\text{{Convert to slope-intercept form: }} {a}x + {b_coef}y = {c}"
            solution = self._format_equation(m, b)

            steps = [
                f"\\text{{Solve for y:}}",
                f"{b_coef}y = -{a}x + {c}",
                f"y = \\frac{{-{a}x + {c}}}{{{b_coef}}}",
                f"y = {m}x + {b}",
                f"\\text{{or }} {solution}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Parallel/perpendicular lines or word problems"""
        problem_type = random.choice(['parallel', 'perpendicular', 'word_problem'])

        if problem_type == 'parallel':
            m = random.randint(-4, 4)
            while m == 0:
                m = random.randint(-4, 4)
            b1 = random.randint(-8, 8)
            x1 = random.randint(-4, 4)
            y1 = random.randint(-8, 8)
            b2 = y1 - m * x1

            given_eq = self._format_equation(m, b1)

            latex = f"\\text{{Write the equation of a line parallel to }} {given_eq} \\text{{ through }} ({x1}, {y1})."
            solution = self._format_equation(m, b2)

            steps = [
                f"\\text{{Parallel lines have equal slopes: }} m = {m}",
                f"\\text{{Use point }} ({x1}, {y1}):",
                f"{y1} = {m}({x1}) + b",
                f"b = {y1} - {m * x1} = {b2}",
                f"\\text{{Equation: }} {solution}"
            ]

        elif problem_type == 'perpendicular':
            m1 = random.choice([2, 3, 4, -2, -3, -4])
            b1 = random.randint(-5, 5)
            m2 = f"-\\frac{{1}}{{{m1}}}" if m1 > 0 else f"\\frac{{1}}{{{abs(m1)}}}"
            m2_val = -1 / m1

            # For clean answer, choose point carefully
            x1 = m1  # x-coordinate
            y1 = random.randint(-5, 5)
            b2 = y1 - m2_val * x1

            given_eq = self._format_equation(m1, b1)

            latex = f"\\text{{Write the equation of a line perpendicular to }} {given_eq} \\text{{ through }} ({x1}, {y1})."
            solution = f"y = {m2}x + {b2}"

            steps = [
                f"\\text{{Perpendicular slope: }} m = -\\frac{{1}}{{{m1}}} = {m2}",
                f"\\text{{Use point }} ({x1}, {y1}):",
                f"\\text{{Equation: }} y = {m2}x + {b2}"
            ]

        else:
            # Word problem
            start = random.randint(100, 500)
            rate = random.randint(10, 50)

            latex = f"\\text{{A phone plan costs \\${start} for the phone plus \\${rate}/month. Write an equation for total cost }} C \\text{{ after }} m \\text{{ months.}}"
            solution = f"C = {rate}m + {start}"

            steps = [
                f"\\text{{Initial cost (y-intercept): }} {start}",
                f"\\text{{Rate of change (slope): }} {rate} \\text{{ per month}}",
                f"C = {rate}m + {start}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = SlopeInterceptFormGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
