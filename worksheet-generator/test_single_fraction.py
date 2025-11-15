"""
Quick test to debug fraction rendering.
"""

from properties_mult_div_generator import PropertiesMultDivGenerator
from pdf_generator import PDFWorksheetGenerator

# Generate a single multiplication problem
gen = PropertiesMultDivGenerator()
problems = gen.generate_worksheet('medium', 3, 'multiplication')

print("Generated problems:")
for i, p in enumerate(problems, 1):
    print(f"{i}. Equation: {p.equation}")
    print(f"   LaTeX: {repr(p.latex)}")
    print(f"   Solution: {p.solution}")
    print()

# Create PDF
pdf_gen = PDFWorksheetGenerator()
output_file = "test_single_fraction.pdf"

print(f"Generating PDF to {output_file}...")
pdf_gen.generate_worksheet(
    problems,
    output_file,
    title="Fraction Test - Mult/Div Properties",
    include_answer_key=True
)
print("Done!")
