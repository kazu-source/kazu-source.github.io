"""
Test script to generate PDFs for all difficulty levels
"""

from generators.chapter04.graphing_points import GraphingPointsGenerator
from pdf_generator import PDFWorksheetGenerator

# Create generators
gen = GraphingPointsGenerator(seed=100)
pdf_gen = PDFWorksheetGenerator()

# Generate and save PDFs for each difficulty level
difficulties = ['easy', 'medium', 'hard', 'challenge']

for difficulty in difficulties:
    print(f"\nGenerating {difficulty.upper()} worksheet...")
    problems = gen.generate_worksheet(difficulty, 4)

    print(f"  Generated {len(problems)} problems:")
    for i, prob in enumerate(problems, 1):
        print(f"    {i}. {len(prob.points)} points: {prob.points}")

    output_path = f"graphing_points_{difficulty}.pdf"
    pdf_gen.generate_worksheet(
        problems,
        output_path,
        title=f"Graphing Points - {difficulty.capitalize()}",
        include_answer_key=True
    )
    print(f"  [OK] Saved to: {output_path}")

print("\n" + "="*60)
print("All PDFs generated successfully!")
print("="*60)
print("\nFiles created:")
for difficulty in difficulties:
    print(f"  - graphing_points_{difficulty}.pdf")
