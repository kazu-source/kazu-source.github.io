"""
Generator for systems of equations using substitution method worksheets.
Chapter 5: Systems of Equations - Using Substitution
"""

import random
import sys
from pathlib import Path
from dataclasses import dataclass
from fractions import Fraction

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


@dataclass
class SubstitutionSystemProblem:
    """Represents a system of equations to be solved using substitution."""
    equation1: str  # First equation in LaTeX
    equation2: str  # Second equation in LaTeX
    solution_x: float  # x-coordinate of solution
    solution_y: float  # y-coordinate of solution
    solution_latex: str  # Solution in LaTeX format
    work_shown: list  # Step-by-step solution
    difficulty: str  # easy, medium, hard, challenge
    problem_latex: str  # Problem statement in LaTeX
    answer_latex: str  # Answer in LaTeX
    system_type: str  # Type of system (consistent, inconsistent, dependent)


class SystemsSubstitutionGenerator:
    """Generator for systems of equations using substitution method."""

    def __init__(self, seed=None):
        """
        Initialize the generator.

        Args:
            seed: Random seed for reproducibility
        """
        if seed is not None:
            random.seed(seed)

    def _format_equation(self, a, b, c, form="standard"):
        """
        Format a linear equation ax + by = c.

        Args:
            a, b, c: Coefficients
            form: "standard" for ax + by = c, "solved_y" for y = mx + b, "solved_x" for x = ...

        Returns:
            LaTeX string for the equation
        """
        if form == "solved_y":
            # Convert to y = mx + b form
            if b == 0:
                return None  # Can't solve for y
            slope = Fraction(-a, b).limit_denominator()
            y_int = Fraction(c, b).limit_denominator()

            slope_str = self._format_fraction(slope)
            y_int_str = self._format_fraction(y_int)

            if slope == 0:
                return f"y = {y_int_str}"
            elif y_int == 0:
                return f"y = {slope_str}x"
            elif y_int > 0:
                return f"y = {slope_str}x + {y_int_str}"
            else:
                return f"y = {slope_str}x - {self._format_fraction(abs(y_int))}"

        elif form == "solved_x":
            # Convert to x = ... form
            if a == 0:
                return None  # Can't solve for x
            x_val = Fraction(c - b * 0, a).limit_denominator()  # Simplified form
            return f"x = \\frac{{{c} - {b}y}}{{{a}}}"

        else:  # standard form
            eq = ""
            if a == 1:
                eq += "x"
            elif a == -1:
                eq += "-x"
            elif a != 0:
                eq += f"{a}x"

            if b > 0:
                if a != 0:
                    eq += " + "
                if b == 1:
                    eq += "y"
                else:
                    eq += f"{b}y"
            elif b < 0:
                if a != 0:
                    eq += " - "
                else:
                    eq += "-"
                if b == -1:
                    eq += "y"
                else:
                    eq += f"{abs(b)}y"

            eq += f" = {c}"
            return eq

    def _format_fraction(self, frac):
        """Format a fraction for display."""
        if isinstance(frac, Fraction):
            if frac.denominator == 1:
                return str(frac.numerator)
            else:
                return f"\\frac{{{frac.numerator}}}{{{frac.denominator}}}"
        else:
            return str(frac)

    def generate_problem(self, difficulty: str) -> SubstitutionSystemProblem:
        """
        Generate a single substitution system problem.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            SubstitutionSystemProblem object
        """
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> SubstitutionSystemProblem:
        """Generate easy problem (one equation already solved for a variable)."""
        # Choose solution
        x_sol = random.randint(-5, 5)
        y_sol = random.randint(-5, 5)

        # First equation: y = mx + b form (already solved for y)
        m = random.randint(1, 3) * random.choice([-1, 1])
        b = y_sol - m * x_sol  # Ensure it passes through solution

        eq1 = f"y = {m}x + {b}" if b >= 0 else f"y = {m}x - {abs(b)}"
        if b == 0:
            eq1 = f"y = {m}x"
        if m == 1:
            eq1 = eq1.replace("1x", "x")
        if m == -1:
            eq1 = eq1.replace("-1x", "-x")

        # Second equation: ax + by = c (standard form)
        a2 = random.randint(1, 3)
        b2 = random.randint(1, 3)
        c2 = a2 * x_sol + b2 * y_sol

        eq2 = self._format_equation(a2, b2, c2, "standard")

        work_shown = [
            f"Equation 1: ${eq1}$ (already solved for y)",
            f"Equation 2: ${eq2}$",
            f"Substitute ${eq1}$ into Equation 2:",
            f"${a2}x + {b2}({m}x + {b}) = {c2}$",
            f"${a2}x + {b2 * m}x + {b2 * b} = {c2}$",
            f"${a2 + b2 * m}x = {c2 - b2 * b}$",
            f"$x = {x_sol}$",
            f"Substitute back: $y = {m}({x_sol}) + {b} = {y_sol}$",
            f"Solution: $({x_sol}, {y_sol})$"
        ]

        problem_latex = f"Solve the system using substitution:\\\\${eq1}$\\\\${eq2}$"
        answer_latex = f"$({x_sol}, {y_sol})$"

        return SubstitutionSystemProblem(
            equation1=eq1,
            equation2=eq2,
            solution_x=x_sol,
            solution_y=y_sol,
            solution_latex=f"({x_sol}, {y_sol})",
            work_shown=work_shown,
            difficulty='easy',
            problem_latex=problem_latex,
            answer_latex=answer_latex,
            system_type="consistent"
        )

    def _generate_medium(self) -> SubstitutionSystemProblem:
        """Generate medium problem (need to solve for a variable first)."""
        # Choose solution
        x_sol = random.randint(-6, 6)
        y_sol = random.randint(-6, 6)

        # First equation: ax + y = c (easy to solve for y)
        a1 = random.randint(1, 4) * random.choice([-1, 1])
        c1 = a1 * x_sol + y_sol

        eq1 = self._format_equation(a1, 1, c1, "standard")

        # Second equation: dx + ey = f
        d = random.randint(2, 5)
        e = random.randint(2, 5) * random.choice([-1, 1])
        f = d * x_sol + e * y_sol

        eq2 = self._format_equation(d, e, f, "standard")

        # Show work
        solved_eq1 = f"y = {c1} - {a1}x" if a1 > 0 else f"y = {c1} + {abs(a1)}x"
        if a1 == 1:
            solved_eq1 = f"y = {c1} - x"
        elif a1 == -1:
            solved_eq1 = f"y = {c1} + x"

        work_shown = [
            f"Equation 1: ${eq1}$",
            f"Equation 2: ${eq2}$",
            f"Solve Equation 1 for y:",
            f"${solved_eq1}$",
            f"Substitute into Equation 2:",
            f"${d}x + {e}({solved_eq1.split(' = ')[1]}) = {f}$",
            f"Simplify and solve for x:",
            f"$x = {x_sol}$",
            f"Substitute back: $y = {y_sol}$",
            f"Solution: $({x_sol}, {y_sol})$"
        ]

        problem_latex = f"Solve the system using substitution:\\\\${eq1}$\\\\${eq2}$"
        answer_latex = f"$({x_sol}, {y_sol})$"

        return SubstitutionSystemProblem(
            equation1=eq1,
            equation2=eq2,
            solution_x=x_sol,
            solution_y=y_sol,
            solution_latex=f"({x_sol}, {y_sol})",
            work_shown=work_shown,
            difficulty='medium',
            problem_latex=problem_latex,
            answer_latex=answer_latex,
            system_type="consistent"
        )

    def _generate_hard(self) -> SubstitutionSystemProblem:
        """Generate hard problem (fractional coefficients, more complex solving)."""
        # Choose solution with possible fractions
        x_sol = Fraction(random.randint(-8, 8), random.randint(1, 2)).limit_denominator()
        y_sol = Fraction(random.randint(-8, 8), random.randint(1, 2)).limit_denominator()

        # First equation with fractions
        a1 = random.randint(2, 6)
        b1 = random.randint(2, 6) * random.choice([-1, 1])
        c1 = a1 * x_sol + b1 * y_sol

        eq1 = self._format_equation(a1, b1, float(c1), "standard")

        # Second equation
        a2 = random.randint(3, 7) * random.choice([-1, 1])
        b2 = random.randint(3, 7)
        c2 = a2 * x_sol + b2 * y_sol

        eq2 = self._format_equation(a2, b2, float(c2), "standard")

        x_str = self._format_fraction(x_sol)
        y_str = self._format_fraction(y_sol)

        work_shown = [
            f"Equation 1: ${eq1}$",
            f"Equation 2: ${eq2}$",
            f"Solve Equation 1 for x:",
            f"$x = \\frac{{{c1} - {b1}y}}{{{a1}}}$",
            f"Substitute into Equation 2:",
            f"Simplify and solve for y:",
            f"$y = {y_str}$",
            f"Substitute back to find x:",
            f"$x = {x_str}$",
            f"Solution: $({x_str}, {y_str})$"
        ]

        problem_latex = f"Solve the system using substitution:\\\\${eq1}$\\\\${eq2}$"
        answer_latex = f"$({x_str}, {y_str})$"

        return SubstitutionSystemProblem(
            equation1=eq1,
            equation2=eq2,
            solution_x=float(x_sol),
            solution_y=float(y_sol),
            solution_latex=f"({x_str}, {y_str})",
            work_shown=work_shown,
            difficulty='hard',
            problem_latex=problem_latex,
            answer_latex=answer_latex,
            system_type="consistent"
        )

    def _generate_challenge(self) -> SubstitutionSystemProblem:
        """Generate challenge problem (no solution, infinite solutions, or complex fractions)."""
        problem_type = random.choice(['no_solution', 'infinite', 'complex'])

        if problem_type == 'no_solution':
            # Parallel lines (no solution)
            m = random.randint(2, 4)
            b1 = random.randint(-5, 5)
            b2 = b1 + random.randint(1, 5) * random.choice([-1, 1])

            eq1 = f"y = {m}x + {b1}" if b1 >= 0 else f"y = {m}x - {abs(b1)}"
            eq2 = f"y = {m}x + {b2}" if b2 >= 0 else f"y = {m}x - {abs(b2)}"

            work_shown = [
                f"Equation 1: ${eq1}$",
                f"Equation 2: ${eq2}$",
                f"Both equations have the same slope ({m}) but different y-intercepts",
                f"These are parallel lines",
                f"The system has no solution"
            ]

            problem_latex = f"Solve the system using substitution:\\\\${eq1}$\\\\${eq2}$"
            answer_latex = "No solution (parallel lines)"

            return SubstitutionSystemProblem(
                equation1=eq1,
                equation2=eq2,
                solution_x=None,
                solution_y=None,
                solution_latex="No solution",
                work_shown=work_shown,
                difficulty='challenge',
                problem_latex=problem_latex,
                answer_latex=answer_latex,
                system_type="inconsistent"
            )

        elif problem_type == 'infinite':
            # Same line (infinite solutions)
            a = random.randint(2, 5)
            b = random.randint(2, 5) * random.choice([-1, 1])
            c = random.randint(5, 15)

            eq1 = self._format_equation(a, b, c, "standard")
            # Second equation is a multiple of the first
            mult = random.randint(2, 3)
            eq2 = self._format_equation(a * mult, b * mult, c * mult, "standard")

            work_shown = [
                f"Equation 1: ${eq1}$",
                f"Equation 2: ${eq2}$",
                f"Notice that Equation 2 is {mult} times Equation 1",
                f"These equations represent the same line",
                f"The system has infinitely many solutions"
            ]

            problem_latex = f"Solve the system using substitution:\\\\${eq1}$\\\\${eq2}$"
            answer_latex = "Infinitely many solutions (same line)"

            return SubstitutionSystemProblem(
                equation1=eq1,
                equation2=eq2,
                solution_x=None,
                solution_y=None,
                solution_latex="Infinitely many solutions",
                work_shown=work_shown,
                difficulty='challenge',
                problem_latex=problem_latex,
                answer_latex=answer_latex,
                system_type="dependent"
            )

        else:  # complex fractions
            # Solution with complex fractions
            x_sol = Fraction(random.randint(-10, 10), random.randint(3, 5)).limit_denominator()
            y_sol = Fraction(random.randint(-10, 10), random.randint(3, 5)).limit_denominator()

            # Equations with larger coefficients
            a1 = random.randint(5, 9)
            b1 = random.randint(5, 9) * random.choice([-1, 1])
            c1 = a1 * x_sol + b1 * y_sol

            a2 = random.randint(4, 8) * random.choice([-1, 1])
            b2 = random.randint(4, 8)
            c2 = a2 * x_sol + b2 * y_sol

            eq1 = self._format_equation(a1, b1, float(c1), "standard")
            eq2 = self._format_equation(a2, b2, float(c2), "standard")

            x_str = self._format_fraction(x_sol)
            y_str = self._format_fraction(y_sol)

            work_shown = [
                f"Equation 1: ${eq1}$",
                f"Equation 2: ${eq2}$",
                f"This system requires careful algebraic manipulation",
                f"After substitution and simplification:",
                f"$x = {x_str}$",
                f"$y = {y_str}$",
                f"Solution: $({x_str}, {y_str})$"
            ]

            problem_latex = f"Solve the system using substitution:\\\\${eq1}$\\\\${eq2}$"
            answer_latex = f"$({x_str}, {y_str})$"

            return SubstitutionSystemProblem(
                equation1=eq1,
                equation2=eq2,
                solution_x=float(x_sol),
                solution_y=float(y_sol),
                solution_latex=f"({x_str}, {y_str})",
                work_shown=work_shown,
                difficulty='challenge',
                problem_latex=problem_latex,
                answer_latex=answer_latex,
                system_type="consistent"
            )

    def generate_worksheet(self, difficulty: str, num_problems: int = 6) -> list:
        """
        Generate multiple substitution system problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of SubstitutionSystemProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty)
            problems.append(problem)
        return problems