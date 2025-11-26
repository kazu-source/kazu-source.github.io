"""
Generator for systems of equations using elimination method worksheets.
Chapter 5: Systems of Equations - Using Elimination
"""

import random
import sys
from pathlib import Path
from dataclasses import dataclass
from fractions import Fraction

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


@dataclass
class EliminationSystemProblem:
    """Represents a system of equations to be solved using elimination."""
    equation1: str  # First equation in LaTeX
    equation2: str  # Second equation in LaTeX
    solution_x: float  # x-coordinate of solution
    solution_y: float  # y-coordinate of solution
    solution_latex: str  # Solution in LaTeX format
    elimination_variable: str  # Which variable to eliminate (x or y)
    multipliers: tuple  # Multipliers used for elimination
    work_shown: list  # Step-by-step solution
    difficulty: str  # easy, medium, hard, challenge
    problem_latex: str  # Problem statement in LaTeX
    answer_latex: str  # Answer in LaTeX
    system_type: str  # Type of system (consistent, inconsistent, dependent)


class SystemsEliminationGenerator:
    """Generator for systems of equations using elimination method."""

    def __init__(self, seed=None):
        """
        Initialize the generator.

        Args:
            seed: Random seed for reproducibility
        """
        if seed is not None:
            random.seed(seed)

    def _gcd(self, a, b):
        """Calculate greatest common divisor."""
        while b:
            a, b = b, a % b
        return abs(a)

    def _lcm(self, a, b):
        """Calculate least common multiple."""
        return abs(a * b) // self._gcd(a, b)

    def _format_equation(self, a, b, c):
        """
        Format a linear equation ax + by = c.

        Args:
            a, b, c: Coefficients

        Returns:
            LaTeX string for the equation
        """
        eq = ""

        # Handle x term
        if a == 1:
            eq += "x"
        elif a == -1:
            eq += "-x"
        elif a != 0:
            eq += f"{a}x"

        # Handle y term
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
                if a == 0:
                    eq += "y"
                else:
                    eq += "y"
            else:
                eq += f"{abs(b)}y"

        eq += f" = {c}"
        return eq

    def _format_fraction(self, value):
        """Format a number as a fraction if needed."""
        if isinstance(value, (int, float)):
            if isinstance(value, float) and not value.is_integer():
                frac = Fraction(value).limit_denominator()
                if frac.denominator != 1:
                    return f"\\frac{{{frac.numerator}}}{{{frac.denominator}}}"
                else:
                    return str(frac.numerator)
            else:
                return str(int(value))
        elif isinstance(value, Fraction):
            if value.denominator != 1:
                return f"\\frac{{{value.numerator}}}{{{value.denominator}}}"
            else:
                return str(value.numerator)
        return str(value)

    def generate_problem(self, difficulty: str) -> EliminationSystemProblem:
        """
        Generate a single elimination system problem.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            EliminationSystemProblem object
        """
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> EliminationSystemProblem:
        """Generate easy problem (coefficients already match for elimination)."""
        # Choose solution
        x_sol = random.randint(-5, 5)
        y_sol = random.randint(-5, 5)

        # Create equations where one variable has same coefficient
        eliminate_var = random.choice(['x', 'y'])

        if eliminate_var == 'x':
            # Same x coefficient
            a = random.randint(1, 3)
            b1 = random.randint(1, 4) * random.choice([-1, 1])
            b2 = random.randint(1, 4) * random.choice([-1, 1])
            while b2 == b1:  # Ensure different y coefficients
                b2 = random.randint(1, 4) * random.choice([-1, 1])

            c1 = a * x_sol + b1 * y_sol
            c2 = a * x_sol + b2 * y_sol

            eq1 = self._format_equation(a, b1, c1)
            eq2 = self._format_equation(a, b2, c2)

            multipliers = (1, -1)

            work_shown = [
                f"Equation 1: ${eq1}$",
                f"Equation 2: ${eq2}$",
                f"The x-coefficients are the same ({a})",
                f"Subtract Equation 2 from Equation 1:",
                f"$({a}x + {b1}y) - ({a}x + {b2}y) = {c1} - {c2}$",
                f"${b1 - b2}y = {c1 - c2}$",
                f"$y = {y_sol}$",
                f"Substitute $y = {y_sol}$ into Equation 1:",
                f"${a}x + {b1}({y_sol}) = {c1}$",
                f"${a}x = {c1 - b1 * y_sol}$",
                f"$x = {x_sol}$"
            ]
        else:  # eliminate y
            # Same y coefficient
            a1 = random.randint(1, 4) * random.choice([-1, 1])
            a2 = random.randint(1, 4) * random.choice([-1, 1])
            while a2 == a1:
                a2 = random.randint(1, 4) * random.choice([-1, 1])
            b = random.randint(1, 3)

            c1 = a1 * x_sol + b * y_sol
            c2 = a2 * x_sol + b * y_sol

            eq1 = self._format_equation(a1, b, c1)
            eq2 = self._format_equation(a2, b, c2)

            multipliers = (1, -1)

            work_shown = [
                f"Equation 1: ${eq1}$",
                f"Equation 2: ${eq2}$",
                f"The y-coefficients are the same ({b})",
                f"Subtract Equation 2 from Equation 1:",
                f"$({a1}x + {b}y) - ({a2}x + {b}y) = {c1} - {c2}$",
                f"${a1 - a2}x = {c1 - c2}$",
                f"$x = {x_sol}$",
                f"Substitute $x = {x_sol}$ into Equation 1:",
                f"${a1}({x_sol}) + {b}y = {c1}$",
                f"${b}y = {c1 - a1 * x_sol}$",
                f"$y = {y_sol}$"
            ]

        problem_latex = f"Solve the system using elimination:\\\\${eq1}$\\\\${eq2}$"
        answer_latex = f"$({x_sol}, {y_sol})$"

        return EliminationSystemProblem(
            equation1=eq1,
            equation2=eq2,
            solution_x=x_sol,
            solution_y=y_sol,
            solution_latex=f"({x_sol}, {y_sol})",
            elimination_variable=eliminate_var,
            multipliers=multipliers,
            work_shown=work_shown,
            difficulty='easy',
            problem_latex=problem_latex,
            answer_latex=answer_latex,
            system_type="consistent"
        )

    def _generate_medium(self) -> EliminationSystemProblem:
        """Generate medium problem (need to multiply one equation)."""
        # Choose solution
        x_sol = random.randint(-6, 6)
        y_sol = random.randint(-6, 6)

        eliminate_var = random.choice(['x', 'y'])

        if eliminate_var == 'x':
            # Different x coefficients, one is multiple of other
            a1 = random.randint(1, 3)
            mult = random.randint(2, 3)
            a2 = a1 * mult

            b1 = random.randint(1, 5) * random.choice([-1, 1])
            b2 = random.randint(1, 5) * random.choice([-1, 1])

            c1 = a1 * x_sol + b1 * y_sol
            c2 = a2 * x_sol + b2 * y_sol

            eq1 = self._format_equation(a1, b1, c1)
            eq2 = self._format_equation(a2, b2, c2)

            multipliers = (mult, 1)

            work_shown = [
                f"Equation 1: ${eq1}$",
                f"Equation 2: ${eq2}$",
                f"To eliminate x, multiply Equation 1 by {mult}:",
                f"${mult}({eq1}) = {self._format_equation(a1*mult, b1*mult, c1*mult)}$",
                f"Now subtract Equation 2:",
                f"${b1*mult - b2}y = {c1*mult - c2}$",
                f"$y = {y_sol}$",
                f"Substitute back to find $x = {x_sol}$"
            ]
        else:  # eliminate y
            a1 = random.randint(1, 5) * random.choice([-1, 1])
            a2 = random.randint(1, 5) * random.choice([-1, 1])

            b1 = random.randint(1, 3)
            mult = random.randint(2, 3)
            b2 = b1 * mult

            c1 = a1 * x_sol + b1 * y_sol
            c2 = a2 * x_sol + b2 * y_sol

            eq1 = self._format_equation(a1, b1, c1)
            eq2 = self._format_equation(a2, b2, c2)

            multipliers = (mult, 1)

            work_shown = [
                f"Equation 1: ${eq1}$",
                f"Equation 2: ${eq2}$",
                f"To eliminate y, multiply Equation 1 by {mult}:",
                f"${mult}({eq1}) = {self._format_equation(a1*mult, b1*mult, c1*mult)}$",
                f"Now subtract Equation 2:",
                f"${a1*mult - a2}x = {c1*mult - c2}$",
                f"$x = {x_sol}$",
                f"Substitute back to find $y = {y_sol}$"
            ]

        problem_latex = f"Solve the system using elimination:\\\\${eq1}$\\\\${eq2}$"
        answer_latex = f"$({x_sol}, {y_sol})$"

        return EliminationSystemProblem(
            equation1=eq1,
            equation2=eq2,
            solution_x=x_sol,
            solution_y=y_sol,
            solution_latex=f"({x_sol}, {y_sol})",
            elimination_variable=eliminate_var,
            multipliers=multipliers,
            work_shown=work_shown,
            difficulty='medium',
            problem_latex=problem_latex,
            answer_latex=answer_latex,
            system_type="consistent"
        )

    def _generate_hard(self) -> EliminationSystemProblem:
        """Generate hard problem (need to multiply both equations)."""
        # Choose solution (may be fractional)
        x_sol = Fraction(random.randint(-8, 8), random.randint(1, 2)).limit_denominator()
        y_sol = Fraction(random.randint(-8, 8), random.randint(1, 2)).limit_denominator()

        # Generate coefficients that require multiplying both equations
        a1 = random.randint(2, 5) * random.choice([-1, 1])
        a2 = random.randint(3, 6) * random.choice([-1, 1])
        while self._gcd(abs(a1), abs(a2)) > 1:  # Ensure they need LCM
            a2 = random.randint(3, 6) * random.choice([-1, 1])

        b1 = random.randint(2, 5) * random.choice([-1, 1])
        b2 = random.randint(3, 6) * random.choice([-1, 1])

        c1 = a1 * x_sol + b1 * y_sol
        c2 = a2 * x_sol + b2 * y_sol

        eq1 = self._format_equation(a1, b1, float(c1))
        eq2 = self._format_equation(a2, b2, float(c2))

        # Find LCM for elimination
        lcm_a = self._lcm(abs(a1), abs(a2))
        mult1 = lcm_a // abs(a1)
        mult2 = lcm_a // abs(a2)

        # Adjust signs for elimination
        if (a1 * mult1) * (a2 * mult2) > 0:
            mult2 = -mult2

        multipliers = (mult1, mult2)

        x_str = self._format_fraction(x_sol)
        y_str = self._format_fraction(y_sol)

        work_shown = [
            f"Equation 1: ${eq1}$",
            f"Equation 2: ${eq2}$",
            f"To eliminate x, find LCM of {abs(a1)} and {abs(a2)} = {lcm_a}",
            f"Multiply Equation 1 by {abs(mult1)}: ${self._format_equation(a1*abs(mult1), b1*abs(mult1), float(c1*abs(mult1)))}$",
            f"Multiply Equation 2 by {abs(mult2)}: ${self._format_equation(a2*abs(mult2), b2*abs(mult2), float(c2*abs(mult2)))}$",
            f"{'Add' if mult2 < 0 else 'Subtract'} the equations to eliminate x",
            f"Solve for y: $y = {y_str}$",
            f"Substitute back to find x: $x = {x_str}$"
        ]

        problem_latex = f"Solve the system using elimination:\\\\${eq1}$\\\\${eq2}$"
        answer_latex = f"$({x_str}, {y_str})$"

        return EliminationSystemProblem(
            equation1=eq1,
            equation2=eq2,
            solution_x=float(x_sol),
            solution_y=float(y_sol),
            solution_latex=f"({x_str}, {y_str})",
            elimination_variable='x',
            multipliers=multipliers,
            work_shown=work_shown,
            difficulty='hard',
            problem_latex=problem_latex,
            answer_latex=answer_latex,
            system_type="consistent"
        )

    def _generate_challenge(self) -> EliminationSystemProblem:
        """Generate challenge problem (no solution, infinite solutions, or complex)."""
        problem_type = random.choice(['no_solution', 'infinite', 'complex_fractions'])

        if problem_type == 'no_solution':
            # Parallel lines
            a1 = random.randint(2, 4)
            b1 = random.randint(2, 4) * random.choice([-1, 1])
            c1 = random.randint(5, 15)

            # Second equation is multiple of first with different constant
            mult = random.randint(2, 3)
            a2 = a1 * mult
            b2 = b1 * mult
            c2 = c1 * mult + random.randint(1, 5) * random.choice([-1, 1])

            eq1 = self._format_equation(a1, b1, c1)
            eq2 = self._format_equation(a2, b2, c2)

            work_shown = [
                f"Equation 1: ${eq1}$",
                f"Equation 2: ${eq2}$",
                f"Multiply Equation 1 by {mult}: ${self._format_equation(a2, b2, c1*mult)}$",
                f"Compare with Equation 2: ${eq2}$",
                f"The left sides are identical but {c1*mult} ≠ {c2}",
                f"This is a contradiction - the lines are parallel",
                f"The system has no solution"
            ]

            problem_latex = f"Solve the system using elimination:\\\\${eq1}$\\\\${eq2}$"
            answer_latex = "No solution (parallel lines)"

            return EliminationSystemProblem(
                equation1=eq1,
                equation2=eq2,
                solution_x=None,
                solution_y=None,
                solution_latex="No solution",
                elimination_variable='both',
                multipliers=(mult, 1),
                work_shown=work_shown,
                difficulty='challenge',
                problem_latex=problem_latex,
                answer_latex=answer_latex,
                system_type="inconsistent"
            )

        elif problem_type == 'infinite':
            # Same line (infinite solutions)
            a = random.randint(3, 6)
            b = random.randint(3, 6) * random.choice([-1, 1])
            c = random.randint(10, 20)

            eq1 = self._format_equation(a, b, c)

            # Second equation is exact multiple
            mult = random.randint(2, 3)
            eq2 = self._format_equation(a*mult, b*mult, c*mult)

            work_shown = [
                f"Equation 1: ${eq1}$",
                f"Equation 2: ${eq2}$",
                f"Notice that Equation 2 = {mult} × Equation 1",
                f"When we eliminate any variable, we get 0 = 0",
                f"The equations represent the same line",
                f"The system has infinitely many solutions"
            ]

            problem_latex = f"Solve the system using elimination:\\\\${eq1}$\\\\${eq2}$"
            answer_latex = "Infinitely many solutions (same line)"

            return EliminationSystemProblem(
                equation1=eq1,
                equation2=eq2,
                solution_x=None,
                solution_y=None,
                solution_latex="Infinitely many solutions",
                elimination_variable='both',
                multipliers=(1, -1/mult),
                work_shown=work_shown,
                difficulty='challenge',
                problem_latex=problem_latex,
                answer_latex=answer_latex,
                system_type="dependent"
            )

        else:  # complex_fractions
            # Complex system with fractional solution
            x_sol = Fraction(random.randint(-10, 10), random.randint(3, 6)).limit_denominator()
            y_sol = Fraction(random.randint(-10, 10), random.randint(3, 6)).limit_denominator()

            # Large prime coefficients
            primes = [3, 5, 7, 11]
            a1 = random.choice(primes) * random.choice([-1, 1])
            a2 = random.choice([p for p in primes if p != abs(a1)]) * random.choice([-1, 1])
            b1 = random.choice(primes) * random.choice([-1, 1])
            b2 = random.choice([p for p in primes if p != abs(b1)]) * random.choice([-1, 1])

            c1 = a1 * x_sol + b1 * y_sol
            c2 = a2 * x_sol + b2 * y_sol

            eq1 = self._format_equation(a1, b1, float(c1))
            eq2 = self._format_equation(a2, b2, float(c2))

            x_str = self._format_fraction(x_sol)
            y_str = self._format_fraction(y_sol)

            work_shown = [
                f"Equation 1: ${eq1}$",
                f"Equation 2: ${eq2}$",
                f"This system requires careful elimination with prime coefficients",
                f"After elimination and simplification:",
                f"$x = {x_str}$",
                f"$y = {y_str}$",
                f"Solution: $({x_str}, {y_str})$"
            ]

            problem_latex = f"Solve the system using elimination:\\\\${eq1}$\\\\${eq2}$"
            answer_latex = f"$({x_str}, {y_str})$"

            return EliminationSystemProblem(
                equation1=eq1,
                equation2=eq2,
                solution_x=float(x_sol),
                solution_y=float(y_sol),
                solution_latex=f"({x_str}, {y_str})",
                elimination_variable='x',
                multipliers=(abs(a2), abs(a1)),
                work_shown=work_shown,
                difficulty='challenge',
                problem_latex=problem_latex,
                answer_latex=answer_latex,
                system_type="consistent"
            )

    def generate_worksheet(self, difficulty: str, num_problems: int = 6) -> list:
        """
        Generate multiple elimination system problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of EliminationSystemProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty)
            problems.append(problem)
        return problems