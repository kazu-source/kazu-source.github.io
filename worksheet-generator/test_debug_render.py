"""
Debug fraction rendering to see what's happening.
"""

from properties_mult_div_generator import PropertiesMultDivGenerator, PropertyProblem
from pdf_generator import PDFWorksheetGenerator
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

# Generate a single multiplication problem
gen = PropertiesMultDivGenerator()
problem = gen.generate_problem('medium', 'multiplication')

print("Problem details:")
print(f"  Equation: {problem.equation}")
print(f"  LaTeX repr: {repr(problem.latex)}")
print(f"  LaTeX value: {problem.latex}")
print(f"  Property type: {problem.property_type}")
print()

# Test rendering
pdf_gen = PDFWorksheetGenerator()

print("Testing render_latex_to_image...")
try:
    img = pdf_gen.render_latex_to_image(problem.latex, 24)
    print("SUCCESS: Rendering worked")
except Exception as e:
    print(f"FAILED: Rendering failed: {e}")
    import traceback
    traceback.print_exc()

# Now test in actual PDF context
print("\nCreating minimal PDF...")
c = canvas.Canvas("test_debug_minimal.pdf", pagesize=letter)
width, height = letter

# Try to detect problem type like the real code does
if isinstance(problem, PropertyProblem):
    if problem.property_type in ['multiplication', 'division']:
        problem_type = 'properties_mult_div'
    else:
        problem_type = 'properties_of_equality'

    print(f"Detected problem_type: {problem_type}")

    from worksheet_config import get_config
    config = get_config(problem_type)
    print(f"Config: fontsize={config.latex_fontsize}, width={config.image_width}, height={config.image_height}")

    # Try rendering
    y_pos = height - 2 * inch
    x_start = 1 * inch

    c.setFont("Helvetica", 11)
    c.drawString(x_start, y_pos, "1.")

    print("\nAttempting to render and draw image...")
    try:
        img = pdf_gen.render_latex_to_image(problem.latex, config.latex_fontsize)
        print("  Render: SUCCESS")
        c.drawImage(
            img,
            x_start + 0.25 * inch,
            y_pos - config.vertical_offset * inch,
            width=config.image_width * inch,
            height=config.image_height * inch,
            preserveAspectRatio=True
        )
        print("  Draw: SUCCESS")
    except Exception as e:
        print(f"  FAILED: {e}")
        import traceback
        traceback.print_exc()
        # Fallback
        c.drawString(x_start + 0.25 * inch, y_pos, problem.equation)

c.save()
print("\nPDF saved to test_debug_minimal.pdf")
