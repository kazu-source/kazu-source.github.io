"""
Graphing utilities for worksheet generation.

This module provides functions to create various types of graphs and coordinate planes
for embedding in PDF worksheets.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np
from io import BytesIO
from PIL import Image


class CoordinatePlane:
    """Class for creating and managing coordinate plane graphs."""

    def __init__(self, x_min=-10, x_max=10, y_min=-10, y_max=10,
                 grid=True, first_quadrant_only=False):
        """
        Initialize a coordinate plane.

        Args:
            x_min: Minimum x value
            x_max: Maximum x value
            y_min: Minimum y value
            y_max: Maximum y value
            grid: Whether to show grid lines
            first_quadrant_only: If True, only show first quadrant (x≥0, y≥0)
        """
        if first_quadrant_only:
            self.x_min = 0
            self.x_max = max(10, x_max)
            self.y_min = 0
            self.y_max = max(10, y_max)
        else:
            self.x_min = x_min
            self.x_max = x_max
            self.y_min = y_min
            self.y_max = y_max

        self.grid = grid
        self.first_quadrant_only = first_quadrant_only

    def create_figure(self, figsize=(6, 6), dpi=150):
        """
        Create a matplotlib figure with the coordinate plane.

        Args:
            figsize: Tuple of (width, height) in inches
            dpi: Dots per inch for resolution

        Returns:
            fig, ax: Matplotlib figure and axes objects
        """
        fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

        # Set axis limits with padding
        ax.set_xlim(self.x_min - 0.5, self.x_max + 0.5)
        ax.set_ylim(self.y_min - 0.5, self.y_max + 0.5)

        # Draw axes
        ax.axhline(y=0, color='black', linewidth=1.5, zorder=3)
        ax.axvline(x=0, color='black', linewidth=1.5, zorder=3)

        # Add arrows to axes
        ax.annotate('', xy=(self.x_max + 0.3, 0), xytext=(self.x_max, 0),
                   arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
        ax.annotate('', xy=(0, self.y_max + 0.3), xytext=(0, self.y_max),
                   arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

        # Add axis labels
        ax.text(self.x_max + 0.5, -0.5, 'x', fontsize=12, ha='center', va='top')
        ax.text(0.5, self.y_max + 0.5, 'y', fontsize=12, ha='left', va='center')

        # Set up grid
        if self.grid:
            ax.grid(True, which='both', linestyle='--', linewidth=0.5,
                   alpha=0.7, zorder=0)
            ax.set_axisbelow(True)

        # Move spines to center (axes at origin)
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        # Set integer ticks
        x_ticks = np.arange(self.x_min, self.x_max + 1, 1)
        y_ticks = np.arange(self.y_min, self.y_max + 1, 1)
        ax.set_xticks(x_ticks)
        ax.set_yticks(y_ticks)

        # Remove tick labels at origin to avoid clutter
        x_labels = [str(int(x)) if x != 0 else '' for x in x_ticks]
        y_labels = [str(int(y)) if y != 0 else '' for y in y_ticks]
        ax.set_xticklabels(x_labels, fontsize=9)
        ax.set_yticklabels(y_labels, fontsize=9)

        # Position tick labels on the axes
        ax.xaxis.set_label_position('bottom')
        ax.yaxis.set_label_position('left')

        # Move x-axis tick labels to just below the x-axis
        ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True)
        # Move y-axis tick labels to just left of the y-axis
        ax.tick_params(axis='y', which='both', left=True, right=False, labelleft=True)

        # Set aspect ratio to equal
        ax.set_aspect('equal', adjustable='box')

        return fig, ax

    def plot_point(self, ax, x, y, label=None, color='blue', size=50, marker='o'):
        """
        Plot a point on the coordinate plane.

        Args:
            ax: Matplotlib axes object
            x: X coordinate
            y: Y coordinate
            label: Optional label for the point
            color: Point color
            size: Point size
            marker: Marker style
        """
        ax.scatter([x], [y], color=color, s=size, marker=marker, zorder=5,
                  edgecolors='black', linewidths=1)

        if label:
            ax.annotate(label, xy=(x, y), xytext=(5, 5),
                       textcoords='offset points', fontsize=10,
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                               edgecolor='black', alpha=0.8))

    def plot_line_from_equation(self, ax, slope=None, y_intercept=None,
                               point=None, standard_form=None,
                               color='red', linewidth=2, linestyle='-', label=None):
        """
        Plot a line from various equation forms.

        Args:
            ax: Matplotlib axes object
            slope: Slope (for slope-intercept or point-slope)
            y_intercept: Y-intercept (for slope-intercept form y = mx + b)
            point: Tuple (x, y) for point-slope form
            standard_form: Tuple (A, B, C) for Ax + By = C
            color: Line color
            linewidth: Line width
            linestyle: Line style ('-' solid, '--' dashed)
            label: Optional label for the line
        """
        x_vals = np.linspace(self.x_min - 1, self.x_max + 1, 500)

        # Slope-intercept form: y = mx + b
        if slope is not None and y_intercept is not None:
            y_vals = slope * x_vals + y_intercept

        # Point-slope form: y - y1 = m(x - x1)
        elif slope is not None and point is not None:
            x1, y1 = point
            y_vals = slope * (x_vals - x1) + y1

        # Standard form: Ax + By = C
        elif standard_form is not None:
            A, B, C = standard_form
            if B != 0:
                y_vals = (C - A * x_vals) / B
            else:
                # Vertical line: x = C/A
                x_val = C / A if A != 0 else 0
                ax.axvline(x=x_val, color=color, linewidth=linewidth,
                          linestyle=linestyle, label=label, zorder=4)
                return
        else:
            raise ValueError("Must provide either (slope, y_intercept), "
                           "(slope, point), or standard_form")

        ax.plot(x_vals, y_vals, color=color, linewidth=linewidth,
               linestyle=linestyle, label=label, zorder=4)

    def plot_parabola(self, ax, a=1, h=0, k=0, color='purple',
                     linewidth=2, linestyle='-', label=None):
        """
        Plot a parabola in vertex form: y = a(x - h)² + k

        Args:
            ax: Matplotlib axes object
            a: Vertical stretch factor
            h: X-coordinate of vertex
            k: Y-coordinate of vertex
            color: Line color
            linewidth: Line width
            linestyle: Line style
            label: Optional label
        """
        x_vals = np.linspace(self.x_min - 1, self.x_max + 1, 500)
        y_vals = a * (x_vals - h)**2 + k

        ax.plot(x_vals, y_vals, color=color, linewidth=linewidth,
               linestyle=linestyle, label=label, zorder=4)

        # Plot vertex
        self.plot_point(ax, h, k, color=color, size=60, marker='o')

    def plot_exponential(self, ax, a=1, b=2, h=0, k=0, color='green',
                        linewidth=2, linestyle='-', label=None):
        """
        Plot an exponential function: y = a * b^(x - h) + k

        Args:
            ax: Matplotlib axes object
            a: Vertical stretch factor
            b: Base (b > 0, b ≠ 1)
            h: Horizontal shift
            k: Vertical shift
            color: Line color
            linewidth: Line width
            linestyle: Line style
            label: Optional label
        """
        x_vals = np.linspace(self.x_min - 1, self.x_max + 1, 500)
        y_vals = a * (b ** (x_vals - h)) + k

        ax.plot(x_vals, y_vals, color=color, linewidth=linewidth,
               linestyle=linestyle, label=label, zorder=4)

    def plot_absolute_value(self, ax, a=1, h=0, k=0, color='orange',
                           linewidth=2, linestyle='-', label=None):
        """
        Plot an absolute value function: y = a|x - h| + k

        Args:
            ax: Matplotlib axes object
            a: Vertical stretch factor
            h: X-coordinate of vertex
            k: Y-coordinate of vertex
            color: Line color
            linewidth: Line width
            linestyle: Line style
            label: Optional label
        """
        x_vals = np.linspace(self.x_min - 1, self.x_max + 1, 500)
        y_vals = a * np.abs(x_vals - h) + k

        ax.plot(x_vals, y_vals, color=color, linewidth=linewidth,
               linestyle=linestyle, label=label, zorder=4)

        # Plot vertex
        self.plot_point(ax, h, k, color=color, size=60, marker='o')

    def shade_inequality(self, ax, slope=None, y_intercept=None,
                        standard_form=None, inequality_type='>',
                        color='blue', alpha=0.3):
        """
        Shade a region for a linear inequality.

        Args:
            ax: Matplotlib axes object
            slope: Slope (for y = mx + b form)
            y_intercept: Y-intercept
            standard_form: Tuple (A, B, C) for Ax + By > C (or <, ≥, ≤)
            inequality_type: '>', '<', '>=', '<='
            color: Shading color
            alpha: Transparency (0-1)
        """
        x_vals = np.linspace(self.x_min - 1, self.x_max + 1, 500)

        # Get y values for the boundary line
        if slope is not None and y_intercept is not None:
            y_vals = slope * x_vals + y_intercept
        elif standard_form is not None:
            A, B, C = standard_form
            if B != 0:
                y_vals = (C - A * x_vals) / B
            else:
                # Handle vertical line case
                return
        else:
            raise ValueError("Must provide either (slope, y_intercept) or standard_form")

        # Determine which region to shade
        if inequality_type in ['>', '>=']:
            ax.fill_between(x_vals, y_vals, self.y_max + 1,
                           color=color, alpha=alpha, zorder=1)
        else:  # '<' or '<='
            ax.fill_between(x_vals, y_vals, self.y_min - 1,
                           color=color, alpha=alpha, zorder=1)

    def add_slope_triangle(self, ax, x1, y1, slope, color='black'):
        """
        Draw a slope triangle (rise over run) at a point.

        Args:
            ax: Matplotlib axes object
            x1: Starting x coordinate
            y1: Starting y coordinate
            slope: Slope (rise/run)
            color: Triangle color
        """
        # Calculate rise and run
        if isinstance(slope, (int, float)):
            run = 1
            rise = slope
        else:
            # Assume slope is already a fraction (rise, run)
            rise, run = slope

        # Draw the triangle
        x_points = [x1, x1 + run, x1 + run, x1]
        y_points = [y1, y1, y1 + rise, y1]

        ax.plot(x_points, y_points, color=color, linewidth=1.5, zorder=6)

        # Add labels
        ax.text(x1 + run/2, y1 - 0.3, f'run = {run}',
               fontsize=9, ha='center', va='top')
        ax.text(x1 + run + 0.3, y1 + rise/2, f'rise = {rise}',
               fontsize=9, ha='left', va='center')

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
                   facecolor='white', edgecolor='none')
        buf.seek(0)
        img = Image.open(buf)
        plt.close(fig)
        return img


def create_blank_coordinate_plane(x_min=-10, x_max=10, y_min=-10, y_max=10,
                                  first_quadrant_only=False, figsize=(6, 6)):
    """
    Create a blank coordinate plane as a PIL Image.

    Args:
        x_min: Minimum x value
        x_max: Maximum x value
        y_min: Minimum y value
        y_max: Maximum y value
        first_quadrant_only: If True, only show first quadrant
        figsize: Figure size in inches

    Returns:
        PIL Image object
    """
    plane = CoordinatePlane(x_min, x_max, y_min, y_max,
                           grid=True, first_quadrant_only=first_quadrant_only)
    fig, ax = plane.create_figure(figsize=figsize)
    return plane.render_to_image(fig)


def graph_points(points, labels=None, x_min=-10, x_max=10, y_min=-10, y_max=10,
                first_quadrant_only=False, figsize=(6, 6)):
    """
    Create a graph with plotted points.

    Args:
        points: List of (x, y) tuples
        labels: Optional list of labels for each point
        x_min, x_max, y_min, y_max: Axis bounds
        first_quadrant_only: If True, only show first quadrant
        figsize: Figure size in inches

    Returns:
        PIL Image object
    """
    plane = CoordinatePlane(x_min, x_max, y_min, y_max,
                           grid=True, first_quadrant_only=first_quadrant_only)
    fig, ax = plane.create_figure(figsize=figsize)

    for i, (x, y) in enumerate(points):
        label = labels[i] if labels and i < len(labels) else None
        plane.plot_point(ax, x, y, label=label)

    return plane.render_to_image(fig)


def graph_line(slope=None, y_intercept=None, point=None, standard_form=None,
              x_min=-10, x_max=10, y_min=-10, y_max=10,
              show_intercepts=False, show_slope_triangle=False,
              first_quadrant_only=False, figsize=(6, 6)):
    """
    Create a graph of a line.

    Args:
        slope: Slope (for slope-intercept or point-slope form)
        y_intercept: Y-intercept (for slope-intercept form)
        point: Tuple (x, y) for point-slope form
        standard_form: Tuple (A, B, C) for Ax + By = C
        x_min, x_max, y_min, y_max: Axis bounds
        show_intercepts: If True, mark and label x and y intercepts
        show_slope_triangle: If True, show slope triangle
        first_quadrant_only: If True, only show first quadrant
        figsize: Figure size in inches

    Returns:
        PIL Image object
    """
    plane = CoordinatePlane(x_min, x_max, y_min, y_max,
                           grid=True, first_quadrant_only=first_quadrant_only)
    fig, ax = plane.create_figure(figsize=figsize)

    # Plot the line
    plane.plot_line_from_equation(ax, slope=slope, y_intercept=y_intercept,
                                 point=point, standard_form=standard_form,
                                 color='red', linewidth=2)

    # Show intercepts if requested
    if show_intercepts and slope is not None and y_intercept is not None:
        # Y-intercept
        plane.plot_point(ax, 0, y_intercept, label=f'(0, {y_intercept})',
                        color='blue')
        # X-intercept (where y = 0)
        if slope != 0:
            x_intercept = -y_intercept / slope
            plane.plot_point(ax, x_intercept, 0,
                           label=f'({x_intercept:.1f}, 0)', color='green')

    # Show slope triangle if requested
    if show_slope_triangle and slope is not None:
        # Pick a good point on the line
        if y_intercept is not None:
            x_start = 0 if 0 >= x_min and 0 <= x_max else x_min + 2
            y_start = slope * x_start + y_intercept
        elif point is not None:
            x_start, y_start = point
        else:
            x_start, y_start = 0, 0

        plane.add_slope_triangle(ax, x_start, y_start, slope)

    return plane.render_to_image(fig)


def graph_inequality(slope=None, y_intercept=None, standard_form=None,
                    inequality_type='>', x_min=-10, x_max=10, y_min=-10, y_max=10,
                    first_quadrant_only=False, figsize=(6, 6)):
    """
    Create a graph of a linear inequality with shading.

    Args:
        slope: Slope
        y_intercept: Y-intercept
        standard_form: Tuple (A, B, C) for Ax + By > C
        inequality_type: '>', '<', '>=', '<='
        x_min, x_max, y_min, y_max: Axis bounds
        first_quadrant_only: If True, only show first quadrant
        figsize: Figure size in inches

    Returns:
        PIL Image object
    """
    plane = CoordinatePlane(x_min, x_max, y_min, y_max,
                           grid=True, first_quadrant_only=first_quadrant_only)
    fig, ax = plane.create_figure(figsize=figsize)

    # Determine line style (solid for ≥/≤, dashed for >/<)
    linestyle = '-' if inequality_type in ['>=', '<='] else '--'

    # Plot the boundary line
    plane.plot_line_from_equation(ax, slope=slope, y_intercept=y_intercept,
                                 standard_form=standard_form,
                                 color='red', linewidth=2, linestyle=linestyle)

    # Shade the region
    plane.shade_inequality(ax, slope=slope, y_intercept=y_intercept,
                          standard_form=standard_form,
                          inequality_type=inequality_type,
                          color='blue', alpha=0.2)

    return plane.render_to_image(fig)


if __name__ == "__main__":
    # Test the graphing utilities
    print("Testing graphing utilities...")

    # Test 1: Blank coordinate plane
    img = create_blank_coordinate_plane()
    img.save("test_blank_plane.png")
    print("[OK] Created blank coordinate plane")

    # Test 2: Plot points
    img = graph_points([(2, 3), (-3, 4), (1, -2)],
                      labels=["A(2,3)", "B(-3,4)", "C(1,-2)"])
    img.save("test_points.png")
    print("[OK] Created point graph")

    # Test 3: Graph a line (slope-intercept)
    img = graph_line(slope=2, y_intercept=1, show_intercepts=True,
                    show_slope_triangle=True)
    img.save("test_line.png")
    print("[OK] Created line graph")

    # Test 4: Graph an inequality
    img = graph_inequality(slope=1, y_intercept=-2, inequality_type='>=')
    img.save("test_inequality.png")
    print("[OK] Created inequality graph")

    # Test 5: First quadrant only
    img = create_blank_coordinate_plane(x_max=15, y_max=15, first_quadrant_only=True)
    img.save("test_first_quadrant.png")
    print("[OK] Created first quadrant plane")

    print("\nAll tests passed! Check the generated PNG files.")
