"""Test the multistep fraction rendering fix."""

from multistep_generator import MultiStepEquationGenerator
from pdf_generator import PDFWorksheetGenerator
import re

# Generate problems
gen = MultiStepEquationGenerator()
problems = gen.generate_worksheet('medium', 6)

# Show what will be displayed
print('=' * 70)
print('Problems to be rendered:')
print('=' * 70)
for i, p in enumerate(problems, 1):
    print(f'\n{i}. LaTeX: {p.latex}')
    # Simulate the fix
    plain = p.latex.replace('\\', '')
    plain = re.sub(r'frac\{([^}]+)\}\{([^}]+)\}', r'\1/\2', plain)
    print(f'   Will display as: {plain}')
    print(f'   Solution: x = {p.solution}')

# Generate PDF
print('\n' + '=' * 70)
print('Generating PDF...')
pdf_gen = PDFWorksheetGenerator()
output_path = 'output/test_multistep_fractions.pdf'
pdf_gen.generate_worksheet(problems, output_path, title='Multi-Step Equations - Fraction Test')
print(f'PDF generated: {output_path}')
print('=' * 70)
