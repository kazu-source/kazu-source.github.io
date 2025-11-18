"""Test system of equations vertical alignment for elimination method."""

from systems_generator import SystemsOfEquationsGenerator
from pdf_generator import PDFWorksheetGenerator

# Generate some systems
gen = SystemsOfEquationsGenerator()
pdf_gen = PDFWorksheetGenerator()

print("=" * 70)
print("Testing Systems of Equations Alignment")
print("=" * 70)

# Test at medium difficulty (best for elimination)
problems = gen.generate_worksheet('medium', 6)

print("\nGenerated Systems:")
for i, p in enumerate(problems, 1):
    print(f"\n{i}. {p.equation1_latex}")
    print(f"   {p.equation2_latex}")
    print(f"   Solution: {p.solution}")
    print(f"   Method: {p.method}")

# Generate PDF
output_path = "output/test_systems_alignment.pdf"
pdf_gen.generate_worksheet(problems, output_path, title='Systems - Alignment Test')
print(f"\n{'=' * 70}")
print(f"PDF generated: {output_path}")
print("Check that x and y terms align vertically for elimination")
print("=" * 70)
