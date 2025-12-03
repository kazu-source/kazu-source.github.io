"""
Why Dividing by Zero Does Not Work Generator
Generates conceptual problems to help students understand why division by zero is undefined
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from equation_generator import Equation


class DividingByZeroExplanationGenerator:
    """Generates problems explaining why division by zero is undefined."""

    def __init__(self, seed=None):
        """Initialize the dividing by zero explanation generator."""
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
        """Generate a single division by zero problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """
        Generate easy problems: Basic examples showing undefined results.
        Focus on recognizing division by zero in simple expressions.
        """
        problem_type = random.choice([
            'basic_division',
            'is_defined',
            'conceptual_check',
            'comparison'
        ])

        if problem_type == 'basic_division':
            # Simple division by zero examples
            numerator = random.randint(1, 20)
            latex = f"\\text{{Is }} \\frac{{{numerator}}}{{0}} \\text{{ defined? (1=yes, 0=no)}}"
            solution = 0  # No, it's not defined
            steps = ["Division by zero is undefined", "Answer: No (0)"]

        elif problem_type == 'is_defined':
            # Ask if various divisions are defined
            if random.choice([True, False]):
                # Division by zero (undefined)
                num = random.randint(1, 15)
                latex = f"\\text{{Is }} {num} \\div 0 \\text{{ defined? (1=yes, 0=no)}}"
                solution = 0
                steps = ["Dividing by zero is undefined", "Answer: No (0)"]
            else:
                # Normal division (defined)
                num = random.randint(1, 15)
                denom = random.randint(1, 10)
                latex = f"\\text{{Is }} {num} \\div {denom} \\text{{ defined? (1=yes, 0=no)}}"
                solution = 1
                steps = ["Dividing by a non-zero number is defined", "Answer: Yes (1)"]

        elif problem_type == 'conceptual_check':
            # Conceptual understanding
            scenarios = [
                (f"\\text{{Can you divide 10 cookies among 0 people? (1=yes, 0=no)}}",
                 0, ["No one to give cookies to", "Division by zero is impossible"]),
                (f"\\text{{Does }} \\frac{{0}}{{5}} \\text{{ equal zero? (1=yes, 0=no)}}",
                 1, ["0 divided by any non-zero number = 0", "Answer: Yes (1)"]),
                (f"\\text{{Is }} \\frac{{7}}{{0}} \\text{{ equal to infinity? (1=yes, 0=no)}}",
                 0, ["Division by zero is undefined, not infinity", "Answer: No (0)"]),
            ]
            latex, solution, steps = random.choice(scenarios)

        else:  # comparison
            # Compare two expressions
            num1 = random.randint(1, 12)
            num2 = random.randint(1, 12)
            denom = random.randint(1, 8)

            scenarios = [
                (f"\\text{{Which is undefined: }} \\frac{{{num1}}}{{0}} \\text{{ or }} \\frac{{{num2}}}{{{denom}}}? \\text{{ (1=first, 2=second, 0=both)}}",
                 1, [f"{num1}/0 is undefined", f"{num2}/{denom} is defined", "Answer: First (1)"]),
                (f"\\text{{Which is defined: }} \\frac{{{num1}}}{{{denom}}} \\text{{ or }} \\frac{{{num2}}}{{0}}? \\text{{ (1=first, 2=second, 0=neither)}}",
                 1, [f"{num1}/{denom} is defined", f"{num2}/0 is undefined", "Answer: First (1)"]),
            ]
            latex, solution, steps = random.choice(scenarios)

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """
        Generate medium problems: Algebraic expressions that would require dividing by zero.
        Students identify when expressions become undefined.
        """
        problem_type = random.choice([
            'simple_fraction',
            'evaluate_fraction',
            'which_undefined',
            'zero_numerator_vs_denominator'
        ])

        if problem_type == 'simple_fraction':
            # Evaluate fractions with variables
            numerator = random.randint(2, 15)
            var = random.choice(['x', 'y', 'n', 'a'])

            scenarios = [
                # x = 0 case
                (f"\\text{{Is }} \\frac{{{numerator}}}{{{var}}} \\text{{ defined when }} {var} = 0? \\text{{ (1=yes, 0=no)}}",
                 0, [f"When {var}=0, denominator = 0", "Division by zero is undefined", "Answer: No (0)"]),
                # x ≠ 0 case
                (f"\\text{{Is }} \\frac{{{numerator}}}{{{var}}} \\text{{ defined when }} {var} = {random.randint(1, 10)}? \\text{{ (1=yes, 0=no)}}",
                 1, [f"Denominator is non-zero", "Division is defined", "Answer: Yes (1)"]),
            ]
            latex, solution, steps = random.choice(scenarios)

        elif problem_type == 'evaluate_fraction':
            # Evaluate or identify as undefined
            numerator = random.randint(3, 20)
            denominator_expr_val = random.choice([0, random.randint(1, 8)])

            if denominator_expr_val == 0:
                latex = f"\\text{{Evaluate }} \\frac{{{numerator}}}{{{denominator_expr_val}}} \\text{{ or write 'undefined' (use 999 for undefined)}}"
                solution = 999  # Code for undefined
                steps = ["Denominator = 0", "Division by zero is undefined", "Answer: undefined (999)"]
            else:
                result = numerator / denominator_expr_val
                if result == int(result):
                    solution = int(result)
                    latex = f"\\text{{Evaluate }} \\frac{{{numerator}}}{{{denominator_expr_val}}}"
                    steps = [f"{numerator} ÷ {denominator_expr_val} = {solution}"]
                else:
                    # Pick a denominator that divides evenly
                    denominator_expr_val = random.choice([d for d in range(2, 9) if numerator % d == 0])
                    solution = numerator // denominator_expr_val
                    latex = f"\\text{{Evaluate }} \\frac{{{numerator}}}{{{denominator_expr_val}}}"
                    steps = [f"{numerator} ÷ {denominator_expr_val} = {solution}"]

        elif problem_type == 'which_undefined':
            # Multiple expressions, identify which is undefined
            var = random.choice(['x', 'a', 'n'])
            var_value = random.choice([0, random.randint(1, 8)])

            num1 = random.randint(5, 20)
            num2 = random.randint(5, 20)

            if var_value == 0:
                latex = f"\\text{{When }} {var} = 0, \\text{{ which is undefined: }} \\frac{{{num1}}}{{{var}}} \\text{{ (enter 1) or }} {num2}{var} \\text{{ (enter 2)?}}"
                solution = 1
                steps = [f"When {var}=0: {num1}/{var} has denominator 0 (undefined)",
                        f"{num2}{var} = 0 (defined)", "Answer: First (1)"]
            else:
                latex = f"\\text{{When }} {var} = {var_value}, \\text{{ how many are undefined: }} \\frac{{{num1}}}{{{var}}}, \\frac{{{num2}}}{{{var_value}}}?"
                solution = 0
                steps = ["Both denominators are non-zero", "Both are defined", "Answer: 0 undefined"]

        else:  # zero_numerator_vs_denominator
            # Understanding difference between 0/n and n/0
            num = random.randint(1, 15)

            scenarios = [
                (f"\\text{{What is }} \\frac{{0}}{{{num}}}?",
                 0, ["Zero divided by any non-zero number", "Equals 0"]),
                (f"\\text{{What is }} \\frac{{{num}}}{{0}}? \\text{{ (use 999 for undefined)}}",
                 999, ["Any number divided by zero", "Is undefined (999)"]),
                (f"\\text{{Which equals 0: }} \\frac{{0}}{{{num}}} \\text{{ (enter 1) or }} \\frac{{{num}}}{{0}} \\text{{ (enter 2)?}}",
                 1, [f"0/{num} = 0", f"{num}/0 is undefined", "Answer: First (1)"]),
            ]
            latex, solution, steps = random.choice(scenarios)

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """
        Generate hard problems: Finding values that make expressions undefined.
        Students solve for values where denominator equals zero.
        """
        problem_type = random.choice([
            'find_undefined_value',
            'linear_denominator',
            'multiple_restrictions',
            'compound_fraction'
        ])

        if problem_type == 'find_undefined_value':
            # Find value of x that makes denominator zero
            var = random.choice(['x', 'y', 'n', 'a'])

            # Simple: denominator is (x - a)
            a = random.randint(-8, 8)
            if a >= 0:
                denom_str = f"{var} - {a}"
            else:
                denom_str = f"{var} + {abs(a)}"

            num = random.randint(3, 15)
            latex = f"\\text{{For what value of }} {var} \\text{{ is }} \\frac{{{num}}}{{{denom_str}}} \\text{{ undefined?}}"
            solution = a
            steps = [f"Set denominator = 0: {denom_str} = 0",
                    f"{var} = {a}",
                    f"When {var} = {a}, expression is undefined"]

        elif problem_type == 'linear_denominator':
            # Denominator is ax + b
            var = random.choice(['x', 'y', 't'])
            a = random.choice([2, 3, 4, 5])
            b = random.randint(-10, 10)

            # Calculate where ax + b = 0
            # ax + b = 0 → x = -b/a
            if b % a == 0:
                solution = -b // a
            else:
                # Adjust b to make it divisible
                b = a * random.randint(-3, 3)
                solution = -b // a

            if b >= 0:
                denom_str = f"{a}{var} + {b}"
            else:
                denom_str = f"{a}{var} - {abs(b)}"

            num = random.randint(5, 20)
            latex = f"\\text{{Find }} {var} \\text{{ where }} \\frac{{{num}}}{{{denom_str}}} \\text{{ is undefined}}"
            steps = [f"Set denominator = 0: {denom_str} = 0",
                    f"{a}{var} = {-b}",
                    f"{var} = {solution}"]

        elif problem_type == 'multiple_restrictions':
            # Count how many values make expression undefined
            var = random.choice(['x', 'n'])

            # Two denominators with different restrictions
            a1 = random.randint(-5, 5)
            a2 = random.randint(-5, 5)
            while a2 == a1:  # Make sure they're different
                a2 = random.randint(-5, 5)

            if a1 >= 0:
                denom1 = f"{var} - {a1}"
            else:
                denom1 = f"{var} + {abs(a1)}"

            if a2 >= 0:
                denom2 = f"{var} - {a2}"
            else:
                denom2 = f"{var} + {abs(a2)}"

            latex = f"\\text{{How many values make }} \\frac{{1}}{{{denom1}}} + \\frac{{1}}{{{denom2}}} \\text{{ undefined?}}"
            solution = 2  # Two different values
            steps = [f"{denom1} = 0 when {var} = {a1}",
                    f"{denom2} = 0 when {var} = {a2}",
                    "Two values make it undefined"]

        else:  # compound_fraction
            # Nested fraction or complex expression
            var = random.choice(['x', 'a'])
            a = random.randint(1, 6)

            scenarios = [
                # 1/(x-a) format - find the restriction
                (f"\\text{{When is }} \\frac{{1}}{{{var} - {a}}} \\text{{ undefined? }} {var} = ?",
                 a, [f"{var} - {a} = 0", f"{var} = {a}"]),
                # More complex: (x+b)/(x-a)
                (f"\\text{{For what }} {var} \\text{{ is }} \\frac{{{var} + {random.randint(1, 5)}}}{{{var} - {a}}} \\text{{ undefined?}}",
                 a, [f"Only denominator matters: {var} - {a} = 0", f"{var} = {a}"]),
            ]
            latex, solution, steps = random.choice(scenarios)

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """
        Generate challenge problems: Analyzing when rational expressions are undefined.
        Complex expressions with multiple variables and restrictions.
        """
        problem_type = random.choice([
            'quadratic_denominator',
            'factored_denominator',
            'system_restrictions',
            'conceptual_analysis'
        ])

        if problem_type == 'quadratic_denominator':
            # Denominator is (x-a)(x-b), find how many restrictions
            var = random.choice(['x', 't'])
            a = random.randint(-4, 4)
            b = random.randint(-4, 4)
            while b == a:
                b = random.randint(-4, 4)

            # Format the factored form
            if a >= 0:
                factor1 = f"{var} - {a}"
            else:
                factor1 = f"{var} + {abs(a)}"

            if b >= 0:
                factor2 = f"{var} - {b}"
            else:
                factor2 = f"{var} + {abs(b)}"

            latex = f"\\text{{How many values make }} \\frac{{1}}{{({factor1})({factor2})}} \\text{{ undefined?}}"
            solution = 2
            steps = [f"({factor1})({factor2}) = 0 when:",
                    f"{var} = {a} or {var} = {b}",
                    "Two values make it undefined"]

        elif problem_type == 'factored_denominator':
            # Find specific restriction from factored form
            var = 'x'
            a = random.randint(2, 8)
            b = random.randint(-6, 6)

            if b >= 0:
                factor = f"{var} - {b}"
            else:
                factor = f"{var} + {abs(b)}"

            scenarios = [
                # Ask for one of the restrictions
                (f"\\text{{Find one value where }} \\frac{{{a}}}{{({var})({factor})}} \\text{{ is undefined (enter smaller value)}}",
                 min(0, b),
                 [f"Denominator = 0 when {var} = 0 or {var} = {b}",
                  f"Smaller value: {min(0, b)}"]),
                # Count restrictions including repeated factors
                (f"\\text{{How many distinct values make }} \\frac{{1}}{{({factor})^2}} \\text{{ undefined?}}",
                 1,
                 [f"({factor})^2 = 0 only when {var} = {b}",
                  "One distinct value"]),
            ]
            latex, solution, steps = random.choice(scenarios)

        elif problem_type == 'system_restrictions':
            # Multiple fractions in one expression
            var = 'x'
            a = random.randint(1, 5)
            b = random.randint(-5, -1)
            c = random.randint(1, 5)
            while c == a:
                c = random.randint(1, 5)

            latex = f"\\text{{How many values make }} \\frac{{1}}{{{var} - {a}}} + \\frac{{2}}{{{var} + {abs(b)}}} + \\frac{{3}}{{{var} - {c}}} \\text{{ undefined?}}"
            solution = 3
            steps = [f"Restrictions: {var} = {a}, {var} = {b}, {var} = {c}",
                    "Three values make it undefined"]

        else:  # conceptual_analysis
            # Deep conceptual questions
            var = random.choice(['x', 'n'])

            scenarios = [
                # Why can't we divide by zero
                (f"\\text{{If }} {var} \\cdot 0 = 5, \\text{{ what is }} {var}? \\text{{ (999=no solution)}}",
                 999,
                 ["Any number times 0 equals 0, not 5",
                  "This equation has no solution",
                  "This is why division by 0 is undefined"]),

                # Understanding limits and division
                (f"\\text{{As denominator approaches 0, does }} \\frac{{1}}{{{var}}} \\text{{ approach a number? (1=yes, 0=no)}}",
                 0,
                 ["As denominator → 0, fraction → ∞ or -∞",
                  "It doesn't approach a specific number",
                  "This is why it's undefined"]),

                # Solving with restrictions
                (f"\\text{{Can }} \\frac{{{var}}}{{{var}}} = 1 \\text{{ when }} {var} = 0? \\text{{ (1=yes, 0=no)}}",
                 0,
                 ["When x=0: 0/0 is indeterminate form",
                  "Cannot simplify before substituting",
                  "Answer: No"]),
            ]
            latex, solution, steps = random.choice(scenarios)

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = DividingByZeroExplanationGenerator()

    print("Testing Dividing by Zero Explanation Generator")
    print("=" * 80)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 80)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=5)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}")
            print(f"   Steps: {problem.steps}")
            print()
