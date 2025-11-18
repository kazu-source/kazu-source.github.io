"""
Test script for easy graphing points (first quadrant only)
"""

from generators.chapter04.graphing_points import GraphingPointsGenerator
from pdf_generator import PDFWorksheetGenerator

# Create generator
gen = GraphingPointsGenerator(seed=123)
pdf_gen = PDFWorksheetGenerator()

# Generate easy problems (first quadrant only)
print("Generating 4 EASY difficulty problems (first quadrant)...")
problems = gen.generate_worksheet('easy', 4)

for i, prob in enumerate(problems, 1):
    print(f"  {i}. Points: {prob.points} (all in quadrant I)")

# Create PDF
output_path = "test_graphing_easy_worksheet.pdf"
pdf_gen.generate_worksheet(
    problems,
    output_path,
    title="Graphing Points - Easy (First Quadrant)",
    include_answer_key=True
)

print(f"\nPDF saved to: {output_path}")
print("All 4 graphs show first quadrant only (0-10 on both axes)")
