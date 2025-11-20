"""
Compound Inequality generator for math worksheets.
Generates compound inequalities (AND/OR) with varying difficulty levels.
Includes number line visualizations for solutions.
"""

import random
from typing import Tuple, List, Optional
from dataclasses import dataclass
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from numberline_utils import create_blank_numberline
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image
import numpy as np


@dataclass
class CompoundInequalityProblem:
    """Represents a compound inequality problem with its solution and visualization."""
    latex: str  # LaTeX formatted compound inequality
    compound_type: str  # 'and' or 'or'
    boundary_1: float  # First boundary value
    boundary_2: float  # Second boundary value
    inequality_type_1: str  # First inequality type ('<', '>', '<=', '>=')
    inequality_type_2: str  # Second inequality type
    number_line_min: int  # Minimum value on number line
    number_line_max: int  # Maximum value on number line
    steps: List[str]  # Solution steps
    difficulty: str  # Difficulty level
    worksheet_image: object = None  # PIL Image for worksheet (blank number line)
    answer_image: object = None  # PIL Image for answer key (with solution)


class CompoundInequalityGenerator:
    """Generates random compound inequalities with different difficulty levels."""

    def __init__(self, seed=None):
        """
        Initialize the compound inequality generator.

        Args:
            seed: Random seed for reproducibility (optional)
        """
        if seed:
            random.seed(seed)

    def generate_inequality(self, difficulty: str, compound_type: Optional[str] = None) -> CompoundInequalityProblem:
        """
        Generate a compound inequality based on difficulty level.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            compound_type: 'and' or 'or', or None to choose randomly

        Returns:
            CompoundInequalityProblem object with problem and solution
        """
        if compound_type is None:
            compound_type = random.choice(['and', 'or'])

        if difficulty == 'easy':
            return self._generate_easy(compound_type)
        elif difficulty == 'medium':
            return self._generate_medium(compound_type)
        elif difficulty == 'hard':
            return self._generate_hard(compound_type)
        elif difficulty == 'challenge':
            return self._generate_challenge(compound_type)
        else:
            raise ValueError(f"Unknown difficulty: {difficulty}")

    def generate_worksheet(self, difficulty: str, num_problems: int,
                          compound_type: Optional[str] = None) -> List[CompoundInequalityProblem]:
        """
        Generate multiple compound inequalities for a worksheet.

        Args:
            difficulty: Difficulty level
            num_problems: Number of problems to generate
            compound_type: 'and', 'or', or None for mixed

        Returns:
            List of CompoundInequalityProblem objects
        """
        return [self.generate_inequality(difficulty, compound_type) for _ in range(num_problems)]

    def _get_number_line_range(self, boundary_1: float, boundary_2: float, padding: int = 3) -> Tuple[int, int]:
        """
        Calculate a good range for the number line based on boundaries.

        Args:
            boundary_1: First boundary value
            boundary_2: Second boundary value
            padding: How many units to show beyond boundaries

        Returns:
            Tuple of (min_value, max_value) for number line
        """
        min_boundary = min(int(boundary_1), int(boundary_2))
        max_boundary = max(int(boundary_1), int(boundary_2))
        return (min_boundary - padding, max_boundary + padding)

    def _create_compound_numberline_with_solution(self, min_val: int, max_val: int,
                                                   boundary_1: float, boundary_2: float,
                                                   inequality_type_1: str, inequality_type_2: str,
                                                   compound_type: str,
                                                   figsize: Tuple[float, float] = (8, 1.2)):
        """
        Create a number line showing compound inequality solution.

        Args:
            min_val: Minimum value on number line
            max_val: Maximum value on number line
            boundary_1: First boundary value
            boundary_2: Second boundary value
            inequality_type_1: First inequality type
            inequality_type_2: Second inequality type
            compound_type: 'and' or 'or'
            figsize: Figure size in inches

        Returns:
            PIL Image object
        """
        from numberline_utils import NumberLine

        line = NumberLine(min_val, max_val)
        fig, ax = line.create_figure(figsize=figsize)

        # Determine if circles are closed or open
        is_equal_1 = inequality_type_1 in ['<=', '>=', '\\leq', '\\geq']
        is_equal_2 = inequality_type_2 in ['<=', '>=', '\\leq', '\\geq']

        if compound_type == 'and':
            # For AND: shade between the two boundaries
            # The region is between boundary_1 and boundary_2
            left_bound = min(boundary_1, boundary_2)
            right_bound = max(boundary_1, boundary_2)

            # Shade the region between boundaries
            ax.fill_between([left_bound, right_bound], [-0.15, -0.15], [0.15, 0.15],
                           alpha=0.3, color='blue')

            # Plot both boundary points
            line.plot_solution_point(ax, boundary_1, is_equal=is_equal_1)
            line.plot_solution_point(ax, boundary_2, is_equal=is_equal_2)

        else:  # compound_type == 'or'
            # For OR: shade two regions (left and right of boundaries)
            # Determine which direction each inequality goes
            is_left_1 = inequality_type_1 in ['<', '<=', '\\lt', '\\leq']
            is_left_2 = inequality_type_2 in ['<', '<=', '\\lt', '\\leq']

            # Plot boundary points
            line.plot_solution_point(ax, boundary_1, is_equal=is_equal_1)
            line.plot_solution_point(ax, boundary_2, is_equal=is_equal_2)

            # Draw solution regions
            line.plot_solution_region(ax, boundary_1, is_left=is_left_1)
            line.plot_solution_region(ax, boundary_2, is_left=is_left_2)

        return line.render_to_image(fig)

    def _generate_easy(self, compound_type: str) -> CompoundInequalityProblem:
        """
        Generate simple compound inequalities (already solved form).
        AND: a < x < b or a <= x <= b
        OR: x < a or x > b
        """
        if compound_type == 'and':
            # Generate a < x < b
            a = random.randint(-10, 5)
            b = a + random.randint(3, 8)

            # Choose inequality types (both same for easy)
            use_equal = random.choice([True, False])
            if use_equal:
                ineq_1 = '\\leq'
                ineq_2 = '\\leq'
                latex = f"{a} \\leq x \\leq {b}"
            else:
                ineq_1 = '<'
                ineq_2 = '<'
                latex = f"{a} < x < {b}"

            steps = [f"Solution is all x between {a} and {b}"]

        else:  # 'or'
            # Generate x < a or x > b
            a = random.randint(-5, 5)
            b = a + random.randint(5, 10)

            use_equal = random.choice([True, False])
            if use_equal:
                ineq_1 = '\\leq'
                ineq_2 = '\\geq'
                latex = f"x \\leq {a} \\text{{ or }} x \\geq {b}"
            else:
                ineq_1 = '<'
                ineq_2 = '>'
                latex = f"x < {a} \\text{{ or }} x > {b}"

            steps = [f"Solution is all x less than {a} or greater than {b}"]

        min_val, max_val = self._get_number_line_range(a, b)

        # Generate images
        worksheet_img = create_blank_numberline(min_val, max_val)
        answer_img = self._create_compound_numberline_with_solution(
            min_val, max_val, a, b, ineq_1, ineq_2, compound_type
        )

        return CompoundInequalityProblem(
            latex=latex,
            compound_type=compound_type,
            boundary_1=a,
            boundary_2=b,
            inequality_type_1=ineq_1,
            inequality_type_2=ineq_2,
            number_line_min=min_val,
            number_line_max=max_val,
            steps=steps,
            difficulty='easy',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_medium(self, compound_type: str) -> CompoundInequalityProblem:
        """
        Generate compound inequalities requiring one or two steps to solve.
        AND: a < x + c < b
        OR: x + c < a or x + c > b
        """
        if compound_type == 'and':
            # Generate a < x + c < b, solve for x
            x_left = random.randint(-8, 4)
            x_right = x_left + random.randint(4, 10)
            c = random.randint(-6, 6)

            a = x_left + c
            b = x_right + c

            use_equal = random.choice([True, False])
            if use_equal:
                ineq_1 = '\\leq'
                ineq_2 = '\\leq'
                c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"
                latex = f"{a} \\leq x {c_str} \\leq {b}"
            else:
                ineq_1 = '<'
                ineq_2 = '<'
                c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"
                latex = f"{a} < x {c_str} < {b}"

            steps = [
                f"Subtract {c} from all parts" if c >= 0 else f"Add {abs(c)} to all parts",
                f"{x_left} {ineq_1} x {ineq_2} {x_right}"
            ]

            boundary_1 = x_left
            boundary_2 = x_right

        else:  # 'or'
            # Generate x + c < a or x + c > b
            x_a = random.randint(-8, 2)
            x_b = x_a + random.randint(6, 12)
            c = random.randint(-6, 6)

            a = x_a + c
            b = x_b + c

            use_equal = random.choice([True, False])
            c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"

            if use_equal:
                ineq_1 = '\\leq'
                ineq_2 = '\\geq'
                latex = f"x {c_str} \\leq {a} \\text{{ or }} x {c_str} \\geq {b}"
            else:
                ineq_1 = '<'
                ineq_2 = '>'
                latex = f"x {c_str} < {a} \\text{{ or }} x {c_str} > {b}"

            steps = [
                f"Subtract {c} from both sides" if c >= 0 else f"Add {abs(c)} to both sides",
                f"x {ineq_1} {x_a} \\text{{ or }} x {ineq_2} {x_b}"
            ]

            boundary_1 = x_a
            boundary_2 = x_b

        min_val, max_val = self._get_number_line_range(boundary_1, boundary_2)

        worksheet_img = create_blank_numberline(min_val, max_val)
        answer_img = self._create_compound_numberline_with_solution(
            min_val, max_val, boundary_1, boundary_2, ineq_1, ineq_2, compound_type
        )

        return CompoundInequalityProblem(
            latex=latex,
            compound_type=compound_type,
            boundary_1=boundary_1,
            boundary_2=boundary_2,
            inequality_type_1=ineq_1,
            inequality_type_2=ineq_2,
            number_line_min=min_val,
            number_line_max=max_val,
            steps=steps,
            difficulty='medium',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_hard(self, compound_type: str) -> CompoundInequalityProblem:
        """
        Generate compound inequalities with multiplication/division.
        AND: a < mx + c < b
        OR: mx + c < a or mx + c > b
        """
        if compound_type == 'and':
            # Generate a < mx + c < b, solve for x
            x_left = random.randint(-6, 3)
            x_right = x_left + random.randint(4, 8)
            m = random.randint(2, 5)
            c = random.randint(-8, 8)

            a = m * x_left + c
            b = m * x_right + c

            use_equal = random.choice([True, False])
            c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"

            if use_equal:
                ineq_1 = '\\leq'
                ineq_2 = '\\leq'
                latex = f"{a} \\leq {m}x {c_str} \\leq {b}"
            else:
                ineq_1 = '<'
                ineq_2 = '<'
                latex = f"{a} < {m}x {c_str} < {b}"

            steps = [
                f"Subtract {c} from all parts" if c >= 0 else f"Add {abs(c)} to all parts",
                f"{a - c} {ineq_1} {m}x {ineq_2} {b - c}",
                f"Divide all parts by {m}",
                f"{x_left} {ineq_1} x {ineq_2} {x_right}"
            ]

            boundary_1 = x_left
            boundary_2 = x_right

        else:  # 'or'
            # Generate mx + c < a or mx + c > b
            x_a = random.randint(-6, 2)
            x_b = x_a + random.randint(5, 10)
            m = random.randint(2, 5)
            c = random.randint(-8, 8)

            a = m * x_a + c
            b = m * x_b + c

            use_equal = random.choice([True, False])
            c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"

            if use_equal:
                ineq_1 = '\\leq'
                ineq_2 = '\\geq'
                latex = f"{m}x {c_str} \\leq {a} \\text{{ or }} {m}x {c_str} \\geq {b}"
            else:
                ineq_1 = '<'
                ineq_2 = '>'
                latex = f"{m}x {c_str} < {a} \\text{{ or }} {m}x {c_str} > {b}"

            steps = [
                f"Subtract {c} from both sides" if c >= 0 else f"Add {abs(c)} to both sides",
                f"{m}x {ineq_1} {a - c} \\text{{ or }} {m}x {ineq_2} {b - c}",
                f"Divide both sides by {m}",
                f"x {ineq_1} {x_a} \\text{{ or }} x {ineq_2} {x_b}"
            ]

            boundary_1 = x_a
            boundary_2 = x_b

        min_val, max_val = self._get_number_line_range(boundary_1, boundary_2, padding=4)

        worksheet_img = create_blank_numberline(min_val, max_val)
        answer_img = self._create_compound_numberline_with_solution(
            min_val, max_val, boundary_1, boundary_2, ineq_1, ineq_2, compound_type
        )

        return CompoundInequalityProblem(
            latex=latex,
            compound_type=compound_type,
            boundary_1=boundary_1,
            boundary_2=boundary_2,
            inequality_type_1=ineq_1,
            inequality_type_2=ineq_2,
            number_line_min=min_val,
            number_line_max=max_val,
            steps=steps,
            difficulty='hard',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_challenge(self, compound_type: str) -> CompoundInequalityProblem:
        """
        Generate complex compound inequalities with potential negative coefficients.
        Requires careful attention to inequality direction when dividing by negatives.
        """
        if compound_type == 'and':
            # Generate a < mx + c < b with possible negative m
            x_left = random.randint(-6, 3)
            x_right = x_left + random.randint(4, 8)
            m = random.choice([-4, -3, -2, 2, 3, 4, 5])
            c = random.randint(-10, 10)

            if m > 0:
                a = m * x_left + c
                b = m * x_right + c
                final_left = x_left
                final_right = x_right
            else:
                # When m is negative, boundaries flip
                a = m * x_right + c
                b = m * x_left + c
                final_left = x_left
                final_right = x_right

            use_equal = random.choice([True, False])
            c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"

            if use_equal:
                ineq_1 = '\\leq'
                ineq_2 = '\\leq'
            else:
                ineq_1 = '<'
                ineq_2 = '<'

            m_str = f"{m}x" if m != -1 else "-x"
            latex = f"{a} {ineq_1} {m_str} {c_str} {ineq_2} {b}"

            if m > 0:
                steps = [
                    f"Subtract {c} from all parts" if c >= 0 else f"Add {abs(c)} to all parts",
                    f"{a - c} {ineq_1} {m}x {ineq_2} {b - c}",
                    f"Divide all parts by {m}",
                    f"{final_left} {ineq_1} x {ineq_2} {final_right}"
                ]
            else:
                steps = [
                    f"Subtract {c} from all parts" if c >= 0 else f"Add {abs(c)} to all parts",
                    f"{a - c} {ineq_1} {m}x {ineq_2} {b - c}",
                    f"Divide all parts by {m} (flip inequality signs)",
                    f"{final_left} {ineq_1} x {ineq_2} {final_right}"
                ]

            boundary_1 = final_left
            boundary_2 = final_right

        else:  # 'or'
            # Generate mx + c < a or mx + c > b with possible negative m
            x_a = random.randint(-6, 2)
            x_b = x_a + random.randint(5, 10)
            m = random.choice([-4, -3, -2, 2, 3, 4, 5])
            c = random.randint(-10, 10)

            a = m * x_a + c
            b = m * x_b + c

            use_equal = random.choice([True, False])
            c_str = f"+ {c}" if c >= 0 else f"- {abs(c)}"
            m_str = f"{m}x" if m != -1 else "-x"

            if use_equal:
                ineq_1 = '\\leq'
                ineq_2 = '\\geq'
            else:
                ineq_1 = '<'
                ineq_2 = '>'

            latex = f"{m_str} {c_str} {ineq_1} {a} \\text{{ or }} {m_str} {c_str} {ineq_2} {b}"

            if m > 0:
                steps = [
                    f"Subtract {c} from both sides" if c >= 0 else f"Add {abs(c)} to both sides",
                    f"{m}x {ineq_1} {a - c} \\text{{ or }} {m}x {ineq_2} {b - c}",
                    f"Divide both sides by {m}",
                    f"x {ineq_1} {x_a} \\text{{ or }} x {ineq_2} {x_b}"
                ]
            else:
                # When dividing by negative, flip inequality signs
                flip_map = {'<': '>', '>': '<', '\\leq': '\\geq', '\\geq': '\\leq'}
                final_ineq_1 = flip_map[ineq_1]
                final_ineq_2 = flip_map[ineq_2]
                steps = [
                    f"Subtract {c} from both sides" if c >= 0 else f"Add {abs(c)} to both sides",
                    f"{m}x {ineq_1} {a - c} \\text{{ or }} {m}x {ineq_2} {b - c}",
                    f"Divide both sides by {m} (flip inequality signs)",
                    f"x {final_ineq_1} {x_a} \\text{{ or }} x {final_ineq_2} {x_b}"
                ]

            boundary_1 = x_a
            boundary_2 = x_b

        min_val, max_val = self._get_number_line_range(boundary_1, boundary_2, padding=5)

        worksheet_img = create_blank_numberline(min_val, max_val)
        answer_img = self._create_compound_numberline_with_solution(
            min_val, max_val, boundary_1, boundary_2, ineq_1, ineq_2, compound_type
        )

        return CompoundInequalityProblem(
            latex=latex,
            compound_type=compound_type,
            boundary_1=boundary_1,
            boundary_2=boundary_2,
            inequality_type_1=ineq_1,
            inequality_type_2=ineq_2,
            number_line_min=min_val,
            number_line_max=max_val,
            steps=steps,
            difficulty='challenge',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )


# Example usage and testing
if __name__ == "__main__":
    generator = CompoundInequalityGenerator()

    print("Compound Inequality Generator Test\n")

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Examples:")
        print("\nAND type:")
        for i in range(2):
            prob = generator.generate_inequality(difficulty, compound_type='and')
            print(f"  {prob.latex}")
            print(f"  Solution: {prob.boundary_1} to {prob.boundary_2}")
            print()

        print("OR type:")
        for i in range(2):
            prob = generator.generate_inequality(difficulty, compound_type='or')
            print(f"  {prob.latex}")
            print(f"  Solution: x < {prob.boundary_1} or x > {prob.boundary_2}")
            print()