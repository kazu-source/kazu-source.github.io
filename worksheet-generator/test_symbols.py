"""Test script to generate Absolute Value and Square Roots worksheets"""

from generators.chapter01.absolute_value_generator import AbsoluteValueGenerator
from generators.chapter01.square_roots_generator import SquareRootsGenerator
from pdf_generator import PDFWorksheetGenerator

# Create generators
abs_gen = AbsoluteValueGenerator(seed=42)
sqrt_gen = SquareRootsGenerator(seed=42)

# Generate problems
abs_problems = abs_gen.generate_worksheet('medium', 8)
sqrt_problems = sqrt_gen.generate_worksheet('hard', 8)

# Create PDFs
pdf_gen = PDFWorksheetGenerator()

# Generate Absolute Value worksheet
pdf_gen.generate_worksheet(
    abs_problems,
    'Absolute Value - Medium - Symbol Test',
    'absolute_value_symbols.pdf'
)
print('Created: absolute_value_symbols.pdf')

# Generate Square Roots worksheet
pdf_gen.generate_worksheet(
    sqrt_problems,
    'Square Roots - Hard - Symbol Test',
    'square_roots_symbols.pdf'
)
print('Created: square_roots_symbols.pdf')

# Also test challenge levels
abs_challenge = abs_gen.generate_worksheet('challenge', 8)
sqrt_challenge = sqrt_gen.generate_worksheet('challenge', 8)

pdf_gen.generate_worksheet(
    abs_challenge,
    'Absolute Value - Challenge - Symbol Test',
    'absolute_value_challenge.pdf'
)
print('Created: absolute_value_challenge.pdf')

pdf_gen.generate_worksheet(
    sqrt_challenge,
    'Square Roots - Challenge - Symbol Test',
    'square_roots_challenge.pdf'
)
print('Created: square_roots_challenge.pdf')

print('\nAll worksheets created successfully!')
