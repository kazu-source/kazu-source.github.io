"""
Slope Generator
Creates problems about calculating and understanding slope
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class SlopeGenerator:
    """Generates problems about slope."""

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

    def _generate_easy(self) -> Equation:
        """Calculate slope from two points with small integers"""
        x1 = random.randint(0, 5)
        y1 = random.randint(0, 5)

        # Ensure non-zero denominator and integer slope
        dx = random.randint(1, 4)
        slope = random.randint(-3, 3)
        dy = slope * dx

        x2 = x1 + dx
        y2 = y1 + dy

        latex = f"\\text{{Find the slope of the line through }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})."
        solution = str(slope)

        steps = [
            f"\\text{{Slope}} = \\frac{{y_2 - y_1}}{{x_2 - x_1}}",
            f"= \\frac{{{y2} - {y1}}}{{{x2} - {x1}}}",
            f"= \\frac{{{dy}}}{{{dx}}}",
            f"= {slope}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Slope with negative coordinates or fractional results"""
        problem_type = random.choice(['fraction', 'negative_coords', 'interpret'])

        if problem_type == 'fraction':
            x1 = random.randint(-5, 5)
            y1 = random.randint(-5, 5)

            dx = random.randint(2, 5)
            dy = random.randint(1, 4)
            # Make sure it's not reducible to integer
            while dy % dx == 0:
                dy = random.randint(1, 4)

            x2 = x1 + dx
            y2 = y1 + dy

            from math import gcd
            g = gcd(abs(dy), abs(dx))
            num = dy // g
            den = dx // g

            latex = f"\\text{{Find the slope of the line through }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})."
            solution = f"\\frac{{{num}}}{{{den}}}"

            steps = [
                f"\\text{{Slope}} = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}} = \\frac{{{dy}}}{{{dx}}} = \\frac{{{num}}}{{{den}}}"
            ]

        elif problem_type == 'negative_coords':
            x1 = random.randint(-8, -2)
            y1 = random.randint(-8, -2)
            x2 = random.randint(2, 8)
            y2 = random.randint(2, 8)

            dy = y2 - y1
            dx = x2 - x1

            from math import gcd
            g = gcd(abs(dy), abs(dx))
            num = dy // g
            den = dx // g

            latex = f"\\text{{Find the slope of the line through }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})."
            if den == 1:
                solution = str(num)
            else:
                solution = f"\\frac{{{num}}}{{{den}}}"

            steps = [
                f"\\text{{Slope}} = \\frac{{{y2} - ({y1})}}{{{x2} - ({x1})}} = \\frac{{{dy}}}{{{dx}}} = {solution}"
            ]

        else:
            # Interpret slope
            slopes = [
                (2, "positive", "rises 2 units for every 1 unit right"),
                (-3, "negative", "falls 3 units for every 1 unit right"),
                (0, "zero", "horizontal line"),
                ("\\frac{1}{2}", "positive", "rises 1 unit for every 2 units right"),
            ]
            slope, sign, meaning = random.choice(slopes)

            latex = f"\\text{{A line has slope }} {slope}. \\text{{ Is it positive, negative, or zero?}}"
            solution = sign

            steps = [
                f"\\text{{Slope }} {slope} \\text{{ is {sign}}}",
                f"\\text{{This means the line {meaning}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Vertical/horizontal lines or find missing coordinate"""
        problem_type = random.choice(['special', 'find_missing'])

        if problem_type == 'special':
            line_type = random.choice(['vertical', 'horizontal'])

            if line_type == 'vertical':
                x = random.randint(-5, 5)
                y1 = random.randint(-5, 0)
                y2 = random.randint(1, 5)

                latex = f"\\text{{Find the slope of the line through }} ({x}, {y1}) \\text{{ and }} ({x}, {y2})."
                solution = "\\text{Undefined}"

                steps = [
                    f"\\text{{Slope}} = \\frac{{{y2} - {y1}}}{{{x} - {x}}} = \\frac{{{y2 - y1}}}{{0}}",
                    f"\\text{{Division by zero is undefined}}",
                    f"\\text{{This is a vertical line with undefined slope}}"
                ]
            else:
                y = random.randint(-5, 5)
                x1 = random.randint(-5, 0)
                x2 = random.randint(1, 5)

                latex = f"\\text{{Find the slope of the line through }} ({x1}, {y}) \\text{{ and }} ({x2}, {y})."
                solution = "0"

                steps = [
                    f"\\text{{Slope}} = \\frac{{{y} - {y}}}{{{x2} - {x1}}} = \\frac{{0}}{{{x2 - x1}}} = 0",
                    f"\\text{{This is a horizontal line with slope 0}}"
                ]
        else:
            # Find missing coordinate given slope
            x1 = random.randint(0, 5)
            y1 = random.randint(0, 5)
            slope = random.randint(-3, 3)
            while slope == 0:
                slope = random.randint(-3, 3)

            dx = random.randint(2, 5)
            x2 = x1 + dx
            y2 = y1 + slope * dx

            # Ask for y2 given everything else
            latex = f"\\text{{Points }} ({x1}, {y1}) \\text{{ and }} ({x2}, y) \\text{{ have slope }} {slope}. \\text{{ Find }} y."
            solution = str(y2)

            steps = [
                f"\\text{{Slope}} = \\frac{{y - {y1}}}{{{x2} - {x1}}} = {slope}",
                f"\\frac{{y - {y1}}}{{{dx}}} = {slope}",
                f"y - {y1} = {slope} \\times {dx} = {slope * dx}",
                f"y = {y1} + {slope * dx} = {y2}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Parallel/perpendicular lines or rate of change context"""
        problem_type = random.choice(['parallel', 'perpendicular', 'rate_of_change'])

        if problem_type == 'parallel':
            m = random.randint(-4, 4)
            while m == 0:
                m = random.randint(-4, 4)

            x1, y1 = random.randint(-5, 5), random.randint(-5, 5)
            x2, y2 = x1 + random.randint(1, 4), y1 + m * random.randint(1, 4)

            latex = f"\\text{{Line 1 passes through }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2}). \\text{{ What slope must a parallel line have?}}"
            solution = str(m)

            steps = [
                f"\\text{{First find slope of Line 1:}}",
                f"m_1 = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}} = {m}",
                f"\\text{{Parallel lines have equal slopes}}",
                f"\\text{{Parallel line slope}} = {m}"
            ]

        elif problem_type == 'perpendicular':
            # Use simple fractions
            m_vals = [(2, "-\\frac{1}{2}"), (3, "-\\frac{1}{3}"), (-2, "\\frac{1}{2}"),
                      (-4, "\\frac{1}{4}"), (1, "-1"), (-1, "1")]
            m, perp_m = random.choice(m_vals)

            latex = f"\\text{{A line has slope }} {m}. \\text{{ What is the slope of a perpendicular line?}}"
            solution = perp_m

            steps = [
                f"\\text{{Perpendicular slopes are negative reciprocals}}",
                f"m_\\perp = -\\frac{{1}}{{{m}}} = {perp_m}"
            ]

        else:
            # Rate of change in context
            rate = random.randint(5, 20)
            start = random.randint(20, 100)

            contexts = [
                (f"water rises {rate} cm per hour", rate, "cm/hour"),
                (f"temperature drops {rate}°F per hour", -rate, "°F/hour"),
                (f"car travels {rate} miles per gallon", rate, "miles/gallon"),
            ]

            context, slope, units = random.choice(contexts)

            latex = f"\\text{{A {context}. What is the rate of change (slope)?}}"
            solution = f"{slope} \\text{{ {units}}}"

            steps = [
                f"\\text{{Rate of change = slope}}",
                f"\\text{{The slope is }} {slope} \\text{{ {units}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = SlopeGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
