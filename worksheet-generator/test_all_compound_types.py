"""
Test script to generate all three types of compound inequality worksheets.
"""

from generators.chapter03.compound_inequalities_generator import CompoundInequalityGenerator
from pdf_generator import PDFWorksheetGenerator

# Create generators
gen = CompoundInequalityGenerator(seed=456)
pdf_gen = PDFWorksheetGenerator()

print("=" * 60)
print("GENERATING ALL COMPOUND INEQUALITY TYPES")
print("=" * 60)

# Test 1: Mixed (both AND and OR)
print("\n1. MIXED (AND + OR)")
print("-" * 60)
problems_mixed = gen.generate_worksheet('medium', 8)
for i, prob in enumerate(problems_mixed, 1):
    print(f"  {i}. [{prob.compound_type.upper()}] {prob.latex}")

output_path = "compound_inequalities_mixed.pdf"
pdf_gen.generate_worksheet(problems_mixed, output_path,
                           "Compound Inequalities - Mixed - Medium",
                           include_answer_key=True)
print(f"\n[OK] Mixed worksheet saved: {output_path}")

# Test 2: AND only
print("\n2. AND ONLY")
print("-" * 60)
problems_and = gen.generate_worksheet('medium', 8, compound_type='and')
for i, prob in enumerate(problems_and, 1):
    print(f"  {i}. [{prob.compound_type.upper()}] {prob.latex}")

output_path = "compound_inequalities_and.pdf"
pdf_gen.generate_worksheet(problems_and, output_path,
                           "Compound Inequalities - AND - Medium",
                           include_answer_key=True)
print(f"\n[OK] AND worksheet saved: {output_path}")

# Test 3: OR only
print("\n3. OR ONLY")
print("-" * 60)
problems_or = gen.generate_worksheet('medium', 8, compound_type='or')
for i, prob in enumerate(problems_or, 1):
    print(f"  {i}. [{prob.compound_type.upper()}] {prob.latex}")

output_path = "compound_inequalities_or.pdf"
pdf_gen.generate_worksheet(problems_or, output_path,
                           "Compound Inequalities - OR - Medium",
                           include_answer_key=True)
print(f"\n[OK] OR worksheet saved: {output_path}")

print("\n" + "=" * 60)
print("ALL THREE TYPES GENERATED SUCCESSFULLY!")
print("=" * 60)
print("\nGenerated PDFs:")
print("  - compound_inequalities_mixed.pdf (both AND and OR)")
print("  - compound_inequalities_and.pdf (only AND)")
print("  - compound_inequalities_or.pdf (only OR)")
