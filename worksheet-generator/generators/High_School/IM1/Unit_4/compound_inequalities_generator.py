"""
Compound Inequalities Generator
Creates problems about AND/OR compound inequalities
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class CompoundInequalitiesGenerator:
    """Generates compound inequality problems."""

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
        """Graph or identify simple compound inequalities"""
        a = random.randint(-5, 3)
        b = random.randint(a + 2, 8)

        compound_type = random.choice(['and', 'or'])

        if compound_type == 'and':
            latex = f"\\text{{Write the compound inequality: }} x \\text{{ is greater than }} {a} \\text{{ AND less than }} {b}"
            solution = f"{a} < x < {b}"
            steps = [
                f"x > {a} \\text{{ AND }} x < {b}",
                f"\\text{{Combined: }} {a} < x < {b}"
            ]
        else:
            latex = f"\\text{{Write the compound inequality: }} x \\text{{ is less than }} {a} \\text{{ OR greater than }} {b}"
            solution = f"x < {a} \\text{{ or }} x > {b}"
            steps = [
                f"x < {a} \\text{{ OR }} x > {b}",
                f"\\text{{This is a disjunction (OR)}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Solve simple compound inequalities"""
        compound_type = random.choice(['and', 'or'])

        if compound_type == 'and':
            # a < x + c < b
            c = random.randint(-5, 5)
            low = random.randint(-8, 0)
            high = random.randint(low + 3, 8)

            result_low = low - c
            result_high = high - c

            if c >= 0:
                latex = f"\\text{{Solve: }} {low} < x + {c} < {high}"
            else:
                latex = f"\\text{{Solve: }} {low} < x - {abs(c)} < {high}"

            solution = f"{result_low} < x < {result_high}"

            steps = [
                f"\\text{{Subtract }} {c} \\text{{ from all parts:}}",
                f"{low} - {c} < x < {high} - {c}",
                f"{result_low} < x < {result_high}"
            ]
        else:
            # x + a < b OR x + a > c
            a = random.randint(1, 5)
            b = random.randint(-5, 0)
            c = random.randint(5, 10)

            sol_b = b - a
            sol_c = c - a

            latex = f"\\text{{Solve: }} x + {a} < {b} \\text{{ OR }} x + {a} > {c}"
            solution = f"x < {sol_b} \\text{{ or }} x > {sol_c}"

            steps = [
                f"\\text{{Solve each inequality separately:}}",
                f"x + {a} < {b} \\Rightarrow x < {sol_b}",
                f"x + {a} > {c} \\Rightarrow x > {sol_c}",
                f"\\text{{Solution: }} x < {sol_b} \\text{{ or }} x > {sol_c}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Multi-step compound inequalities"""
        compound_type = random.choice(['and', 'or'])

        if compound_type == 'and':
            # a < bx + c < d
            b = random.randint(2, 4)
            c = random.randint(-8, 8)

            # Choose result bounds first for clean answers
            result_low = random.randint(-5, 0)
            result_high = random.randint(result_low + 2, 5)

            # Calculate original bounds
            low = b * result_low + c
            high = b * result_high + c

            if c >= 0:
                latex = f"\\text{{Solve: }} {low} < {b}x + {c} < {high}"
            else:
                latex = f"\\text{{Solve: }} {low} < {b}x - {abs(c)} < {high}"

            solution = f"{result_low} < x < {result_high}"

            steps = [
                f"\\text{{Subtract }} {c} \\text{{ from all parts:}}",
                f"{low - c} < {b}x < {high - c}",
                f"\\text{{Divide all parts by }} {b}:",
                f"{result_low} < x < {result_high}"
            ]
        else:
            # ax + b <= c OR ax + b >= d
            a = random.randint(2, 4)
            b = random.randint(-5, 5)

            result_c = random.randint(-5, 0)
            result_d = random.randint(3, 8)

            c = a * result_c + b
            d = a * result_d + b

            b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"

            latex = f"\\text{{Solve: }} {a}x {b_str} \\leq {c} \\text{{ OR }} {a}x {b_str} \\geq {d}"
            solution = f"x \\leq {result_c} \\text{{ or }} x \\geq {result_d}"

            steps = [
                f"\\text{{Solve each:}}",
                f"{a}x {b_str} \\leq {c} \\Rightarrow {a}x \\leq {c - b} \\Rightarrow x \\leq {result_c}",
                f"{a}x {b_str} \\geq {d} \\Rightarrow {a}x \\geq {d - b} \\Rightarrow x \\geq {result_d}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Special cases or word problems"""
        problem_type = random.choice(['no_solution', 'all_reals', 'word_problem'])

        if problem_type == 'no_solution':
            # AND inequality with no overlap
            a = random.randint(5, 10)
            b = random.randint(-5, 0)

            latex = f"\\text{{Solve: }} x > {a} \\text{{ AND }} x < {b}"
            solution = "\\text{No solution}"

            steps = [
                f"\\text{{For AND, we need the intersection}}",
                f"\\text{{There are no numbers that are both > }} {a} \\text{{ AND < }} {b}",
                f"\\text{{No solution (empty set)}}"
            ]

        elif problem_type == 'all_reals':
            # OR inequality that covers everything
            a = random.randint(-3, 3)
            b = random.randint(-3, 3)
            while b < a:
                b = random.randint(-3, 3)

            latex = f"\\text{{Solve: }} x \\leq {b} \\text{{ OR }} x \\geq {a}"
            solution = "\\text{All real numbers}"

            steps = [
                f"\\text{{For OR, we need the union}}",
                f"\\text{{Every number is either }} \\leq {b} \\text{{ or }} \\geq {a}",
                f"\\text{{Since }} {a} \\leq {b}, \\text{{ the union is all real numbers}}"
            ]

        else:
            # Word problem
            low = random.randint(60, 70)
            high = random.randint(85, 95)

            latex = f"\\text{{A healthy body temperature is between }} {low}°F \\text{{ and }} {high}°F. \\text{{ Write this as a compound inequality using }} T."
            solution = f"{low} \\leq T \\leq {high}"

            steps = [
                f"\\text{{\"Between\" suggests AND (intersection)}}",
                f"T \\geq {low} \\text{{ AND }} T \\leq {high}",
                f"\\text{{Combined: }} {low} \\leq T \\leq {high}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = CompoundInequalitiesGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
