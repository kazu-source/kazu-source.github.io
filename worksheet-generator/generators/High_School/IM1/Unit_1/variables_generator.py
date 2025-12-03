"""
Variables Generator
Creates problems about understanding variables as unknown values
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class VariablesGenerator:
    """Generates problems about variables."""

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
        """Identify variables and constants"""
        problem_type = random.choice(['identify_var', 'identify_const', 'meaning'])

        if problem_type == 'identify_var':
            expressions = [
                ("3x + 5", "x"),
                ("7y - 2", "y"),
                ("4a + 9", "a"),
                ("2n + 6", "n"),
                ("5m - 3", "m"),
            ]
            expr, var = random.choice(expressions)

            latex = f"\\text{{What is the variable in the expression }} {expr}?"
            solution = var
            steps = [
                f"\\text{{A variable is a letter that represents an unknown value.}}",
                f"\\text{{In }} {expr}, \\text{{ the variable is }} {var}"
            ]

        elif problem_type == 'identify_const':
            a = random.randint(2, 10)
            b = random.randint(1, 15)
            var = random.choice(['x', 'y', 'n'])

            latex = f"\\text{{What are the constants in }} {a}{var} + {b}?"
            solution = f"{a} \\text{{ and }} {b}"
            steps = [
                f"\\text{{Constants are fixed numbers that don't change.}}",
                f"\\text{{In }} {a}{var} + {b}, \\text{{ the constants are }} {a} \\text{{ and }} {b}"
            ]

        else:
            contexts = [
                ("Let x = the number of apples", "x", "the number of apples"),
                ("Let n = your age in years", "n", "your age in years"),
                ("Let h = height in inches", "h", "height in inches"),
                ("Let t = time in hours", "t", "time in hours"),
            ]
            statement, var, meaning = random.choice(contexts)

            latex = f"\\text{{In the statement \"}} {statement} \\text{{\", what does }} {var} \\text{{ represent?}}"
            solution = meaning
            steps = [
                f"\\text{{The variable }} {var} \\text{{ stands for {meaning}.}}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Translate words to variable expressions"""
        problem_type = random.choice(['translate', 'evaluate'])

        if problem_type == 'translate':
            phrases = [
                ("a number plus 7", "n + 7", "n"),
                ("5 more than a number", "n + 5", "n"),
                ("a number minus 3", "n - 3", "n"),
                ("8 less than a number", "n - 8", "n"),
                ("twice a number", "2n", "n"),
                ("a number divided by 4", "\\frac{n}{4}", "n"),
                ("3 times a number plus 2", "3n + 2", "n"),
            ]
            phrase, expr, var = random.choice(phrases)

            latex = f"\\text{{Write as an algebraic expression: \"}} {phrase} \\text{{\" (use }} {var} \\text{{ for the number)}}"
            solution = expr
            steps = [
                f"\\text{{Identify the operation(s) described}}",
                f"\\text{{\"}} {phrase} \\text{{\" translates to }} {expr}"
            ]

        else:
            # Evaluate a simple expression
            a = random.randint(2, 6)
            b = random.randint(1, 10)
            x_val = random.randint(1, 5)
            result = a * x_val + b

            latex = f"\\text{{If }} x = {x_val}, \\text{{ find the value of }} {a}x + {b}"
            solution = str(result)
            steps = [
                f"\\text{{Substitute }} x = {x_val}",
                f"{a}({x_val}) + {b} = {a * x_val} + {b} = {result}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Write expressions for real-world situations"""
        scenarios = [
            {
                "context": "A movie ticket costs $12. Write an expression for the cost of n tickets.",
                "solution": "12n",
                "explanation": "Cost per ticket × number of tickets = 12n"
            },
            {
                "context": "You have $50 and spend $x. Write an expression for the money you have left.",
                "solution": "50 - x",
                "explanation": "Starting amount minus amount spent = 50 - x"
            },
            {
                "context": "A rectangle has length L and width 5. Write an expression for the perimeter.",
                "solution": "2L + 10",
                "explanation": "Perimeter = 2(length) + 2(width) = 2L + 2(5) = 2L + 10"
            },
            {
                "context": "You earn $15 per hour plus a $25 bonus. Write an expression for your total pay for h hours.",
                "solution": "15h + 25",
                "explanation": "Hourly pay × hours + bonus = 15h + 25"
            },
            {
                "context": "A phone plan costs $40 per month plus $0.10 per text. Write an expression for the monthly cost with t texts.",
                "solution": "40 + 0.1t",
                "explanation": "Base cost + cost per text × texts = 40 + 0.1t"
            }
        ]

        scenario = random.choice(scenarios)

        latex = f"\\text{{{scenario['context']}}}"
        solution = scenario['solution']
        steps = [
            f"\\text{{{scenario['explanation']}}}"
        ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Multi-step scenarios or comparing expressions"""
        problem_type = random.choice(['two_variables', 'compare', 'interpret'])

        if problem_type == 'two_variables':
            # Expression with two variables
            scenarios = [
                {
                    "context": "A store sells pens for $2 each and notebooks for $5 each. Write an expression for the total cost of p pens and n notebooks.",
                    "solution": "2p + 5n",
                    "explanation": "Cost of pens + Cost of notebooks = 2p + 5n"
                },
                {
                    "context": "A rectangle has length L and width W. Write an expression for its area.",
                    "solution": "LW \\text{ or } L \\times W",
                    "explanation": "Area = length × width = LW"
                }
            ]
            scenario = random.choice(scenarios)

            latex = f"\\text{{{scenario['context']}}}"
            solution = scenario['solution']
            steps = [f"\\text{{{scenario['explanation']}}}"]

        elif problem_type == 'compare':
            a = random.randint(3, 8)
            b = random.randint(5, 15)
            c = random.randint(2, 6)
            d = random.randint(8, 20)

            x_val = random.randint(1, 10)
            expr1_val = a * x_val + b
            expr2_val = c * x_val + d

            if expr1_val > expr2_val:
                answer = f"{a}x + {b}"
            elif expr1_val < expr2_val:
                answer = f"{c}x + {d}"
            else:
                answer = "They are equal"

            latex = f"\\text{{If }} x = {x_val}, \\text{{ which is greater: }} {a}x + {b} \\text{{ or }} {c}x + {d}?"
            solution = answer
            steps = [
                f"{a}x + {b} = {a}({x_val}) + {b} = {expr1_val}",
                f"{c}x + {d} = {c}({x_val}) + {d} = {expr2_val}",
                f"\\text{{{answer} is greater}}" if expr1_val != expr2_val else "\\text{{They are equal}}"
            ]

        else:
            # Interpret expression in context
            interpretations = [
                {
                    "expr": "50 - 3d",
                    "context": "A 50-gallon tank loses 3 gallons per day",
                    "meaning": "The amount of water remaining after d days"
                },
                {
                    "expr": "20 + 5w",
                    "context": "A plant is 20 cm tall and grows 5 cm per week",
                    "meaning": "The height of the plant after w weeks"
                }
            ]
            interp = random.choice(interpretations)

            latex = f"\\text{{What does the expression }} {interp['expr']} \\text{{ represent in the context: {interp['context']}?}}"
            solution = interp['meaning']
            steps = [f"\\text{{{interp['meaning']}}}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')


def main():
    """Test the generator."""
    generator = VariablesGenerator()

    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
