"""Test fraction rendering across all generators that use fractions."""

from generators.chapter01.evaluating_expressions_generator import EvaluatingExpressionsGenerator
from generators.chapter01.substitution_generator import SubstitutionGenerator
from multistep_generator import MultiStepEquationGenerator
from pdf_generator import PDFWorksheetGenerator

# Test each generator
generators_to_test = [
    ("Evaluating Expressions", EvaluatingExpressionsGenerator(), "output/test_eval_fractions.pdf"),
    ("Substitution", SubstitutionGenerator(), "output/test_subst_fractions.pdf"),
    ("Multi-Step", MultiStepEquationGenerator(), "output/test_multistep_fractions.pdf"),
]

pdf_gen = PDFWorksheetGenerator()

for name, gen, output_path in generators_to_test:
    print(f"\n{'='*70}")
    print(f"Testing {name}")
    print('='*70)

    # Generate medium difficulty problems
    problems = gen.generate_worksheet('medium', 6)

    # Show problems
    for i, p in enumerate(problems, 1):
        print(f"{i}. {p.latex}")

    # Generate PDF
    pdf_gen.generate_worksheet(problems, output_path, title=f'{name} - Fraction Test')
    print(f"\nPDF generated: {output_path}")

print(f"\n{'='*70}")
print("All PDFs generated successfully!")
print('='*70)
