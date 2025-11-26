"""
Configuration for worksheet generation.
Centralizes all rendering settings for different problem types.
"""

from dataclasses import dataclass, field
from typing import Dict, Union


@dataclass
class ProblemTypeConfig:
    """Configuration for rendering a specific problem type."""

    # Rendering settings
    latex_fontsize: int  # Font size for LaTeX rendering
    image_width: float  # Width in inches for rendered image
    image_height: float  # Height in inches for rendered image
    vertical_offset: float  # Vertical offset from problem number (inches)

    # Layout settings
    problems_per_page: int  # Maximum problems per page
    vertical_spacing: float  # Space between problems (inches) - DEPRECATED: use min/max_spacing
    default_num_problems: Union[int, Dict[str, int]]  # Default number of problems - can be int or dict by difficulty

    # Dynamic spacing constraints
    min_spacing: float  # Minimum vertical spacing (inches) - prevents cramping
    max_spacing: float  # Maximum vertical spacing (inches) - prevents excessive spreading

    # Instructions text
    instructions: str  # Instruction text for worksheet

    def get_default_num_problems(self, difficulty: str = 'medium') -> int:
        """
        Get the default number of problems for a given difficulty.

        Args:
            difficulty: 'easy', 'medium', 'hard', or 'challenge'

        Returns:
            Default number of problems for that difficulty
        """
        if isinstance(self.default_num_problems, dict):
            return self.default_num_problems.get(difficulty, self.default_num_problems.get('medium', 10))
        return self.default_num_problems

    def __repr__(self):
        if isinstance(self.default_num_problems, dict):
            return f"ProblemTypeConfig(fontsize={self.latex_fontsize}, {self.problems_per_page}/page, defaults={self.default_num_problems})"
        return f"ProblemTypeConfig(fontsize={self.latex_fontsize}, {self.problems_per_page}/page, default={self.default_num_problems})"


# Configuration for each problem type
PROBLEM_TYPE_CONFIGS: Dict[str, ProblemTypeConfig] = {
    # Chapter 1: Basics
    'variables': ProblemTypeConfig(
        latex_fontsize=21,
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=16,
        vertical_spacing=0.8,
        default_num_problems={'easy': 16, 'medium': 16, 'hard': 16, 'challenge': 8},
        min_spacing=0.8,
        max_spacing=2.0,
        instructions="Answer each question about variables."
    ),

    'exponents': ProblemTypeConfig(
        latex_fontsize=21,
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=16,
        vertical_spacing=0.8,
        default_num_problems={'easy': 16, 'medium': 16, 'hard': 16, 'challenge': 8},
        min_spacing=0.7,
        max_spacing=2.0,
        instructions="Evaluate each exponential expression."
    ),

    'evaluating_expressions': ProblemTypeConfig(
        latex_fontsize=21,
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=16,
        vertical_spacing=0.8,
        default_num_problems={'easy': 16, 'medium': 16, 'hard': 16, 'challenge': 8},
        min_spacing=0.8,
        max_spacing=2.0,
        instructions="Evaluate each expression using the given value."
    ),

    'substitution': ProblemTypeConfig(
        latex_fontsize=21,
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=16,
        vertical_spacing=0.8,
        default_num_problems={'easy': 16, 'medium': 16, 'hard': 16, 'challenge': 8},
        min_spacing=0.8,
        max_spacing=2.0,
        instructions="Substitute the given value and solve."
    ),

    'combining_like_terms': ProblemTypeConfig(
        latex_fontsize=21,
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=16,
        vertical_spacing=0.8,
        default_num_problems={'easy': 16, 'medium': 16, 'hard': 16, 'challenge': 8},
        min_spacing=0.8,
        max_spacing=2.0,
        instructions="Simplify by combining like terms."
    ),

    # Chapter 2: Equations
    'equations_intro': ProblemTypeConfig(
        latex_fontsize=21,
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=16,
        vertical_spacing=0.8,
        default_num_problems={'easy': 16, 'medium': 16, 'hard': 16, 'challenge': 8},
        min_spacing=0.8,
        max_spacing=2.0,
        instructions="Answer each question about equations."
    ),

    'inputs_outputs': ProblemTypeConfig(
        latex_fontsize=21,
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=16,
        vertical_spacing=0.8,
        default_num_problems={'easy': 16, 'medium': 16, 'hard': 16, 'challenge': 8},
        min_spacing=0.8,
        max_spacing=2.0,
        instructions="Find the output or input using the given rule."
    ),

    'solutions': ProblemTypeConfig(
        latex_fontsize=21,
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=16,
        vertical_spacing=0.8,
        default_num_problems={'easy': 16, 'medium': 16, 'hard': 16, 'challenge': 8},
        min_spacing=0.8,
        max_spacing=2.0,
        instructions="Determine if the value is a solution or find the solution."
    ),

    'variables_both_sides': ProblemTypeConfig(
        latex_fontsize=21,
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=16,
        vertical_spacing=0.8,
        default_num_problems={'easy': 16, 'medium': 16, 'hard': 16, 'challenge': 8},
        min_spacing=0.8,
        max_spacing=2.0,
        instructions="Solve each equation with variables on both sides."
    ),

    'linear_equation': ProblemTypeConfig(
        latex_fontsize=21,  # Standard equation font (1.75x ratio with 12pt problem numbers)
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=15,
        vertical_spacing=0.8,  # DEPRECATED: kept for backwards compatibility
        default_num_problems=16,
        min_spacing=0.6,  # Minimum spacing to prevent cramping
        max_spacing=2.5,  # Maximum spacing to allow proper stretching with fewer problems
        instructions="Solve for x. Show your work."
    ),

    'system_of_equations': ProblemTypeConfig(
        latex_fontsize=21,  # Standard equation font (1.75x ratio with 12pt problem numbers)
        image_width=3.5,
        image_height=1.1,
        vertical_offset=0.55,
        problems_per_page=8,
        vertical_spacing=1.3,  # DEPRECATED: kept for backwards compatibility
        default_num_problems={'easy': 16, 'medium': 16, 'hard': 16, 'challenge': 8},
        min_spacing=1.0,  # Minimum spacing to prevent cramping
        max_spacing=2.0,  # Maximum spacing to prevent excessive spreading
        instructions="Solve each system of equations. Show your work."
    ),

    'inequality': ProblemTypeConfig(
        latex_fontsize=21,  # Standard equation font (1.75x ratio with 12pt problem numbers)
        image_width=3.0,    # Smaller width for 2-column layout
        image_height=1.0,   # Height for number line
        vertical_offset=0.5,
        problems_per_page=8,  # 2 columns x 4 rows
        vertical_spacing=2.0,  # DEPRECATED: kept for backwards compatibility
        default_num_problems=16,
        min_spacing=1.5,  # Minimum spacing to prevent cramping (larger for number lines)
        max_spacing=2.5,  # Maximum spacing to prevent excessive spreading
        instructions="Solve each inequality and graph the solution on the number line."
    ),

    'compound_inequality': ProblemTypeConfig(
        latex_fontsize=21,  # Standard equation font (1.75x ratio with 12pt problem numbers)
        image_width=3.0,    # Smaller width for 2-column layout
        image_height=1.0,   # Height for number line
        vertical_offset=0.5,
        problems_per_page=8,  # 2 columns x 4 rows
        vertical_spacing=2.0,  # DEPRECATED: kept for backwards compatibility
        default_num_problems=16,
        min_spacing=1.5,  # Minimum spacing to prevent cramping (larger for number lines)
        max_spacing=2.5,  # Maximum spacing to prevent excessive spreading
        instructions="Solve each compound inequality and graph the solution on the number line."
    ),

    'compound_inequality_and': ProblemTypeConfig(
        latex_fontsize=21,  # Standard equation font (1.75x ratio with 12pt problem numbers)
        image_width=3.0,    # Smaller width for 2-column layout
        image_height=1.0,   # Height for number line
        vertical_offset=0.5,
        problems_per_page=8,  # 2 columns x 4 rows
        vertical_spacing=2.0,  # DEPRECATED: kept for backwards compatibility
        default_num_problems=16,
        min_spacing=1.5,  # Minimum spacing to prevent cramping (larger for number lines)
        max_spacing=2.5,  # Maximum spacing to prevent excessive spreading
        instructions="Solve each compound inequality (AND type) and graph the solution on the number line."
    ),

    'compound_inequality_or': ProblemTypeConfig(
        latex_fontsize=21,  # Standard equation font (1.75x ratio with 12pt problem numbers)
        image_width=3.0,    # Smaller width for 2-column layout
        image_height=1.0,   # Height for number line
        vertical_offset=0.5,
        problems_per_page=8,  # 2 columns x 4 rows
        vertical_spacing=2.0,  # DEPRECATED: kept for backwards compatibility
        default_num_problems=16,
        min_spacing=1.5,  # Minimum spacing to prevent cramping (larger for number lines)
        max_spacing=2.5,  # Maximum spacing to prevent excessive spreading
        instructions="Solve each compound inequality (OR type) and graph the solution on the number line."
    ),

    'properties_of_equality': ProblemTypeConfig(
        latex_fontsize=21,  # Standard equation font (1.75x ratio with 12pt problem numbers)
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=16,  # 2 columns x 8 rows
        vertical_spacing=1.0,  # DEPRECATED: kept for backwards compatibility
        default_num_problems={'easy': 16, 'medium': 16, 'hard': 16, 'challenge': 8},
        min_spacing=0.8,  # Minimum spacing
        max_spacing=2.0,  # Maximum spacing
        instructions="Solve for x. Identify the property of equality used."
    ),

    'properties_mult_div': ProblemTypeConfig(
        latex_fontsize=21,  # Standard equation font (1.75x ratio with 12pt problem numbers)
        image_width=2.5,    # Reduced width to match smaller font
        image_height=0.5,   # Reduced height to match smaller font
        vertical_offset=0.15,  # Reduced offset for better alignment
        problems_per_page=16,  # 2 columns x 8 rows
        vertical_spacing=1.0,  # DEPRECATED: kept for backwards compatibility
        default_num_problems={'easy': 16, 'medium': 16, 'hard': 16, 'challenge': 8},
        min_spacing=0.8,  # Minimum spacing
        max_spacing=2.0,  # Maximum spacing
        instructions="Solve for x. Identify which property of equality you used."
    ),

    'word_problems': ProblemTypeConfig(
        latex_fontsize=21,  # Standard equation font (1.75x ratio with 12pt problem numbers)
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=8,  # 8 word problems per page
        vertical_spacing=1.2,  # DEPRECATED: kept for backwards compatibility
        default_num_problems={'easy': 8, 'medium': 8, 'hard': 8, 'challenge': 8},
        min_spacing=1.5,  # Larger minimum spacing for word problems
        max_spacing=3.0,  # Maximum spacing
        instructions="Read each word problem carefully. Write an equation and solve for x."
    ),

    'multistep_equations': ProblemTypeConfig(
        latex_fontsize=21,  # Standard equation font (1.75x ratio with 12pt problem numbers)
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=16,  # 2 columns x 8 rows
        vertical_spacing=1.0,  # DEPRECATED: kept for backwards compatibility
        default_num_problems=16,
        min_spacing=0.6,  # Reduced minimum spacing to match linear equations
        max_spacing=1.5,  # Reduced maximum spacing to match linear equations
        instructions="Solve each two-step equation. Show your work."
    ),

    'graphing_points': ProblemTypeConfig(
        latex_fontsize=18,  # N/A for graphing (images are coordinate planes)
        image_width=3.0,    # Width for coordinate plane graph
        image_height=3.0,   # Height for coordinate plane graph (square)
        vertical_offset=0.3,
        problems_per_page=4,  # 2 columns x 2 rows for graphs
        vertical_spacing=1.5,  # DEPRECATED: kept for backwards compatibility
        default_num_problems={'easy': 8, 'medium': 8, 'hard': 8, 'challenge': 4},
        min_spacing=1.2,  # Minimum spacing for graphs
        max_spacing=2.5,  # Maximum spacing
        instructions="Plot each point on the coordinate plane. Label each point with its letter and coordinates."
    ),

    'graphing_lines': ProblemTypeConfig(
        latex_fontsize=18,  # N/A for graphing (images are coordinate planes)
        image_width=3.0,    # Width for coordinate plane graph
        image_height=3.0,   # Height for coordinate plane graph (square)
        vertical_offset=0.3,
        problems_per_page=4,  # 2 columns x 2 rows for graphs
        vertical_spacing=1.5,  # DEPRECATED: kept for backwards compatibility
        default_num_problems={'easy': 8, 'medium': 8, 'hard': 8, 'challenge': 4},
        min_spacing=3.8,  # Minimum spacing for graphs
        max_spacing=4.5,  # Maximum spacing
        instructions="Graph the line through the two given points."
    ),

    'slope_intercept': ProblemTypeConfig(
        latex_fontsize=18,  # N/A for graphing (images are coordinate planes)
        image_width=3.0,    # Width for coordinate plane graph
        image_height=3.0,   # Height for coordinate plane graph (square)
        vertical_offset=0.3,
        problems_per_page=4,  # 2 columns x 2 rows for graphs
        vertical_spacing=1.5,  # DEPRECATED: kept for backwards compatibility
        default_num_problems={'easy': 8, 'medium': 8, 'hard': 8, 'challenge': 4},
        min_spacing=3.8,  # Minimum spacing for graphs
        max_spacing=4.5,  # Maximum spacing
        instructions="Graph each line using the slope-intercept form y = mx + b."
    ),

    'point_slope': ProblemTypeConfig(
        latex_fontsize=18,  # N/A for graphing (images are coordinate planes)
        image_width=3.0,    # Width for coordinate plane graph
        image_height=3.0,   # Height for coordinate plane graph (square)
        vertical_offset=0.3,
        problems_per_page=4,  # 2 columns x 2 rows for graphs
        vertical_spacing=1.5,  # DEPRECATED: kept for backwards compatibility
        default_num_problems={'easy': 8, 'medium': 8, 'hard': 8, 'challenge': 4},
        min_spacing=3.8,  # Minimum spacing for graphs
        max_spacing=4.5,  # Maximum spacing
        instructions="Graph each line using the point-slope form y - y₁ = m(x - x₁)."
    ),

    'standard_form': ProblemTypeConfig(
        latex_fontsize=18,  # N/A for graphing (images are coordinate planes)
        image_width=3.0,    # Width for coordinate plane graph
        image_height=3.0,   # Height for coordinate plane graph (square)
        vertical_offset=0.3,
        problems_per_page=4,  # 2 columns x 2 rows for graphs
        vertical_spacing=1.5,  # DEPRECATED: kept for backwards compatibility
        default_num_problems={'easy': 8, 'medium': 8, 'hard': 8, 'challenge': 4},
        min_spacing=3.8,  # Minimum spacing for graphs
        max_spacing=4.5,  # Maximum spacing
        instructions="Graph each line using the standard form Ax + By = C."
    ),

    'graphing_systems': ProblemTypeConfig(
        latex_fontsize=18,  # N/A for graphing (equations shown on graph)
        image_width=3.0,    # Width for coordinate plane graph
        image_height=3.0,   # Height for coordinate plane graph (square)
        vertical_offset=0.3,
        problems_per_page=4,  # 2 columns x 2 rows for graphs
        vertical_spacing=1.5,  # DEPRECATED: kept for backwards compatibility
        default_num_problems={'easy': 8, 'medium': 8, 'hard': 8, 'challenge': 4},
        min_spacing=3.8,  # Minimum spacing for graphs (same as graphing_points)
        max_spacing=4.5,  # Maximum spacing
        instructions="Graph both equations on the same coordinate plane. Find and label the intersection point."
    ),

    'graphing_parabolas': ProblemTypeConfig(
        latex_fontsize=18,  # N/A for graphing (equation shown on graph)
        image_width=3.0,    # Width for coordinate plane graph
        image_height=3.0,   # Height for coordinate plane graph (square)
        vertical_offset=0.3,
        problems_per_page=4,  # 2 columns x 2 rows for graphs
        vertical_spacing=1.5,  # DEPRECATED: kept for backwards compatibility
        default_num_problems={'easy': 8, 'medium': 8, 'hard': 8, 'challenge': 4},
        min_spacing=3.8,  # Minimum spacing for graphs (same as other graphing types)
        max_spacing=4.5,  # Maximum spacing
        instructions="Graph the parabola and identify the vertex."
    ),

    # Unit 11: More Quadratics
    'completing_the_square': ProblemTypeConfig(
        latex_fontsize=21,  # Standard equation font
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=16,  # 2 columns x 8 rows
        vertical_spacing=1.0,  # DEPRECATED: kept for backwards compatibility
        default_num_problems={'easy': 16, 'medium': 16, 'hard': 16, 'challenge': 8},
        min_spacing=0.8,
        max_spacing=2.0,
        instructions="Complete the square and write in vertex form."
    ),

    'quadratic_formula': ProblemTypeConfig(
        latex_fontsize=21,  # Standard equation font
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=16,  # 2 columns x 8 rows
        vertical_spacing=1.0,  # DEPRECATED: kept for backwards compatibility
        default_num_problems={'easy': 16, 'medium': 16, 'hard': 16, 'challenge': 8},
        min_spacing=0.8,
        max_spacing=2.0,
        instructions="Solve using the quadratic formula: x = (-b ± √(b²-4ac)) / 2a"
    ),

    # Unit 12: Quadratic Functions
    'quadratic_functions': ProblemTypeConfig(
        latex_fontsize=21,  # Standard equation font
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=16,  # 2 columns x 8 rows
        vertical_spacing=1.0,  # DEPRECATED: kept for backwards compatibility
        default_num_problems={'easy': 16, 'medium': 16, 'hard': 12, 'challenge': 8},
        min_spacing=0.8,
        max_spacing=2.0,
        instructions="Analyze the quadratic function and answer the question."
    ),

    # Unit 13: Sequences
    'arithmetic_sequences': ProblemTypeConfig(
        latex_fontsize=21,  # Standard equation font
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=16,  # 2 columns x 8 rows
        vertical_spacing=1.0,  # DEPRECATED: kept for backwards compatibility
        default_num_problems={'easy': 16, 'medium': 16, 'hard': 12, 'challenge': 8},
        min_spacing=0.8,
        max_spacing=2.0,
        instructions="Work with the arithmetic sequence to answer each question."
    ),

    # Future problem types can be added here
}


def get_config(problem_type: str) -> ProblemTypeConfig:
    """
    Get configuration for a problem type.

    Args:
        problem_type: Type identifier (e.g., 'linear_equation', 'system_of_equations')

    Returns:
        ProblemTypeConfig object

    Raises:
        KeyError: If problem type not found
    """
    if problem_type not in PROBLEM_TYPE_CONFIGS:
        raise KeyError(f"Unknown problem type: {problem_type}. "
                      f"Available types: {list(PROBLEM_TYPE_CONFIGS.keys())}")

    return PROBLEM_TYPE_CONFIGS[problem_type]


def list_problem_types() -> list:
    """Get list of all configured problem types."""
    return list(PROBLEM_TYPE_CONFIGS.keys())


# Example usage
if __name__ == "__main__":
    print("Configured Problem Types:")
    print("=" * 50)

    for ptype in list_problem_types():
        config = get_config(ptype)
        print(f"\n{ptype}:")
        print(f"  LaTeX font size: {config.latex_fontsize}pt")
        print(f"  Image size: {config.image_width}\" x {config.image_height}\"")
        print(f"  Problems per page: {config.problems_per_page}")
        print(f"  Default # problems: {config.default_num_problems}")
        print(f"  Spacing: {config.vertical_spacing}\"")
        print(f"  Instructions: {config.instructions}")
