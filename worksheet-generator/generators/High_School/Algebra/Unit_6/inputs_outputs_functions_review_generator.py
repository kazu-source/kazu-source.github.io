"""
Inputs and Outputs + How It Relates to Functions Review Generator (Unit 6)
Reviews inputs/outputs in the context of functions
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class InputsOutputsFunctionsReviewGenerator:
    """Generates review problems connecting inputs/outputs to functions."""

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
        """Easy: Identify function notation from input/output"""
        a = random.randint(2, 5)
        b = random.randint(1, 10)
        x_val = random.randint(1, 8)
        fx_val = a * x_val + b

        latex = f"\\text{{Function: }} f(x) = {a}x + {b}. \\text{{Find }} f({x_val})"
        solution = fx_val

        steps = [
            f"f({x_val}) = {a}({x_val}) + {b}",
            f"f({x_val}) = {a * x_val} + {b}",
            f"f({x_val}) = {fx_val}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Medium: Connect input/output table to function"""
        a = random.randint(2, 4)
        b = random.randint(-5, 10)
        
        x_vals = random.sample(range(1, 10), 3)
        y_vals = [a * x + b for x in x_vals]

        latex = f"\\text{{Table shows inputs }} x \\text{{ and outputs }} y. "
        latex += f"\\text{{Pattern: }} y = {a}x + {b}. "
        latex += f"\\text{{Write as function: }} y = f(x) = \\text{{?}}"
        solution = f"{a}x + {b}"

        steps = [
            f"\\text{{Output = }} {a} \\times \\text{{input}} + {b}",
            f"f(x) = {a}x + {b}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Hard: Given function, find input for specific output"""
        a = random.randint(2, 5)
        b = random.randint(1, 10)
        fx_val = random.randint(20, 50)
        
        x_val = (fx_val - b) // a

        latex = f"\\text{{If }} f(x) = {a}x + {b} \\text{{ and }} f(x) = {fx_val}\\text{{, find }} x"
        solution = x_val

        steps = [
            f"{fx_val} = {a}x + {b}",
            f"{fx_val - b} = {a}x",
            f"x = {x_val}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Challenge: Composite functions or inverse thinking"""
        a = random.randint(2, 4)
        b = random.randint(1, 8)
        c = random.randint(2, 3)
        
        x_val = random.randint(2, 6)
        
        # f(g(x)) where g(x) = cx and f(x) = ax + b
        gx_val = c * x_val
        fgx_val = a * gx_val + b

        latex = f"\\text{{If }} f(x) = {a}x + {b} \\text{{ and }} g(x) = {c}x\\text{{, find }} f(g({x_val}))"
        solution = fgx_val

        steps = [
            f"\\text{{First find }} g({x_val}) = {c} \\times {x_val} = {gx_val}",
            f"\\text{{Then find }} f({gx_val}) = {a}({gx_val}) + {b}",
            f"f(g({x_val})) = {fgx_val}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

