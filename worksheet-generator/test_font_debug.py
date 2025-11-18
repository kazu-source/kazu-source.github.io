"""Debug test to check font sizes being used."""

from multistep_generator import MultiStepEquationGenerator
from pdf_generator import PDFWorksheetGenerator

# Generate one problem
gen = MultiStepEquationGenerator()
problems = gen.generate_worksheet('medium', 1)

print(f"Problem: {problems[0].latex}")
print(f"\nPDF Generator Constants:")
pdf_gen = PDFWorksheetGenerator()
print(f"PROBLEM_NUMBER_FONT_SIZE: {pdf_gen.PROBLEM_NUMBER_FONT_SIZE}")
print(f"EQUATION_FONT_SIZE: {pdf_gen.EQUATION_FONT_SIZE}")

# Generate a test PDF
output_path = 'output/font_size_test.pdf'
pdf_gen.generate_worksheet(problems, output_path, title='Font Size Debug Test')
print(f"\nPDF generated: {output_path}")
