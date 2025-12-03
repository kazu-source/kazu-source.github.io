"""
Exponential Growth and Decay Generator
Creates problems about exponential growth and decay applications
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class ExponentialGrowthDecayGenerator:
    """Generates exponential growth and decay problems."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Identify growth vs decay from equation"""
        a = random.randint(50, 500)

        growth_type = random.choice(['growth', 'decay'])

        if growth_type == 'growth':
            b = round(random.uniform(1.05, 1.5), 2)
            answer = "Growth"
            reason = f"b = {b} > 1"
        else:
            b = round(random.uniform(0.5, 0.95), 2)
            answer = "Decay"
            reason = f"b = {b} < 1"

        latex = f"\\text{{Is }} y = {a}({b})^x \\text{{ growth or decay?}}"
        solution = answer

        steps = [
            f"\\text{{In }} y = a \\cdot b^x:",
            f"\\text{{Growth if }} b > 1, \\text{{ Decay if }} 0 < b < 1",
            f"\\text{{Here, }} {reason}, \\text{{ so this is {answer.lower()}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Calculate value after given time periods"""
        problem_type = random.choice(['growth', 'decay'])

        if problem_type == 'growth':
            initial = random.randint(100, 1000)
            rate = random.choice([0.05, 0.1, 0.2])
            rate_percent = int(rate * 100)
            time = random.randint(2, 4)

            b = 1 + rate
            final = initial * (b ** time)

            latex = f"\\text{{A population of {initial} grows by {rate_percent}% per year. What is the population after {time} years?}}"
            solution = f"{final:.0f}"

            steps = [
                f"\\text{{Formula: }} P = P_0(1 + r)^t",
                f"P = {initial}(1 + {rate})^{time}",
                f"P = {initial}({b})^{time}",
                f"P = {initial} \\times {b**time:.4f}",
                f"P \\approx {final:.0f}"
            ]
        else:
            initial = random.randint(500, 2000)
            rate = random.choice([0.1, 0.15, 0.2])
            rate_percent = int(rate * 100)
            time = random.randint(2, 4)

            b = 1 - rate
            final = initial * (b ** time)

            latex = f"\\text{{A car worth $}} {initial} \\text{{ depreciates by {rate_percent}% per year. What is its value after {time} years?}}"
            solution = f"\\${final:.0f}"

            steps = [
                f"\\text{{Formula: }} V = V_0(1 - r)^t",
                f"V = {initial}(1 - {rate})^{time}",
                f"V = {initial}({b})^{time}",
                f"V = {initial} \\times {b**time:.4f}",
                f"V \\approx \\${final:.0f}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Write equations from context or find rate"""
        problem_type = random.choice(['write_equation', 'find_rate'])

        if problem_type == 'write_equation':
            initial = random.randint(200, 1000)
            rate = random.choice([0.05, 0.08, 0.1, 0.12])
            rate_percent = int(rate * 100)
            growth = random.choice([True, False])

            if growth:
                b = 1 + rate
                context = f"bacteria colony starts at {initial} and grows {rate_percent}% per hour"
            else:
                b = 1 - rate
                context = f"medicine starts at {initial}mg and decreases by {rate_percent}% per hour"

            latex = f"\\text{{A {context}. Write the equation for the amount after }} t \\text{{ hours.}}"
            solution = f"A = {initial}({b})^t"

            steps = [
                f"\\text{{Initial amount: }} a = {initial}",
                f"\\text{{Growth/decay factor: }} b = {b}",
                f"\\text{{Equation: }} A = {initial}({b})^t"
            ]
        else:
            # Find rate given two values
            initial = random.randint(100, 500)
            rate = random.choice([0.1, 0.2, 0.25])
            time = 2

            b = 1 + rate
            final = initial * (b ** time)

            latex = f"\\text{{A population grew from {initial} to {final:.0f} in {time} years. What is the annual growth rate?}}"
            solution = f"{int(rate * 100)}\\%"

            steps = [
                f"\\text{{Use: }} {final:.0f} = {initial} \\cdot b^{time}",
                f"b^{time} = \\frac{{{final:.0f}}}{{{initial}}} = {b**time}",
                f"b = \\sqrt[{time}]{{{b**time}}} = {b}",
                f"r = b - 1 = {b} - 1 = {rate} = {int(rate*100)}\\%"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Half-life, doubling time, or compound interest"""
        problem_type = random.choice(['half_life', 'doubling', 'compound'])

        if problem_type == 'half_life':
            initial = random.randint(100, 500)
            half_life = random.choice([2, 4, 5, 10])
            time = half_life * random.randint(2, 4)

            periods = time // half_life
            final = initial / (2 ** periods)

            latex = f"\\text{{A substance has a half-life of {half_life} years. If you start with {initial}g, how much remains after {time} years?}}"
            solution = f"{final:.2f}g"

            steps = [
                f"\\text{{Number of half-lives: }} \\frac{{{time}}}{{{half_life}}} = {periods}",
                f"\\text{{Formula: }} A = A_0 \\cdot \\left(\\frac{{1}}{{2}}\\right)^n",
                f"A = {initial} \\cdot \\left(\\frac{{1}}{{2}}\\right)^{periods}",
                f"A = {initial} \\cdot \\frac{{1}}{{{2**periods}}} = {final:.2f}g"
            ]

        elif problem_type == 'doubling':
            initial = random.randint(50, 200)
            double_time = random.choice([3, 4, 5, 6])
            time = double_time * random.randint(2, 3)

            periods = time // double_time
            final = initial * (2 ** periods)

            latex = f"\\text{{A population doubles every {double_time} years. Starting at {initial}, what is the population after {time} years?}}"
            solution = str(int(final))

            steps = [
                f"\\text{{Number of doublings: }} \\frac{{{time}}}{{{double_time}}} = {periods}",
                f"\\text{{Formula: }} P = P_0 \\cdot 2^n",
                f"P = {initial} \\cdot 2^{periods}",
                f"P = {initial} \\cdot {2**periods} = {int(final)}"
            ]

        else:
            # Compound interest
            principal = random.randint(5, 20) * 100
            rate = random.choice([0.05, 0.06, 0.08])
            rate_percent = int(rate * 100)
            time = random.randint(2, 4)
            n = random.choice([1, 4, 12])
            n_name = {1: "annually", 4: "quarterly", 12: "monthly"}[n]

            amount = principal * ((1 + rate/n) ** (n * time))

            latex = f"\\text{{$}} {principal} \\text{{ invested at {rate_percent}% compounded {n_name} for {time} years. Find the final amount.}}"
            solution = f"\\${amount:.2f}"

            steps = [
                f"\\text{{Formula: }} A = P\\left(1 + \\frac{{r}}{{n}}\\right)^{{nt}}",
                f"A = {principal}\\left(1 + \\frac{{{rate}}}{{{n}}}\\right)^{{{n} \\cdot {time}}}",
                f"A = {principal}\\left({1 + rate/n:.4f}\\right)^{{{n * time}}}",
                f"A = {principal} \\times {((1 + rate/n) ** (n * time)):.4f}",
                f"A \\approx \\${amount:.2f}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = ExponentialGrowthDecayGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
