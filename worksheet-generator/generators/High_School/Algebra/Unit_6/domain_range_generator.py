"""
Generator for domain and range worksheets.
Chapter 6: Functions - Domain and Range
"""

import random
import sys
from pathlib import Path
from dataclasses import dataclass
from fractions import Fraction
import math

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


@dataclass
class DomainRangeProblem:
    """Represents a domain and range problem."""
    problem_type: str  # 'find_domain', 'find_range', 'both', 'from_graph', 'from_table'
    function: str  # Function expression in LaTeX
    domain: str  # Domain in interval notation or set notation
    range: str  # Range in interval notation or set notation
    domain_latex: str  # Domain in LaTeX format
    range_latex: str  # Range in LaTeX format
    restrictions: list  # List of restrictions (e.g., "x ≠ 2", "x ≥ 0")
    problem_latex: str  # Problem statement in LaTeX
    answer_latex: str  # Answer in LaTeX
    work_shown: list  # Step-by-step solution
    difficulty: str  # easy, medium, hard, challenge


class DomainRangeGenerator:
    """Generator for domain and range problems."""

    def __init__(self, seed=None):
        """
        Initialize the generator.

        Args:
            seed: Random seed for reproducibility
        """
        if seed is not None:
            random.seed(seed)

    def _format_interval(self, start, end, start_inclusive=True, end_inclusive=True):
        """Format an interval in proper notation."""
        if start == float('-inf') and end == float('inf'):
            return "(-\\infty, \\infty)"

        start_bracket = "[" if start_inclusive else "("
        end_bracket = "]" if end_inclusive else ")"

        if start == float('-inf'):
            start_str = "-\\infty"
            start_bracket = "("
        else:
            start_str = str(start)

        if end == float('inf'):
            end_str = "\\infty"
            end_bracket = ")"
        else:
            end_str = str(end)

        return f"{start_bracket}{start_str}, {end_str}{end_bracket}"

    def _format_set_notation(self, values):
        """Format a set of values in set notation."""
        if isinstance(values, list):
            return "\\{" + ", ".join(str(v) for v in sorted(values)) + "\\}"
        return str(values)

    def generate_problem(self, difficulty: str) -> DomainRangeProblem:
        """
        Generate a single domain and range problem.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            DomainRangeProblem object
        """
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> DomainRangeProblem:
        """Generate easy problem (linear functions, simple quadratics)."""
        problem_type = random.choice(['linear', 'quadratic', 'constant'])

        if problem_type == 'linear':
            # Linear function f(x) = mx + b
            m = random.randint(1, 5) * random.choice([-1, 1])
            b = random.randint(-10, 10)

            if m > 0:
                function = f"f(x) = {m}x + {b}" if b >= 0 else f"f(x) = {m}x - {abs(b)}"
            else:
                function = f"f(x) = {m}x + {b}" if b >= 0 else f"f(x) = {m}x - {abs(b)}"

            if m == 1:
                function = f"f(x) = x + {b}" if b >= 0 else f"f(x) = x - {abs(b)}"
            elif m == -1:
                function = f"f(x) = -x + {b}" if b >= 0 else f"f(x) = -x - {abs(b)}"

            domain = "all real numbers"
            range = "all real numbers"
            domain_latex = "(-\\infty, \\infty)"
            range_latex = "(-\\infty, \\infty)"
            restrictions = []

            work_shown = [
                f"The function ${function}$ is a linear function",
                "Linear functions are defined for all real numbers",
                "Linear functions can output all real numbers",
                f"Domain: ${domain_latex}$",
                f"Range: ${range_latex}$"
            ]

        elif problem_type == 'quadratic':
            # Simple quadratic f(x) = x²
            function = "f(x) = x^2"
            domain = "all real numbers"
            range = "y ≥ 0"
            domain_latex = "(-\\infty, \\infty)"
            range_latex = "[0, \\infty)"
            restrictions = []

            work_shown = [
                f"The function ${function}$ is a quadratic function",
                "Quadratic functions are defined for all real numbers",
                "Since $x^2 \\geq 0$ for all real x, the range is $y \\geq 0$",
                f"Domain: ${domain_latex}$",
                f"Range: ${range_latex}$"
            ]

        else:  # constant
            # Constant function
            c = random.randint(-10, 10)
            function = f"f(x) = {c}"
            domain = "all real numbers"
            range = f"\\{{{c}\\}}"
            domain_latex = "(-\\infty, \\infty)"
            range_latex = f"\\{{{c}\\}}"
            restrictions = []

            work_shown = [
                f"The function ${function}$ is a constant function",
                "Constant functions are defined for all real numbers",
                f"The output is always {c}, regardless of input",
                f"Domain: ${domain_latex}$",
                f"Range: ${range_latex}$ (single value)"
            ]

        problem_latex = f"Find the domain and range of ${function}$"
        answer_latex = f"Domain: ${domain_latex}$, Range: ${range_latex}$"

        return DomainRangeProblem(
            problem_type='both',
            function=function,
            domain=domain,
            range=range,
            domain_latex=domain_latex,
            range_latex=range_latex,
            restrictions=restrictions,
            problem_latex=problem_latex,
            answer_latex=answer_latex,
            work_shown=work_shown,
            difficulty='easy'
        )

    def _generate_medium(self) -> DomainRangeProblem:
        """Generate medium problem (square roots, simple rational functions)."""
        problem_type = random.choice(['square_root', 'simple_rational', 'absolute_value'])

        if problem_type == 'square_root':
            # Square root function f(x) = √(x + a)
            a = random.randint(-5, 5)
            if a >= 0:
                function = f"f(x) = \\sqrt{{x + {a}}}"
            else:
                function = f"f(x) = \\sqrt{{x - {abs(a)}}}"

            domain_start = -a
            domain = f"x ≥ {domain_start}"
            range = "y ≥ 0"
            domain_latex = f"[{domain_start}, \\infty)"
            range_latex = "[0, \\infty)"
            restrictions = [f"x + {a} \\geq 0" if a >= 0 else f"x - {abs(a)} \\geq 0"]

            work_shown = [
                f"For ${function}$ to be defined, we need the expression under the square root to be non-negative",
                f"${restrictions[0]}$",
                f"$x \\geq {domain_start}$",
                "The square root function outputs non-negative values",
                f"Domain: ${domain_latex}$",
                f"Range: ${range_latex}$"
            ]

        elif problem_type == 'simple_rational':
            # Rational function f(x) = 1/(x - a)
            a = random.randint(-5, 5)
            if a >= 0:
                function = f"f(x) = \\frac{{1}}{{x - {a}}}" if a != 0 else "f(x) = \\frac{1}{x}"
            else:
                function = f"f(x) = \\frac{{1}}{{x + {abs(a)}}}"

            domain = f"all real numbers except x = {a}"
            range = "all real numbers except y = 0"
            domain_latex = f"(-\\infty, {a}) \\cup ({a}, \\infty)"
            range_latex = "(-\\infty, 0) \\cup (0, \\infty)"
            restrictions = [f"x \\neq {a}"]

            work_shown = [
                f"For ${function}$, the denominator cannot be zero",
                f"$x - {a} \\neq 0$" if a >= 0 else f"$x + {abs(a)} \\neq 0$",
                f"$x \\neq {a}$",
                "The function can never output 0 (asymptote at y = 0)",
                f"Domain: ${domain_latex}$",
                f"Range: ${range_latex}$"
            ]

        else:  # absolute_value
            # Absolute value function f(x) = |x - a| + b
            a = random.randint(-3, 3)
            b = random.randint(-5, 5)

            if a == 0 and b == 0:
                function = "f(x) = |x|"
            elif a == 0:
                function = f"f(x) = |x| + {b}" if b > 0 else f"f(x) = |x| - {abs(b)}"
            elif b == 0:
                function = f"f(x) = |x - {a}|" if a > 0 else f"f(x) = |x + {abs(a)}|"
            else:
                x_part = f"x - {a}" if a > 0 else f"x + {abs(a)}"
                b_part = f" + {b}" if b > 0 else f" - {abs(b)}"
                function = f"f(x) = |{x_part}|{b_part}"

            domain = "all real numbers"
            range = f"y ≥ {b}"
            domain_latex = "(-\\infty, \\infty)"
            range_latex = f"[{b}, \\infty)"
            restrictions = []

            work_shown = [
                f"The function ${function}$ is an absolute value function",
                "Absolute value functions are defined for all real numbers",
                f"The minimum value occurs at the vertex when $x = {a}$",
                f"Minimum value: $|0| + {b} = {b}$" if b != 0 else f"Minimum value: $|0| = 0$",
                f"Domain: ${domain_latex}$",
                f"Range: ${range_latex}$"
            ]

        problem_latex = f"Find the domain and range of ${function}$"
        answer_latex = f"Domain: ${domain_latex}$, Range: ${range_latex}$"

        return DomainRangeProblem(
            problem_type='both',
            function=function,
            domain=domain,
            range=range,
            domain_latex=domain_latex,
            range_latex=range_latex,
            restrictions=restrictions,
            problem_latex=problem_latex,
            answer_latex=answer_latex,
            work_shown=work_shown,
            difficulty='medium'
        )

    def _generate_hard(self) -> DomainRangeProblem:
        """Generate hard problem (complex rational, composite functions, from table/graph)."""
        problem_type = random.choice(['complex_rational', 'quadratic_transformed', 'from_table'])

        if problem_type == 'complex_rational':
            # Rational function f(x) = (ax + b)/(cx + d)
            a = random.randint(1, 3)
            b = random.randint(-5, 5)
            c = random.randint(1, 2)
            d = random.randint(-5, 5)

            # Ensure not a constant function
            while a * d == b * c:
                d = random.randint(-5, 5)

            numerator = f"{a}x + {b}" if b >= 0 else f"{a}x - {abs(b)}"
            denominator = f"{c}x + {d}" if d >= 0 else f"{c}x - {abs(d)}"
            if c == 1:
                denominator = f"x + {d}" if d >= 0 else f"x - {abs(d)}"

            function = f"f(x) = \\frac{{{numerator}}}{{{denominator}}}"

            # Domain: all real except where denominator = 0
            x_restricted = -d / c
            domain = f"all real numbers except x = {x_restricted:.2f}"
            domain_latex = f"(-\\infty, {x_restricted:.2f}) \\cup ({x_restricted:.2f}, \\infty)"

            # Range: all real except horizontal asymptote
            h_asymptote = a / c
            range = f"all real numbers except y = {h_asymptote:.2f}"
            range_latex = f"(-\\infty, {h_asymptote:.2f}) \\cup ({h_asymptote:.2f}, \\infty)"

            restrictions = [f"x \\neq {x_restricted:.2f}"]

            work_shown = [
                f"For ${function}$, find where denominator = 0:",
                f"${denominator} = 0$",
                f"$x = {x_restricted:.2f}$",
                f"Horizontal asymptote: $y = \\frac{{{a}}}{{{c}}} = {h_asymptote:.2f}$",
                f"Domain: ${domain_latex}$",
                f"Range: ${range_latex}$"
            ]

        elif problem_type == 'quadratic_transformed':
            # Transformed quadratic f(x) = a(x - h)² + k
            a = random.choice([-2, -1, 1, 2])
            h = random.randint(-3, 3)
            k = random.randint(-5, 5)

            x_part = f"(x - {h})" if h > 0 else f"(x + {abs(h)})" if h < 0 else "x"
            function = f"f(x) = {a}{x_part}^2 + {k}" if k >= 0 else f"f(x) = {a}{x_part}^2 - {abs(k)}"
            if a == 1:
                function = f"f(x) = {x_part}^2 + {k}" if k >= 0 else f"f(x) = {x_part}^2 - {abs(k)}"
            elif a == -1:
                function = f"f(x) = -{x_part}^2 + {k}" if k >= 0 else f"f(x) = -{x_part}^2 - {abs(k)}"

            domain = "all real numbers"
            domain_latex = "(-\\infty, \\infty)"

            if a > 0:
                range = f"y ≥ {k}"
                range_latex = f"[{k}, \\infty)"
            else:
                range = f"y ≤ {k}"
                range_latex = f"(-\\infty, {k}]"

            restrictions = []

            work_shown = [
                f"The function ${function}$ is a transformed quadratic",
                f"Vertex form with vertex at $({h}, {k})$",
                f"Opens {'upward' if a > 0 else 'downward'}",
                f"Domain: ${domain_latex}$ (all quadratics)",
                f"Range: ${range_latex}$ ({'minimum' if a > 0 else 'maximum'} at vertex)"
            ]

        else:  # from_table
            # Function from a table
            x_values = sorted(random.sample(range(-5, 6), 5))
            y_values = [random.randint(-8, 8) for _ in range(5)]

            # Make it a function (no repeated x-values)
            table_str = "\\begin{array}{|c|c|}\\hline x & f(x) \\\\ \\hline "
            for x, y in zip(x_values, y_values):
                table_str += f"{x} & {y} \\\\ "
            table_str += "\\hline \\end{array}"

            function = f"function given by table: {table_str}"
            domain = f"\\{{{', '.join(map(str, x_values))}\\}}"
            range_values = sorted(set(y_values))
            range = f"\\{{{', '.join(map(str, range_values))}\\}}"
            domain_latex = domain
            range_latex = range
            restrictions = [f"x ∈ {domain}"]

            work_shown = [
                "For a function defined by a table:",
                f"Domain = set of all x-values = ${domain_latex}$",
                f"Range = set of all y-values = ${range_latex}$",
                "Note: The range includes each unique y-value once"
            ]

        problem_latex = f"Find the domain and range of the {function}"
        answer_latex = f"Domain: ${domain_latex}$, Range: ${range_latex}$"

        return DomainRangeProblem(
            problem_type='both',
            function=function,
            domain=domain,
            range=range,
            domain_latex=domain_latex,
            range_latex=range_latex,
            restrictions=restrictions,
            problem_latex=problem_latex,
            answer_latex=answer_latex,
            work_shown=work_shown,
            difficulty='hard'
        )

    def _generate_challenge(self) -> DomainRangeProblem:
        """Generate challenge problem (piecewise, composite, logarithmic)."""
        problem_type = random.choice(['piecewise', 'composite_root', 'exponential'])

        if problem_type == 'piecewise':
            # Piecewise function
            # First piece: linear for x < a
            a = random.randint(-2, 2)
            m1 = random.randint(1, 3)
            b1 = random.randint(-3, 3)

            # Second piece: quadratic for x ≥ a
            c = random.randint(-2, 2)

            piece1 = f"{m1}x + {b1}" if b1 >= 0 else f"{m1}x - {abs(b1)}"
            piece2 = f"x^2 + {c}" if c >= 0 else f"x^2 - {abs(c)}"

            function = f"f(x) = \\begin{{cases}} {piece1} & \\text{{if }} x < {a} \\\\ {piece2} & \\text{{if }} x \\geq {a} \\end{{cases}}"

            # Calculate range
            y_at_boundary_left = m1 * a + b1  # Value from left piece at x = a
            y_at_boundary_right = a * a + c   # Value from right piece at x = a

            domain = "all real numbers"
            domain_latex = "(-\\infty, \\infty)"

            # Range depends on the pieces
            min_quadratic = c  # Minimum of x² + c is c (at x = 0 if a ≤ 0)
            if a <= 0:
                range_latex = f"[{min(c, y_at_boundary_left)}, \\infty)"
            else:
                range_latex = f"(-\\infty, \\infty)"

            range = "see work"
            restrictions = []

            work_shown = [
                f"The piecewise function has two parts:",
                f"For $x < {a}$: linear piece ${piece1}$ has range $(-\\infty, {y_at_boundary_left})$",
                f"For $x \\geq {a}$: quadratic piece ${piece2}$ has range $[{y_at_boundary_right}, \\infty)$",
                f"Domain: ${domain_latex}$ (union of both pieces)",
                f"Range: ${range_latex}$ (union of both ranges)"
            ]

        elif problem_type == 'composite_root':
            # Composite with square root: f(x) = √(4 - x²)
            function = "f(x) = \\sqrt{4 - x^2}"
            domain = "-2 ≤ x ≤ 2"
            domain_latex = "[-2, 2]"
            range = "0 ≤ y ≤ 2"
            range_latex = "[0, 2]"
            restrictions = ["4 - x^2 \\geq 0", "x^2 \\leq 4", "-2 \\leq x \\leq 2"]

            work_shown = [
                f"For ${function}$ to be defined:",
                "$4 - x^2 \\geq 0$",
                "$x^2 \\leq 4$",
                "$|x| \\leq 2$",
                "$-2 \\leq x \\leq 2$",
                "Maximum value when $x = 0$: $f(0) = \\sqrt{4} = 2$",
                "Minimum value at endpoints: $f(\\pm 2) = \\sqrt{0} = 0$",
                f"Domain: ${domain_latex}$",
                f"Range: ${range_latex}$"
            ]

        else:  # exponential
            # Exponential function f(x) = 2^x - a
            a = random.randint(1, 5)
            function = f"f(x) = 2^x - {a}"
            domain = "all real numbers"
            domain_latex = "(-\\infty, \\infty)"
            range = f"y > -{a}"
            range_latex = f"(-{a}, \\infty)"
            restrictions = []

            work_shown = [
                f"The function ${function}$ is an exponential function",
                "Exponential functions are defined for all real numbers",
                f"As $x \\to -\\infty$, $2^x \\to 0$, so $f(x) \\to -{a}$",
                f"As $x \\to \\infty$, $2^x \\to \\infty$, so $f(x) \\to \\infty$",
                f"Horizontal asymptote at $y = -{a}$",
                f"Domain: ${domain_latex}$",
                f"Range: ${range_latex}$"
            ]

        problem_latex = f"Find the domain and range of ${function}$"
        answer_latex = f"Domain: ${domain_latex}$, Range: ${range_latex}$"

        return DomainRangeProblem(
            problem_type='both',
            function=function,
            domain=domain,
            range=range,
            domain_latex=domain_latex,
            range_latex=range_latex,
            restrictions=restrictions,
            problem_latex=problem_latex,
            answer_latex=answer_latex,
            work_shown=work_shown,
            difficulty='challenge'
        )

    def generate_worksheet(self, difficulty: str, num_problems: int = 6) -> list:
        """
        Generate multiple domain and range problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of DomainRangeProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty)
            problems.append(problem)
        return problems