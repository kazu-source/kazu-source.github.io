"""
Graphing Systems of Equations Generator
Unit 5: Systems of Equations

Generates problems for finding solutions to systems of linear equations by graphing.
The solution is the intersection point where both equations are satisfied.
"""

import random
import sys
from pathlib import Path
from fractions import Fraction

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent))

from equation_generator import Equation


class GraphingSystemsOfEquationsGenerator:
    """Generates problems for graphing systems of linear equations."""

    def __init__(self, seed=None):
        """
        Initialize the generator.

        Args:
            seed: Random seed for reproducibility (optional)
        """
        if seed is not None:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int):
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of Equation objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str):
        """
        Generate a single problem.

        Args:
            difficulty: Problem difficulty level

        Returns:
            Equation object
        """
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _format_equation(self, m, b, var='y'):
        """
        Format equation in slope-intercept form with proper signs.

        Args:
            m: Slope
            b: Y-intercept
            var: Variable (default 'y')

        Returns:
            LaTeX string for the equation
        """
        if m == 0:
            return f"{var} = {b}"
        elif m == 1:
            if b == 0:
                return f"{var} = x"
            elif b > 0:
                return f"{var} = x + {b}"
            else:
                return f"{var} = x - {abs(b)}"
        elif m == -1:
            if b == 0:
                return f"{var} = -x"
            elif b > 0:
                return f"{var} = -x + {b}"
            else:
                return f"{var} = -x - {abs(b)}"
        else:
            # Handle fractions
            if isinstance(m, Fraction):
                if m.denominator == 1:
                    m_str = str(m.numerator)
                else:
                    m_str = f"\\frac{{{m.numerator}}}{{{m.denominator}}}"
            else:
                m_str = str(m)

            if b == 0:
                return f"{var} = {m_str}x"
            elif b > 0:
                return f"{var} = {m_str}x + {b}"
            else:
                return f"{var} = {m_str}x - {abs(b)}"

    def _format_standard_form(self, a, b, c):
        """
        Format equation in standard form Ax + By = C.

        Args:
            a, b, c: Coefficients

        Returns:
            LaTeX string for the equation
        """
        # Handle signs properly
        if a == 1:
            eq = "x"
        elif a == -1:
            eq = "-x"
        elif a == 0:
            eq = ""
        else:
            eq = f"{a}x"

        if b == 1:
            if eq:
                eq += " + y"
            else:
                eq = "y"
        elif b == -1:
            eq += " - y"
        elif b == 0:
            pass
        elif b > 0:
            if eq:
                eq += f" + {b}y"
            else:
                eq = f"{b}y"
        else:
            eq += f" - {abs(b)}y"

        return f"{eq} = {c}"

    def _generate_easy(self):
        """
        Generate an easy problem.
        Two lines in slope-intercept form with different slopes.
        Integer intersection point.
        """
        # Generate intersection point first to ensure integer solution
        x_sol = random.randint(-4, 4)
        y_sol = random.randint(-4, 4)

        # Generate first line that passes through (x_sol, y_sol)
        m1 = random.randint(-3, 3)
        while m1 == 0:
            m1 = random.randint(-3, 3)

        # Calculate b1 so line passes through (x_sol, y_sol)
        # y_sol = m1 * x_sol + b1
        b1 = y_sol - m1 * x_sol

        # Generate second line with different slope
        m2 = random.randint(-3, 3)
        while m2 == m1 or m2 == 0:
            m2 = random.randint(-3, 3)

        # Calculate b2 so line passes through (x_sol, y_sol)
        b2 = y_sol - m2 * x_sol

        # Format equations
        eq1 = self._format_equation(m1, b1)
        eq2 = self._format_equation(m2, b2)

        latex = f"\\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}"
        solution = f"({x_sol}, {y_sol})"

        # Create cleaner step formatting
        eq1_simple = f"{m1}x + {b1}" if b1 >= 0 else f"{m1}x - {abs(b1)}"
        eq2_simple = f"{m2}x + {b2}" if b2 >= 0 else f"{m2}x - {abs(b2)}"

        steps = [
            f"Set equations equal: {eq1_simple} = {eq2_simple}",
            f"Solve for x: ({m1} - {m2})x = {b2 - b1}",
            f"x = {x_sol}",
            f"Substitute to find y: y = {m1}({x_sol}) + {b1} = {y_sol}",
            f"Solution: {solution}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self):
        """
        Generate a medium problem.
        One or both equations need to be converted to slope-intercept form.
        May have fractional intersection point.
        """
        # Generate intersection point first
        x_sol = random.randint(-4, 4)
        y_sol = random.randint(-4, 4)

        # Generate first line in standard form that passes through (x_sol, y_sol)
        # Ax + By = C
        a1 = random.randint(1, 4)
        b1 = random.choice([1, 2, -1, -2])
        c1 = a1 * x_sol + b1 * y_sol

        # Generate second line in slope-intercept form
        m2 = random.randint(-3, 3)
        while m2 == 0:
            m2 = random.randint(-3, 3)

        # Calculate b2 so line passes through (x_sol, y_sol)
        # y_sol = m2 * x_sol + b2
        b2 = y_sol - m2 * x_sol

        # Format equations
        eq1 = self._format_standard_form(a1, b1, c1)
        eq2 = self._format_equation(m2, b2)

        latex = f"\\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}"
        solution = f"({x_sol}, {y_sol})"

        # Convert first equation to slope-intercept form for steps
        # By = -Ax + C
        # y = (-A/B)x + (C/B)
        m1 = Fraction(-a1, b1)
        b1_intercept = Fraction(c1, b1)

        steps = [
            f"Convert first equation to slope-intercept form",
            f"Solve {eq1} for y",
            f"{self._format_equation(m1, b1_intercept)}",
            f"Set equal to second equation and solve",
            f"Solution: {solution}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self):
        """
        Generate a hard problem.
        Systems with no solution (parallel lines) or infinite solutions (same line).
        """
        problem_type = random.choice(['no_solution', 'infinite_solutions'])

        if problem_type == 'no_solution':
            # Parallel lines: same slope, different y-intercepts
            m = random.randint(-3, 3)
            while m == 0:
                m = random.randint(-3, 3)

            b1 = random.randint(-5, 5)
            b2 = random.randint(-5, 5)
            while b2 == b1:
                b2 = random.randint(-5, 5)

            eq1 = self._format_equation(m, b1)
            eq2 = self._format_equation(m, b2)

            latex = f"\\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}"
            solution = "No solution (parallel lines)"

            steps = [
                f"Both equations have slope m = {m}",
                f"Different y-intercepts: {b1} and {b2}",
                "Lines are parallel and never intersect",
                "No solution"
            ]

        else:  # infinite_solutions
            # Same line represented differently
            m = random.randint(-3, 3)
            while m == 0:
                m = random.randint(-3, 3)

            b = random.randint(-5, 5)

            # First equation in slope-intercept form
            eq1 = self._format_equation(m, b)

            # Second equation: multiply by a constant and rearrange to standard form
            multiplier = random.choice([2, 3, -1, -2])
            # y = mx + b becomes:
            # multiplier*y = multiplier*m*x + multiplier*b
            # -multiplier*m*x + multiplier*y = multiplier*b
            a2 = -multiplier * m
            b2 = multiplier
            c2 = multiplier * b

            eq2 = self._format_standard_form(a2, b2, c2)

            latex = f"\\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}"
            solution = "Infinite solutions (same line)"

            steps = [
                f"Convert second equation to slope-intercept form",
                f"Both equations simplify to: {eq1}",
                "Equations represent the same line",
                "Infinite solutions"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self):
        """
        Generate a challenge problem.
        Word problems requiring interpretation of the intersection point.
        """
        # Choose a context
        contexts = [
            {
                'name': 'rental',
                'var1': 'Company A',
                'var2': 'Company B',
                'y_label': 'total cost',
                'x_label': 'hours rented',
                'interpretation': 'At this number of hours, both companies cost the same'
            },
            {
                'name': 'phone',
                'var1': 'Plan A',
                'var2': 'Plan B',
                'y_label': 'total cost',
                'x_label': 'minutes used',
                'interpretation': 'At this many minutes, both plans cost the same'
            },
            {
                'name': 'subscription',
                'var1': 'Service A',
                'var2': 'Service B',
                'y_label': 'total cost',
                'x_label': 'months',
                'interpretation': 'After this many months, both services cost the same'
            }
        ]

        context = random.choice(contexts)

        # Generate realistic values
        # Company A: higher initial cost, lower rate
        initial_a = random.randint(20, 50)
        rate_a = random.randint(2, 8)

        # Company B: lower initial cost, higher rate
        initial_b = random.randint(5, initial_a - 10)
        rate_b = random.randint(rate_a + 2, rate_a + 8)

        # Calculate intersection
        # initial_a + rate_a * x = initial_b + rate_b * x
        # (rate_a - rate_b) * x = initial_b - initial_a
        x_solution = (initial_b - initial_a) / (rate_a - rate_b)
        y_solution = initial_a + rate_a * x_solution

        # Format equations
        eq1 = self._format_equation(rate_a, initial_a, 'y')
        eq2 = self._format_equation(rate_b, initial_b, 'y')

        # Create word problem
        if context['name'] == 'rental':
            problem_text = (
                f"\\text{{{context['var1']} charges \\${initial_a} plus \\${rate_a} per hour.}} \\\\ "
                f"\\text{{{context['var2']} charges \\${initial_b} plus \\${rate_b} per hour.}} \\\\ "
                f"\\text{{Find when both companies charge the same amount.}}"
            )
        elif context['name'] == 'phone':
            problem_text = (
                f"\\text{{{context['var1']}: \\${initial_a} base fee plus \\${rate_a} per minute.}} \\\\ "
                f"\\text{{{context['var2']}: \\${initial_b} base fee plus \\${rate_b} per minute.}} \\\\ "
                f"\\text{{At how many minutes do both plans cost the same?}}"
            )
        else:  # subscription
            problem_text = (
                f"\\text{{{context['var1']}: \\${initial_a} sign-up plus \\${rate_a}/month.}} \\\\ "
                f"\\text{{{context['var2']}: \\${initial_b} sign-up plus \\${rate_b}/month.}} \\\\ "
                f"\\text{{After how many months do both services cost the same?}}"
            )

        latex = f"{problem_text} \\\\ \\text{{System: }} \\begin{{cases}} {eq1} \\\\ {eq2} \\end{{cases}}"

        # Format solution with interpretation
        if x_solution == int(x_solution) and y_solution == int(y_solution):
            solution = (
                f"({int(x_solution)}, {int(y_solution)}): "
                f"{context['interpretation']} (${int(y_solution)})"
            )
        else:
            solution = (
                f"({x_solution:.1f}, {y_solution:.2f}): "
                f"{context['interpretation']} (${y_solution:.2f})"
            )

        steps = [
            f"Set up equations: y = cost, x = {context['x_label']}",
            f"{context['var1']}: {eq1}",
            f"{context['var2']}: {eq2}",
            f"Solve: {rate_a}x + {initial_a} = {rate_b}x + {initial_b}",
            f"x = {x_solution:.1f} {context['x_label']}",
            f"y = ${y_solution:.2f}",
            f"Interpretation: {context['interpretation']}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


# Example usage and testing
if __name__ == "__main__":
    generator = GraphingSystemsOfEquationsGenerator(seed=42)

    print("Graphing Systems of Equations Generator Test\n")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Examples:")
        print("-" * 60)
        for i in range(2):
            eq = generator._generate_problem(difficulty)
            print(f"\nProblem {i+1}:")
            print(f"  {eq.latex}")
            print(f"  Solution: {eq.solution}")
            print(f"  Steps:")
            for step in eq.steps:
                print(f"    - {step}")
        print()
