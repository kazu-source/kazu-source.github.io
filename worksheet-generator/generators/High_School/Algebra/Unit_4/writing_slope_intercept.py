"""
Generator for writing slope-intercept equations worksheets.
Chapter 4: Linear Equations (Two Variables) - Writing Slope-Intercept Equations
"""

import random
import sys
from pathlib import Path
from dataclasses import dataclass
from fractions import Fraction

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


@dataclass
class WritingSlopeInterceptProblem:
    """Represents a problem for writing equations in slope-intercept form."""
    given_info: str  # What information is given (e.g., "slope and point", "two points", etc.)
    given_data: dict  # Dictionary containing the given information
    equation_latex: str  # The resulting equation in LaTeX
    work_shown: list  # Steps to solve the problem
    difficulty: str  # easy, medium, hard, challenge
    problem_latex: str  # LaTeX string for the problem statement
    answer_latex: str  # LaTeX string for the answer


class WritingSlopeInterceptGenerator:
    """Generator for writing slope-intercept equations problems."""

    def __init__(self, seed=None):
        """
        Initialize the generator.

        Args:
            seed: Random seed for reproducibility
        """
        if seed is not None:
            random.seed(seed)

    def _format_slope(self, numerator, denominator=1):
        """Format a slope as a fraction or integer."""
        if denominator == 1:
            if numerator == 1:
                return ""
            elif numerator == -1:
                return "-"
            else:
                return str(numerator)
        else:
            frac = Fraction(numerator, denominator).limit_denominator()
            if frac.denominator == 1:
                if frac.numerator == 1:
                    return ""
                elif frac.numerator == -1:
                    return "-"
                else:
                    return str(frac.numerator)
            else:
                return f"\\frac{{{frac.numerator}}}{{{frac.denominator}}}"

    def _calculate_from_two_points(self, x1, y1, x2, y2):
        """Calculate slope and y-intercept from two points."""
        if x2 == x1:
            return None, None, "undefined"  # Vertical line

        slope = Fraction(y2 - y1, x2 - x1).limit_denominator()
        y_intercept = y1 - slope * x1

        return float(slope), float(y_intercept), slope

    def _format_equation(self, slope, y_intercept):
        """Format the equation in slope-intercept form."""
        if isinstance(slope, Fraction):
            slope_str = self._format_slope(slope.numerator, slope.denominator)
        else:
            slope_frac = Fraction(slope).limit_denominator()
            slope_str = self._format_slope(slope_frac.numerator, slope_frac.denominator)

        if isinstance(y_intercept, Fraction):
            y_int_frac = y_intercept
        else:
            y_int_frac = Fraction(y_intercept).limit_denominator()

        # Handle special cases
        if slope == 0:
            return f"y = {y_int_frac}"

        # Format the equation
        if slope_str == "":
            slope_part = "x"
        elif slope_str == "-":
            slope_part = "-x"
        else:
            slope_part = f"{slope_str}x"

        if y_int_frac == 0:
            equation = f"y = {slope_part}"
        elif y_int_frac > 0:
            if y_int_frac.denominator == 1:
                equation = f"y = {slope_part} + {y_int_frac.numerator}"
            else:
                equation = f"y = {slope_part} + \\frac{{{y_int_frac.numerator}}}{{{y_int_frac.denominator}}}"
        else:
            if y_int_frac.denominator == 1:
                equation = f"y = {slope_part} - {abs(y_int_frac.numerator)}"
            else:
                equation = f"y = {slope_part} - \\frac{{{abs(y_int_frac.numerator)}}}{{{y_int_frac.denominator}}}"

        return equation

    def generate_problem(self, difficulty: str) -> WritingSlopeInterceptProblem:
        """
        Generate a single writing slope-intercept equation problem.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            WritingSlopeInterceptProblem object
        """
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> WritingSlopeInterceptProblem:
        """Generate easy problem (given slope and y-intercept directly)."""
        slope = random.randint(1, 5) * random.choice([-1, 1])
        y_intercept = random.randint(-8, 8)

        given_info = "slope and y-intercept"
        given_data = {
            'slope': slope,
            'y_intercept': y_intercept
        }

        equation = self._format_equation(slope, y_intercept)

        problem_latex = f"Write the equation of a line with slope $m = {slope}$ and y-intercept $b = {y_intercept}$"
        answer_latex = f"${equation}$"

        work_shown = [
            f"Using slope-intercept form: $y = mx + b$",
            f"Substitute $m = {slope}$ and $b = {y_intercept}$",
            f"Equation: ${equation}$"
        ]

        return WritingSlopeInterceptProblem(
            given_info=given_info,
            given_data=given_data,
            equation_latex=equation,
            work_shown=work_shown,
            difficulty='easy',
            problem_latex=problem_latex,
            answer_latex=answer_latex
        )

    def _generate_medium(self) -> WritingSlopeInterceptProblem:
        """Generate medium problem (given slope and a point)."""
        slope = Fraction(random.randint(-5, 5), random.randint(1, 3)).limit_denominator()
        while slope == 0:
            slope = Fraction(random.randint(-5, 5), random.randint(1, 3)).limit_denominator()

        # Generate a point
        x = random.randint(-6, 6)
        y = random.randint(-6, 6)

        # Calculate y-intercept: b = y - mx
        y_intercept = y - slope * x

        given_info = "slope and a point"
        given_data = {
            'slope': float(slope),
            'point': (x, y)
        }

        equation = self._format_equation(slope, y_intercept)
        slope_str = self._format_slope(slope.numerator, slope.denominator)

        problem_latex = f"Write the equation of a line with slope $m = {slope_str}$ that passes through the point $({x}, {y})$"
        answer_latex = f"${equation}$"

        work_shown = [
            f"Use point-slope form: $y - y_1 = m(x - x_1)$",
            f"Substitute $m = {slope_str}$, $(x_1, y_1) = ({x}, {y})$",
            f"$y - {y} = {slope_str}(x - {x})$",
            f"Solve for y to get slope-intercept form",
            f"${equation}$"
        ]

        return WritingSlopeInterceptProblem(
            given_info=given_info,
            given_data=given_data,
            equation_latex=equation,
            work_shown=work_shown,
            difficulty='medium',
            problem_latex=problem_latex,
            answer_latex=answer_latex
        )

    def _generate_hard(self) -> WritingSlopeInterceptProblem:
        """Generate hard problem (given two points)."""
        # Generate two points
        x1 = random.randint(-8, -2)
        y1 = random.randint(-8, 8)
        x2 = random.randint(2, 8)
        y2 = random.randint(-8, 8)

        # Ensure different x-coordinates
        while x2 == x1:
            x2 = random.randint(2, 8)

        slope_val, y_int_val, slope_frac = self._calculate_from_two_points(x1, y1, x2, y2)

        given_info = "two points"
        given_data = {
            'point1': (x1, y1),
            'point2': (x2, y2)
        }

        equation = self._format_equation(slope_val, y_int_val)

        problem_latex = f"Write the equation of a line that passes through the points $({x1}, {y1})$ and $({x2}, {y2})$"
        answer_latex = f"${equation}$"

        slope_str = self._format_slope(slope_frac.numerator, slope_frac.denominator)

        work_shown = [
            f"First, find the slope: $m = \\frac{{y_2 - y_1}}{{x_2 - x_1}}$",
            f"$m = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}} = \\frac{{{y2 - y1}}}{{{x2 - x1}}} = {slope_str}$",
            f"Use point-slope form with one of the points",
            f"Using point $({x1}, {y1})$: $y - {y1} = {slope_str}(x - {x1})$",
            f"Solve for y to get slope-intercept form",
            f"${equation}$"
        ]

        return WritingSlopeInterceptProblem(
            given_info=given_info,
            given_data=given_data,
            equation_latex=equation,
            work_shown=work_shown,
            difficulty='hard',
            problem_latex=problem_latex,
            answer_latex=answer_latex
        )

    def _generate_challenge(self) -> WritingSlopeInterceptProblem:
        """Generate challenge problem (given intercepts or parallel/perpendicular conditions)."""
        problem_type = random.choice(['intercepts', 'parallel', 'perpendicular'])

        if problem_type == 'intercepts':
            # Given x-intercept and y-intercept
            x_int = random.randint(1, 8) * random.choice([-1, 1])
            y_int = random.randint(-8, 8)
            while y_int == 0:  # Avoid line through origin
                y_int = random.randint(-8, 8)

            # Slope = -b/a where (a, 0) is x-intercept and (0, b) is y-intercept
            slope = Fraction(-y_int, x_int).limit_denominator()

            given_info = "x-intercept and y-intercept"
            given_data = {
                'x_intercept': x_int,
                'y_intercept': y_int
            }

            equation = self._format_equation(slope, y_int)

            problem_latex = f"Write the equation of a line with x-intercept ${x_int}$ and y-intercept ${y_int}$"
            answer_latex = f"${equation}$"

            work_shown = [
                f"Points: $({x_int}, 0)$ and $(0, {y_int})$",
                f"Find slope: $m = \\frac{{{y_int} - 0}}{{0 - {x_int}}} = \\frac{{{y_int}}}{{{-x_int}}}$",
                f"Y-intercept is already given: $b = {y_int}$",
                f"${equation}$"
            ]

        elif problem_type == 'parallel':
            # Parallel to given line through a point
            ref_slope = random.randint(1, 4) * random.choice([-1, 1])
            ref_y_int = random.randint(-5, 5)
            ref_equation = self._format_equation(ref_slope, ref_y_int)

            point_x = random.randint(-6, 6)
            point_y = random.randint(-6, 6)

            # Parallel lines have same slope
            slope = ref_slope
            y_intercept = point_y - slope * point_x

            given_info = "parallel to line through point"
            given_data = {
                'reference_line': ref_equation,
                'point': (point_x, point_y),
                'reference_slope': ref_slope
            }

            equation = self._format_equation(slope, y_intercept)

            problem_latex = f"Write the equation of a line parallel to ${ref_equation}$ that passes through $({point_x}, {point_y})$"
            answer_latex = f"${equation}$"

            work_shown = [
                f"Parallel lines have the same slope",
                f"Slope of ${ref_equation}$ is $m = {ref_slope}$",
                f"Use point-slope form with $m = {ref_slope}$ and point $({point_x}, {point_y})$",
                f"${equation}$"
            ]

        else:  # perpendicular
            # Perpendicular to given line through a point
            ref_slope = random.choice([2, 3, 4]) * random.choice([-1, 1])
            ref_y_int = random.randint(-5, 5)
            ref_equation = self._format_equation(ref_slope, ref_y_int)

            point_x = random.randint(-6, 6)
            point_y = random.randint(-6, 6)

            # Perpendicular slope is negative reciprocal
            perp_slope = Fraction(-1, ref_slope).limit_denominator()
            y_intercept = point_y - perp_slope * point_x

            given_info = "perpendicular to line through point"
            given_data = {
                'reference_line': ref_equation,
                'point': (point_x, point_y),
                'reference_slope': ref_slope
            }

            equation = self._format_equation(perp_slope, y_intercept)
            perp_slope_str = self._format_slope(perp_slope.numerator, perp_slope.denominator)

            problem_latex = f"Write the equation of a line perpendicular to ${ref_equation}$ that passes through $({point_x}, {point_y})$"
            answer_latex = f"${equation}$"

            work_shown = [
                f"Perpendicular slopes are negative reciprocals",
                f"Slope of ${ref_equation}$ is $m_1 = {ref_slope}$",
                f"Perpendicular slope: $m_2 = -\\frac{{1}}{{{ref_slope}}} = {perp_slope_str}$",
                f"Use point-slope form with this slope and point $({point_x}, {point_y})$",
                f"${equation}$"
            ]

        return WritingSlopeInterceptProblem(
            given_info=given_info,
            given_data=given_data,
            equation_latex=equation,
            work_shown=work_shown,
            difficulty='challenge',
            problem_latex=problem_latex,
            answer_latex=answer_latex
        )

    def generate_worksheet(self, difficulty: str, num_problems: int = 6) -> list:
        """
        Generate multiple writing slope-intercept equation problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of WritingSlopeInterceptProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty)
            problems.append(problem)
        return problems