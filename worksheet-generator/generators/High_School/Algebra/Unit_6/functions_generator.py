"""
Generator for functions worksheets.
Chapter 6: Functions - Function Notation and Evaluation
"""

import random
import sys
from pathlib import Path
from dataclasses import dataclass
from fractions import Fraction

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))


@dataclass
class FunctionsProblem:
    """Represents a functions problem."""
    problem_type: str  # 'evaluate', 'notation', 'equation_vs_function', 'composite'
    function_notation: str  # e.g., f(x) = 2x + 3
    problem_latex: str  # Problem statement in LaTeX
    answer_latex: str  # Answer in LaTeX
    work_shown: list  # Step-by-step solution
    difficulty: str  # easy, medium, hard, challenge


class FunctionsGenerator:
    """Generator for functions problems."""

    def __init__(self, seed=None):
        """
        Initialize the generator.

        Args:
            seed: Random seed for reproducibility
        """
        if seed is not None:
            random.seed(seed)

    def _generate_function(self, difficulty):
        """Generate a function based on difficulty level."""
        if difficulty == 'easy':
            # Linear functions
            a = random.randint(1, 5) * random.choice([-1, 1])
            b = random.randint(-10, 10)
            if b >= 0:
                return f"{a}x + {b}", lambda x: a * x + b
            else:
                return f"{a}x - {abs(b)}", lambda x: a * x + b

        elif difficulty == 'medium':
            # Quadratic or more complex linear
            func_type = random.choice(['quadratic', 'complex_linear'])
            if func_type == 'quadratic':
                a = random.randint(1, 3) * random.choice([-1, 1])
                b = random.randint(-5, 5)
                c = random.randint(-10, 10)

                func_str = f"{a}x^2"
                if b > 0:
                    func_str += f" + {b}x"
                elif b < 0:
                    func_str += f" - {abs(b)}x"

                if c > 0:
                    func_str += f" + {c}"
                elif c < 0:
                    func_str += f" - {abs(c)}"

                return func_str, lambda x: a * x**2 + b * x + c
            else:
                # Complex linear with fractions
                num = random.randint(1, 5) * random.choice([-1, 1])
                den = random.randint(2, 4)
                b = random.randint(-10, 10)

                if b >= 0:
                    return f"\\frac{{{num}x}}{{{den}}} + {b}", lambda x: (num * x) / den + b
                else:
                    return f"\\frac{{{num}x}}{{{den}}} - {abs(b)}", lambda x: (num * x) / den + b

        elif difficulty == 'hard':
            # Cubic or rational
            func_type = random.choice(['cubic', 'rational'])
            if func_type == 'cubic':
                a = random.randint(1, 2) * random.choice([-1, 1])
                b = random.randint(-3, 3)
                c = random.randint(-5, 5)

                func_str = f"{a}x^3"
                if b != 0:
                    if b > 0:
                        func_str += f" + {b}x"
                    else:
                        func_str += f" - {abs(b)}x"
                if c > 0:
                    func_str += f" + {c}"
                elif c < 0:
                    func_str += f" - {abs(c)}"

                return func_str, lambda x: a * x**3 + b * x + c
            else:
                # Simple rational
                a = random.randint(1, 5)
                b = random.randint(1, 3)
                return f"\\frac{{{a}}}{{x + {b}}}", lambda x: a / (x + b) if x != -b else None

        else:  # challenge
            # Composite or piecewise
            func_type = random.choice(['composite', 'absolute'])
            if func_type == 'absolute':
                a = random.randint(1, 3) * random.choice([-1, 1])
                b = random.randint(-5, 5)
                if b >= 0:
                    return f"|{a}x + {b}|", lambda x: abs(a * x + b)
                else:
                    return f"|{a}x - {abs(b)}|", lambda x: abs(a * x + b)
            else:
                # Square root
                a = random.randint(1, 4)
                b = random.randint(0, 5)
                return f"\\sqrt{{{a}x + {b}}}", lambda x: (a * x + b) ** 0.5 if a * x + b >= 0 else None

    def generate_problem(self, difficulty: str) -> FunctionsProblem:
        """
        Generate a single functions problem.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            FunctionsProblem object
        """
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> FunctionsProblem:
        """Generate easy problem (evaluate simple linear functions)."""
        problem_type = random.choice(['evaluate', 'notation'])

        if problem_type == 'evaluate':
            # Evaluate f(a) for a linear function
            func_str, func = self._generate_function('easy')
            func_name = random.choice(['f', 'g', 'h'])
            x_val = random.randint(-5, 5)
            result = func(x_val)

            function_notation = f"{func_name}(x) = {func_str}"
            problem_latex = f"If ${function_notation}$, find ${func_name}({x_val})$"
            answer_latex = f"${func_name}({x_val}) = {result}$"

            work_shown = [
                f"Given: ${function_notation}$",
                f"To find ${func_name}({x_val})$, substitute $x = {x_val}$:",
                f"${func_name}({x_val}) = {func_str.replace('x', f'({x_val})')}$",
                f"${func_name}({x_val}) = {result}$"
            ]

        else:  # notation
            # Understanding function notation
            func_str, func = self._generate_function('easy')
            func_name = random.choice(['f', 'g', 'h'])

            function_notation = f"{func_name}(x) = {func_str}"
            problem_latex = f"Express the equation $y = {func_str}$ using function notation with ${func_name}$"
            answer_latex = f"${function_notation}$"

            work_shown = [
                f"The equation $y = {func_str}$ can be written as:",
                f"${function_notation}$",
                f"This means that ${func_name}$ is a function that takes an input $x$",
                f"and outputs the value ${func_str}$"
            ]

        return FunctionsProblem(
            problem_type=problem_type,
            function_notation=function_notation,
            problem_latex=problem_latex,
            answer_latex=answer_latex,
            work_shown=work_shown,
            difficulty='easy'
        )

    def _generate_medium(self) -> FunctionsProblem:
        """Generate medium problem (quadratic functions, multiple evaluations)."""
        problem_type = random.choice(['evaluate_quadratic', 'multiple_values', 'find_input'])

        if problem_type == 'evaluate_quadratic':
            func_str, func = self._generate_function('medium')
            func_name = random.choice(['f', 'g', 'h'])
            x_val = random.randint(-3, 3)
            result = func(x_val)

            function_notation = f"{func_name}(x) = {func_str}"
            problem_latex = f"If ${function_notation}$, find ${func_name}({x_val})$"

            # Handle fractions in result
            if isinstance(result, float) and not result.is_integer():
                result_frac = Fraction(result).limit_denominator()
                answer_latex = f"${func_name}({x_val}) = \\frac{{{result_frac.numerator}}}{{{result_frac.denominator}}}$"
            else:
                answer_latex = f"${func_name}({x_val}) = {int(result) if isinstance(result, float) else result}$"

            work_shown = [
                f"Given: ${function_notation}$",
                f"Substitute $x = {x_val}$:",
                f"${func_name}({x_val}) = {func_str.replace('x', f'({x_val})')}$",
                f"Calculate the result:",
                answer_latex
            ]

        elif problem_type == 'multiple_values':
            # Evaluate function at multiple points
            func_str, func = self._generate_function('easy')
            func_name = random.choice(['f', 'g'])
            x_vals = random.sample(range(-5, 6), 3)
            results = [func(x) for x in x_vals]

            function_notation = f"{func_name}(x) = {func_str}"
            problem_latex = f"If ${function_notation}$, find ${func_name}({x_vals[0]})$, ${func_name}({x_vals[1]})$, and ${func_name}({x_vals[2]})$"
            answer_latex = f"${func_name}({x_vals[0]}) = {results[0]}$, ${func_name}({x_vals[1]}) = {results[1]}$, ${func_name}({x_vals[2]}) = {results[2]}$"

            work_shown = [
                f"Given: ${function_notation}$",
                f"For ${func_name}({x_vals[0]})$: substitute $x = {x_vals[0]}$ to get {results[0]}",
                f"For ${func_name}({x_vals[1]})$: substitute $x = {x_vals[1]}$ to get {results[1]}",
                f"For ${func_name}({x_vals[2]})$: substitute $x = {x_vals[2]}$ to get {results[2]}"
            ]

        else:  # find_input
            # Given f(x) = y, find x
            a = random.randint(2, 5)
            b = random.randint(-5, 5)
            func_str = f"{a}x + {b}" if b >= 0 else f"{a}x - {abs(b)}"
            func = lambda x: a * x + b
            func_name = random.choice(['f', 'g', 'h'])

            # Choose y value that gives integer x
            y_val = random.choice([v for v in range(-10, 11) if (v - b) % a == 0])
            x_val = (y_val - b) // a

            function_notation = f"{func_name}(x) = {func_str}"
            problem_latex = f"If ${function_notation}$ and ${func_name}(x) = {y_val}$, find $x$"
            answer_latex = f"$x = {x_val}$"

            work_shown = [
                f"Given: ${function_notation}$",
                f"We need to solve: ${func_name}(x) = {y_val}$",
                f"So: ${func_str} = {y_val}$",
                f"${a}x = {y_val - b}$",
                f"$x = {x_val}$"
            ]

        return FunctionsProblem(
            problem_type=problem_type,
            function_notation=function_notation,
            problem_latex=problem_latex,
            answer_latex=answer_latex,
            work_shown=work_shown,
            difficulty='medium'
        )

    def _generate_hard(self) -> FunctionsProblem:
        """Generate hard problem (composition, inverse thinking)."""
        problem_type = random.choice(['composition', 'equation_vs_function', 'table'])

        if problem_type == 'composition':
            # f(g(x)) or g(f(x))
            f_str = f"{random.randint(2, 4)}x + {random.randint(-3, 3)}"
            g_str = f"{random.randint(1, 3)}x - {random.randint(1, 5)}"

            x_val = random.randint(-3, 3)

            # Calculate f(g(x))
            g_result = eval(g_str.replace('x', str(x_val)))
            fg_result = eval(f_str.replace('x', str(g_result)))

            function_notation = f"f(x) = {f_str}, g(x) = {g_str}"
            problem_latex = f"If ${function_notation}$, find $f(g({x_val}))$"
            answer_latex = f"$f(g({x_val})) = {fg_result}$"

            work_shown = [
                f"Given: $f(x) = {f_str}$ and $g(x) = {g_str}$",
                f"First find $g({x_val})$:",
                f"$g({x_val}) = {g_str.replace('x', str(x_val))} = {g_result}$",
                f"Then find $f({g_result})$:",
                f"$f({g_result}) = {f_str.replace('x', str(g_result))} = {fg_result}$"
            ]

        elif problem_type == 'equation_vs_function':
            # Distinguish between equations and functions
            examples = [
                ("y = 2x + 3", True, "Each x-value has exactly one y-value"),
                ("x^2 + y^2 = 25", False, "Circle: some x-values have two y-values"),
                ("y = x^2 - 4", True, "Each x-value has exactly one y-value"),
                ("x = y^2", False, "Some x-values have two y-values"),
                ("y = |x|", True, "Each x-value has exactly one y-value")
            ]

            equation, is_function, reason = random.choice(examples)

            function_notation = equation
            problem_latex = f"Determine if the equation ${equation}$ represents a function. Explain why or why not."
            answer_latex = f"{'Yes, it is a function' if is_function else 'No, it is not a function'}: {reason}"

            work_shown = [
                f"To be a function, each input (x-value) must have exactly one output (y-value)",
                f"For ${equation}$:",
                reason,
                f"Therefore, this {'is' if is_function else 'is not'} a function"
            ]

        else:  # table
            # Function from a table
            x_values = sorted(random.sample(range(-5, 6), 4))
            a = random.randint(2, 4)
            b = random.randint(-5, 5)
            y_values = [a * x + b for x in x_values]

            func_name = random.choice(['f', 'g', 'h'])
            test_x = random.choice([x for x in range(-5, 6) if x not in x_values])
            test_y = a * test_x + b

            table_str = "\\begin{array}{|c|c|}\\hline x & " + func_name + "(x) \\\\ \\hline "
            for x, y in zip(x_values, y_values):
                table_str += f"{x} & {y} \\\\ "
            table_str += "\\hline \\end{array}"

            function_notation = f"{func_name}(x) = {a}x + {b}" if b >= 0 else f"{func_name}(x) = {a}x - {abs(b)}"
            problem_latex = f"The table shows values for function ${func_name}$: ${table_str}$ Find ${func_name}({test_x})$"
            answer_latex = f"${func_name}({test_x}) = {test_y}$"

            work_shown = [
                f"Identify the pattern in the table:",
                f"The function appears to be linear",
                f"Find the rate of change: $\\frac{{{y_values[1]} - {y_values[0]}}}{{{x_values[1]} - {x_values[0]}}} = {a}$",
                f"Find the y-intercept using a point: ${function_notation}$",
                f"Therefore: ${func_name}({test_x}) = {test_y}$"
            ]

        return FunctionsProblem(
            problem_type=problem_type,
            function_notation=function_notation,
            problem_latex=problem_latex,
            answer_latex=answer_latex,
            work_shown=work_shown,
            difficulty='hard'
        )

    def _generate_challenge(self) -> FunctionsProblem:
        """Generate challenge problem (piecewise, domain restrictions, inverses)."""
        problem_type = random.choice(['piecewise', 'domain_restriction', 'inverse'])

        if problem_type == 'piecewise':
            # Piecewise function
            a1 = random.randint(1, 3)
            b1 = random.randint(-3, 3)
            a2 = random.randint(-3, -1)
            b2 = random.randint(-3, 3)
            split = random.randint(-2, 2)

            func_name = random.choice(['f', 'g', 'h'])
            test_vals = [split - 2, split, split + 2]

            results = []
            for x in test_vals:
                if x < split:
                    results.append(a1 * x + b1)
                else:
                    results.append(a2 * x + b2)

            function_notation = f"{func_name}(x) = \\begin{{cases}} {a1}x + {b1} & \\text{{if }} x < {split} \\\\ {a2}x + {b2} & \\text{{if }} x \\geq {split} \\end{{cases}}"
            problem_latex = f"For the piecewise function ${function_notation}$, find ${func_name}({test_vals[0]})$, ${func_name}({test_vals[1]})$, and ${func_name}({test_vals[2]})$"
            answer_latex = f"${func_name}({test_vals[0]}) = {results[0]}$, ${func_name}({test_vals[1]}) = {results[1]}$, ${func_name}({test_vals[2]}) = {results[2]}$"

            work_shown = [
                f"For ${func_name}({test_vals[0]})$: since {test_vals[0]} < {split}, use first piece: {results[0]}",
                f"For ${func_name}({test_vals[1]})$: since {test_vals[1]} {'< ' + str(split) if test_vals[1] < split else '≥ ' + str(split)}, use {'first' if test_vals[1] < split else 'second'} piece: {results[1]}",
                f"For ${func_name}({test_vals[2]})$: since {test_vals[2]} ≥ {split}, use second piece: {results[2]}"
            ]

        elif problem_type == 'domain_restriction':
            # Function with domain restriction
            a = random.randint(1, 5)
            b = random.randint(1, 4)
            func_name = random.choice(['f', 'g', 'h'])

            function_notation = f"{func_name}(x) = \\frac{{{a}}}{{x - {b}}}"
            test_x = b  # Test at the restriction

            problem_latex = f"For the function ${function_notation}$, what is the domain? What happens when $x = {b}$?"
            answer_latex = f"Domain: all real numbers except $x = {b}$ (undefined at $x = {b}$)"

            work_shown = [
                f"The function ${function_notation}$ has a denominator of $x - {b}$",
                f"Division by zero is undefined",
                f"When $x = {b}$: denominator = ${b} - {b} = 0$",
                f"Therefore, the domain is all real numbers except $x = {b}$",
                f"In interval notation: $(-\\infty, {b}) \\cup ({b}, \\infty)$"
            ]

        else:  # inverse
            # Find inverse function value
            a = random.choice([2, 3, 4, 5])
            b = random.randint(-5, 5)
            func_str = f"{a}x + {b}" if b >= 0 else f"{a}x - {abs(b)}"
            func_name = random.choice(['f', 'g'])

            y_val = random.choice([v for v in range(-10, 11) if (v - b) % a == 0])
            x_val = (y_val - b) // a

            function_notation = f"{func_name}(x) = {func_str}"
            problem_latex = f"If ${function_notation}$ and ${func_name}^{{-1}}({y_val})$ represents the inverse function value, find ${func_name}^{{-1}}({y_val})$"
            answer_latex = f"${func_name}^{{-1}}({y_val}) = {x_val}$"

            work_shown = [
                f"To find ${func_name}^{{-1}}({y_val})$, we need to find $x$ such that ${func_name}(x) = {y_val}$",
                f"Set up equation: ${func_str} = {y_val}$",
                f"Solve for $x$: ${a}x = {y_val - b}$",
                f"$x = {x_val}$",
                f"Therefore: ${func_name}^{{-1}}({y_val}) = {x_val}$"
            ]

        return FunctionsProblem(
            problem_type=problem_type,
            function_notation=function_notation,
            problem_latex=problem_latex,
            answer_latex=answer_latex,
            work_shown=work_shown,
            difficulty='challenge'
        )

    def generate_worksheet(self, difficulty: str, num_problems: int = 6) -> list:
        """
        Generate multiple functions problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of FunctionsProblem objects
        """
        problems = []
        # Ensure variety in problem types
        if difficulty in ['hard', 'challenge']:
            # For harder difficulties, ensure we get different problem types
            num_each_type = max(1, num_problems // 3)
            for _ in range(num_problems):
                problem = self.generate_problem(difficulty)
                problems.append(problem)
        else:
            for _ in range(num_problems):
                problem = self.generate_problem(difficulty)
                problems.append(problem)
        return problems