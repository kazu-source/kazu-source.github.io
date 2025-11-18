"""
Test script to generate inequality PDFs with new refined number line styling.
Compares the new number line style with the coordinate plane graphs.
"""

from inequalities_generator import InequalityGenerator
from pdf_generator import PDFWorksheetGenerator

# Create generators
gen = InequalityGenerator(seed=200)
pdf_gen = PDFWorksheetGenerator()

# Generate and save PDFs for each difficulty level
difficulties = ['easy', 'medium', 'hard', 'challenge']

for difficulty in difficulties:
    print(f"\nGenerating {difficulty.upper()} inequality worksheet...")
    problems = gen.generate_worksheet(difficulty, 8)

    print(f"  Generated {len(problems)} problems")
    for i, prob in enumerate(problems, 1):
        print(f"    {i}. {prob.latex} (solution: x {prob.inequality_type} {prob.solution})")

    output_path = f"inequality_{difficulty}.pdf"
    pdf_gen.generate_worksheet(
        problems,
        output_path,
        title=f"Inequalities - {difficulty.capitalize()}",
        include_answer_key=True
    )
    print(f"  [OK] Saved to: {output_path}")

print("\n" + "="*60)
print("All inequality PDFs generated successfully!")
print("="*60)
print("\nFiles created:")
for difficulty in difficulties:
    print(f"  - inequality_{difficulty}.pdf")

print("\n" + "="*60)
print("STYLING NOTES:")
print("="*60)
print("\nNumber lines now use REFINED styling:")
print("  - Line width: 1.5 (matches coordinate plane axes)")
print("  - Tick width: 1.5, length: 8")
print("  - Label size: 9 (matches coordinate plane tick labels)")
print("  - Point marker: 10 (proportional to coordinate plane points)")
print("  - Arrow width: 2")
print("\nThis creates visual consistency with the graphing points worksheets!")
print("="*60)
