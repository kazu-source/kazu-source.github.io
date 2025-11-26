"""
Inputs and Outputs Review Generator (Unit 4)
Reviews the concept of inputs and outputs in preparation for coordinate plane work
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class InputsOutputsReviewGenerator:
    """Generates review problems about inputs and outputs."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """Generate worksheet problems."""
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
        """Generate easy: Identify inputs and outputs from rules"""
        problem_type = random.choice(['simple_rule', 'table', 'word_rule'])

        if problem_type == 'simple_rule':
            # Given input, find output
            a = random.randint(2, 5)
            b = random.randint(1, 10)
            input_val = random.randint(1, 8)
            output_val = a * input_val + b

            latex = f"\\text{{Rule: output = }} {a} \\times \\text{{input}} + {b}. "
            latex += f"\\text{{If input = }} {input_val}\\text{{, what is output?}}"
            solution = output_val

            steps = [
                f"\\text{{output}} = {a} \\times {input_val} + {b}",
                f"\\text{{output}} = {a * input_val} + {b}",
                f"\\text{{output}} = {output_val}"
            ]

        elif problem_type == 'table':
            # Complete the table
            a = random.randint(2, 4)
            inputs = [1, 2, 3]
            outputs = [a * i for i in inputs]
            missing_input = 4
            missing_output = a * missing_input

            latex = f"\\text{{Table: Input }} \\to \\text{{ Output}}. \\text{{Pattern: multiply by }} {a}. "
            latex += f"\\text{{If input = }} {missing_input}\\text{{, output = ?}}"
            solution = missing_output

            steps = [
                f"\\text{{Pattern: output = }} {a} \\times \\text{{input}}",
                f"\\text{{output}} = {a} \\times {missing_input} = {missing_output}"
            ]

        else:  # word_rule
            # Word description
            per_item = random.randint(3, 8)
            items = random.randint(5, 10)
            total = per_item * items

            latex = f"\\text{{Cost is }} \\${per_item} \\text{{ per item. Input: number of items. "
            latex += f"\\text{{If input = }} {items}\\text{{, what is output (total cost)?}}"
            solution = total

            steps = [
                f"\\text{{Output = }} {per_item} \\times \\text{{input}}",
                f"\\text{{Output = }} {per_item} \\times {items} = \\${total}"
            ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium: Work backwards from output to input"""
        a = random.randint(2, 6)
        b = random.randint(1, 10)
        output_val = random.randint(20, 50)
        
        # Solve for input: output = a * input + b
        # input = (output - b) / a
        input_val = (output_val - b) // a

        latex = f"\\text{{Rule: output = }} {a} \\times \\text{{input}} + {b}. "
        latex += f"\\text{{If output = }} {output_val}\\text{{, what was input?}}"
        solution = input_val

        steps = [
            f"{output_val} = {a} \\times \\text{{input}} + {b}",
            f"{output_val - b} = {a} \\times \\text{{input}}",
            f"\\text{{input}} = \\frac{{{output_val - b}}}{{{a}}} = {input_val}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard: Multiple steps or patterns"""
        a = random.randint(2, 4)
        b = random.randint(1, 8)
        c = random.randint(2, 5)
        
        # Two-step rule
        input_val = random.randint(3, 8)
        intermediate = a * input_val + b
        output_val = intermediate * c

        latex = f"\\text{{Rule: multiply input by }} {a}\\text{{, add }} {b}\\text{{, then multiply by }} {c}. "
        latex += f"\\text{{If input = }} {input_val}\\text{{, what is output?}}"
        solution = output_val

        steps = [
            f"\\text{{Step 1: }} {a} \\times {input_val} + {b} = {intermediate}",
            f"\\text{{Step 2: }} {intermediate} \\times {c} = {output_val}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge: Complex relationships"""
        # Function with multiple operations
        input_val = random.randint(5, 12)
        a = random.randint(2, 4)
        b = random.randint(3, 8)
        
        # Rule: (input * a) - b, then square
        intermediate = input_val * a - b
        output_val = intermediate ** 2

        latex = f"\\text{{Rule: multiply input by }} {a}\\text{{, subtract }} {b}\\text{{, then square the result. "
        latex += f"\\text{{If input = }} {input_val}\\text{{, what is output?}}"
        solution = output_val

        steps = [
            f"\\text{{Step 1: }} {input_val} \\times {a} - {b} = {intermediate}",
            f"\\text{{Step 2: }} ({intermediate})^2 = {output_val}"
        ]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )

