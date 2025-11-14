"""
Configuration for worksheet generation.
Centralizes all rendering settings for different problem types.
"""

from dataclasses import dataclass
from typing import Dict


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
    default_num_problems: int  # Default number of problems for new worksheets

    # Dynamic spacing constraints
    min_spacing: float  # Minimum vertical spacing (inches) - prevents cramping
    max_spacing: float  # Maximum vertical spacing (inches) - prevents excessive spreading

    # Instructions text
    instructions: str  # Instruction text for worksheet

    def __repr__(self):
        return f"ProblemTypeConfig(fontsize={self.latex_fontsize}, {self.problems_per_page}/page, default={self.default_num_problems})"


# Configuration for each problem type
PROBLEM_TYPE_CONFIGS: Dict[str, ProblemTypeConfig] = {
    'linear_equation': ProblemTypeConfig(
        latex_fontsize=24,  # Larger font for better readability
        image_width=3.5,
        image_height=0.7,
        vertical_offset=0.3,
        problems_per_page=15,
        vertical_spacing=0.8,  # DEPRECATED: kept for backwards compatibility
        default_num_problems=10,  # Pure equations default to 10
        min_spacing=0.6,  # Minimum spacing to prevent cramping
        max_spacing=2.5,  # Maximum spacing to allow proper stretching with fewer problems
        instructions="Solve for x. Show your work."
    ),

    'system_of_equations': ProblemTypeConfig(
        latex_fontsize=22,  # Larger font for systems
        image_width=3.5,
        image_height=1.1,
        vertical_offset=0.55,
        problems_per_page=8,
        vertical_spacing=1.3,  # DEPRECATED: kept for backwards compatibility
        default_num_problems=8,  # Systems default to 8 problems
        min_spacing=1.0,  # Minimum spacing to prevent cramping
        max_spacing=2.0,  # Maximum spacing to prevent excessive spreading
        instructions="Solve each system of equations. Show your work."
    ),

    'inequality': ProblemTypeConfig(
        latex_fontsize=22,  # Larger font for better readability
        image_width=3.0,    # Smaller width for 2-column layout
        image_height=1.0,   # Height for number line
        vertical_offset=0.5,
        problems_per_page=8,  # 2 columns x 4 rows
        vertical_spacing=2.0,  # DEPRECATED: kept for backwards compatibility
        default_num_problems=8,  # Number line worksheets default to 8
        min_spacing=1.5,  # Minimum spacing to prevent cramping (larger for number lines)
        max_spacing=2.5,  # Maximum spacing to prevent excessive spreading
        instructions="Solve each inequality and graph the solution on the number line."
    ),

    # Future problem types can be added here
    # 'quadratic': ProblemTypeConfig(...),
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
