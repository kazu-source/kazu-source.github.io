"""Test Properties Mult/Div generator to check text wrapping issue."""

from properties_mult_div_generator import PropertiesMultDivGenerator
from pdf_generator import PDFWorksheetGenerator

# Generate problems
gen = PropertiesMultDivGenerator()
pdf_gen = PDFWorksheetGenerator()

print("=" * 70)
print("Testing Properties Mult/Div Generator")
print("=" * 70)

# Test at hard difficulty (mentioned in user's issue list)
problems = gen.generate_worksheet('hard', 6)

print("\nGenerated Problems:")
for i, p in enumerate(problems, 1):
    print(f"\n{i}. {p.latex}")
    print(f"   Solution: {p.solution}")

# Generate PDF
output_path = "output/test_properties_multdiv.pdf"
pdf_gen.generate_worksheet(problems, output_path, title='Properties of Equality - Mult/Div - Hard')
print(f"\n{'=' * 70}")
print(f"PDF generated: {output_path}")
print("Check for text wrapping issues with 1 inch margins")
print("=" * 70)
