"""
Desktop GUI for the Math Worksheet Generator using Tkinter.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import sys
import subprocess
import threading
from datetime import datetime
from pathlib import Path
import importlib.util

# PyInstaller support
from resource_helper import resource_path, is_frozen

# Legacy imports (commented out - now using dynamic generator discovery)
# from equation_generator import LinearEquationGenerator
# from systems_generator import SystemsOfEquationsGenerator
# from inequalities_generator import InequalityGenerator
# from properties_generator import PropertiesOfEqualityGenerator
# from properties_mult_div_generator import PropertiesMultDivGenerator
# from word_problems_generator import WordProblemsGenerator
# from multistep_generator import MultiStepEquationGenerator

# Still needed for PDF generation and config
from pdf_generator import PDFWorksheetGenerator
from worksheet_config import get_config

# Chapter 1 Generators
from generators.High_School.Algebra.Unit_1.combining_like_terms_generator import CombiningLikeTermsGenerator
from generators.High_School.Algebra.Unit_1.evaluating_expressions_generator import EvaluatingExpressionsGenerator
from generators.High_School.Algebra.Unit_1.exponents_generator import ExponentsGenerator
from generators.High_School.Algebra.Unit_9.parts_of_term_generator import PartsOfTermGenerator
from generators.High_School.Algebra.number_properties_generator import NumberPropertiesGenerator
from generators.High_School.Algebra.order_of_operations_generator import OrderOfOperationsGenerator
from generators.High_School.Algebra.Unit_7.square_roots_generator import SquareRootsGenerator
from generators.High_School.Algebra.Unit_1.substitution_generator import SubstitutionGenerator
from generators.High_School.Algebra.Unit_1.variables_generator import VariablesGenerator

# Chapter 2 Generators
from generators.High_School.Algebra.Unit_2.equations_intro_generator import EquationsIntroGenerator
from generators.High_School.Algebra.Unit_2.inputs_outputs_generator import InputsOutputsGenerator
from generators.High_School.Algebra.Unit_2.solutions_generator import SolutionsGenerator
from generators.High_School.Algebra.Unit_1.variables_both_sides_generator import VariablesBothSidesGenerator
from generators.High_School.Algebra.Unit_2.property_equality_add_sub_generator import PropertyEqualityAddSubGenerator
from generators.High_School.Algebra.Unit_2.property_equality_mult_div_generator import PropertyEqualityMultDivGenerator
from generators.High_School.Algebra.Unit_2.linear_equations_generator import LinearEquationsGenerator
from generators.High_School.Algebra.Unit_2.linear_equation_word_problems_generator import LinearEquationWordProblemsGenerator

# Chapter 3 Generators
from generators.High_School.Algebra.Unit_3.compound_inequalities_generator import CompoundInequalityGenerator
from generators.High_School.Algebra.Unit_3.simple_inequalities_generator import SimpleInequalitiesGenerator
from generators.High_School.Algebra.Unit_3.inequality_word_problems_generator import InequalityWordProblemsGenerator

# Chapter 4 Generators
from generators.High_School.Algebra.Unit_4.graphing_points import GraphingPointsGenerator
from generators.High_School.Algebra.Unit_4.graphing_lines import GraphingLinesGenerator
from generators.High_School.Algebra.Unit_4.graphing_slope_intercept import SlopeInterceptGenerator
from generators.High_School.Algebra.Unit_4.graphing_point_slope import PointSlopeGenerator
from generators.High_School.Algebra.Unit_4.graphing_standard_form import StandardFormGenerator
from generators.High_School.Algebra.Unit_4.inputs_outputs_review_generator import InputsOutputsReviewGenerator
from generators.High_School.Algebra.Unit_4.slope_generator import SlopeGenerator
from generators.High_School.Algebra.Unit_4.intercepts_generator import InterceptsGenerator
from generators.High_School.Algebra.Unit_4.writing_slope_intercept import WritingSlopeInterceptGenerator

# Chapter 5 Generators
from generators.High_School.Algebra.Unit_5.graphing_systems import GraphingSystemsGenerator
from generators.High_School.Algebra.Unit_5.systems_substitution import SystemsSubstitutionGenerator
from generators.High_School.Algebra.Unit_5.systems_elimination import SystemsEliminationGenerator

# Chapter 6 Generators
from generators.High_School.Algebra.Unit_6.inputs_outputs_functions_review_generator import InputsOutputsFunctionsReviewGenerator
from generators.High_School.Algebra.Unit_6.functions_generator import FunctionsGenerator
from generators.High_School.Algebra.Unit_6.domain_range_generator import DomainRangeGenerator

# Chapter 7 Generators
from generators.High_School.Algebra.Unit_7.exponent_properties_generator import ExponentPropertiesGenerator
from generators.High_School.Algebra.Unit_1.expanding_exponents_generator import ExpandingExponentsGenerator
from generators.High_School.Algebra.Unit_7.radical_properties_generator import RadicalPropertiesGenerator

# Chapter 8 Generators
from generators.High_School.Algebra.Unit_8.equivalent_exponential_review_generator import EquivalentExponentialReviewGenerator
from generators.High_School.Algebra.Unit_8.exponential_functions_generator import ExponentialFunctionsGenerator
from generators.High_School.Algebra.Unit_8.exponential_growth_decay_generator import ExponentialGrowthDecayGenerator

# Chapter 9 Generators
from generators.High_School.Algebra.Unit_1.parts_of_term_exponents_review_generator import PartsOfTermExponentsReviewGenerator
from generators.High_School.Algebra.Unit_9.polynomial_operations_generator import PolynomialOperationsGenerator
from generators.High_School.Algebra.Unit_9.factoring_generator import FactoringGenerator

# Chapter 10 Generators
from generators.High_School.Algebra.Unit_2.quadratic_equations_generator import QuadraticEquationsGenerator
from generators.High_School.Algebra.Unit_10.quadratic_graphing_generator import QuadraticGraphingGenerator

# Chapter 11 Generators
from generators.High_School.Algebra.Unit_4.graphing_parabolas import ParabolaGraphingGenerator
from generators.High_School.Algebra.Unit_11.completing_the_square_generator import CompletingTheSquareGenerator as CompletingSquareSimpleGenerator
from generators.High_School.Algebra.Unit_11.quadratic_formula_hard_to_use_the_three_main_methods_and_completing_the_square_generator import QuadraticFormulaHardToUseTheThreeMainMethodsAndCompletingTheSquareGenerator as QuadraticFormulaSimpleGenerator

# Chapter 12 Generators
from generators.High_School.Algebra.Unit_12.quadratic_functions_generator import QuadraticFunctionsGenerator as QuadraticFunctionsSimpleGenerator

# Chapter 13 Generators
from generators.High_School.Algebra.Unit_13.absolute_value_generator import AbsoluteValueGenerator
from generators.High_School.Algebra.Unit_13.absolute_value_inequalities_generator import AbsoluteValueInequalitiesGenerator
from generators.High_School.Algebra.Unit_13.constructing_geometric_sequences_generator import ConstructingGeometricSequencesGenerator
from generators.High_School.Algebra.Unit_13.modeling_with_sequences_generator import ModelingWithSequencesGenerator
from generators.High_School.Algebra.Unit_13.constructing_geometric_sequences_generator import ConstructingGeometricSequencesGenerator as ArithmeticSequencesSimpleGenerator
from generators.High_School.Algebra.Unit_13.constructing_geometric_sequences_generator import ConstructingGeometricSequencesGenerator as GeometricSequencesSimpleGenerator


class WorksheetGeneratorGUI:
    """Main GUI application for generating math worksheets."""

    @staticmethod
    def discover_generators():
        """
        Discover all generator files in generators/K_8/ and generators/High_School/ directories.

        When running as a PyInstaller executable, uses the pre-built generator registry.
        When running in development, dynamically discovers generators.

        Returns dict: {class_name: {unit_name: {topic_name: generator_class}}}
        where class_name is like "High School - Algebra" or "K-8 - Grade 5"
        and unit_name is like "Unit 1", "Unit 2", or "No Unit" for ungrouped generators
        """
        # Check if running as PyInstaller executable
        if is_frozen():
            # Use pre-built registry for frozen executable - need to reorganize it
            try:
                from generator_registry import GENERATOR_REGISTRY
                # Reorganize flat registry into Class → Unit → Topic structure
                return WorksheetGeneratorGUI._organize_by_units(GENERATOR_REGISTRY)
            except ImportError as e:
                print(f"Error: Could not load generator registry: {e}")
                return {}

        # Development mode: dynamic discovery
        generators_by_subject = {}
        generators_base = Path(resource_path("generators"))

        if not generators_base.exists():
            return generators_by_subject

        # Find K-8 and High_School directories
        category_dirs = []
        for category in ['K_8', 'High_School']:
            category_path = generators_base / category
            if category_path.exists() and category_path.is_dir():
                category_dirs.append((category, category_path))

        for category_name, category_path in category_dirs:
            # Find all subject/grade directories within this category
            subject_dirs = sorted([d for d in category_path.iterdir() if d.is_dir()])

            for subject_dir in subject_dirs:
                # Create display name like "High School - Algebra" or "K-8 - Grade 5"
                category_display = category_name.replace('_', '-')
                subject_display = subject_dir.name.replace('_', ' ')
                full_path = f"{category_display} - {subject_display}"

                generators_by_subject[full_path] = {}

                # Check for generators directly in subject folder (ungrouped)
                direct_generators = [f for f in subject_dir.glob('*_generator.py')
                                   if f.name != '__init__.py']

                if direct_generators:
                    generators_by_subject[full_path]["No Unit"] = {}
                    for gen_file in direct_generators:
                        gen_class = WorksheetGeneratorGUI._load_generator(gen_file, category_name, subject_dir.name, None)
                        if gen_class:
                            topic_name = gen_file.stem.replace('_generator', '').replace('_', ' ').title()
                            generators_by_subject[full_path]["No Unit"][topic_name] = gen_class

                # Check for generators in Unit subfolders
                # Support both naming patterns: Unit_1, Unit_2 (High School) and Unit01, Unit02 (K-8)
                unit_dirs = sorted([d for d in subject_dir.iterdir()
                                  if d.is_dir() and (d.name.startswith('Unit_') or d.name.startswith('Unit'))])

                for unit_dir in unit_dirs:
                    # Extract unit number and create display name
                    # Handle both Unit_1 and Unit01 formats
                    if unit_dir.name.startswith('Unit_'):
                        unit_num = unit_dir.name.replace('Unit_', '')
                    else:
                        # Remove 'Unit' prefix and strip leading zeros
                        unit_num = unit_dir.name.replace('Unit', '').lstrip('0') or '0'
                    unit_display = f"Unit {unit_num}"

                    generators_by_subject[full_path][unit_display] = {}

                    unit_generators = [f for f in unit_dir.glob('*_generator.py')
                                     if f.name != '__init__.py']

                    for gen_file in unit_generators:
                        gen_class = WorksheetGeneratorGUI._load_generator(gen_file, category_name, subject_dir.name, unit_dir.name)
                        if gen_class:
                            topic_name = gen_file.stem.replace('_generator', '').replace('_', ' ').title()
                            generators_by_subject[full_path][unit_display][topic_name] = gen_class

        return generators_by_subject

    @staticmethod
    def _load_generator(gen_file, category_name, subject_name, unit_name):
        """Helper to load a generator class from a file."""
        try:
            # Determine module path
            if unit_name:
                module_name = f"generators.{category_name}.{subject_name}.{unit_name}.{gen_file.stem}"
            else:
                module_name = f"generators.{category_name}.{subject_name}.{gen_file.stem}"

            spec = importlib.util.spec_from_file_location(module_name, gen_file)
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)

            # Find the generator class
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if (isinstance(attr, type) and
                    attr_name.endswith('Generator') and
                    attr_name != 'Generator' and
                    hasattr(attr, 'generate_worksheet')):
                    return attr
            return None
        except Exception as e:
            print(f"Warning: Failed to load {gen_file}: {e}")
            return None

    @staticmethod
    def _organize_by_units(flat_registry):
        """Reorganize flat registry into Class → Unit → Topic structure."""
        organized = {}

        for class_name, topics in flat_registry.items():
            organized[class_name] = {}

            for topic_name, generator_class in topics.items():
                # Extract unit info from the generator's module path
                # Module path format: generators.Category.Subject.UnitXX.topic_generator
                try:
                    module_path = generator_class.__module__
                    parts = module_path.split('.')

                    # Find the Unit part in the module path
                    unit_display = "No Unit"
                    for part in parts:
                        if part.startswith('Unit_'):
                            # High School format: Unit_1
                            unit_num = part.replace('Unit_', '')
                            unit_display = f"Unit {unit_num}"
                            break
                        elif part.startswith('Unit'):
                            # K-8 format: Unit01
                            unit_num = part.replace('Unit', '').lstrip('0') or '0'
                            unit_display = f"Unit {unit_num}"
                            break

                    # Initialize unit dict if needed
                    if unit_display not in organized[class_name]:
                        organized[class_name][unit_display] = {}

                    # Add topic to the appropriate unit
                    organized[class_name][unit_display][topic_name] = generator_class

                except Exception as e:
                    # Fallback: put in "No Unit" if there's any issue
                    if "No Unit" not in organized[class_name]:
                        organized[class_name]["No Unit"] = {}
                    organized[class_name]["No Unit"][topic_name] = generator_class

        return organized

    def __init__(self, root):
        """
        Initialize the GUI application.

        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("Math Worksheet Generator")
        self.root.geometry("680x680")
        self.root.resizable(False, False)

        # Configure modern styling
        self._configure_styles()

        # Initialize generators
        # Chapter 1
        self.absolute_value_gen = AbsoluteValueGenerator()
        self.combining_like_terms_gen = CombiningLikeTermsGenerator()
        self.evaluating_expressions_gen = EvaluatingExpressionsGenerator()
        self.exponents_gen = ExponentsGenerator()
        self.parts_of_term_gen = PartsOfTermGenerator()
        self.number_properties_gen = NumberPropertiesGenerator()
        self.order_of_operations_gen = OrderOfOperationsGenerator()
        self.square_roots_gen = SquareRootsGenerator()
        self.substitution_gen = SubstitutionGenerator()
        self.variables_gen = VariablesGenerator()

        # Chapter 2
        self.equations_intro_gen = EquationsIntroGenerator()
        self.inputs_outputs_gen = InputsOutputsGenerator()
        # Legacy generators (commented out - now using dynamic discovery)
        # self.word_problems_gen = WordProblemsGenerator()
        # self.equation_gen = LinearEquationGenerator()
        # self.properties_gen = PropertiesOfEqualityGenerator()
        # self.properties_mult_div_gen = PropertiesMultDivGenerator()
        self.variables_both_sides_gen = VariablesBothSidesGenerator()
        # self.multistep_gen = MultiStepEquationGenerator()
        self.solutions_gen = SolutionsGenerator()
        # New Unit 2 generators
        self.property_equality_add_sub_gen = PropertyEqualityAddSubGenerator()
        self.property_equality_mult_div_gen = PropertyEqualityMultDivGenerator()
        self.linear_equations_gen = LinearEquationsGenerator()
        self.linear_equation_word_problems_gen = LinearEquationWordProblemsGenerator()

        # Chapter 3
        # self.inequality_gen = InequalityGenerator()  # Legacy - now using dynamic discovery
        self.compound_inequality_gen = CompoundInequalityGenerator()
        self.simple_inequalities_gen = SimpleInequalitiesGenerator()
        self.absolute_value_inequalities_gen = AbsoluteValueInequalitiesGenerator()
        self.inequality_word_problems_gen = InequalityWordProblemsGenerator()

        # Chapter 4
        self.graphing_points_gen = GraphingPointsGenerator()
        self.graphing_lines_gen = GraphingLinesGenerator()
        self.slope_intercept_gen = SlopeInterceptGenerator()
        self.point_slope_gen = PointSlopeGenerator()
        self.standard_form_gen = StandardFormGenerator()
        self.inputs_outputs_review_gen = InputsOutputsReviewGenerator()
        self.slope_gen = SlopeGenerator()
        self.intercepts_gen = InterceptsGenerator()
        self.writing_slope_intercept_gen = WritingSlopeInterceptGenerator()

        # Chapter 5
        # self.systems_gen = SystemsOfEquationsGenerator()  # Legacy - now using dynamic discovery
        self.graphing_systems_gen = GraphingSystemsGenerator()
        self.systems_substitution_gen = SystemsSubstitutionGenerator()
        self.systems_elimination_gen = SystemsEliminationGenerator()

        # Chapter 6
        self.inputs_outputs_functions_gen = InputsOutputsFunctionsReviewGenerator()
        self.functions_gen = FunctionsGenerator()
        self.domain_range_gen = DomainRangeGenerator()

        # Chapter 7
        self.exponent_properties_gen = ExponentPropertiesGenerator()
        self.expanding_exponents_gen = ExpandingExponentsGenerator()
        self.radical_properties_gen = RadicalPropertiesGenerator()

        # Chapter 8
        self.equivalent_exponential_gen = EquivalentExponentialReviewGenerator()
        self.exponential_functions_gen = ExponentialFunctionsGenerator()
        self.exponential_growth_decay_gen = ExponentialGrowthDecayGenerator()

        # Chapter 9
        self.parts_of_term_exponents_gen = PartsOfTermExponentsReviewGenerator()
        self.polynomial_operations_gen = PolynomialOperationsGenerator()
        self.factoring_gen = FactoringGenerator()

        # Chapter 10
        self.quadratic_equations_gen = QuadraticEquationsGenerator()
        self.quadratic_graphing_gen = QuadraticGraphingGenerator()

        # Chapter 11
        self.parabola_gen = ParabolaGraphingGenerator()
        self.completing_square_gen = CompletingSquareSimpleGenerator()
        self.quadratic_formula_gen = QuadraticFormulaSimpleGenerator()

        # Chapter 12
        self.quadratic_functions_gen = QuadraticFunctionsSimpleGenerator()

        # Chapter 13
        self.constructing_geometric_seq_gen = ConstructingGeometricSequencesGenerator()
        self.modeling_sequences_gen = ModelingWithSequencesGenerator()
        self.arithmetic_sequences_gen = ArithmeticSequencesSimpleGenerator()
        self.geometric_sequences_gen = GeometricSequencesSimpleGenerator()

        self.pdf_gen = PDFWorksheetGenerator()

        # Discover all available generators dynamically
        print("Discovering generators...")
        self.discovered_generators = self.discover_generators()

        # Cache generator instances
        self.generator_instances = {}

        # Build chapter_topics from discovered generators
        # Structure: {class_name: {unit_name: {topic_name: generator_class}}}
        self.chapter_topics = {}
        for class_name, units_dict in self.discovered_generators.items():
            self.chapter_topics[class_name] = units_dict

        # Count total topics across all classes and units
        total_topics = sum(
            len(topics)
            for units in self.chapter_topics.values()
            for topics in units.values()
        )

        # If no generators discovered, will fall back to legacy topics below
        print(f"Discovered {len(self.chapter_topics)} classes with {total_topics} total topics")

        # Map chapters to topics (kept for backward compatibility with hardcoded ones)
        # Structure: {chapter_name: {topic_display_name: (generator_name, config_key)}}
        self.chapter_topics_legacy = {
            'Chapter 1: Intro to Variables': {
                'Absolute Value': ('absolute_value', 'absolute_value'),
                'Combining Like Terms': ('combining_like_terms', 'combining_like_terms'),
                'Evaluating an Expression': ('evaluating_expressions', 'evaluating_expressions'),
                'Exponents': ('exponents', 'exponents'),
                'Parts of a Term': ('parts_of_term', 'parts_of_term'),
                'Number Properties': ('number_properties', 'number_properties'),
                'Order of Operations': ('order_of_operations', 'order_of_operations'),
                'Square Roots': ('square_roots', 'square_roots'),
                'Substitution of Variables': ('substitution', 'substitution'),
                'Variables': ('variables', 'variables'),
            },
            'Chapter 2: Solving Simple Equations': {
                'Equations': ('equations_intro', 'equations_intro'),
                'Inputs and Outputs': ('inputs_outputs', 'inputs_outputs'),
                'Linear Equation Word Problems (OLD)': ('word_problems', 'word_problems'),
                'Linear Equation Word Problems': ('linear_equation_word_problems', 'linear_equation_word_problems'),
                'Linear Equations (OLD)': ('linear', 'linear_equation'),
                'Linear Equations': ('linear_equations', 'linear_equations'),
                'Properties of Equality - Add/Subtract (OLD)': ('properties', 'properties_of_equality'),
                'Property of Equality - Add/Subtract': ('property_equality_add_sub', 'property_equality_add_sub'),
                'Properties of Equality - Mult/Div (OLD)': ('properties_mult_div', 'properties_mult_div'),
                'Property of Equality - Mult/Div': ('property_equality_mult_div', 'property_equality_mult_div'),
                'Solving Equations with Variables on Both Sides': ('variables_both_sides', 'variables_both_sides'),
                'Solving Multi-Step Equations': ('multistep', 'multistep_equations'),
                'What Are Solutions?': ('solutions', 'solutions'),
            },
            'Chapter 3: Inequalities': {
                'One-Step Inequalities': ('simple_inequalities', 'simple_inequalities'),
                'Compound Inequalities - AND': ('compound_inequality_and', 'compound_inequality_and'),
                'Compound Inequalities - Mixed': ('compound_inequality', 'compound_inequality'),
                'Compound Inequalities - OR': ('compound_inequality_or', 'compound_inequality_or'),
                'Absolute Value Inequalities': ('absolute_value_inequalities', 'absolute_value_inequalities'),
                'Inequality Word Problems': ('inequality_word_problems', 'inequality_word_problems'),
            },
            'Chapter 4: Linear Equations - Two Variables': {
                'Review: Inputs and Outputs': ('inputs_outputs_review', 'inputs_outputs_review'),
                'Points on a Coordinate Plane': ('graphing_points', 'graphing_points'),
                'Line on a Coordinate Plane': ('graphing_lines', 'graphing_lines'),
                'Slope': ('slope', 'slope'),
                'X and Y Intercepts': ('intercepts', 'intercepts'),
                'Slope-Intercept Form': ('slope_intercept', 'slope_intercept'),
                'Writing Slope-Intercept Equations': ('writing_slope_intercept', 'writing_slope_intercept'),
                'Point-Slope Form': ('point_slope', 'point_slope'),
                'Standard Form': ('standard_form', 'standard_form'),
            },
            'Chapter 5: Systems of Equations': {
                'Systems of Equations - Graphing': ('graphing_systems', 'graphing_systems'),
                'Systems of Equations - Intro': ('systems', 'system_of_equations'),
                'Systems of Equations Using Substitution': ('systems_substitution', 'systems_substitution'),
                'Systems of Equations Using Elimination': ('systems_elimination', 'systems_elimination'),
            },
            'Chapter 6: Functions': {
                'Functions': ('functions', 'functions'),
                'Review: Inputs/Outputs and Functions': ('inputs_outputs_functions', 'inputs_outputs_functions'),
                'Domain and Range': ('domain_range', 'domain_range'),
            },
            'Chapter 7: Exponents and Radicals': {
                'Exponents - Properties': ('exponent_properties', 'exponent_properties'),
                'Expanding and Simplifying Expressions with Exponents': ('expanding_exponents', 'expanding_exponents'),
                'Properties of Radicals': ('radical_properties', 'radical_properties'),
            },
            'Chapter 8: Exponential Functions': {
                'Review: Equivalent Exponential Expressions': ('equivalent_exponential', 'equivalent_exponential'),
                'Exponential Functions': ('exponential_functions', 'exponential_functions'),
                'Exponential Growth and Decay': ('exponential_growth_decay', 'exponential_growth_decay'),
            },
            'Chapter 9: Polynomials and Factoring': {
                'Review: Parts of a Term with Exponents': ('parts_of_term_exponents', 'parts_of_term_exponents'),
                'Polynomial Operations': ('polynomial_operations', 'polynomial_operations'),
                'Factoring': ('factoring', 'factoring'),
            },
            'Chapter 10: Quadratic Equations': {
                'Quadratic Equations': ('quadratic_equations', 'quadratic_equations'),
                'Quadratic Graphing': ('quadratic_graphing', 'quadratic_graphing'),
            },
            'Chapter 11: Advanced Quadratics': {
                'Completing the Square': ('completing_square', 'completing_square'),
                'Quadratic Formula': ('quadratic_formula', 'quadratic_formula'),
                'Using Vertex Form': ('graphing_parabolas', 'graphing_parabolas'),
            },
            'Chapter 12: Quadratic Functions': {
                'Quadratic Functions': ('quadratic_functions', 'quadratic_functions'),
            },
            'Chapter 13: Sequences': {
                'Arithmetic Sequences': ('arithmetic_sequences', 'arithmetic_sequences'),
                'Geometric Sequences': ('geometric_sequences', 'geometric_sequences'),
                'Constructing Geometric Sequences': ('constructing_geometric_seq', 'constructing_geometric_seq'),
                'Modeling with Sequences': ('modeling_sequences', 'modeling_sequences'),
            },
        }

        # Legacy map for backwards compatibility
        self.problem_type_map = {
            # Chapter 1
            'Absolute Value': 'absolute_value',
            'Combining Like Terms': 'combining_like_terms',
            'Evaluating an Expression': 'evaluating_expressions',
            'Exponents': 'exponents',
            'Parts of a Term': 'parts_of_term',
            'Number Properties': 'number_properties',
            'Order of Operations': 'order_of_operations',
            'Square Roots': 'square_roots',
            'Substitution of Variables': 'substitution',
            'Variables': 'variables',
            # Chapter 2
            'Equations': 'equations_intro',
            'Inputs and Outputs': 'inputs_outputs',
            'Linear Equation Word Problems': 'word_problems',
            'Linear Equations': 'linear_equation',
            'Properties of Equality - Add/Subtract': 'properties_of_equality',
            'Properties of Equality - Mult/Div': 'properties_mult_div',
            'Solving Equations with Variables on Both Sides': 'variables_both_sides',
            'Solving Multi-Step Equations': 'multistep_equations',
            'What Are Solutions?': 'solutions',
            # Chapter 3
            'One-Step Inequalities': 'simple_inequalities',
            'Compound Inequalities - AND': 'compound_inequality_and',
            'Compound Inequalities - Mixed': 'compound_inequality',
            'Compound Inequalities - OR': 'compound_inequality_or',
            'Absolute Value Inequalities': 'absolute_value_inequalities',
            'Inequality Word Problems': 'inequality_word_problems',
            # Chapter 4
            'Review: Inputs and Outputs': 'inputs_outputs_review',
            'Points on a Coordinate Plane': 'graphing_points',
            'Line on a Coordinate Plane': 'graphing_lines',
            'Slope': 'slope',
            'X and Y Intercepts': 'intercepts',
            'Slope-Intercept Form': 'slope_intercept',
            'Writing Slope-Intercept Equations': 'writing_slope_intercept',
            'Point-Slope Form': 'point_slope',
            'Standard Form': 'standard_form',
            # Chapter 5
            'Systems of Equations - Graphing': 'graphing_systems',
            'Systems of Equations - Intro': 'system_of_equations',
            'Systems of Equations Using Substitution': 'systems_substitution',
            'Systems of Equations Using Elimination': 'systems_elimination',
            # Chapter 6
            'Functions': 'functions',
            'Review: Inputs/Outputs and Functions': 'inputs_outputs_functions',
            'Domain and Range': 'domain_range',
            # Chapter 7
            'Exponents - Properties': 'exponent_properties',
            'Expanding and Simplifying Expressions with Exponents': 'expanding_exponents',
            'Properties of Radicals': 'radical_properties',
            # Chapter 8
            'Review: Equivalent Exponential Expressions': 'equivalent_exponential',
            'Exponential Functions': 'exponential_functions',
            'Exponential Growth and Decay': 'exponential_growth_decay',
            # Chapter 9
            'Review: Parts of a Term with Exponents': 'parts_of_term_exponents',
            'Polynomial Operations': 'polynomial_operations',
            'Factoring': 'factoring',
            # Chapter 10
            'Quadratic Equations': 'quadratic_equations',
            'Quadratic Graphing': 'quadratic_graphing',
            # Chapter 11
            'Completing the Square': 'completing_square',
            'Quadratic Formula': 'quadratic_formula',
            'Using Vertex Form': 'graphing_parabolas',
            # Chapter 12
            'Quadratic Functions': 'quadratic_functions',
            # Chapter 13
            'Arithmetic Sequences': 'arithmetic_sequences',
            'Geometric Sequences': 'geometric_sequences',
            'Constructing Geometric Sequences': 'constructing_geometric_seq',
            'Modeling with Sequences': 'modeling_sequences',
            # Old names for backwards compatibility
            'Systems of Equations - Algebraic': 'system_of_equations',
            'Inequalities': 'inequality',
            'Word Problems - Add/Subtract': 'word_problems',
            'Multi-Step Equations': 'multistep_equations',
            'Graphing Points': 'graphing_points',
            'Graphing Parabolas': 'graphing_parabolas'
        }

        # Use legacy topics if no generators were discovered
        if not self.chapter_topics:
            print("No generators discovered, using legacy topic list")
            self.chapter_topics = self.chapter_topics_legacy

        # Setup UI
        self._create_widgets()

    def _configure_styles(self):
        """Configure modern visual styling for the application."""
        # Create style object
        self.style = ttk.Style()

        # Use modern theme
        try:
            self.style.theme_use('vista')  # Windows modern theme
        except:
            try:
                self.style.theme_use('clam')  # Cross-platform modern theme
            except:
                self.style.theme_use('default')

        # Define color palette
        self.colors = {
            'primary': '#2E86AB',      # Blue
            'primary_dark': '#1E5B7A', # Darker blue
            'secondary': '#A23B72',    # Purple accent
            'success': '#2D9F3F',      # Green
            'background': '#F8F9FA',   # Light gray
            'surface': '#FFFFFF',      # White
            'text': '#212529',         # Dark gray
            'text_secondary': '#6C757D', # Medium gray
            'border': '#DEE2E6',       # Light border
            'header_bg': '#2E86AB',    # Header blue
            'header_text': '#FFFFFF'   # Header white text
        }

        # Configure window background
        self.root.configure(bg=self.colors['background'])

        # Configure TFrame
        self.style.configure('TFrame', background=self.colors['background'])
        self.style.configure('Card.TFrame', background=self.colors['surface'],
                           relief='flat', borderwidth=0)

        # Configure TLabel
        self.style.configure('TLabel',
                           background=self.colors['background'],
                           foreground=self.colors['text'],
                           font=('Segoe UI', 10))

        self.style.configure('Title.TLabel',
                           font=('Segoe UI', 22, 'bold'),
                           foreground=self.colors['primary'],
                           background=self.colors['background'])

        self.style.configure('Subtitle.TLabel',
                           font=('Segoe UI', 10),
                           foreground=self.colors['text_secondary'],
                           background=self.colors['background'])

        self.style.configure('SectionHeader.TLabel',
                           font=('Segoe UI', 11, 'bold'),
                           foreground=self.colors['text'],
                           background=self.colors['surface'])

        self.style.configure('Description.TLabel',
                           font=('Segoe UI', 9, 'italic'),
                           foreground=self.colors['text_secondary'],
                           background=self.colors['surface'])

        self.style.configure('Status.TLabel',
                           font=('Segoe UI', 9),
                           foreground=self.colors['primary'],
                           background=self.colors['surface'],
                           padding=(10, 5))

        # Configure TLabelframe
        self.style.configure('TLabelframe',
                           background=self.colors['surface'],
                           borderwidth=2,
                           relief='solid')
        self.style.configure('TLabelframe.Label',
                           font=('Segoe UI', 11, 'bold'),
                           foreground=self.colors['primary'],
                           background=self.colors['surface'])

        # Configure TCombobox
        self.style.configure('TCombobox',
                           fieldbackground=self.colors['surface'],
                           background=self.colors['surface'],
                           foreground=self.colors['text'],
                           arrowcolor=self.colors['primary'])

        # Configure TEntry
        self.style.configure('TEntry',
                           fieldbackground=self.colors['surface'],
                           foreground=self.colors['text'])

        # Configure TButton - Default style
        self.style.configure('TButton',
                           font=('Segoe UI', 10),
                           borderwidth=0,
                           focuscolor='none',
                           relief='flat',
                           padding=(12, 8))

        # Primary button style
        self.style.configure('Primary.TButton',
                           font=('Segoe UI', 11, 'bold'),
                           foreground=self.colors['header_text'],
                           background=self.colors['primary'],
                           borderwidth=0,
                           focuscolor='none',
                           padding=(20, 12))

        self.style.map('Primary.TButton',
                      background=[('active', self.colors['primary_dark']),
                                ('pressed', self.colors['primary_dark'])])

        # Secondary button style
        self.style.configure('Secondary.TButton',
                           font=('Segoe UI', 10),
                           borderwidth=1,
                           relief='solid')

        # Configure TCheckbutton
        self.style.configure('TCheckbutton',
                           background=self.colors['surface'],
                           foreground=self.colors['text'],
                           font=('Segoe UI', 10))

        # Configure TSpinbox
        self.style.configure('TSpinbox',
                           fieldbackground=self.colors['surface'],
                           background=self.colors['surface'],
                           foreground=self.colors['text'])

    def _create_widgets(self):
        """Create and layout all GUI widgets with modern styling."""
        # Main frame with padding
        main_frame = ttk.Frame(self.root, padding="25")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Header section
        header_frame = ttk.Frame(main_frame)
        header_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))

        title_label = ttk.Label(header_frame, text="📝 Math Worksheet Generator",
                               style='Title.TLabel')
        title_label.pack()

        subtitle_label = ttk.Label(header_frame,
                                   text="Generate customized math worksheets for your students",
                                   style='Subtitle.TLabel')
        subtitle_label.pack(pady=(5, 0))

        # Get first class, unit, and topic dynamically
        first_class = list(self.chapter_topics.keys())[0] if self.chapter_topics else "Class"
        first_unit_dict = self.chapter_topics[first_class] if first_class in self.chapter_topics else {}
        first_unit = list(first_unit_dict.keys())[0] if first_unit_dict else "Unit"
        first_topic_dict = first_unit_dict.get(first_unit, {}) if first_unit_dict else {}
        first_topic = list(first_topic_dict.keys())[0] if first_topic_dict else "Topic"

        # Worksheet Selection Section
        selection_frame = ttk.LabelFrame(main_frame, text="📚 Worksheet Selection", padding="15")
        selection_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))

        # Class selection
        class_label = ttk.Label(selection_frame, text="Class:")
        class_label.grid(row=0, column=0, sticky=tk.W, pady=8)

        self.chapter_var = tk.StringVar(value=first_class)
        self.chapter_combo = ttk.Combobox(selection_frame, textvariable=self.chapter_var,
                                         state="readonly", width=35)
        self.chapter_combo['values'] = tuple(self.chapter_topics.keys())
        self.chapter_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=8, padx=(10, 0))

        # Unit selection
        unit_label = ttk.Label(selection_frame, text="Unit:")
        unit_label.grid(row=1, column=0, sticky=tk.W, pady=8)

        self.unit_var = tk.StringVar(value=first_unit)
        self.unit_combo = ttk.Combobox(selection_frame, textvariable=self.unit_var,
                                       state="readonly", width=35)
        self.unit_combo['values'] = tuple(first_unit_dict.keys()) if first_unit_dict else ()
        self.unit_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=8, padx=(10, 0))

        # Topic selection
        topic_label = ttk.Label(selection_frame, text="Topic:")
        topic_label.grid(row=2, column=0, sticky=tk.W, pady=8)

        self.topic_var = tk.StringVar(value=first_topic)
        self.topic_combo = ttk.Combobox(selection_frame, textvariable=self.topic_var,
                                       state="readonly", width=35)
        self.topic_combo['values'] = tuple(first_topic_dict.keys()) if first_topic_dict else ()
        self.topic_combo.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=8, padx=(10, 0))

        # Checkbox for generating entire unit
        self.generate_entire_chapter_var = tk.BooleanVar(value=False)
        self.generate_entire_chapter_check = ttk.Checkbutton(
            selection_frame,
            text="✓ Generate all topics in this unit",
            variable=self.generate_entire_chapter_var,
            command=self._toggle_chapter_mode
        )
        self.generate_entire_chapter_check.grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=(10, 0))

        # Configure grid weights for responsive layout
        selection_frame.columnconfigure(1, weight=1)

        # Update units when class changes
        def update_class(event=None):
            class_name = self.chapter_var.get()
            units = list(self.chapter_topics[class_name].keys()) if class_name in self.chapter_topics else []
            self.unit_combo['values'] = units
            if units:
                self.unit_var.set(units[0])
                # Update topics for first unit
                update_unit()
            else:
                self.topic_combo['values'] = ()

        self.chapter_combo.bind('<<ComboboxSelected>>', update_class)

        # Update topics when unit changes
        def update_unit(event=None):
            class_name = self.chapter_var.get()
            unit_name = self.unit_var.get()
            if class_name in self.chapter_topics and unit_name in self.chapter_topics[class_name]:
                topics = list(self.chapter_topics[class_name][unit_name].keys())
                self.topic_combo['values'] = topics
                if topics:
                    self.topic_var.set(topics[0])
            else:
                self.topic_combo['values'] = ()
            self._update_difficulty_descriptions()
            self._update_worksheet_title()
            self._update_default_num_problems()

        self.unit_combo.bind('<<ComboboxSelected>>', update_unit)
        
        # Initialize chapter mode state
        self._toggle_chapter_mode()

        # Update when topic changes
        def update_topic(event=None):
            self._update_difficulty_descriptions()
            self._update_worksheet_title()
            self._update_default_num_problems()

        self.topic_combo.bind('<<ComboboxSelected>>', update_topic)

        # Store label references for enabling/disabling
        self.unit_label = unit_label
        self.topic_label = topic_label

        # Worksheet Options Section
        options_frame = ttk.LabelFrame(main_frame, text="⚙️ Worksheet Options", padding="15")
        options_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))

        # Difficulty level selection
        difficulty_label = ttk.Label(options_frame, text="Difficulty Level:")
        difficulty_label.grid(row=0, column=0, sticky=tk.W, pady=8)

        self.difficulty_var = tk.StringVar(value="medium")
        difficulty_combo = ttk.Combobox(options_frame, textvariable=self.difficulty_var,
                                        state="readonly", width=35)
        difficulty_combo['values'] = ('easy', 'medium', 'hard', 'challenge')
        difficulty_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=8, padx=(10, 0))

        # Difficulty descriptions - store for later updates
        self.difficulty_descriptions = {
            # Chapter 1
            'Absolute Value': {
                'easy': 'Simple absolute value |a|',
                'medium': 'With arithmetic |a + b|',
                'hard': 'With multiplication |a × b|',
                'challenge': 'Nested ||a| - |b||'
            },
            'Combining Like Terms': {
                'easy': 'Simple terms (2x + 3x)',
                'medium': 'Multiple terms (3x + 5 - x + 2)',
                'hard': 'More complex (4x + 2y - x + 3y)',
                'challenge': 'Challenging combinations'
            },
            'Evaluating an Expression': {
                'easy': 'Simple substitution (x + 5, x = 3)',
                'medium': 'Multiple variables (2x + y)',
                'hard': 'Complex expressions',
                'challenge': 'Very complex expressions'
            },
            'Exponents': {
                'easy': 'Simple exponents (2³)',
                'medium': 'Multiple operations',
                'hard': 'Complex exponent rules',
                'challenge': 'Very challenging exponents'
            },
            'Square Roots': {
                'easy': 'Perfect squares √9, √16',
                'medium': 'Multiplication √4 × √9',
                'hard': 'Products √(4 × 9)',
                'challenge': 'Nested/Pythagorean'
            },
            'Substitution of Variables': {
                'easy': 'Simple substitution',
                'medium': 'Multiple variables',
                'hard': 'Complex substitution',
                'challenge': 'Very complex substitution'
            },
            'Variables': {
                'easy': 'Basic variable identification',
                'medium': 'Multiple variables',
                'hard': 'Complex expressions',
                'challenge': 'Very complex expressions'
            },
            # Chapter 2
            'Equations': {
                'easy': 'Simple equations',
                'medium': 'Two-step equations',
                'hard': 'Multi-step equations',
                'challenge': 'Complex equations'
            },
            'Inputs and Outputs': {
                'easy': 'Simple functions',
                'medium': 'Standard functions',
                'hard': 'Complex functions',
                'challenge': 'Very complex functions'
            },
            'Linear Equation Word Problems': {
                'easy': 'Numbers 1-20 (simple contexts)',
                'medium': 'Numbers 1-50 (varied contexts)',
                'hard': 'Numbers 1-100 (complex scenarios)',
                'challenge': 'Numbers 1-100 (complex scenarios)'
            },
            'Linear Equations': {
                'easy': 'Simple (ax + b = c)',
                'medium': 'Distribution, combining terms',
                'hard': 'Variables on both sides',
                'challenge': 'Fractions, nested parentheses'
            },
            'Linear Equations (OLD)': {
                'easy': 'One-step equations (x + 5 = 12)',
                'medium': 'Two-step equations (2x + 3 = 11)',
                'hard': 'Multi-step with parentheses',
                'challenge': 'Variables on both sides'
            },
            'Linear Equation Word Problems': {
                'easy': 'Direct relationships (age, money)',
                'medium': 'Equation setup required',
                'hard': 'Multiple variables/constraints',
                'challenge': 'Investment, speed, percentages'
            },
            'Linear Equation Word Problems (OLD)': {
                'easy': 'Simple scenarios',
                'medium': 'Multi-step problems',
                'hard': 'Complex word problems',
                'challenge': 'Advanced problem solving'
            },
            'Property of Equality - Add/Subtract': {
                'easy': 'Simple (x + a = b)',
                'medium': 'Subtraction (x - a = b)',
                'hard': 'Negative numbers, larger values',
                'challenge': 'Multiple terms, reorganization'
            },
            'Properties of Equality - Add/Subtract (OLD)': {
                'easy': 'Numbers 1-10 (x + 3 = 8, x - 5 = 2)',
                'medium': 'Numbers 1-20 (x + 12 = 25, x - 8 = 14)',
                'hard': 'Numbers 1-50 (may result in negatives)',
                'challenge': 'Numbers 1-50 (may result in negatives)'
            },
            'Property of Equality - Mult/Div': {
                'easy': 'Simple division (ax = b)',
                'medium': 'Fractions (x/a = b)',
                'hard': 'Negative coefficients',
                'challenge': 'Fraction coefficients, mixed ops'
            },
            'Properties of Equality - Mult/Div (OLD)': {
                'easy': 'Numbers 1-10 (3x = 12, x/2 = 5)',
                'medium': 'Numbers 1-20 (7x = 42, x/4 = 9)',
                'hard': 'Numbers 1-50 (larger products/quotients)',
                'challenge': 'Numbers 1-50 (larger products/quotients)'
            },
            'Solving Equations with Variables on Both Sides': {
                'easy': 'Simple variables both sides',
                'medium': 'Standard equations',
                'hard': 'Complex equations',
                'challenge': 'Very complex equations'
            },
            'Solving Multi-Step Equations': {
                'easy': 'Two-step equations',
                'medium': 'Three-step equations',
                'hard': 'Multi-step with parentheses',
                'challenge': 'Very complex multi-step'
            },
            'What Are Solutions?': {
                'easy': 'Identify solutions',
                'medium': 'Check solutions',
                'hard': 'Find number of solutions',
                'challenge': 'Complex solution analysis'
            },
            # Chapter 3
            'Compound Inequalities - AND': {
                'easy': 'Simple AND (3 < x < 7)',
                'medium': 'One-step solving (5 < x + 2 < 9)',
                'hard': 'Two-step solving (1 < 2x + 3 < 11)',
                'challenge': 'Negative coefficients (flip directions)'
            },
            'Compound Inequalities - Mixed': {
                'easy': 'Simple compound (3 < x < 7 or x < 2)',
                'medium': 'One-step solving (5 < x + 2 < 9)',
                'hard': 'Two-step solving (1 < 2x + 3 < 11)',
                'challenge': 'Negative coefficients (flip directions)'
            },
            'Compound Inequalities - OR': {
                'easy': 'Simple OR (x < 2 or x > 5)',
                'medium': 'One-step solving (x + 2 < 3 or x + 2 > 7)',
                'hard': 'Two-step solving (2x + 3 < 1 or 2x + 3 > 11)',
                'challenge': 'Negative coefficients (flip directions)'
            },
            'One-Step Inequalities': {
                'easy': 'Simple one-step (x + 5 < 12)',
                'medium': 'Standard one-step (2x > 8)',
                'hard': 'Harder one-step',
                'challenge': 'Challenging one-step'
            },
            # Chapter 4
            'Line on a Coordinate Plane': {
                'easy': 'Simple lines',
                'medium': 'Standard lines',
                'hard': 'Complex lines',
                'challenge': 'Very complex lines'
            },
            'Point-Slope Form': {
                'easy': 'Simple point-slope',
                'medium': 'Standard point-slope',
                'hard': 'Complex point-slope',
                'challenge': 'Very complex point-slope'
            },
            'Points on a Coordinate Plane': {
                'easy': '3 points, first quadrant only (0-10)',
                'medium': '4 points, all 4 quadrants (-5 to 5)',
                'hard': '5 points, all 4 quadrants (-10 to 10)',
                'challenge': '6 points, all 4 quadrants + axes'
            },
            'Slope-Intercept Form': {
                'easy': 'Simple slope-intercept',
                'medium': 'Standard slope-intercept',
                'hard': 'Complex slope-intercept',
                'challenge': 'Very complex slope-intercept'
            },
            'Standard Form': {
                'easy': 'Simple standard form',
                'medium': 'Standard form equations',
                'hard': 'Complex standard form',
                'challenge': 'Very complex standard form'
            },
            # Chapter 5
            'Systems of Equations - Graphing': {
                'easy': 'Integer slopes (±1, ±2), integer solution',
                'medium': 'Fractional slopes, mixed forms',
                'hard': 'Standard form, may have fractional solution',
                'challenge': 'Complex forms, fractional solutions'
            },
            'Systems of Equations - Intro': {
                'easy': 'One variable already solved',
                'medium': 'Standard form, elimination/substitution',
                'hard': 'Larger coefficients',
                'challenge': 'May have fraction solutions'
            },
            # Chapter 11
            'Using Vertex Form': {
                'easy': 'y = x² or y = -x² (vertex at origin)',
                'medium': 'y = (x - h)² + k (integer h, k)',
                'hard': 'y = a(x - h)² + k (a ≠ 1, stretch/compress)',
                'challenge': 'Fractional a, h, or k values'
            },
            # Old names for backwards compatibility
            'Inequalities': {
                'easy': 'One-step inequalities (x + 5 < 12)',
                'medium': 'Two-step inequalities (2x + 3 > 11)',
                'hard': 'Multi-step with parentheses',
                'challenge': 'Variables on both sides (direction may flip)'
            },
            'Systems of Equations': {
                'easy': 'One variable already solved',
                'medium': 'Standard form, elimination/substitution',
                'hard': 'Larger coefficients',
                'challenge': 'May have fraction solutions'
            },
            'Graphing Points': {
                'easy': '3 points, first quadrant only (0-10)',
                'medium': '4 points, all 4 quadrants (-5 to 5)',
                'hard': '5 points, all 4 quadrants (-10 to 10)',
                'challenge': '6 points, all 4 quadrants + axes'
            },
            'Graphing Parabolas': {
                'easy': 'y = x² or y = -x² (vertex at origin)',
                'medium': 'y = (x - h)² + k (integer h, k)',
                'hard': 'y = a(x - h)² + k (a ≠ 1, stretch/compress)',
                'challenge': 'Fractional a, h, or k values'
            }
        }

        # Set default description based on discovered first topic
        default_desc = ""
        if first_topic in self.difficulty_descriptions:
            default_desc = self.difficulty_descriptions[first_topic]['medium']
        self.desc_var = tk.StringVar(value=default_desc)
        desc_label = ttk.Label(options_frame, textvariable=self.desc_var,
                              style='Description.TLabel')
        desc_label.grid(row=1, column=1, sticky=tk.W, padx=(10, 0), pady=(0, 8))

        # Update description when difficulty changes
        def update_description(event=None):
            topic = self.topic_var.get()
            difficulty = self.difficulty_var.get()
            if topic in self.difficulty_descriptions:
                self.desc_var.set(self.difficulty_descriptions[topic][difficulty])
            self._update_worksheet_title()

        difficulty_combo.bind('<<ComboboxSelected>>', update_description)

        # Number of problems
        num_problems_label = ttk.Label(options_frame, text="Number of Problems:")
        num_problems_label.grid(row=2, column=0, sticky=tk.W, pady=8)

        self.num_problems_var = tk.StringVar(value="10")
        num_problems_spinbox = ttk.Spinbox(options_frame, from_=4, to=16,
                                          textvariable=self.num_problems_var,
                                          width=35)
        num_problems_spinbox.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=8, padx=(10, 0))

        # Worksheet title
        title_input_label = ttk.Label(options_frame, text="Worksheet Title:")
        title_input_label.grid(row=3, column=0, sticky=tk.W, pady=8)

        default_title = f"{first_topic} - Medium"
        self.title_var = tk.StringVar(value=default_title)
        title_entry = ttk.Entry(options_frame, textvariable=self.title_var, width=35)
        title_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=8, padx=(10, 0))

        # Include answer key checkbox
        self.answer_key_var = tk.BooleanVar(value=True)
        answer_key_check = ttk.Checkbutton(options_frame, text="✓ Include Answer Key",
                                          variable=self.answer_key_var)
        answer_key_check.grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=(10, 0))

        # Configure grid weights for responsive layout
        options_frame.columnconfigure(1, weight=1)

        # Action Buttons Section
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=(0, 15))

        # Primary action button
        generate_btn = ttk.Button(button_frame, text="📄 Generate Worksheet",
                                 command=self.generate_worksheet,
                                 style='Primary.TButton')
        generate_btn.pack(side=tk.TOP, fill=tk.X, pady=(0, 10))

        # Secondary action buttons
        secondary_frame = ttk.Frame(button_frame)
        secondary_frame.pack(fill=tk.X)

        batch_btn = ttk.Button(secondary_frame, text="Batch Generate All",
                              command=self.batch_generate,
                              style='Secondary.TButton')
        batch_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

        open_folder_btn = ttk.Button(secondary_frame, text="📁 Open Folder",
                                     command=self.open_output_folder,
                                     style='Secondary.TButton')
        open_folder_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 0))

        # Status Bar Section
        status_frame = ttk.Frame(main_frame, style='Card.TFrame', padding="10")
        status_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))

        self.status_var = tk.StringVar(value="Ready to generate worksheet")
        status_label = ttk.Label(status_frame, textvariable=self.status_var,
                                style='Status.TLabel')
        status_label.pack()

        # Configure grid weights for responsive layout
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

    def _update_difficulty_descriptions(self):
        """Update the difficulty description based on problem type."""
        topic = self.topic_var.get()
        difficulty = self.difficulty_var.get()
        if topic in self.difficulty_descriptions:
            self.desc_var.set(self.difficulty_descriptions[topic][difficulty])

    def _update_worksheet_title(self):
        """Update the worksheet title based on selected problem type and difficulty."""
        topic = self.topic_var.get()
        difficulty = self.difficulty_var.get()
        # Capitalize difficulty level for display
        difficulty_capitalized = difficulty.capitalize()
        self.title_var.set(f"{topic} - {difficulty_capitalized}")

    def _toggle_chapter_mode(self):
        """Enable/disable topic selection based on unit generation mode."""
        if self.generate_entire_chapter_var.get():
            # Disable topic selection when generating entire unit
            self.topic_combo.config(state="disabled")
        else:
            # Enable topic selection for single topic mode
            self.topic_combo.config(state="readonly")

    def _update_default_num_problems(self):
        """Update the default number of problems based on problem type."""
        topic = self.topic_var.get()
        # Get the config key from the display name
        config_key = self.problem_type_map.get(topic)
        if config_key:
            try:
                config = get_config(config_key)
                self.num_problems_var.set(str(config.default_num_problems))
            except KeyError:
                # Config not found for this topic, use default of 10
                self.num_problems_var.set("10")

    def generate_worksheet(self):
        """Generate the worksheet PDF based on user inputs."""
        try:
            # Check if generating entire chapter
            if self.generate_entire_chapter_var.get():
                self.generate_chapter_worksheets()
                return
            
            # Validate inputs
            num_problems = int(self.num_problems_var.get())
            if num_problems < 4 or num_problems > 16:
                messagebox.showerror("Invalid Input",
                                   "Number of problems must be between 4 and 16")
                return

            difficulty = self.difficulty_var.get()
            chapter = self.chapter_var.get()
            unit = self.unit_var.get()
            topic = self.topic_var.get()
            title = self.title_var.get()
            include_answer_key = self.answer_key_var.get()

            # Update status
            self.status_var.set(f"Generating {topic}...")
            self.root.update()

            # Get generator dynamically from the three-level structure
            if (chapter in self.chapter_topics and
                unit in self.chapter_topics[chapter] and
                topic in self.chapter_topics[chapter][unit]):
                generator_class = self.chapter_topics[chapter][unit][topic]
                generator_instance = generator_class()
                equations = generator_instance.generate_worksheet(difficulty, num_problems)
            # Legacy fallback for hard-coded generators
            elif topic == "Absolute Value":
                equations = self.absolute_value_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Combining Like Terms":
                equations = self.combining_like_terms_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Evaluating an Expression":
                equations = self.evaluating_expressions_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Exponents":
                equations = self.exponents_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Parts of a Term":
                equations = self.parts_of_term_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Number Properties":
                equations = self.number_properties_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Order of Operations":
                equations = self.order_of_operations_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Square Roots":
                equations = self.square_roots_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Substitution of Variables":
                equations = self.substitution_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Variables":
                equations = self.variables_gen.generate_worksheet(difficulty, num_problems)
            # Chapter 2
            elif topic == "Equations":
                equations = self.equations_intro_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Inputs and Outputs":
                equations = self.inputs_outputs_gen.generate_worksheet(difficulty, num_problems)
            # New generators
            elif topic == "Linear Equation Word Problems":
                equations = self.linear_equation_word_problems_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Linear Equation Word Problems (OLD)":
                equations = self.word_problems_gen.generate_worksheet(difficulty, num_problems, 'mixed')
            elif topic == "Linear Equations":
                equations = self.linear_equations_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Linear Equations (OLD)":
                equations = self.equation_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Property of Equality - Add/Subtract":
                equations = self.property_equality_add_sub_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Properties of Equality - Add/Subtract (OLD)":
                equations = self.properties_gen.generate_worksheet(difficulty, num_problems, 'mixed')
            elif topic == "Property of Equality - Mult/Div":
                equations = self.property_equality_mult_div_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Properties of Equality - Mult/Div (OLD)":
                equations = self.properties_mult_div_gen.generate_worksheet(difficulty, num_problems, 'mixed')
            elif topic == "Solving Equations with Variables on Both Sides":
                equations = self.variables_both_sides_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Solving Multi-Step Equations":
                equations = self.multistep_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "What Are Solutions?":
                equations = self.solutions_gen.generate_worksheet(difficulty, num_problems)
            # Chapter 3
            elif topic == "Compound Inequalities - AND":
                equations = self.compound_inequality_gen.generate_worksheet(difficulty, num_problems, compound_type='and')
            elif topic == "Compound Inequalities - Mixed":
                equations = self.compound_inequality_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Compound Inequalities - OR":
                equations = self.compound_inequality_gen.generate_worksheet(difficulty, num_problems, compound_type='or')
            elif topic == "One-Step Inequalities":
                equations = self.simple_inequalities_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Absolute Value Inequalities":
                equations = self.absolute_value_inequalities_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Inequality Word Problems":
                equations = self.inequality_word_problems_gen.generate_worksheet(difficulty, num_problems)
            # Chapter 4
            elif topic == "Line on a Coordinate Plane":
                equations = self.graphing_lines_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Point-Slope Form":
                equations = self.point_slope_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Points on a Coordinate Plane":
                equations = self.graphing_points_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Slope-Intercept Form":
                equations = self.slope_intercept_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Standard Form":
                equations = self.standard_form_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Review: Inputs and Outputs":
                equations = self.inputs_outputs_review_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Slope":
                equations = self.slope_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "X and Y Intercepts":
                equations = self.intercepts_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Writing Slope-Intercept Equations":
                equations = self.writing_slope_intercept_gen.generate_worksheet(difficulty, num_problems)
            # Chapter 5
            elif topic == "Systems of Equations - Graphing":
                equations = self.graphing_systems_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Systems of Equations - Intro":
                equations = self.systems_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Systems of Equations Using Substitution":
                equations = self.systems_substitution_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Systems of Equations Using Elimination":
                equations = self.systems_elimination_gen.generate_worksheet(difficulty, num_problems)
            # Chapter 6
            elif topic == "Functions":
                equations = self.functions_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Review: Inputs/Outputs and Functions":
                equations = self.inputs_outputs_functions_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Domain and Range":
                equations = self.domain_range_gen.generate_worksheet(difficulty, num_problems)
            # Chapter 7
            elif topic == "Exponents - Properties":
                equations = self.exponent_properties_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Expanding and Simplifying Expressions with Exponents":
                equations = self.expanding_exponents_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Properties of Radicals":
                equations = self.radical_properties_gen.generate_worksheet(difficulty, num_problems)
            # Chapter 8
            elif topic == "Review: Equivalent Exponential Expressions":
                equations = self.equivalent_exponential_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Exponential Functions":
                equations = self.exponential_functions_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Exponential Growth and Decay":
                equations = self.exponential_growth_decay_gen.generate_worksheet(difficulty, num_problems)
            # Chapter 9
            elif topic == "Review: Parts of a Term with Exponents":
                equations = self.parts_of_term_exponents_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Polynomial Operations":
                equations = self.polynomial_operations_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Factoring":
                equations = self.factoring_gen.generate_worksheet(difficulty, num_problems)
            # Chapter 10
            elif topic == "Quadratic Equations":
                equations = self.quadratic_equations_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Quadratic Graphing":
                equations = self.quadratic_graphing_gen.generate_worksheet(difficulty, num_problems)
            # Chapter 11
            elif topic == "Completing the Square":
                equations = self.completing_square_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Quadratic Formula":
                equations = self.quadratic_formula_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Using Vertex Form":
                equations = self.parabola_gen.generate_worksheet(difficulty, num_problems)
            # Chapter 12
            elif topic == "Quadratic Functions":
                equations = self.quadratic_functions_gen.generate_worksheet(difficulty, num_problems)
            # Chapter 13
            elif topic == "Arithmetic Sequences":
                equations = self.arithmetic_sequences_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Geometric Sequences":
                equations = self.geometric_sequences_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Constructing Geometric Sequences":
                equations = self.constructing_geometric_seq_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Modeling with Sequences":
                equations = self.modeling_sequences_gen.generate_worksheet(difficulty, num_problems)
            # Backwards compatibility
            elif topic == "Systems of Equations - Algebraic":
                equations = self.systems_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Inequalities":
                equations = self.inequality_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Word Problems - Add/Subtract":
                equations = self.word_problems_gen.generate_worksheet(difficulty, num_problems, 'mixed')
            elif topic == "Multi-Step Equations":
                equations = self.multistep_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Graphing Points":
                equations = self.graphing_points_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Graphing Parabolas":
                equations = self.parabola_gen.generate_worksheet(difficulty, num_problems)
            else:
                equations = self.equation_gen.generate_worksheet(difficulty, num_problems)

            # Ask user where to save
            # Get the config key for the problem type
            config_key = self.problem_type_map.get(topic)
            default_filename = f"{config_key}_{difficulty}.pdf"
            # Uncomment below to include timestamp in filename:
            # default_filename = f"{config_key}_{difficulty}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            output_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
                initialfile=default_filename
            )

            if not output_path:
                # User cancelled
                self.status_var.set("Ready to generate worksheet")
                return

            # Update status
            self.status_var.set("Creating PDF...")
            self.root.update()

            # Generate PDF
            self.pdf_gen.generate_worksheet(equations, output_path, title, include_answer_key)

            # Success message
            self.status_var.set(f"Worksheet saved successfully!")
            messagebox.showinfo("Success",
                              f"Worksheet generated successfully!\n\nSaved to:\n{output_path}")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)}")
            self.status_var.set("Error generating worksheet")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
            self.status_var.set("Error generating worksheet")
    
    def open_output_folder(self):
        """Open the output folder in file explorer."""
        # Determine the most likely output folder
        possible_folders = [
            "easy_worksheets",
            "medium_worksheets",
            "hard_worksheets",
            "challenge_worksheets",
            "output"
        ]

        # Find the first existing folder or use current directory
        output_folder = "."
        for folder in possible_folders:
            if os.path.exists(folder):
                output_folder = folder
                break

        # Open folder in system file explorer
        try:
            if os.name == 'nt':  # Windows
                os.startfile(os.path.abspath(output_folder))
            elif os.name == 'posix':  # macOS/Linux
                subprocess.run(['open' if sys.platform == 'darwin' else 'xdg-open',
                              os.path.abspath(output_folder)])
            self.status_var.set(f"Opened folder: {output_folder}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not open folder:\n{str(e)}")

    def batch_generate(self):
        """Launch batch generation dialog and run batch generator script."""
        # Create dialog window
        dialog = tk.Toplevel(self.root)
        dialog.title("Batch Generate Worksheets")
        dialog.geometry("550x400")
        dialog.resizable(False, False)

        # Make dialog modal
        dialog.transient(self.root)
        dialog.grab_set()
        dialog.focus_set()

        # Main frame
        frame = ttk.Frame(dialog, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(frame, text="Batch Generate All Worksheets",
                               font=("Helvetica", 14, "bold"))
        title_label.pack(pady=(0, 20))

        # Info text
        info_text = tk.Text(frame, height=8, width=55, wrap=tk.WORD,
                           font=("Helvetica", 9))
        info_text.pack(pady=(0, 10))
        info_text.insert("1.0",
            "This will automatically discover and generate worksheets from ALL "
            "generators in the generators/chapter## directories.\n\n"
            "• Discovers 100+ generators automatically\n"
            "• Skips generators that timeout (>6 seconds)\n"
            "• Logs errors and continues\n"
            "• Saves to easy_worksheets/ folder\n\n"
            "This may take 3-5 minutes to complete.")
        info_text.config(state=tk.DISABLED)

        # Difficulty selection
        difficulty_frame = ttk.Frame(frame)
        difficulty_frame.pack(pady=10)

        ttk.Label(difficulty_frame, text="Difficulty:").pack(side=tk.LEFT, padx=5)
        difficulty_var = tk.StringVar(value="easy")
        difficulty_combo = ttk.Combobox(difficulty_frame, textvariable=difficulty_var,
                                       values=["easy", "medium", "hard", "challenge"],
                                       state="readonly", width=15)
        difficulty_combo.pack(side=tk.LEFT, padx=5)

        # Progress bar
        progress_bar = ttk.Progressbar(frame, length=400, mode='determinate')
        progress_bar.pack(pady=10)

        # Progress/Status label
        status_var = tk.StringVar(value="")
        status_label = ttk.Label(frame, textvariable=status_var,
                                font=("Helvetica", 9), foreground="blue")
        status_label.pack(pady=5)

        # Button frame
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=20)

        def run_batch():
            """Run the batch generation in a separate thread."""
            difficulty = difficulty_var.get()
            output_dir = f"{difficulty}_worksheets"

            # Disable buttons during generation
            start_btn.config(state=tk.DISABLED)
            cancel_btn.config(text="Close", command=dialog.destroy)

            status_var.set(f"Generating {difficulty} worksheets...")
            dialog.update()

            def run_script():
                try:
                    import re
                    # Run batch_generate_worksheets.py script with live output
                    process = subprocess.Popen(
                        ["python", "batch_generate_worksheets.py",
                         "--difficulty", difficulty,
                         "--output", output_dir],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        text=True,
                        bufsize=1,
                        cwd=os.path.dirname(os.path.abspath(__file__))
                    )

                    total_generators = 0
                    current = 0

                    # Read output line by line for progress updates
                    for line in process.stdout:
                        # Extract total from "Found X generators"
                        if "Found" in line and "generators" in line:
                            match = re.search(r"Found (\d+) generators", line)
                            if match:
                                total_generators = int(match.group(1))

                        # Extract current progress from "[X/Y]"
                        match = re.search(r"\[(\d+)/(\d+)\]", line)
                        if match:
                            current = int(match.group(1))
                            total = int(match.group(2))
                            progress = (current / total) * 100
                            progress_bar['value'] = progress
                            status_var.set(f"Generating worksheet {current}/{total}...")
                            dialog.update()

                    process.wait()

                    # Final status
                    progress_bar['value'] = 100
                    status_var.set(f"✓ Complete! Generated {current}/{total_generators} worksheets")

                    messagebox.showinfo("Batch Generation Complete",
                                      f"Worksheets saved to:\n{output_dir}/\n\n"
                                      f"Successfully generated {current} worksheets!")

                except Exception as e:
                    status_var.set(f"Error: {str(e)[:50]}")
                    messagebox.showerror("Error", f"Batch generation failed:\n{str(e)}")

                finally:
                    start_btn.config(state=tk.NORMAL)

            # Run in separate thread to keep GUI responsive
            thread = threading.Thread(target=run_script)
            thread.daemon = True
            thread.start()

        start_btn = ttk.Button(btn_frame, text="Start Batch Generation", command=run_batch)
        start_btn.pack(side=tk.LEFT, padx=5)

        cancel_btn = ttk.Button(btn_frame, text="Cancel", command=dialog.destroy)
        cancel_btn.pack(side=tk.LEFT, padx=5)

        # Ensure all widgets are rendered
        dialog.update_idletasks()

    def generate_chapter_worksheets(self):
        """Generate worksheets for all topics in the selected unit."""
        try:
            # Validate inputs
            num_problems = int(self.num_problems_var.get())
            if num_problems < 4 or num_problems > 16:
                messagebox.showerror("Invalid Input",
                                   "Number of problems must be between 4 and 16")
                return

            difficulty = self.difficulty_var.get()
            chapter = self.chapter_var.get()
            unit = self.unit_var.get()
            include_answer_key = self.answer_key_var.get()

            # Get all topics for this unit
            if chapter not in self.chapter_topics or unit not in self.chapter_topics[chapter]:
                messagebox.showerror("Error", "Invalid class or unit selection")
                return

            topics = list(self.chapter_topics[chapter][unit].keys())
            if not topics:
                messagebox.showerror("Error", "No topics found for this unit")
                return

            # Ask user where to save the unit folder
            output_dir = filedialog.askdirectory(
                title=f"Select folder to save {unit} worksheets"
            )

            if not output_dir:
                # User cancelled
                self.status_var.set("Ready to generate worksheet")
                return

            # Create unit folder
            import os
            folder_name = f"{chapter}_{unit}".replace(":", "").replace(" ", "_")
            unit_dir = os.path.join(output_dir, folder_name)
            os.makedirs(unit_dir, exist_ok=True)
            
            # Generate worksheets for each topic
            total_topics = len(topics)
            successful = 0
            failed = []
            
            self.status_var.set(f"Generating {total_topics} worksheets...")
            self.root.update()
            
            for idx, topic in enumerate(topics, 1):
                try:
                    self.status_var.set(f"Generating {idx}/{total_topics}: {topic}...")
                    self.root.update()
                    
                    # Generate problems for this topic
                    equations = self._get_equations_for_topic(topic, difficulty, num_problems)
                    
                    if not equations:
                        failed.append((topic, "No problems generated"))
                        continue
                    
                    # Create filename
                    safe_topic = topic.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")
                    filename = f"{safe_topic}_{difficulty}.pdf"
                    output_path = os.path.join(unit_dir, filename)

                    # Generate title
                    title = f"{chapter} - {unit} - {topic} ({difficulty.capitalize()})"

                    # Generate PDF
                    self.pdf_gen.generate_worksheet(equations, output_path, title, include_answer_key)
                    successful += 1

                except Exception as e:
                    failed.append((topic, str(e)))
                    continue

            # Show completion message
            message = f"Unit generation complete!\n\n"
            message += f"Successful: {successful}/{total_topics}\n"
            message += f"Saved to: {unit_dir}\n"

            if failed:
                message += f"\nFailed topics ({len(failed)}):\n"
                for topic, error in failed[:5]:  # Show first 5 failures
                    message += f"  - {topic}: {error[:50]}\n"
                if len(failed) > 5:
                    message += f"  ... and {len(failed) - 5} more"

            self.status_var.set(f"Generated {successful}/{total_topics} worksheets")
            messagebox.showinfo("Unit Generation Complete", message)

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)}")
            self.status_var.set("Error generating unit")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
            self.status_var.set("Error generating unit")
    
    def _get_equations_for_topic(self, topic, difficulty, num_problems):
        """Get equations for a given topic. Reuses the logic from generate_worksheet."""
        # Chapter 1
        if topic == "Absolute Value":
            return self.absolute_value_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Combining Like Terms":
            return self.combining_like_terms_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Evaluating an Expression":
            return self.evaluating_expressions_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Exponents":
            return self.exponents_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Parts of a Term":
            return self.parts_of_term_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Number Properties":
            return self.number_properties_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Order of Operations":
            return self.order_of_operations_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Square Roots":
            return self.square_roots_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Substitution of Variables":
            return self.substitution_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Variables":
            return self.variables_gen.generate_worksheet(difficulty, num_problems)
        # Chapter 2
        elif topic == "Equations":
            return self.equations_intro_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Inputs and Outputs":
            return self.inputs_outputs_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Linear Equation Word Problems":
            return self.linear_equation_word_problems_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Linear Equation Word Problems (OLD)":
            return self.word_problems_gen.generate_worksheet(difficulty, num_problems, 'mixed')
        elif topic == "Linear Equations":
            return self.linear_equations_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Linear Equations (OLD)":
            return self.equation_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Property of Equality - Add/Subtract":
            return self.property_equality_add_sub_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Properties of Equality - Add/Subtract (OLD)":
            return self.properties_gen.generate_worksheet(difficulty, num_problems, 'mixed')
        elif topic == "Property of Equality - Mult/Div":
            return self.property_equality_mult_div_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Properties of Equality - Mult/Div (OLD)":
            return self.properties_mult_div_gen.generate_worksheet(difficulty, num_problems, 'mixed')
        elif topic == "Solving Equations with Variables on Both Sides":
            return self.variables_both_sides_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Solving Multi-Step Equations":
            return self.multistep_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "What Are Solutions?":
            return self.solutions_gen.generate_worksheet(difficulty, num_problems)
        # Chapter 3
        elif topic == "Compound Inequalities - AND":
            return self.compound_inequality_gen.generate_worksheet(difficulty, num_problems, compound_type='and')
        elif topic == "Compound Inequalities - Mixed":
            return self.compound_inequality_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Compound Inequalities - OR":
            return self.compound_inequality_gen.generate_worksheet(difficulty, num_problems, compound_type='or')
        elif topic == "One-Step Inequalities":
            return self.simple_inequalities_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Absolute Value Inequalities":
            return self.absolute_value_inequalities_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Inequality Word Problems":
            return self.inequality_word_problems_gen.generate_worksheet(difficulty, num_problems)
        # Chapter 4
        elif topic == "Line on a Coordinate Plane":
            return self.graphing_lines_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Point-Slope Form":
            return self.point_slope_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Points on a Coordinate Plane":
            return self.graphing_points_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Slope-Intercept Form":
            return self.slope_intercept_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Standard Form":
            return self.standard_form_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Review: Inputs and Outputs":
            return self.inputs_outputs_review_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Slope":
            return self.slope_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "X and Y Intercepts":
            return self.intercepts_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Writing Slope-Intercept Equations":
            return self.writing_slope_intercept_gen.generate_worksheet(difficulty, num_problems)
        # Chapter 5
        elif topic == "Systems of Equations - Graphing":
            return self.graphing_systems_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Systems of Equations - Intro":
            return self.systems_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Systems of Equations Using Substitution":
            return self.systems_substitution_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Systems of Equations Using Elimination":
            return self.systems_elimination_gen.generate_worksheet(difficulty, num_problems)
        # Chapter 6
        elif topic == "Functions":
            return self.functions_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Review: Inputs/Outputs and Functions":
            return self.inputs_outputs_functions_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Domain and Range":
            return self.domain_range_gen.generate_worksheet(difficulty, num_problems)
        # Chapter 7
        elif topic == "Exponents - Properties":
            return self.exponent_properties_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Expanding and Simplifying Expressions with Exponents":
            return self.expanding_exponents_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Properties of Radicals":
            return self.radical_properties_gen.generate_worksheet(difficulty, num_problems)
        # Chapter 8
        elif topic == "Review: Equivalent Exponential Expressions":
            return self.equivalent_exponential_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Exponential Functions":
            return self.exponential_functions_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Exponential Growth and Decay":
            return self.exponential_growth_decay_gen.generate_worksheet(difficulty, num_problems)
        # Chapter 9
        elif topic == "Review: Parts of a Term with Exponents":
            return self.parts_of_term_exponents_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Polynomial Operations":
            return self.polynomial_operations_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Factoring":
            return self.factoring_gen.generate_worksheet(difficulty, num_problems)
        # Chapter 10
        elif topic == "Quadratic Equations":
            return self.quadratic_equations_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Quadratic Graphing":
            return self.quadratic_graphing_gen.generate_worksheet(difficulty, num_problems)
        # Chapter 11
        elif topic == "Completing the Square":
            return self.completing_square_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Quadratic Formula":
            return self.quadratic_formula_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Using Vertex Form":
            return self.parabola_gen.generate_worksheet(difficulty, num_problems)
        # Chapter 12
        elif topic == "Quadratic Functions":
            return self.quadratic_functions_gen.generate_worksheet(difficulty, num_problems)
        # Chapter 13
        elif topic == "Arithmetic Sequences":
            return self.arithmetic_sequences_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Geometric Sequences":
            return self.geometric_sequences_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Constructing Geometric Sequences":
            return self.constructing_geometric_seq_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Modeling with Sequences":
            return self.modeling_sequences_gen.generate_worksheet(difficulty, num_problems)
        # Backwards compatibility
        elif topic == "Systems of Equations - Algebraic":
            return self.systems_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Inequalities":
            return self.inequality_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Word Problems - Add/Subtract":
            return self.word_problems_gen.generate_worksheet(difficulty, num_problems, 'mixed')
        elif topic == "Multi-Step Equations":
            return self.multistep_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Graphing Points":
            return self.graphing_points_gen.generate_worksheet(difficulty, num_problems)
        elif topic == "Graphing Parabolas":
            return self.parabola_gen.generate_worksheet(difficulty, num_problems)
        else:
            return self.equation_gen.generate_worksheet(difficulty, num_problems)


def main():
    """Main entry point for the GUI application."""
    root = tk.Tk()
    app = WorksheetGeneratorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
