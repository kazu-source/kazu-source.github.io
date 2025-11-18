"""
Variables Generator - Introduction to algebraic variables
Generates problems about recognizing and understanding variables
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class VariablesGenerator:
    """Generates problems introducing variables and their meaning."""

    def __init__(self, seed=None):
        """Initialize the variables generator."""
        if seed:
            random.seed(seed)

        # Different contexts for variables
        self.contexts = {
            'easy': [
                ("x", "an unknown number"),
                ("n", "a number"),
                ("y", "a value"),
                ("a", "any number"),
                ("b", "some number"),
            ],
            'medium': [
                ("x", "the number of apples"),
                ("t", "time in hours"),
                ("d", "distance in miles"),
                ("p", "price in dollars"),
                ("n", "number of students"),
            ],
            'hard': [
                ("v", "velocity in meters per second"),
                ("A", "area in square units"),
                ("P", "perimeter in units"),
                ("r", "radius"),
                ("h", "height"),
            ],
            'challenge': [
                ("alpha", "rate of acceleration in m/s^2"),
                ("theta", "angle of rotation in radians"),
                ("lambda", "wavelength in nanometers"),
                ("V", "volume of a cylinder"),
                ("delta", "change in temperature"),
            ]
        }

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard'
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
        """Generate a single variable problem."""
        if difficulty == 'challenge':
            problem_type = random.choice(['identify', 'meaning', 'substitute_concept', 'multi_context'])
        else:
            problem_type = random.choice(['identify', 'meaning', 'substitute_concept'])

        if problem_type == 'identify':
            return self._generate_identify_problem(difficulty)
        elif problem_type == 'meaning':
            return self._generate_meaning_problem(difficulty)
        elif problem_type == 'multi_context':
            return self._generate_multi_context_problem()
        else:
            return self._generate_substitute_concept_problem(difficulty)

    def _generate_identify_problem(self, difficulty: str) -> Equation:
        """Generate a problem asking to identify variables in an expression."""
        var, context = random.choice(self.contexts.get(difficulty, self.contexts['easy']))

        if difficulty == 'easy':
            # Simple: What is the variable in this expression?
            expressions = [
                (f"{var} + 5", var),
                (f"3{var}", var),
                (f"{var} - 2", var),
                (f"7 + {var}", var),
            ]
            expr, solution = random.choice(expressions)
            latex = f"\\text{{What is the variable in: }} {expr}?"

        elif difficulty == 'medium':
            # Multiple terms: Identify the variable
            num1 = random.randint(2, 9)
            num2 = random.randint(1, 9)
            expr = f"{num1}{var} + {num2}"
            latex = f"\\text{{Identify the variable in: }} {expr}"
            solution = var

        elif difficulty == 'hard':
            # Two potential variables, identify the actual variable
            var2 = random.choice(['a', 'b', 'c', 'm', 'n', 'p'])
            while var2 == var:
                var2 = random.choice(['a', 'b', 'c', 'm', 'n', 'p'])

            num = random.randint(2, 12)
            latex = f"\\text{{In }} {num}{var} + {var2}, \\text{{ what represents the coefficient's variable?}}"
            solution = var

        else:  # challenge
            # Multiple variables in complex expression
            vars_list = ['x', 'y', 'z', 'w']
            num_vars = random.randint(3, 4)
            selected_vars = random.sample(vars_list, num_vars)

            num1 = random.randint(2, 8)
            num2 = random.randint(2, 8)
            num3 = random.randint(2, 8)

            if num_vars == 3:
                expr = f"{num1}{selected_vars[0]}^2 + {num2}{selected_vars[1]} - {num3}{selected_vars[2]}"
                latex = f"\\text{{List all variables in: }} {expr}"
                solution = ", ".join(sorted(selected_vars))
            else:
                expr = f"{num1}{selected_vars[0]}{selected_vars[1]} + {num2}{selected_vars[2]}^2 - {num3}{selected_vars[3]}"
                latex = f"\\text{{List all variables in: }} {expr}"
                solution = ", ".join(sorted(selected_vars))

        # For Variables problems, we use numeric solutions where possible, otherwise 0
        numeric_solution = 0
        try:
            numeric_solution = float(solution) if solution.replace('.', '', 1).replace('-', '', 1).isdigit() else 0
        except:
            numeric_solution = 0
        return Equation(latex=latex, solution=numeric_solution, steps=[solution], difficulty=difficulty)

    def _generate_meaning_problem(self, difficulty: str) -> Equation:
        """Generate a problem about what a variable represents."""
        var, context = random.choice(self.contexts.get(difficulty, self.contexts['easy']))

        if difficulty == 'easy':
            latex = f"\\text{{If }} {var} \\text{{ represents {context}, what does it stand for?}}"
            solution = context

        elif difficulty == 'medium':
            # Word problem context
            latex = f"\\text{{Let }} {var} \\text{{ represent {context}. What does }} {var} \\text{{ mean?}}"
            solution = context

        elif difficulty == 'hard':
            # Application context
            latex = f"\\text{{In the expression for {context}, the variable }} {var} \\text{{ stands for:}}"
            solution = context

        else:  # challenge
            # Multiple variables with complex relationships
            var1, context1 = random.choice(self.contexts['challenge'])
            var2, context2 = random.choice(self.contexts['challenge'])
            while var2 == var1:
                var2, context2 = random.choice(self.contexts['challenge'])

            latex = f"\\text{{In }} {var1} \\cdot {var2}, \\text{{ if }} {var1} \\text{{ is {context1} and }} {var2} \\text{{ is {context2}, explain the product}}"
            solution = f"product of {context1} and {context2}"

        # For Variables problems, we use numeric solutions where possible, otherwise 0
        numeric_solution = 0
        try:
            numeric_solution = float(solution) if solution.replace('.', '', 1).replace('-', '', 1).isdigit() else 0
        except:
            numeric_solution = 0
        return Equation(latex=latex, solution=numeric_solution, steps=[solution], difficulty=difficulty)

    def _generate_substitute_concept_problem(self, difficulty: str) -> Equation:
        """Generate a conceptual problem about variable substitution."""
        var = random.choice(['x', 'n', 'y', 'a'])

        if difficulty == 'easy':
            num = random.randint(1, 10)
            latex = f"\\text{{If }} {var} = {num}, \\text{{ what does }} {var} \\text{{ equal?}}"
            solution = str(num)

        elif difficulty == 'medium':
            num1 = random.randint(2, 9)
            num2 = random.randint(1, 9)
            value = random.randint(2, 8)
            result = num1 * value + num2
            latex = f"\\text{{If }} {var} = {value} \\text{{ in }} {num1}{var} + {num2}, \\text{{ what is the result?}}"
            solution = str(result)

        elif difficulty == 'hard':
            # Multiple variables concept
            num1 = random.randint(2, 6)
            num2 = random.randint(2, 6)
            value = random.randint(2, 5)
            result = num1 * value + num2 * value
            latex = f"\\text{{If both variables equal }} {value} \\text{{ in }} {num1}x + {num2}y, \\text{{ find the sum}}"
            solution = str(result)

        else:  # challenge
            # Three variables with different values
            x_val = random.randint(3, 12)
            y_val = random.randint(3, 12)
            z_val = random.randint(3, 12)
            a = random.randint(2, 5)
            b = random.randint(2, 5)
            c = random.randint(2, 5)
            result = a * x_val + b * y_val - c * z_val
            latex = f"\\text{{Evaluate }} {a}x + {b}y - {c}z \\text{{ when }} x={x_val}, y={y_val}, z={z_val}"
            solution = str(result)

        # For Variables problems, we use numeric solutions where possible, otherwise 0
        numeric_solution = 0
        try:
            numeric_solution = float(solution) if solution.replace('.', '', 1).replace('-', '', 1).isdigit() else 0
        except:
            numeric_solution = 0
        return Equation(latex=latex, solution=numeric_solution, steps=[solution], difficulty=difficulty)

    def _generate_multi_context_problem(self) -> Equation:
        """Generate a challenge problem with multiple variables in real-world context."""
        contexts = [
            ("t", "time in seconds", "d", "distance in meters", "v", "velocity in m/s", "d = v \\cdot t"),
            ("F", "force in Newtons", "m", "mass in kg", "a", "acceleration in m/s^2", "F = m \\cdot a"),
            ("P", "power in watts", "V", "voltage in volts", "I", "current in amperes", "P = V \\cdot I"),
        ]

        var1, context1, var2, context2, var3, context3, formula = random.choice(contexts)

        latex = f"\\text{{Given }} {formula}, \\text{{ identify all three variables and their meanings}}"
        solution = f"{var1}: {context1}, {var2}: {context2}, {var3}: {context3}"

        numeric_solution = 0
        return Equation(latex=latex, solution=numeric_solution, steps=[solution], difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = VariablesGenerator()

    print("Testing Variables Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}\n")
