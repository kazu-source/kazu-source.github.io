"""
Test script for complete graphing points workflow: generate → PDF
"""

from generators.chapter04.graphing_points import GraphingPointsGenerator
from pdf_generator import PDFWorksheetGenerator

# Create generator
print("Creating graphing points generator...")
gen = GraphingPointsGenerator(seed=42)

# Generate problems
print("Generating 4 medium difficulty problems...")
problems = gen.generate_worksheet('medium', 4)

print(f"Generated {len(problems)} problems:")
for i, prob in enumerate(problems, 1):
    print(f"  {i}. Points: {prob.points}")
    print(f"     Labels: {prob.labels}")

# Create PDF
print("\nGenerating PDF...")
pdf_gen = PDFWorksheetGenerator()
output_path = "test_graphing_points_worksheet.pdf"

pdf_gen.generate_worksheet(
    problems,
    output_path,
    title="Graphing Points on a Coordinate Plane - Medium",
    include_answer_key=True
)

print(f"\nSuccess! PDF saved to: {output_path}")
print("Check the PDF to see:")
print("  - Page 1: Blank coordinate planes for students")
print("  - Page 2: Answer key with plotted points")
