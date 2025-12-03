"""
Why an Even Square Root Cannot Be Negative Generator - Unit 8
Generates problems about understanding why principal square roots are positive
and the conceptual foundation of square root definitions.
"""

import random
from typing import List
import sys
import os

# Add the parent directory to sys.path to import equation_generator
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.insert(0, parent_dir)
from equation_generator import Equation


class WhySquareRootsArePositiveGenerator:
    """Generates problems about principal square roots and why they are defined as positive."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
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

    def _generate_problem(self, difficulty: str) -> Equation:
        """Generate a single problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate easy problems: Identify if sqrt results are positive/negative"""
        problem_types = ['identify_principal', 'true_false_negative', 'evaluate_principal']
        problem_type = random.choice(problem_types)

        if problem_type == 'identify_principal':
            # Is the principal square root positive or negative?
            perfect_squares = [4, 9, 16, 25, 36, 49, 64, 81, 100]
            value = random.choice(perfect_squares)
            sqrt_value = int(value ** 0.5)

            latex = f"\\text{{Is }} \\sqrt{{{value}}} \\text{{ positive or negative?}}"
            solution = "positive"
            steps = [f"The principal square root \\sqrt{{{value}}} = {sqrt_value}, which is positive"]

        elif problem_type == 'true_false_negative':
            # True or False: sqrt(a) can be negative
            perfect_squares = [9, 16, 25, 36, 49]
            value = random.choice(perfect_squares)
            sqrt_value = int(value ** 0.5)

            latex = f"\\text{{True or False: }} \\sqrt{{{value}}} = -{sqrt_value}"
            solution = "False"
            steps = [f"\\sqrt{{{value}}} = {sqrt_value} (positive by definition), not -{sqrt_value}"]

        else:  # evaluate_principal
            # Evaluate the principal square root
            perfect_squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
            value = random.choice(perfect_squares)
            sqrt_value = int(value ** 0.5)

            latex = f"\\text{{Evaluate the principal square root: }} \\sqrt{{{value}}}"
            solution = sqrt_value
            steps = [f"\\sqrt{{{value}}} = {sqrt_value} (the positive root)"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate medium problems: Principal vs negative square roots, ±sqrt notation"""
        problem_types = ['plus_minus_notation', 'both_roots', 'principal_vs_negative', 'which_notation']
        problem_type = random.choice(problem_types)

        if problem_type == 'plus_minus_notation':
            # Identify both solutions using ±
            perfect_squares = [4, 9, 16, 25, 36, 49, 64, 81]
            value = random.choice(perfect_squares)
            sqrt_value = int(value ** 0.5)

            latex = f"\\text{{If }} x^2 = {value}, \\text{{ what are both solutions?}}"
            solution = f"x = \\pm{sqrt_value}"
            steps = [
                f"x^2 = {value}",
                f"x = \\pm\\sqrt{{{value}}}",
                f"x = \\pm{sqrt_value}"
            ]

        elif problem_type == 'both_roots':
            # Find both the positive and negative square roots
            perfect_squares = [9, 16, 25, 36, 49, 64]
            value = random.choice(perfect_squares)
            sqrt_value = int(value ** 0.5)

            latex = f"\\text{{Find both square roots of }} {value}"
            solution = f"{sqrt_value} \\text{{ and }} -{sqrt_value}"
            steps = [
                f"\\text{{Positive root: }} {sqrt_value}",
                f"\\text{{Negative root: }} -{sqrt_value}",
                f"\\text{{Both: }} \\pm{sqrt_value}"
            ]

        elif problem_type == 'principal_vs_negative':
            # Compare principal root to negative root
            perfect_squares = [16, 25, 36, 49, 64]
            value = random.choice(perfect_squares)
            sqrt_value = int(value ** 0.5)

            latex = f"\\text{{What is the difference between }} \\sqrt{{{value}}} \\text{{ and }} -\\sqrt{{{value}}}?"
            solution = f"\\sqrt{{{value}}} = {sqrt_value} \\text{{ (principal/positive), }} -\\sqrt{{{value}}} = -{sqrt_value} \\text{{ (negative)}}"
            steps = [
                f"\\sqrt{{{value}}} = {sqrt_value} \\text{{ (principal root, always positive)}}",
                f"-\\sqrt{{{value}}} = -{sqrt_value} \\text{{ (negation of the principal root)}}"
            ]

        else:  # which_notation
            # Choose correct notation
            perfect_squares = [9, 25, 36, 49]
            value = random.choice(perfect_squares)
            sqrt_value = int(value ** 0.5)

            latex = f"\\text{{Which notation represents both solutions to }} x^2 = {value}\\text{{: (A) }} \\sqrt{{{value}}}\\text{{, (B) }} \\pm\\sqrt{{{value}}}\\text{{, (C) }} -\\sqrt{{{value}}}?"
            solution = f"(B) \\pm\\sqrt{{{value}}}"
            steps = [
                f"x^2 = {value} \\text{{ has two solutions}}",
                f"x = {sqrt_value} \\text{{ and }} x = -{sqrt_value}",
                f"\\text{{Written as: }} x = \\pm\\sqrt{{{value}}} = \\pm{sqrt_value}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate hard problems: Solving equations with square roots, checking for extraneous solutions"""
        problem_types = ['solve_sqrt_equation', 'extraneous_solution', 'sqrt_both_sides', 'isolate_sqrt']
        problem_type = random.choice(problem_types)

        if problem_type == 'solve_sqrt_equation':
            # Solve sqrt(x) = a
            perfect_squares = [2, 3, 4, 5, 6, 7, 8]
            a = random.choice(perfect_squares)
            x = a ** 2

            latex = f"\\text{{Solve: }} \\sqrt{{x}} = {a}"
            solution = x
            steps = [
                f"\\sqrt{{x}} = {a}",
                f"(\\sqrt{{x}})^2 = ({a})^2",
                f"x = {x}",
                f"\\text{{Check: }} \\sqrt{{{x}}} = {a} \\checkmark"
            ]

        elif problem_type == 'extraneous_solution':
            # Solve equation that produces extraneous solution
            a = random.randint(2, 6)
            b = random.randint(1, 4)
            # sqrt(x) + a = b, where b < a gives no solution
            if b > a:
                b, a = a, b  # Swap to ensure valid solution
            x = (b - a) ** 2 if b > a else None

            if x is not None and x >= 0:
                latex = f"\\text{{Solve: }} \\sqrt{{x}} + {a} = {b}"
                solution = x
                steps = [
                    f"\\sqrt{{x}} = {b - a}",
                    f"x = {x}",
                    f"\\text{{Check: }} \\sqrt{{{x}}} + {a} = {b - a} + {a} = {b} \\checkmark"
                ]
            else:
                # No solution case
                latex = f"\\text{{Solve: }} \\sqrt{{x}} = -{abs(b - a)}"
                solution = "\\text{No solution}"
                steps = [
                    f"\\sqrt{{x}} = -{abs(b - a)}",
                    f"\\text{{Since }} \\sqrt{{x}} \\geq 0 \\text{{ always, there is no solution}}"
                ]

        elif problem_type == 'sqrt_both_sides':
            # Solve x = sqrt(a), then check
            perfect_squares = [4, 9, 16, 25, 36, 49]
            a = random.choice(perfect_squares)
            sqrt_a = int(a ** 0.5)

            # Create equation: sqrt(x + b) = c
            c = random.randint(3, 7)
            b = c ** 2 - random.randint(1, 10)
            x = c ** 2 - b

            latex = f"\\text{{Solve: }} \\sqrt{{x + {b}}} = {c}"
            solution = x
            steps = [
                f"\\sqrt{{x + {b}}} = {c}",
                f"x + {b} = {c ** 2}",
                f"x = {x}",
                f"\\text{{Check: }} \\sqrt{{{x} + {b}}} = \\sqrt{{{c ** 2}}} = {c} \\checkmark"
            ]

        else:  # isolate_sqrt
            # Isolate square root first
            a = random.randint(2, 5)
            b = random.randint(1, 4)
            c = random.randint(6, 10)
            # a*sqrt(x) + b = c
            sqrt_x_val = (c - b) / a
            if sqrt_x_val > 0 and sqrt_x_val == int(sqrt_x_val):
                x = int(sqrt_x_val) ** 2
                sqrt_x_val = int(sqrt_x_val)

                latex = f"\\text{{Solve: }} {a}\\sqrt{{x}} + {b} = {c}"
                solution = x
                steps = [
                    f"{a}\\sqrt{{x}} = {c - b}",
                    f"\\sqrt{{x}} = {sqrt_x_val}",
                    f"x = {x}",
                    f"\\text{{Check: }} {a}\\sqrt{{{x}}} + {b} = {a}({sqrt_x_val}) + {b} = {c} \\checkmark"
                ]
            else:
                # Fallback to simpler equation
                sqrt_x_val = random.randint(2, 6)
                x = sqrt_x_val ** 2
                latex = f"\\text{{Solve: }} \\sqrt{{x}} = {sqrt_x_val}"
                solution = x
                steps = [f"x = {x}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: Domain restrictions due to square roots"""
        problem_types = ['domain_restriction', 'compound_sqrt', 'system_with_sqrt', 'why_positive']
        problem_type = random.choice(problem_types)

        if problem_type == 'domain_restriction':
            # Find domain where sqrt is defined
            a = random.randint(1, 5)
            b = random.randint(1, 10)
            # sqrt(ax + b) requires ax + b >= 0

            latex = f"\\text{{Find the domain of }} f(x) = \\sqrt{{{a}x + {b}}}"
            solution = f"x \\geq {-b/a:.2f}" if a > 0 else f"x \\leq {-b/a:.2f}"
            steps = [
                f"\\text{{For }} \\sqrt{{{a}x + {b}}} \\text{{ to be defined:}}",
                f"{a}x + {b} \\geq 0",
                f"{a}x \\geq {-b}",
                solution
            ]

        elif problem_type == 'compound_sqrt':
            # Solve equation with two square roots
            # sqrt(x) + sqrt(y) = a, with constraint
            a = random.randint(3, 6)
            x = random.randint(1, 4) ** 2
            y = (a - int(x ** 0.5)) ** 2

            latex = f"\\text{{If }} \\sqrt{{x}} + \\sqrt{{y}} = {a} \\text{{ and }} x = {x}, \\text{{ find }} y"
            solution = y
            steps = [
                f"\\sqrt{{{x}}} + \\sqrt{{y}} = {a}",
                f"{int(x ** 0.5)} + \\sqrt{{y}} = {a}",
                f"\\sqrt{{y}} = {a - int(x ** 0.5)}",
                f"y = {y}"
            ]

        elif problem_type == 'system_with_sqrt':
            # System involving square root
            perfect_squares = [4, 9, 16, 25]
            x_squared = random.choice(perfect_squares)
            x = int(x_squared ** 0.5)
            a = random.randint(2, 5)
            y = a * x

            latex = f"\\text{{Solve the system: }} \\sqrt{{x}} = {x}, \\; y = {a}\\sqrt{{x}}"
            solution = f"x = {x_squared}, y = {y}"
            steps = [
                f"\\text{{From }} \\sqrt{{x}} = {x}:",
                f"x = {x_squared}",
                f"\\text{{Substitute into }} y = {a}\\sqrt{{x}}:",
                f"y = {a}\\sqrt{{{x_squared}}} = {a}({x}) = {y}",
                f"\\text{{Solution: }} ({x_squared}, {y})"
            ]

        else:  # why_positive
            # Explain why principal root is positive
            perfect_squares = [16, 25, 36, 49, 64]
            value = random.choice(perfect_squares)
            sqrt_value = int(value ** 0.5)

            latex = f"\\text{{Explain why }} \\sqrt{{{value}}} = {sqrt_value} \\text{{ and not }} -{sqrt_value}"
            solution = f"\\text{{By definition, }} \\sqrt{{a}} \\text{{ denotes the principal (positive) square root. While both }} {sqrt_value} \\text{{ and }} -{sqrt_value} \\text{{ square to }} {value}\\text{{, the radical symbol }} \\sqrt{{\\;}} \\text{{ always represents the non-negative root.}}"
            steps = [
                f"\\text{{Both }} {sqrt_value} \\text{{ and }} -{sqrt_value} \\text{{ satisfy }} x^2 = {value}",
                f"\\text{{However, }} \\sqrt{{{value}}} \\text{{ specifically means the principal (positive) root}}",
                f"\\sqrt{{{value}}} = {sqrt_value} \\text{{ by definition}}",
                f"\\text{{To represent the negative root, we write }} -\\sqrt{{{value}}} = -{sqrt_value}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = WhySquareRootsArePositiveGenerator()

    print("Testing Why Square Roots Are Positive Generator")
    print("=" * 80)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 80)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}")
            if problem.steps:
                print(f"   Steps:")
                for step in problem.steps:
                    print(f"      {step}")
            print()
