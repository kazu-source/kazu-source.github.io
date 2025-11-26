"""
Literal Equations Generator - Solving for specific variables
Generates problems where students solve for a specific variable in an equation
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class LiteralEquationsGenerator:
    """Generates literal equation problems."""

    def __init__(self, seed=None):
        """Initialize the literal equations generator."""
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
        """Generate a single literal equation problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate simple literal equation: solve for one variable"""
        formulas = [
            ("d = rt", "r", "r = \\frac{d}{t}"),
            ("d = rt", "t", "t = \\frac{d}{r}"),
            ("A = lw", "l", "l = \\frac{A}{w}"),
            ("A = lw", "w", "w = \\frac{A}{l}"),
            ("C = 2\\pi r", "r", "r = \\frac{C}{2\\pi}"),
            ("V = lwh", "h", "h = \\frac{V}{lw}"),
        ]

        formula, solve_for, solution = random.choice(formulas)
        latex = f"\\text{{Solve for }} {solve_for}: {formula}"

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate literal equation with addition/subtraction"""
        formulas = [
            ("y = mx + b", "x", "x = \\frac{y - b}{m}"),
            ("y = mx + b", "m", "m = \\frac{y - b}{x}"),
            ("y = mx + b", "b", "b = y - mx"),
            ("A = \\frac{1}{2}bh", "b", "b = \\frac{2A}{h}"),
            ("A = \\frac{1}{2}bh", "h", "h = \\frac{2A}{b}"),
            ("P = 2l + 2w", "l", "l = \\frac{P - 2w}{2}"),
            ("P = 2l + 2w", "w", "w = \\frac{P - 2l}{2}"),
        ]

        formula, solve_for, solution = random.choice(formulas)
        latex = f"\\text{{Solve for }} {solve_for}: {formula}"

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate literal equation with multiple operations"""
        formulas = [
            ("F = \\frac{9}{5}C + 32", "C", "C = \\frac{5(F - 32)}{9}"),
            ("A = P(1 + rt)", "r", "r = \\frac{A - P}{Pt}"),
            ("A = P(1 + rt)", "t", "t = \\frac{A - P}{Pr}"),
            ("ax + by = c", "x", "x = \\frac{c - by}{a}"),
            ("ax + by = c", "y", "y = \\frac{c - ax}{b}"),
            ("s = \\frac{1}{2}at^2", "a", "a = \\frac{2s}{t^2}"),
            ("s = \\frac{1}{2}at^2", "t", "t = \\sqrt{\\frac{2s}{a}}"),
        ]

        formula, solve_for, solution = random.choice(formulas)
        latex = f"\\text{{Solve for }} {solve_for}: {formula}"

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate complex literal equations"""
        formulas = [
            ("\\frac{1}{f} = \\frac{1}{d_o} + \\frac{1}{d_i}", "f",
             "f = \\frac{d_o d_i}{d_o + d_i}"),
            ("\\frac{1}{f} = \\frac{1}{d_o} + \\frac{1}{d_i}", "d_o",
             "d_o = \\frac{fd_i}{d_i - f}"),
            ("v^2 = u^2 + 2as", "s", "s = \\frac{v^2 - u^2}{2a}"),
            ("v^2 = u^2 + 2as", "a", "a = \\frac{v^2 - u^2}{2s}"),
            ("v^2 = u^2 + 2as", "u", "u = \\sqrt{v^2 - 2as}"),
            ("\\frac{x - h}{a} = \\frac{y - k}{b}", "y", "y = \\frac{b(x - h)}{a} + k"),
            ("\\frac{x - h}{a} = \\frac{y - k}{b}", "x", "x = \\frac{a(y - k)}{b} + h"),
        ]

        formula, solve_for, solution = random.choice(formulas)
        latex = f"\\text{{Solve for }} {solve_for}: {formula}"

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = LiteralEquationsGenerator()

    print("Testing Literal Equations Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}\n")