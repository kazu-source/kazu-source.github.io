"""
Generate a sample compound inequalities worksheet PDF.
"""

from generators.chapter03.compound_inequalities_generator import CompoundInequalityGenerator
from pdf_generator import PDFWorksheetGenerator

# Create generators
gen = CompoundInequalityGenerator(seed=123)
pdf_gen = PDFWorksheetGenerator()

# Generate worksheet (mixed AND/OR types)
print("Generating compound inequalities worksheet...")
problems = gen.generate_worksheet('medium', 8)

# Show what we generated
print("\nProblems generated:")
for i, prob in enumerate(problems, 1):
    print(f"  {i}. [{prob.compound_type.upper()}] {prob.latex}")

# Generate PDF
output_path = "compound_inequalities_medium_sample.pdf"
title = "Compound Inequalities - Medium"

print(f"\nGenerating PDF: {output_path}")
pdf_gen.generate_worksheet(problems, output_path, title, include_answer_key=True)

print(f"\n[OK] Worksheet saved to: {output_path}")
print("     Includes answer key with number line solutions!")
