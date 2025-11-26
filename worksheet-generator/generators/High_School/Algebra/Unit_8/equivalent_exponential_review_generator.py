"""
Equivalent Exponential Expressions Review Generator (Unit 8)
Reviews concepts of equivalent exponential expressions
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class EquivalentExponentialReviewGenerator:
    """Generates review problems about equivalent exponential expressions."""

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
        """Easy: Are two simple expressions equivalent?"""
        base = random.randint(2, 5)
        exp1 = random.randint(2, 4)
        exp2 = random.randint(2, 4)
        
        # Sometimes they're equal, sometimes not
        if random.choice([True, False]):
            exp2 = exp1
            latex = f"\\text{{Are }} {base}^{{{exp1}}} \\text{{ and }} {base}^{{{exp2}}} \\text{{ equivalent?}}"
            solution = "Yes"
        else:
            while exp2 == exp1:
                exp2 = random.randint(2, 4)
            latex = f"\\text{{Are }} {base}^{{{exp1}}} \\text{{ and }} {base}^{{{exp2}}} \\text{{ equivalent?}}"
            solution = "No"

        steps = [
            f"{base}^{{{exp1}}} = {base ** exp1}",
            f"{base}^{{{exp2}}} = {base ** exp2}",
            f"\\text{{Answer: }} {solution}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Medium: Simplify using exponent rules"""
        base = random.randint(2, 4)
        exp1 = random.randint(2, 4)
        exp2 = random.randint(2, 4)
        
        operation = random.choice(['multiply', 'divide'])
        
        if operation == 'multiply':
            result_exp = exp1 + exp2
            latex = f"\\text{{Simplify: }} {base}^{{{exp1}}} \\times {base}^{{{exp2}}}"
            solution = f"{base}^{{{result_exp}}}"
            
            steps = [
                f"\\text{{When multiplying same base, add exponents}}",
                f"{base}^{{{exp1}}} \\times {base}^{{{exp2}}} = {base}^{{{exp1}+{exp2}}}",
                f"= {base}^{{{result_exp}}}"
            ]
        else:  # divide
            result_exp = exp1 - exp2
            latex = f"\\text{{Simplify: }} {base}^{{{exp1}}} \\div {base}^{{{exp2}}}"
            solution = f"{base}^{{{result_exp}}}"
            
            steps = [
                f"\\text{{When dividing same base, subtract exponents}}",
                f"{base}^{{{exp1}}} \\div {base}^{{{exp2}}} = {base}^{{{exp1}-{exp2}}}",
                f"= {base}^{{{result_exp}}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Hard: Complex equivalence with power rules"""
        base = random.randint(2, 3)
        exp1 = random.randint(2, 3)
        exp2 = random.randint(2, 3)
        
        # (a^m)^n = a^(mn)
        result_exp = exp1 * exp2
        
        latex = f"\\text{{Simplify: }} ({base}^{{{exp1}}})^{{{exp2}}}"
        solution = f"{base}^{{{result_exp}}}"

        steps = [
            f"\\text{{Power of a power: multiply exponents}}",
            f"({base}^{{{exp1}}})^{{{exp2}}} = {base}^{{{exp1} \\times {exp2}}}",
            f"= {base}^{{{result_exp}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Challenge: Multiple operations"""
        base = random.randint(2, 3)
        exp1 = random.randint(2, 3)
        exp2 = random.randint(2, 3)
        exp3 = random.randint(2, 3)
        
        # Multiply then power: (a^m * a^n)^p = a^((m+n)p)
        sum_exp = exp1 + exp2
        result_exp = sum_exp * exp3
        
        latex = f"\\text{{Simplify: }} ({base}^{{{exp1}}} \\times {base}^{{{exp2}}})^{{{exp3}}}"
        solution = f"{base}^{{{result_exp}}}"

        steps = [
            f"\\text{{Step 1: Add exponents inside}}",
            f"({base}^{{{exp1}+{exp2}}})^{{{exp3}}} = ({base}^{{{sum_exp}}})^{{{exp3}}}",
            f"\\text{{Step 2: Multiply exponents}}",
            f"= {base}^{{{sum_exp} \\times {exp3}}} = {base}^{{{result_exp}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

