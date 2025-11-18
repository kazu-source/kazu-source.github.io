"""Comprehensive test of all worksheet generators."""

from equation_generator import LinearEquationGenerator
from inequalities_generator import InequalityGenerator
from multistep_generator import MultiStepEquationGenerator
from properties_generator import PropertiesOfEqualityGenerator
from properties_mult_div_generator import PropertiesMultDivGenerator
from systems_generator import SystemGenerator
from word_problems_generator import WordProblemGenerator
from generators.chapter01.combining_like_terms_generator import CombiningLikeTermsGenerator
from generators.chapter01.evaluating_expressions_generator import EvaluatingExpressionsGenerator
from generators.chapter01.exponents_generator import ExponentsGenerator
from generators.chapter01.substitution_generator import SubstitutionGenerator
from generators.chapter01.variables_generator import VariablesGenerator
from generators.chapter02.equations_intro_generator import EquationsIntroGenerator
from generators.chapter02.inputs_outputs_generator import InputsOutputsGenerator
from generators.chapter02.solutions_generator import SolutionsGenerator
from generators.chapter02.variables_both_sides_generator import VariablesBothSidesGenerator
from pdf_generator import PDFWorksheetGenerator

# Test all generators
generators_to_test = [
    ("Variables", VariablesGenerator()),
    ("Exponents", ExponentsGenerator()),
    ("Combining Like Terms", CombiningLikeTermsGenerator()),
    ("Evaluating Expressions", EvaluatingExpressionsGenerator()),
    ("Substitution", SubstitutionGenerator()),
    ("Equations Intro", EquationsIntroGenerator()),
    ("Solutions", SolutionsGenerator()),
    ("Inputs/Outputs", InputsOutputsGenerator()),
    ("Variables Both Sides", VariablesBothSidesGenerator()),
    ("Basic Equations", LinearEquationGenerator()),
    ("Inequalities", InequalityGenerator()),
    ("Multi-Step", MultiStepEquationGenerator()),
    ("Properties", PropertiesOfEqualityGenerator()),
    ("Properties Mult/Div", PropertiesMultDivGenerator()),
    ("Systems", SystemGenerator()),
    ("Word Problems", WordProblemGenerator()),
]

pdf_gen = PDFWorksheetGenerator()

print("\n" + "="*80)
print("TESTING ALL WORKSHEET GENERATORS")
print("="*80)

for name, gen in generators_to_test:
    print(f"\n{name}:")
    print("-" * 40)

    try:
        # Generate 3 problems at medium difficulty
        problems = gen.generate_worksheet('medium', 3)

        # Show first problem
        if hasattr(problems[0], 'latex'):
            latex = problems[0].latex
            # Check for issues
            issues = []
            if 'text{' in latex:
                issues.append("HAS text{} brackets")
            if '\\frac' in latex:
                issues.append("HAS fractions")

            if issues:
                print(f"  Sample: {latex[:80]}... [{', '.join(issues)}]")
            else:
                print(f"  Sample: {latex[:80]}{'...' if len(latex) > 80 else ''}")
        else:
            print(f"  [No latex attribute - likely graphing]")

        # Generate PDF
        output_path = f"output/test_{name.lower().replace(' ', '_').replace('/', '_')}.pdf"
        pdf_gen.generate_worksheet(problems, output_path, title=f'{name} Test')
        print(f"  ✓ PDF: {output_path}")

    except Exception as e:
        print(f"  ✗ ERROR: {e}")

print("\n" + "="*80)
print("TESTING COMPLETE")
print("="*80)
