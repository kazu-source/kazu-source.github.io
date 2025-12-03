"""
Graphing Inequalities on Number Line Generator
Creates problems for graphing and interpreting inequalities on a number line
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class GraphingInequalitiesGenerator:
    """Generates problems for graphing inequalities on a number line."""

    def __init__(self, seed=None):
        """Initialize the graphing inequalities generator."""
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
        """Generate a single graphing inequality problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate simple inequality graphing: x > 3, x ≤ -2"""
        inequality_sign = random.choice(['<', '>', '\\leq', '\\geq'])
        value = random.randint(-5, 8)

        latex = f"\\text{{Graph on a number line: }} x {inequality_sign} {value}"

        # Determine circle type and direction
        if inequality_sign in ['<', '\\leq']:
            direction = "left"
        else:
            direction = "right"

        if inequality_sign in ['<', '>']:
            circle = "open circle"
        else:
            circle = "closed circle"

        # Interval notation
        if inequality_sign == '<':
            interval = f"(-\\infty, {value})"
        elif inequality_sign == '>':
            interval = f"({value}, \\infty)"
        elif inequality_sign == '\\leq':
            interval = f"(-\\infty, {value}]"
        else:  # ≥
            interval = f"[{value}, \\infty)"

        solution = f"{circle} at {value}, arrow {direction}"

        steps = [
            f"\\text{{Place {circle} at }} x = {value}",
            f"\\text{{Draw arrow pointing {direction}}}",
            f"\\text{{Interval notation: }} {interval}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate compound inequalities: 2 < x < 5 or x ≤ -1 or x > 3"""
        problem_type = random.choice(['and', 'or'])

        if problem_type == 'and':
            # Compound inequality: a < x < b
            a = random.randint(-5, 2)
            b = random.randint(a + 3, a + 8)

            # Vary the inequality signs
            left_sign = random.choice(['<', '\\leq'])
            right_sign = random.choice(['<', '\\leq'])

            latex = f"\\text{{Graph on a number line: }} {a} {left_sign} x {right_sign} {b}"

            # Determine circle types
            left_circle = "closed circle" if left_sign == '\\leq' else "open circle"
            right_circle = "closed circle" if right_sign == '\\leq' else "open circle"

            # Interval notation
            left_bracket = "[" if left_sign == '\\leq' else "("
            right_bracket = "]" if right_sign == '\\leq' else ")"
            interval = f"{left_bracket}{a}, {b}{right_bracket}"

            solution = f"{left_circle} at {a}, {right_circle} at {b}, line between"

            steps = [
                f"\\text{{Place {left_circle} at }} x = {a}",
                f"\\text{{Place {right_circle} at }} x = {b}",
                f"\\text{{Draw line segment connecting them}}",
                f"\\text{{Interval notation: }} {interval}"
            ]

        else:  # or
            # Disjoint inequality: x ≤ a or x > b
            a = random.randint(-5, 0)
            b = random.randint(2, 6)

            left_sign = random.choice(['<', '\\leq'])
            right_sign = random.choice(['>', '\\geq'])

            latex = f"\\text{{Graph on a number line: }} x {left_sign} {a} \\text{{ or }} x {right_sign} {b}"

            # Determine circle types and directions
            left_circle = "closed circle" if left_sign == '\\leq' else "open circle"
            right_circle = "closed circle" if right_sign == '\\geq' else "open circle"

            # Interval notation
            left_bracket = "]" if left_sign == '\\leq' else ")"
            right_bracket = "[" if right_sign == '\\geq' else "("
            interval = f"(-\\infty, {a}{left_bracket} \\cup {right_bracket}{b}, \\infty)"

            solution = f"{left_circle} at {a} (arrow left), {right_circle} at {b} (arrow right)"

            steps = [
                f"\\text{{Place {left_circle} at }} x = {a}, \\text{{arrow left}}",
                f"\\text{{Place {right_circle} at }} x = {b}, \\text{{arrow right}}",
                f"\\text{{Two separate rays}}",
                f"\\text{{Interval notation: }} {interval}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Determine inequality from a graph description"""
        problem_type = random.choice(['simple', 'compound'])

        if problem_type == 'simple':
            value = random.randint(-5, 8)
            circle_type = random.choice(['open', 'closed'])
            direction = random.choice(['left', 'right'])

            circle_desc = "open circle" if circle_type == 'open' else "closed circle"

            latex = f"\\text{{Write the inequality: {circle_desc} at }} {value} \\text{{, arrow pointing {direction}}}"

            if direction == 'left':
                if circle_type == 'open':
                    solution = f"x < {value}"
                else:
                    solution = f"x \\leq {value}"
            else:  # right
                if circle_type == 'open':
                    solution = f"x > {value}"
                else:
                    solution = f"x \\geq {value}"

            steps = [
                f"\\text{{{circle_desc} means }} {'<' if circle_type == 'open' else '\\leq'} \\text{{ or }} {'>' if circle_type == 'open' else '\\geq'}",
                f"\\text{{Arrow {direction} means }} {'x <' if direction == 'left' else 'x >'} \\text{{ region}}",
                f"\\text{{Inequality: }} {solution}"
            ]

        else:  # compound
            a = random.randint(-5, 2)
            b = random.randint(a + 3, a + 8)

            left_type = random.choice(['open', 'closed'])
            right_type = random.choice(['open', 'closed'])

            left_desc = "open circle" if left_type == 'open' else "closed circle"
            right_desc = "open circle" if right_type == 'open' else "closed circle"

            latex = f"\\text{{Write the inequality: {left_desc} at }} {a}, \\text{{ {right_desc} at }} {b}, \\text{{ line between}}"

            left_sign = "<" if left_type == 'open' else "\\leq"
            right_sign = "<" if right_type == 'open' else "\\leq"

            solution = f"{a} {left_sign} x {right_sign} {b}"

            steps = [
                f"\\text{{Line between points means 'and' compound inequality}}",
                f"\\text{{{left_desc} at {a} means }} {left_sign}",
                f"\\text{{{right_desc} at {b} means }} {right_sign}",
                f"\\text{{Inequality: }} {solution}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Graph solutions to inequalities after solving"""
        problem_type = random.choice(['one_step', 'two_step', 'negative_coef'])

        if problem_type == 'one_step':
            # x + a < b
            a = random.randint(1, 10)
            b = random.randint(5, 20)
            x_value = b - a
            inequality_sign = random.choice(['<', '>', '\\leq', '\\geq'])

            if random.choice([True, False]):
                latex = f"\\text{{Solve and graph: }} x + {a} {inequality_sign} {b}"
                solution_ineq = f"x {inequality_sign} {x_value}"
            else:
                latex = f"\\text{{Solve and graph: }} x - {a} {inequality_sign} {b}"
                x_value = b + a
                solution_ineq = f"x {inequality_sign} {x_value}"

            # Graph description
            if inequality_sign in ['<', '>']:
                circle = "open circle"
            else:
                circle = "closed circle"

            if inequality_sign in ['<', '\\leq']:
                direction = "left"
            else:
                direction = "right"

            solution = f"{solution_ineq}; {circle} at {x_value}, arrow {direction}"

            steps = [
                f"\\text{{Solve: }} {solution_ineq}",
                f"\\text{{Graph: {circle} at }} {x_value}",
                f"\\text{{Arrow pointing {direction}}}"
            ]

        elif problem_type == 'two_step':
            # ax + b < c
            a = random.randint(2, 5)
            b = random.randint(1, 8)
            x_value = random.randint(1, 10)
            c = a * x_value + b
            inequality_sign = random.choice(['<', '>', '\\leq', '\\geq'])

            latex = f"\\text{{Solve and graph: }} {a}x + {b} {inequality_sign} {c}"
            solution_ineq = f"x {inequality_sign} {x_value}"

            # Graph description
            if inequality_sign in ['<', '>']:
                circle = "open circle"
            else:
                circle = "closed circle"

            if inequality_sign in ['<', '\\leq']:
                direction = "left"
            else:
                direction = "right"

            solution = f"{solution_ineq}; {circle} at {x_value}, arrow {direction}"

            steps = [
                f"\\text{{Subtract {b}: }} {a}x {inequality_sign} {c - b}",
                f"\\text{{Divide by {a}: }} {solution_ineq}",
                f"\\text{{Graph: {circle} at }} {x_value}, \\text{{arrow {direction}}}"
            ]

        else:  # negative_coef
            # -ax + b < c (flip sign when dividing)
            a = random.randint(2, 5)
            b = random.randint(10, 20)
            x_value = random.randint(1, 8)
            c = -a * x_value + b
            inequality_sign = random.choice(['<', '>', '\\leq', '\\geq'])

            latex = f"\\text{{Solve and graph: }} -{a}x + {b} {inequality_sign} {c}"

            # Flip inequality when dividing by negative
            flipped_sign = {
                '<': '>',
                '>': '<',
                '\\leq': '\\geq',
                '\\geq': '\\leq'
            }[inequality_sign]

            solution_ineq = f"x {flipped_sign} {x_value}"

            # Graph description
            if flipped_sign in ['<', '>']:
                circle = "open circle"
            else:
                circle = "closed circle"

            if flipped_sign in ['<', '\\leq']:
                direction = "left"
            else:
                direction = "right"

            solution = f"{solution_ineq}; {circle} at {x_value}, arrow {direction}"

            steps = [
                f"\\text{{Subtract {b}: }} -{a}x {inequality_sign} {c - b}",
                f"\\text{{Divide by }}-{a}\\text{{ (flip sign): }} {solution_ineq}",
                f"\\text{{Graph: {circle} at }} {x_value}, \\text{{arrow {direction}}}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = GraphingInequalitiesGenerator()

    print("GRAPHING INEQUALITIES ON NUMBER LINE GENERATOR TEST")
    print("=" * 70)

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        print("-" * 70)
        for i, problem in enumerate(generator.generate_worksheet(diff, 3), 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}")
            if problem.steps:
                print(f"   Steps:")
                for step in problem.steps:
                    print(f"     - {step}")
            print()


if __name__ == '__main__':
    main()
