"""
Number line utilities for worksheet generation.

This module provides functions to create number lines with consistent styling
that matches the coordinate plane graphs.
"""

import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from PIL import Image


class NumberLine:
    """Class for creating and managing number line graphs."""

    def __init__(self, min_val=-10, max_val=10):
        """
        Initialize a number line.

        Args:
            min_val: Minimum value on number line
            max_val: Maximum value on number line
        """
        self.min_val = min_val
        self.max_val = max_val

    def create_figure(self, figsize=(8, 1.2), dpi=150):
        """
        Create a matplotlib figure with the number line.

        Args:
            figsize: Tuple of (width, height) in inches
            dpi: Dots per inch for resolution

        Returns:
            fig, ax: Matplotlib figure and axes objects
        """
        fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

        # Set axis limits with padding
        ax.set_xlim(self.min_val - 0.5, self.max_val + 0.5)
        ax.set_ylim(-1, 1)

        # Style the axes - only show bottom spine (the number line itself)
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['bottom'].set_linewidth(1.5)  # Match coordinate plane axes
        ax.yaxis.set_visible(False)

        # Set x-axis ticks and labels
        x_ticks = np.arange(self.min_val, self.max_val + 1, 1)
        ax.set_xticks(x_ticks)
        ax.tick_params(axis='x', width=1.5, length=8, labelsize=15)

        # Add arrows to both ends
        # Arrow on the right end
        ax.annotate('', xy=(self.max_val + 0.4, 0), xytext=(self.max_val + 0.1, 0),
                   arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
        # Arrow on the left end
        ax.annotate('', xy=(self.min_val - 0.4, 0), xytext=(self.min_val - 0.1, 0),
                   arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

        return fig, ax

    def plot_solution_point(self, ax, value, is_equal=True, color='blue'):
        """
        Plot a solution point on the number line.

        Args:
            ax: Matplotlib axes object
            value: X value for the point
            is_equal: If True, draw closed circle; if False, draw open circle
            color: Point color
        """
        if is_equal:
            # Closed circle (matches size of coordinate plane points proportionally)
            ax.plot(value, 0, 'o', markersize=10, color=color,
                   markerfacecolor=color, markeredgewidth=1, markeredgecolor='black')
        else:
            # Open circle
            ax.plot(value, 0, 'o', markersize=10, color=color,
                   fillstyle='none', markeredgewidth=1.5, markeredgecolor=color)

    def plot_solution_region(self, ax, boundary_value, is_left=True, color='blue'):
        """
        Plot an arrow showing the solution region.

        Args:
            ax: Matplotlib axes object
            boundary_value: The boundary value (where the arrow starts)
            is_left: If True, arrow points left; if False, arrow points right
            color: Arrow color
        """
        if is_left:
            # Arrow pointing left
            ax.annotate('', xy=(self.min_val - 0.3, 0), xytext=(boundary_value, 0),
                       arrowprops=dict(arrowstyle='->', color=color, lw=2))
        else:
            # Arrow pointing right
            ax.annotate('', xy=(self.max_val + 0.3, 0), xytext=(boundary_value, 0),
                       arrowprops=dict(arrowstyle='->', color=color, lw=2))

    def render_to_image(self, fig):
        """
        Render the matplotlib figure to a PIL Image.

        Args:
            fig: Matplotlib figure object

        Returns:
            PIL Image object
        """
        buf = BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight',
                   facecolor='white', edgecolor='none', pad_inches=0.1)
        buf.seek(0)
        img = Image.open(buf)
        plt.close(fig)
        return img


def create_blank_numberline(min_val=-10, max_val=10, figsize=(8, 1.2)):
    """
    Create a blank number line as a PIL Image.

    Args:
        min_val: Minimum value on number line
        max_val: Maximum value on number line
        figsize: Figure size in inches

    Returns:
        PIL Image object
    """
    line = NumberLine(min_val, max_val)
    fig, ax = line.create_figure(figsize=figsize)
    return line.render_to_image(fig)


def create_numberline_with_solution(min_val=-10, max_val=10,
                                     boundary_value=0,
                                     inequality_type='>=',
                                     figsize=(8, 1.2)):
    """
    Create a number line with inequality solution shown.

    Args:
        min_val: Minimum value on number line
        max_val: Maximum value on number line
        boundary_value: The boundary value for the inequality
        inequality_type: One of '<', '>', '<=', '>='
        figsize: Figure size in inches

    Returns:
        PIL Image object
    """
    line = NumberLine(min_val, max_val)
    fig, ax = line.create_figure(figsize=figsize)

    # Determine if closed or open circle
    is_equal = inequality_type in ['<=', '>=', '\\leq', '\\geq']

    # Determine direction of arrow
    is_left = inequality_type in ['<', '<=', '\\lt', '\\leq']

    # Plot the solution
    line.plot_solution_point(ax, boundary_value, is_equal=is_equal)
    line.plot_solution_region(ax, boundary_value, is_left=is_left)

    return line.render_to_image(fig)


if __name__ == "__main__":
    # Test the number line utilities
    print("Testing number line utilities...")

    # Test 1: Blank number line
    img = create_blank_numberline()
    img.save("test_blank_numberline.png")
    print("[OK] Created blank number line")

    # Test 2: Number line with solution (x >= 3)
    img = create_numberline_with_solution(
        min_val=-5, max_val=10,
        boundary_value=3,
        inequality_type='>='
    )
    img.save("test_numberline_gte.png")
    print("[OK] Created number line with x >= 3")

    # Test 3: Number line with solution (x < -2)
    img = create_numberline_with_solution(
        min_val=-10, max_val=5,
        boundary_value=-2,
        inequality_type='<'
    )
    img.save("test_numberline_lt.png")
    print("[OK] Created number line with x < -2")

    # Test 4: Compact range
    img = create_numberline_with_solution(
        min_val=-3, max_val=3,
        boundary_value=1,
        inequality_type='<='
    )
    img.save("test_numberline_compact.png")
    print("[OK] Created compact number line with x <= 1")

    print("\nAll tests passed! Check the generated PNG files.")
    print("\nStyle notes:")
    print("  - Line width: 1.5 (matches coordinate plane axes)")
    print("  - Tick width: 1.5, length: 8")
    print("  - Label size: 14 (larger for better readability)")
    print("  - Point marker size: 10 (proportional to coordinate plane)")
    print("  - Arrow line width: 2 (proportional to coordinate plane)")
    print("  - Arrows on both ends of number line")
