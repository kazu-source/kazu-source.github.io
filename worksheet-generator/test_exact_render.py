"""
Test the exact render path to see where it's failing.
"""

import matplotlib.pyplot as plt
import io
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

# Exact latex string from generator
latex_str = r"\frac{x}{9} = 7"

print(f"LaTeX string: {repr(latex_str)}")
print(f"Display: {latex_str}")
print()

# Test matplotlib rendering
print("Step 1: Create matplotlib figure...")
fig = plt.figure(figsize=(4, 0.5))
fig.patch.set_visible(False)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')

print(f"Step 2: Add text: ${latex_str}$")
text_obj = ax.text(0.05, 0.5, f'${latex_str}$', fontsize=24, verticalalignment='center')

# Save to buffer
buf = io.BytesIO()
print("Step 3: Save to buffer...")
try:
    plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', pad_inches=0.1,
                transparent=False, facecolor='white')
    buf.seek(0)
    print("  SUCCESS")
except Exception as e:
    print(f"  FAILED: {e}")
    import traceback
    traceback.print_exc()
    plt.close(fig)
    exit(1)

plt.close(fig)

# Create ImageReader
print("Step 4: Create ImageReader...")
try:
    img = ImageReader(buf)
    print("  SUCCESS")
except Exception as e:
    print(f"  FAILED: {e}")
    exit(1)

# Create PDF and draw
print("Step 5: Create PDF and draw image...")
c = canvas.Canvas("test_exact_render.pdf", pagesize=letter)
width, height = letter

y_pos = height - 2 * inch
x_start = 1 * inch

c.setFont("Helvetica", 11)
c.drawString(x_start, y_pos, "1.")

try:
    c.drawImage(
        img,
        x_start + 0.25 * inch,
        y_pos - 0.3 * inch,
        width=3.5 * inch,
        height=0.7 * inch,
        preserveAspectRatio=True
    )
    print("  SUCCESS")
except Exception as e:
    print(f"  FAILED: {e}")
    import traceback
    traceback.print_exc()

c.save()
print("\nPDF saved to test_exact_render.pdf")
print("Please check this PDF to see if the fraction renders correctly")
