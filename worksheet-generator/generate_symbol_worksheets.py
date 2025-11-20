"""
Generate Absolute Value and Square Roots worksheets to test symbol rendering.
"""

from generators.chapter01.absolute_value_generator import AbsoluteValueGenerator
from generators.chapter01.square_roots_generator import SquareRootsGenerator
from pdf_generator import PDFWorksheetGenerator

# Create generators
abs_gen = AbsoluteValueGenerator(seed=123)
sqrt_gen = SquareRootsGenerator(seed=123)
pdf_gen = PDFWorksheetGenerator()

# Generate Absolute Value - Medium
print("Generating Absolute Value worksheet (Medium)...")
abs_problems = abs_gen.generate_worksheet('medium', 8)
output_path = "absolute_value_medium.pdf"
title = "Absolute Value - Medium"
pdf_gen.generate_worksheet(abs_problems, output_path, title, include_answer_key=True)
print(f"[OK] Saved to: {output_path}")

# Generate Square Roots - Hard
print("\nGenerating Square Roots worksheet (Hard)...")
sqrt_problems = sqrt_gen.generate_worksheet('hard', 8)
output_path = "square_roots_hard.pdf"
title = "Square Roots - Hard"
pdf_gen.generate_worksheet(sqrt_problems, output_path, title, include_answer_key=True)
print(f"[OK] Saved to: {output_path}")

# Generate Absolute Value - Challenge (nested symbols)
print("\nGenerating Absolute Value worksheet (Challenge - nested)...")
abs_challenge = abs_gen.generate_worksheet('challenge', 8)
output_path = "absolute_value_challenge.pdf"
title = "Absolute Value - Challenge"
pdf_gen.generate_worksheet(abs_challenge, output_path, title, include_answer_key=True)
print(f"[OK] Saved to: {output_path}")

# Generate Square Roots - Challenge (complex symbols)
print("\nGenerating Square Roots worksheet (Challenge - complex)...")
sqrt_challenge = sqrt_gen.generate_worksheet('challenge', 8)
output_path = "square_roots_challenge.pdf"
title = "Square Roots - Challenge"
pdf_gen.generate_worksheet(sqrt_challenge, output_path, title, include_answer_key=True)
print(f"[OK] Saved to: {output_path}")

print("\n" + "="*60)
print("All symbol test worksheets generated successfully!")
print("="*60)
