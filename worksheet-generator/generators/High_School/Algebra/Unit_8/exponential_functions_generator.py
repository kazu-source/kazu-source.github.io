"""
Exponential Functions Generator - Unit 8
Generates problems about exponential functions, including writing and evaluating
"""

import random
from dataclasses import dataclass
from typing import List, Tuple, Dict


@dataclass
class ExponentialFunctionProblem:
    """Represents an exponential function problem."""
    latex: str  # LaTeX formatted problem
    solution: str  # The answer
    difficulty: str
    problem_type: str  # Type of exponential problem
    table_data: Dict = None  # Optional table data for graphing problems


class ExponentialFunctionsGenerator:
    """Generates problems about exponential functions."""

    def __init__(self, seed=None):
        """Initialize the exponential functions generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[ExponentialFunctionProblem]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of ExponentialFunctionProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> ExponentialFunctionProblem:
        """Generate a single exponential function problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> ExponentialFunctionProblem:
        """Generate easy exponential function problems (basic evaluation, simple growth)."""
        problem_type = random.choice(['evaluate_function', 'identify_base', 'simple_table'])

        if problem_type == 'evaluate_function':
            # Evaluate f(x) = 2^x at specific points
            base = random.choice([2, 3, 4, 5])
            x_val = random.randint(0, 4)
            result = base ** x_val
            latex = f"\\text{{Evaluate: }} f(x) = {base}^x \\text{{ when }} x = {x_val}"
            solution = str(result)

        elif problem_type == 'identify_base':
            # Given points, identify the base
            base = random.choice([2, 3, 4, 5])
            x1, x2 = 1, 2
            y1, y2 = base, base**2
            latex = f"\\text{{Find the base b if }} f(x) = b^x \\text{{ passes through }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})"
            solution = str(base)

        else:  # simple_table
            # Create a table of values for f(x) = 2^x
            base = random.choice([2, 3])
            x_values = list(range(0, 5))
            y_values = [base**x for x in x_values]
            table_str = "x: " + " | ".join(map(str, x_values)) + "\\n"
            table_str += "y: " + " | ".join(map(str, y_values))
            latex = f"\\text{{Complete the table for }} f(x) = {base}^x"
            solution = table_str
            table_data = {"x": x_values, "y": y_values, "function": f"f(x) = {base}^x"}

            return ExponentialFunctionProblem(
                latex=latex,
                solution=solution,
                difficulty='easy',
                problem_type=problem_type,
                table_data=table_data
            )

        return ExponentialFunctionProblem(
            latex=latex,
            solution=solution,
            difficulty='easy',
            problem_type=problem_type
        )

    def _generate_medium(self) -> ExponentialFunctionProblem:
        """Generate medium exponential function problems (coefficients, transformations)."""
        problem_type = random.choice(['with_coefficient', 'find_equation', 'compare_growth'])

        if problem_type == 'with_coefficient':
            # f(x) = a * b^x
            a = random.randint(2, 5)
            b = random.choice([2, 3, 4])
            x = random.randint(1, 3)
            result = a * (b ** x)
            latex = f"\\text{{Evaluate: }} f(x) = {a} \\cdot {b}^x \\text{{ when }} x = {x}"
            solution = str(result)

        elif problem_type == 'find_equation':
            # Find exponential equation from two points
            a = random.randint(2, 4)
            b = random.choice([2, 3])
            x1, x2 = 0, 2
            y1 = a
            y2 = a * (b ** 2)
            latex = f"\\text{{Find }} f(x) = a \\cdot b^x \\text{{ passing through }} ({x1}, {y1}) \\text{{ and }} ({x2}, {y2})"
            solution = f"f(x) = {a} \\cdot {b}^x"

        else:  # compare_growth
            # Compare linear vs exponential
            linear_m = random.randint(2, 5)
            exp_base = 2
            x = random.randint(4, 6)
            linear_val = linear_m * x
            exp_val = exp_base ** x
            latex = f"\\text{{Compare at }} x = {x}: \\text{{ Linear: }} f(x) = {linear_m}x \\text{{ vs Exponential: }} g(x) = {exp_base}^x"
            solution = f"Linear: {linear_val}, Exponential: {exp_val}"

        return ExponentialFunctionProblem(
            latex=latex,
            solution=solution,
            difficulty='medium',
            problem_type=problem_type
        )

    def _generate_hard(self) -> ExponentialFunctionProblem:
        """Generate hard exponential function problems (word problems, growth/decay)."""
        problem_type = random.choice(['growth_problem', 'decay_problem', 'find_time'])

        if problem_type == 'growth_problem':
            # Population growth problem
            initial = random.choice([100, 200, 500, 1000])
            rate = random.choice([1.05, 1.1, 1.15, 1.2])  # 5%, 10%, 15%, 20% growth
            years = random.randint(2, 5)
            final = initial * (rate ** years)
            rate_percent = int((rate - 1) * 100)
            latex = f"\\text{{A population of {initial} grows at {rate_percent}\\% per year. Find the population after {years} years.}}"
            solution = f"{final:.0f}"

        elif problem_type == 'decay_problem':
            # Radioactive decay problem
            initial = random.choice([100, 200, 400, 800])
            half_life = random.randint(2, 5)
            time = half_life * random.randint(1, 3)
            num_half_lives = time / half_life
            final = initial * (0.5 ** num_half_lives)
            latex = f"\\text{{A substance has {initial}g initially with half-life of {half_life} years. How much remains after {time} years?}}"
            solution = f"{final:.1f}g"

        else:  # find_time
            # Find when population doubles
            initial = random.choice([100, 200, 500])
            rate = random.choice([1.1, 1.15, 1.2])  # 10%, 15%, 20% growth
            target = initial * 2
            # Solve: initial * rate^t = target
            # t = log(2) / log(rate)
            import math
            time = math.log(2) / math.log(rate)
            latex = f"\\text{{Population starts at {initial} and grows at {int((rate-1)*100)}\\% per year. When will it double?}}"
            solution = f"{time:.1f} years"

        return ExponentialFunctionProblem(
            latex=latex,
            solution=solution,
            difficulty='hard',
            problem_type=problem_type
        )

    def _generate_challenge(self) -> ExponentialFunctionProblem:
        """Generate challenge exponential function problems (complex modeling, compound interest)."""
        problem_type = random.choice(['compound_interest', 'continuous_growth', 'compare_models'])

        if problem_type == 'compound_interest':
            # Compound interest with different compounding periods
            principal = random.choice([1000, 2000, 5000])
            rate = random.choice([0.04, 0.05, 0.06])  # 4%, 5%, 6%
            time = random.randint(3, 10)
            n = random.choice([1, 4, 12])  # Annually, quarterly, monthly
            compound_names = {1: "annually", 4: "quarterly", 12: "monthly"}
            amount = principal * ((1 + rate/n) ** (n * time))
            latex = f"\\text{{\\${principal} invested at {int(rate*100)}\\% compounded {compound_names[n]} for {time} years. Find the amount.}}"
            solution = f"\\${amount:.2f}"

        elif problem_type == 'continuous_growth':
            # Continuous exponential growth A = Pe^(rt)
            principal = random.choice([1000, 2000, 3000])
            rate = random.choice([0.03, 0.04, 0.05])
            time = random.randint(5, 15)
            import math
            amount = principal * math.exp(rate * time)
            latex = f"\\text{{\\${principal} grows continuously at {int(rate*100)}\\% for {time} years. Find the amount.}}"
            solution = f"\\${amount:.2f}"

        else:  # compare_models
            # Compare two exponential models
            model1_init = random.choice([100, 200])
            model1_rate = random.choice([1.1, 1.15])
            model2_init = random.choice([150, 250])
            model2_rate = random.choice([1.05, 1.08])
            time = random.randint(5, 10)

            val1 = model1_init * (model1_rate ** time)
            val2 = model2_init * (model2_rate ** time)

            latex = f"\\text{{Model A: {model1_init}({model1_rate})^t, Model B: {model2_init}({model2_rate})^t. Compare at t = {time}}}"
            solution = f"Model A: {val1:.0f}, Model B: {val2:.0f}"

        return ExponentialFunctionProblem(
            latex=latex,
            solution=solution,
            difficulty='challenge',
            problem_type=problem_type
        )


if __name__ == "__main__":
    # Test the generator
    gen = ExponentialFunctionsGenerator()

    print("Testing Exponential Functions Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=5)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Answer: {problem.solution}")
            print(f"   Type: {problem.problem_type}")
            if problem.table_data:
                print(f"   Table data: {problem.table_data}")