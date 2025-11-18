"""Test fraction rendering with hard/challenge difficulties."""

from generators.chapter01.evaluating_expressions_generator import EvaluatingExpressionsGenerator
from generators.chapter01.substitution_generator import SubstitutionGenerator
from pdf_generator import PDFWorksheetGenerator

# Test hard difficulty to get fractions
generators_to_test = [
    ("Evaluating Expressions Hard", EvaluatingExpressionsGenerator(), 'hard', "output/test_eval_hard_fractions.pdf"),
    ("Substitution Challenge", SubstitutionGenerator(), 'challenge', "output/test_subst_challenge_fractions.pdf"),
]

pdf_gen = PDFWorksheetGenerator()

for name, gen, difficulty, output_path in generators_to_test:
    print(f"\n{'='*70}")
    print(f"Testing {name} ({difficulty})")
    print('='*70)

    # Generate problems with specified difficulty
    problems = gen.generate_worksheet(difficulty, 10)

    # Show problems
    for i, p in enumerate(problems, 1):
        if 'frac' in p.latex:
            print(f"{i}. {p.latex} *** HAS FRACTION ***")
        else:
            print(f"{i}. {p.latex}")

    # Generate PDF
    pdf_gen.generate_worksheet(problems, output_path, title=f'{name}')
    print(f"\nPDF generated: {output_path}")

print(f"\n{'='*70}")
print("Done!")
print('='*70)
