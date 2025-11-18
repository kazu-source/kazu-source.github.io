"""Comprehensive test of rendering across all worksheet generators."""

from equation_generator import LinearEquationGenerator
from inequalities_generator import InequalityGenerator
from multistep_generator import MultiStepEquationGenerator
from properties_generator import PropertiesOfEqualityGenerator
from properties_mult_div_generator import PropertiesMultDivGenerator
from systems_generator import SystemsOfEquationsGenerator
from word_problems_generator import WordProblemsGenerator
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

# Test all generators at various difficulty levels
generators_to_test = [
    ("Variables_medium", VariablesGenerator(), 'medium'),
    ("Exponents_hard", ExponentsGenerator(), 'hard'),
    ("Combining_Like_Terms_medium", CombiningLikeTermsGenerator(), 'medium'),
    ("Evaluating_Expressions_hard", EvaluatingExpressionsGenerator(), 'hard'),
    ("Substitution_challenge", SubstitutionGenerator(), 'challenge'),
    ("Equations_Intro_medium", EquationsIntroGenerator(), 'medium'),
    ("Solutions_medium", SolutionsGenerator(), 'medium'),
    ("Inputs_Outputs_medium", InputsOutputsGenerator(), 'medium'),
    ("Variables_Both_Sides_hard", VariablesBothSidesGenerator(), 'hard'),
    ("Basic_Equations_medium", LinearEquationGenerator(), 'medium'),
    ("Inequalities_medium", InequalityGenerator(), 'medium'),
    ("Multi_Step_medium", MultiStepEquationGenerator(), 'medium'),
    ("Properties_medium", PropertiesOfEqualityGenerator(), 'medium'),
    ("Properties_MultDiv_hard", PropertiesMultDivGenerator(), 'hard'),
    ("Systems_medium", SystemsOfEquationsGenerator(), 'medium'),
    ("Word_Problems_medium", WordProblemsGenerator(), 'medium'),
]

pdf_gen = PDFWorksheetGenerator()

print("\n" + "="*80)
print("COMPREHENSIVE RENDERING TEST")
print("="*80)
print("\nChecking for:")
print("  - Fractions (frac{}) rendering with proper bars")
print("  - Exponents (^) rendering as superscripts")
print("  - Text{} brackets removed")
print("  - Consistent 12pt font for equations")
print("  - Graphing problems with coordinate planes")
print("="*80)

results = {
    'has_fractions': [],
    'has_exponents': [],
    'has_text_brackets': [],
    'has_graphs': [],
    'success': [],
    'errors': []
}

for name, gen, difficulty in generators_to_test:
    print(f"\n{name} ({difficulty}):")
    print("-" * 50)

    try:
        # Generate 6 problems
        problems = gen.generate_worksheet(difficulty, 6)

        # Analyze problems
        features = {
            'fractions': False,
            'exponents': False,
            'text_brackets': False,
            'graphs': False
        }

        for i, p in enumerate(problems, 1):
            if hasattr(p, 'latex'):
                latex = p.latex
                if '\\frac' in latex or 'frac{' in latex:
                    features['fractions'] = True
                if '^' in latex:
                    features['exponents'] = True
                if '\\text{' in latex or 'text{' in latex:
                    features['text_brackets'] = True
            if hasattr(p, 'worksheet_image') or hasattr(p, 'solution_image'):
                features['graphs'] = True

        # Show sample
        if hasattr(problems[0], 'latex'):
            sample = problems[0].latex[:70]
            print(f"  Sample: {sample}{'...' if len(problems[0].latex) > 70 else ''}")
        else:
            print(f"  Sample: [Graphing problem - has images]")

        # Report features
        feature_list = []
        if features['fractions']:
            feature_list.append("[FRACTIONS]")
            results['has_fractions'].append(name)
        if features['exponents']:
            feature_list.append("[EXPONENTS]")
            results['has_exponents'].append(name)
        if features['text_brackets']:
            feature_list.append("[!text{} brackets!]")
            results['has_text_brackets'].append(name)
        if features['graphs']:
            feature_list.append("[GRAPHS]")
            results['has_graphs'].append(name)

        if feature_list:
            print(f"  Features: {', '.join(feature_list)}")
        else:
            print(f"  Features: Basic equations only")

        # Generate PDF
        output_path = f"output/comprehensive_test/{name}.pdf"
        pdf_gen.generate_worksheet(problems, output_path, title=f'{name.replace("_", " ")} Test')
        print(f"  [OK] PDF: {output_path}")
        results['success'].append(name)

    except Exception as e:
        print(f"  [ERROR]: {str(e)[:60]}")
        results['errors'].append((name, str(e)))

print("\n" + "="*80)
print("SUMMARY")
print("="*80)
print(f"\n[OK] Successful: {len(results['success'])}/{len(generators_to_test)}")
print(f"[X] Errors: {len(results['errors'])}")

print(f"\nGenerators with FRACTIONS: {len(results['has_fractions'])}")
for gen in results['has_fractions']:
    print(f"  - {gen}")

print(f"\nGenerators with EXPONENTS: {len(results['has_exponents'])}")
for gen in results['has_exponents']:
    print(f"  - {gen}")

print(f"\nGenerators with GRAPHS: {len(results['has_graphs'])}")
for gen in results['has_graphs']:
    print(f"  - {gen}")

if results['has_text_brackets']:
    print(f"\n[!] ISSUES - Generators still have text{{}} brackets: {len(results['has_text_brackets'])}")
    for gen in results['has_text_brackets']:
        print(f"  - {gen}")

if results['errors']:
    print(f"\n[X] ERRORS:")
    for name, error in results['errors']:
        print(f"  - {name}: {error[:60]}")

print("\n" + "="*80)
print("TEST COMPLETE - Check PDFs in output/comprehensive_test/")
print("="*80)
