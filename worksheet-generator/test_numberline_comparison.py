"""
Test script to compare old vs new number line styles.
Shows side-by-side comparison of styling approaches.
"""

import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from PIL import Image

from numberline_utils import create_blank_numberline, create_numberline_with_solution


def create_old_style_numberline(min_val=-10, max_val=10, boundary_value=3,
                                inequality_type='>=', show_solution=True):
    """Create a number line using the OLD thick style."""
    fig, ax = plt.subplots(figsize=(8, 1.2), dpi=150)

    ax.set_xlim(min_val - 0.5, max_val + 0.5)
    ax.set_ylim(-1, 1)

    # OLD STYLE - Thick lines
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['bottom'].set_linewidth(3)  # THICK
    ax.yaxis.set_visible(False)

    ax.set_xticks(range(min_val, max_val + 1))
    ax.tick_params(axis='x', width=3, length=10, labelsize=14)  # THICK & LARGE

    if show_solution:
        is_equal = inequality_type in ['<=', '>=', '\\leq', '\\geq']
        if is_equal:
            ax.plot(boundary_value, 0, 'o', markersize=15, color='blue',
                   markerfacecolor='blue', markeredgewidth=3)
        else:
            ax.plot(boundary_value, 0, 'o', markersize=15, color='blue',
                   fillstyle='none', markeredgewidth=3)

        is_left = inequality_type in ['<', '<=', '\\lt', '\\leq']
        if is_left:
            ax.annotate('', xy=(min_val - 0.3, 0), xytext=(boundary_value, 0),
                       arrowprops=dict(arrowstyle='->', color='blue', lw=4))  # THICK
        else:
            ax.annotate('', xy=(max_val + 0.3, 0), xytext=(boundary_value, 0),
                       arrowprops=dict(arrowstyle='->', color='blue', lw=4))  # THICK

    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png', bbox_inches='tight',
                pad_inches=0.1, facecolor='white')
    buf.seek(0)
    img = Image.open(buf)
    plt.close(fig)
    return img


# Test 1: Blank number lines comparison
print("Generating comparison images...")

print("\n1. Blank number line comparison")
old_blank = create_old_style_numberline(-5, 10, 3, '>=', show_solution=False)
old_blank.save("comparison_old_blank.png")
print("   [OK] Old style blank: comparison_old_blank.png")

new_blank = create_blank_numberline(-5, 10)
new_blank.save("comparison_new_blank.png")
print("   [OK] New style blank: comparison_new_blank.png")

# Test 2: Number line with solution (x >= 3)
print("\n2. Number line with solution (x >= 3)")
old_solution = create_old_style_numberline(-5, 10, 3, '>=', show_solution=True)
old_solution.save("comparison_old_solution_gte.png")
print("   [OK] Old style (x >= 3): comparison_old_solution_gte.png")

new_solution = create_numberline_with_solution(-5, 10, 3, '>=')
new_solution.save("comparison_new_solution_gte.png")
print("   [OK] New style (x >= 3): comparison_new_solution_gte.png")

# Test 3: Number line with solution (x < -2)
print("\n3. Number line with solution (x < -2)")
old_lt = create_old_style_numberline(-10, 5, -2, '<', show_solution=True)
old_lt.save("comparison_old_solution_lt.png")
print("   [OK] Old style (x < -2): comparison_old_solution_lt.png")

new_lt = create_numberline_with_solution(-10, 5, -2, '<')
new_lt.save("comparison_new_solution_lt.png")
print("   [OK] New style (x < -2): comparison_new_solution_lt.png")

print("\n" + "="*60)
print("STYLE COMPARISON SUMMARY")
print("="*60)
print("\nOLD STYLE (thick/bold):")
print("  - Line width: 3")
print("  - Tick width: 3, length: 10")
print("  - Label size: 14")
print("  - Point marker size: 15")
print("  - Arrow line width: 4")
print("  - Color: Blue")

print("\nNEW STYLE (matches coordinate planes):")
print("  - Line width: 1.5")
print("  - Tick width: 1.5, length: 8")
print("  - Label size: 9")
print("  - Point marker size: 10")
print("  - Arrow line width: 2")
print("  - Color: Blue")

print("\nKEY DIFFERENCES:")
print("  - More refined, less bold appearance")
print("  - Matches coordinate plane axis styling")
print("  - Better visual consistency across worksheet types")
print("  - Smaller text matches coordinate plane tick labels")

print("\n" + "="*60)
print("Files generated for comparison:")
print("  OLD: comparison_old_blank.png, comparison_old_solution_*.png")
print("  NEW: comparison_new_blank.png, comparison_new_solution_*.png")
print("="*60)
