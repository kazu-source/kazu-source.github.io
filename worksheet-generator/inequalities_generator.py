"""
Inequality generator for math worksheets.
Generates inequalities with varying difficulty levels and tracks solutions with number lines.
"""

import random
from typing import Tuple, List
from dataclasses import dataclass

from numberline_utils import create_blank_numberline, create_numberline_with_solution


@dataclass
class InequalityProblem:
    """Represents an inequality problem with its solution and number line range."""
    latex: str  # LaTeX formatted inequality
    solution: float  # The solution value (or boundary)
    inequality_type: str  # '<', '>', '<=', '>='
    is_solution_left: bool  # True if solution is x < value, False if x > value
    number_line_min: int  # Minimum value on number line
    number_line_max: int  # Maximum value on number line
    steps: List[str]  # Solution steps (for future expansion)
    difficulty: str  # Difficulty level
    worksheet_image: object = None  # PIL Image for worksheet (blank number line)
    answer_image: object = None  # PIL Image for answer key (with solution)


class InequalityGenerator:
    """Generates random inequalities with different difficulty levels."""

    def __init__(self, seed=None):
        """
        Initialize the inequality generator.

        Args:
            seed: Random seed for reproducibility (optional)
        """
        if seed:
            random.seed(seed)

    def generate_inequality(self, difficulty: str) -> InequalityProblem:
        """
        Generate an inequality based on difficulty level.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            InequalityProblem object with problem and solution
        """
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        elif difficulty == 'challenge':
            return self._generate_challenge()
        else:
            raise ValueError(f"Unknown difficulty: {difficulty}")

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[InequalityProblem]:
        """
        Generate multiple inequalities for a worksheet.

        Args:
            difficulty: Difficulty level
            num_problems: Number of problems to generate

        Returns:
            List of InequalityProblem objects
        """
        return [self.generate_inequality(difficulty) for _ in range(num_problems)]

    def _get_number_line_range(self, solution: float, padding: int = 5) -> Tuple[int, int]:
        """
        Calculate a good range for the number line based on solution.

        Args:
            solution: The solution value
            padding: How many units to show on each side

        Returns:
            Tuple of (min_value, max_value) for number line
        """
        solution_int = int(solution)
        return (solution_int - padding, solution_int + padding)

    def _generate_easy(self) -> InequalityProblem:
        """
        Generate one-step inequalities: x + a < b or x - a > b
        Example: x + 5 < 12, x - 3 > 7
        """
        # Choose solution
        x = random.randint(-5, 15)

        # Choose inequality type
        ineq_symbols = ['<', '>', '\\leq', '\\geq']
        ineq_type = random.choice(ineq_symbols)
        is_solution_left = ineq_type in ['<', '\\leq']

        # Choose operation
        if random.choice([True, False]):
            # x + a ineq b
            a = random.randint(1, 15)
            b = x + a
            if a >= 0:
                latex = f"x + {a} {ineq_type} {b}"
            else:
                latex = f"x - {abs(a)} {ineq_type} {b}"
            steps = [f"x {ineq_type} {b} - {a}", f"x {ineq_type} {x}"]
        else:
            # x - a ineq b
            a = random.randint(1, 15)
            b = x - a
            latex = f"x - {a} {ineq_type} {b}"
            steps = [f"x {ineq_type} {b} + {a}", f"x {ineq_type} {x}"]

        min_val, max_val = self._get_number_line_range(x)

        # Generate number line images
        worksheet_img = create_blank_numberline(min_val, max_val)
        answer_img = create_numberline_with_solution(
            min_val, max_val,
            boundary_value=x,
            inequality_type=ineq_type
        )

        return InequalityProblem(
            latex=latex,
            solution=x,
            inequality_type=ineq_type,
            is_solution_left=is_solution_left,
            number_line_min=min_val,
            number_line_max=max_val,
            steps=steps,
            difficulty='easy',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_medium(self) -> InequalityProblem:
        """
        Generate two-step inequalities: ax + b < c
        Example: 2x + 3 < 11
        """
        # Choose solution
        x = random.randint(-8, 12)

        # Choose inequality type
        ineq_symbols = ['<', '>', '\\leq', '\\geq']
        ineq_type = random.choice(ineq_symbols)
        is_solution_left = ineq_type in ['<', '\\leq']

        # ax + b ineq c
        a = random.randint(2, 8)
        b = random.randint(-12, 12)
        c = a * x + b

        # Format with proper signs
        if b >= 0:
            latex = f"{a}x + {b} {ineq_type} {c}"
        else:
            latex = f"{a}x - {abs(b)} {ineq_type} {c}"

        steps = [
            f"{a}x {ineq_type} {c - b}",
            f"x {ineq_type} {(c - b) / a}",
            f"x {ineq_type} {x}"
        ]

        min_val, max_val = self._get_number_line_range(x)

        # Generate number line images
        worksheet_img = create_blank_numberline(min_val, max_val)
        answer_img = create_numberline_with_solution(
            min_val, max_val,
            boundary_value=x,
            inequality_type=ineq_type
        )

        return InequalityProblem(
            latex=latex,
            solution=x,
            inequality_type=ineq_type,
            is_solution_left=is_solution_left,
            number_line_min=min_val,
            number_line_max=max_val,
            steps=steps,
            difficulty='medium',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_hard(self) -> InequalityProblem:
        """
        Generate multi-step inequalities with parentheses: a(x + b) + c < d
        Example: 3(x + 2) - 5 < 10
        """
        # Choose solution
        x = random.randint(-10, 15)

        # Choose inequality type
        ineq_symbols = ['<', '>', '\\leq', '\\geq']
        ineq_type = random.choice(ineq_symbols)
        is_solution_left = ineq_type in ['<', '\\leq']

        # a(x + b) + c ineq d
        a = random.randint(2, 6)
        b = random.randint(-8, 8)
        c = random.randint(-12, 12)
        d = a * (x + b) + c

        # Format with proper signs
        b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
        c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"

        latex = f"{a}(x {b_str}) {c_str} {ineq_type} {d}"

        steps = [
            f"{a}(x {b_str}) {ineq_type} {d - c}",
            f"x {b_str} {ineq_type} {(d - c) / a}",
            f"x {ineq_type} {x}"
        ]

        min_val, max_val = self._get_number_line_range(x)

        # Generate number line images
        worksheet_img = create_blank_numberline(min_val, max_val)
        answer_img = create_numberline_with_solution(
            min_val, max_val,
            boundary_value=x,
            inequality_type=ineq_type
        )

        return InequalityProblem(
            latex=latex,
            solution=x,
            inequality_type=ineq_type,
            is_solution_left=is_solution_left,
            number_line_min=min_val,
            number_line_max=max_val,
            steps=steps,
            difficulty='hard',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_challenge(self) -> InequalityProblem:
        """
        Generate inequalities with variables on both sides: ax + b < cx + d
        Note: Need to handle direction flip when dividing by negative
        Example: 2x + 3 < x + 7 or -2x + 5 > -x + 1
        """
        # Choose solution
        x = random.randint(-10, 15)

        # Choose inequality type
        ineq_symbols = ['<', '>', '\\leq', '\\geq']
        ineq_type = random.choice(ineq_symbols)
        is_solution_left = ineq_type in ['<', '\\leq']

        # ax + b ineq cx + d
        a = random.randint(-8, 8)
        while a == 0:
            a = random.randint(-8, 8)

        c = random.randint(-8, 8)
        while c == 0 or c == a:
            c = random.randint(-8, 8)

        b = random.randint(-12, 12)
        d = a * x + b - c * x

        # Format equations with proper signs
        b_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
        d_str = f"+ {d}" if d >= 0 else f"- {abs(d)}"

        # Handle negative coefficients
        a_str = f"{a}x" if a != 1 else "x" if a == 1 else f"-x" if a == -1 else f"{a}x"
        c_str = f"{c}x" if c != 1 else "x" if c == 1 else f"-x" if c == -1 else f"{c}x"

        latex = f"{a_str} {b_str} {ineq_type} {c_str} {d_str}"

        # Check if we divide by negative (inequality flips)
        coef_diff = a - c
        if coef_diff < 0:
            # Flip inequality
            flip_map = {'<': '>', '>': '<', '\\leq': '\\geq', '\\geq': '\\leq'}
            final_ineq = flip_map[ineq_type]
            is_solution_left = final_ineq in ['<', '\\leq']
        else:
            final_ineq = ineq_type

        steps = [
            f"{a - c}x {final_ineq} {d - b}",
            f"x {final_ineq} {x}"
        ]

        min_val, max_val = self._get_number_line_range(x, padding=6)

        # Generate number line images
        worksheet_img = create_blank_numberline(min_val, max_val)
        answer_img = create_numberline_with_solution(
            min_val, max_val,
            boundary_value=x,
            inequality_type=final_ineq
        )

        return InequalityProblem(
            latex=latex,
            solution=x,
            inequality_type=final_ineq,
            is_solution_left=is_solution_left,
            number_line_min=min_val,
            number_line_max=max_val,
            steps=steps,
            difficulty='challenge',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )


# Example usage and testing
if __name__ == "__main__":
    generator = InequalityGenerator()

    print("Inequality Generator Test\n")

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Examples:")
        for i in range(3):
            ineq = generator.generate_inequality(difficulty)
            print(f"  {ineq.latex}")
            print(f"  Solution: x {ineq.inequality_type} {ineq.solution}")
            print(f"  Number line: [{ineq.number_line_min}, {ineq.number_line_max}]")
            print()
