"""
Inputs and Outputs Generator - Understanding function inputs and outputs
Generates problems about input/output relationships
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class InputsOutputsGenerator:
    """Generates problems about inputs and outputs."""

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
        # Simple input/output: given input, find output
        input_val = random.randint(1, 10)
        add = random.randint(1, 8)
        output = input_val + add

        latex = f"Input: {input_val}, Rule: add {add}, Output: ?"
        return Equation(latex=latex, solution=output, steps=[], difficulty='easy')

    def _generate_medium(self) -> Equation:
        # Two-step rule: multiply then add
        input_val = random.randint(2, 8)
        mult = random.randint(2, 5)
        add = random.randint(1, 7)
        output = mult * input_val + add

        latex = f"Input: {input_val}, Rule: multiply by {mult} then add {add}, Output: ?"
        return Equation(latex=latex, solution=output, steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        # Given output, find input (working backwards)
        output = random.randint(15, 40)
        mult = random.randint(2, 4)
        add = random.randint(3, 10)

        # output = mult * input + add, so input = (output - add) / mult
        input_val = (output - add) // mult
        actual_output = mult * input_val + add

        latex = f"Rule: {mult}x + {add}, Output: {actual_output}, Input: ?"
        return Equation(latex=latex, solution=input_val, steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        # Reverse engineering with complex rules: find the rule or multi-step reasoning
        problem_type = random.choice(['find_rule', 'multi_input_pattern', 'complex_reverse'])

        if problem_type == 'find_rule':
            # Given multiple input-output pairs, find the missing output
            # Rule: ax + b
            a = random.randint(2, 5)
            b = random.randint(3, 10)
            input_val = random.randint(5, 12)
            output = a * input_val + b

            # Show pattern: (input1, output1), (input2, output2), find output for input3
            input1 = random.randint(1, 4)
            output1 = a * input1 + b
            input2 = random.randint(5, 8)
            output2 = a * input2 + b

            latex = f"Pattern: ({input1}, {output1}), ({input2}, {output2}). Find output for input {input_val}"
            solution = output

        elif problem_type == 'multi_input_pattern':
            # Complex pattern with two operations
            # Rule: ax^2 + b (but we'll simplify to keep integer solutions)
            # Actually use: (x * mult) + add1, then + add2
            input_val = random.randint(2, 6)
            mult = random.randint(3, 6)
            add = random.randint(5, 15)

            # Two-stage: first multiply, then square the input before adding
            # To keep it reasonable: mult * (input + add)
            output = mult * (input_val + add)

            latex = f"Rule: {mult}(x + {add}), Input: {input_val}, Output: ?"
            solution = output

        else:  # complex_reverse
            # Given complex rule and output, find input
            # Rule: 2(x + 3) + 5, find x given output
            mult = random.randint(2, 4)
            add_inner = random.randint(2, 7)
            add_outer = random.randint(3, 12)

            # output = mult * (input + add_inner) + add_outer
            # input = (output - add_outer) / mult - add_inner
            input_val = random.randint(2, 8)
            output = mult * (input_val + add_inner) + add_outer

            latex = f"Rule: {mult}(x + {add_inner}) + {add_outer}, Output: {output}, Input: ?"
            solution = input_val

        return Equation(latex=latex, solution=solution, steps=[], difficulty='challenge')


if __name__ == "__main__":
    gen = InputsOutputsGenerator()
    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()}:")
        for p in gen.generate_worksheet(difficulty, 3):
            print(f"  {p.latex} = {p.solution}")
