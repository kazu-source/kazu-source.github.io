"""
Solving Multi-Step Equations Generator
Generates problems requiring multiple steps to solve linear equations
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
from equation_generator import Equation


class SolvingMultiStepEquationsGenerator:
    """Generates multi-step equation problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """Generate worksheet problems."""
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        """Generate a single problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _format_term(self, coef: int, var: str = 'x') -> str:
        """Format coefficient with variable."""
        if coef == 1:
            return var
        elif coef == -1:
            return f"-{var}"
        else:
            return f"{coef}{var}"

    def _generate_easy(self) -> Equation:
        """Generate easy: Two-step equations (ax + b = c)."""
        a = random.choice([2, 3, 4, 5])
        x = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = a * x + b

        # Format equation
        if b >= 0:
            latex = f"{self._format_term(a)} + {b} = {c}"
        else:
            latex = f"{self._format_term(a)} - {abs(b)} = {c}"

        solution = str(x)

        steps = [
            f"\\text{{Subtract {b} from both sides}}" if b > 0 else f"\\text{{Add {abs(b)} to both sides}}",
            f"{self._format_term(a)} = {c - b}",
            f"\\text{{Divide both sides by {a}}}",
            f"x = {x}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium: Three-step equations with distribution or combining."""
        problem_type = random.choice(['distribute', 'combine_then_solve'])

        if problem_type == 'distribute':
            # a(x + b) = c
            a = random.choice([2, 3, 4])
            x = random.randint(-8, 8)
            b = random.randint(-5, 5)
            c = a * (x + b)

            if b >= 0:
                latex = f"{a}(x + {b}) = {c}"
            else:
                latex = f"{a}(x - {abs(b)}) = {c}"

            solution = str(x)

            steps = [
                f"\\text{{Distribute: }} {a}x + {a * b} = {c}" if a * b >= 0 else f"\\text{{Distribute: }} {a}x - {abs(a * b)} = {c}",
                f"\\text{{Subtract {a * b} from both sides}}" if a * b > 0 else f"\\text{{Add {abs(a * b)} to both sides}}",
                f"{a}x = {c - a * b}",
                f"x = {x}"
            ]

        else:  # combine_then_solve
            # ax + bx + c = d
            a = random.randint(2, 5)
            b = random.randint(1, 4)
            x = random.randint(-8, 8)
            c = random.randint(-10, 10)
            d = (a + b) * x + c

            latex = f"{a}x + {b}x + {c} = {d}" if c >= 0 else f"{a}x + {b}x - {abs(c)} = {d}"
            solution = str(x)

            combined = a + b
            steps = [
                f"\\text{{Combine like terms: }} {combined}x + {c} = {d}" if c >= 0 else f"\\text{{Combine: }} {combined}x - {abs(c)} = {d}",
                f"{combined}x = {d - c}",
                f"x = {x}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard: Multi-step with fractions or multiple distributions."""
        problem_type = random.choice(['two_distributions', 'fraction_coef'])

        if problem_type == 'two_distributions':
            # a(x + b) + c(x + d) = e
            a = random.choice([2, 3])
            c = random.choice([2, 3, 4])
            x = random.randint(-5, 5)
            b = random.randint(-4, 4)
            d = random.randint(-4, 4)
            e = a * (x + b) + c * (x + d)

            b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
            d_str = f"+ {d}" if d >= 0 else f"- {abs(d)}"

            latex = f"{a}(x {b_str}) + {c}(x {d_str}) = {e}"
            solution = str(x)

            expanded_const = a * b + c * d
            combined_coef = a + c

            steps = [
                f"\\text{{Distribute both terms}}",
                f"{a}x + {a * b} + {c}x + {c * d} = {e}",
                f"\\text{{Combine like terms: }} {combined_coef}x + {expanded_const} = {e}",
                f"{combined_coef}x = {e - expanded_const}",
                f"x = {x}"
            ]

        else:  # fraction_coef
            # (1/2)x + b = c  (use even numbers for clean answers)
            x = random.choice([2, 4, 6, 8, 10]) * random.choice([-1, 1])
            b = random.randint(-10, 10)
            c = x // 2 + b

            latex = f"\\frac{{1}}{{2}}x + {b} = {c}" if b >= 0 else f"\\frac{{1}}{{2}}x - {abs(b)} = {c}"
            solution = str(x)

            steps = [
                f"\\text{{Subtract {b} from both sides}}" if b > 0 else f"\\text{{Add {abs(b)} to both sides}}",
                f"\\frac{{1}}{{2}}x = {c - b}",
                f"\\text{{Multiply both sides by 2}}",
                f"x = {x}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge: Complex multi-step with variables on one side."""
        problem_type = random.choice(['nested', 'multiple_fractions', 'complex_combine'])

        if problem_type == 'nested':
            # a(b(x + c) + d) = e
            a = 2
            b = random.choice([2, 3])
            x = random.randint(-4, 4)
            c = random.randint(-3, 3)
            d = random.randint(-5, 5)
            e = a * (b * (x + c) + d)

            c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"
            d_str = f"+ {d}" if d >= 0 else f"- {abs(d)}"

            latex = f"{a}({b}(x {c_str}) {d_str}) = {e}"
            solution = str(x)

            inner = b * (x + c)
            steps = [
                f"\\text{{Work from inside out}}",
                f"\\text{{Inner: }} {b}(x {c_str}) = {b}x + {b * c}",
                f"{a}({b}x + {b * c} {d_str}) = {e}",
                f"\\text{{Distribute the {a}}}",
                f"{a * b}x + {a * (b * c + d)} = {e}",
                f"x = {x}"
            ]

        elif problem_type == 'multiple_fractions':
            # x/a + x/b = c
            a = random.choice([2, 3])
            b = random.choice([4, 6])
            lcm = (a * b) // 2 if a * b % 2 == 0 else a * b  # Simplified LCM for 2,4 or 3,6
            x = lcm * random.choice([1, 2])
            c = x // a + x // b

            latex = f"\\frac{{x}}{{{a}}} + \\frac{{x}}{{{b}}} = {c}"
            solution = str(x)

            steps = [
                f"\\text{{Find common denominator: }} {a * b // (2 if a == 2 or b == 2 else 1)}",
                f"\\text{{Combine fractions}}",
                f"x = {x}"
            ]

        else:  # complex_combine
            # ax + b - cx + d = e
            a = random.randint(3, 6)
            c = random.randint(1, a - 1)
            x = random.randint(-8, 8)
            b = random.randint(-10, 10)
            d = random.randint(-10, 10)
            e = a * x + b - c * x + d

            b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
            d_str = f"+ {d}" if d >= 0 else f"- {abs(d)}"

            latex = f"{a}x {b_str} - {c}x {d_str} = {e}"
            solution = str(x)

            combined_coef = a - c
            combined_const = b + d

            steps = [
                f"\\text{{Combine like terms}}",
                f"{combined_coef}x + {combined_const} = {e}" if combined_const >= 0 else f"{combined_coef}x - {abs(combined_const)} = {e}",
                f"{combined_coef}x = {e - combined_const}",
                f"x = {x}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = SolvingMultiStepEquationsGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: x = {problem.solution}\n")


if __name__ == '__main__':
    main()
