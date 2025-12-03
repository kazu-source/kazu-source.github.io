# Claude Code Session Context
**Last Updated:** December 2, 2025

## Current Session: High School Worksheet Generators

### Progress Check
Run this command anytime to see visual progress:
```bash
python check_progress.py
```

**Current Status: 36/188 generators (19%)**

### What We're Building
Python worksheet generators for 3 high school courses:
- **Geometry** (9 Units, 60 topics) - 19 done
- **Algebra 2** (12 Units, 63 topics) - 10 done
- **IM1** (9 Units, 65 topics) - 7 done

Each generator creates randomized math problems with 4 difficulty levels and LaTeX step-by-step solutions.

---

## Directory Structure
```
generators/High_School/
├── Geometry/Unit_1/ through Unit_9/
├── Algebra_2/Unit_1/ through Unit_12/
└── IM1/Unit_1/ through Unit_9/
```

## Generator Template
```python
"""
[Topic Name] Generator
Creates problems about [topic description]
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation


class [TopicName]Generator:
    """Generates problems about [topic]."""

    def __init__(self, seed=None):
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Basic concept recognition"""
        problem_type = random.choice(['type1', 'type2'])
        latex = "\\text{Problem here}"
        solution = "answer"
        steps = ["Step 1", "Step 2"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Apply concept with simple values"""
        return Equation(latex="...", solution="...", steps=[], difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Multi-step or algebraic problems"""
        return Equation(latex="...", solution="...", steps=[], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Word problems or proofs"""
        return Equation(latex="...", solution="...", steps=[], difficulty='challenge')


def main():
    """Test the generator."""
    generator = [TopicName]Generator()
    for diff in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{diff.upper()} Problems:")
        for problem in generator.generate_worksheet(diff, 2):
            print(f"  {problem.latex}")
            print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
```

## LaTeX Formatting Reference
- Text: `\\text{word}`
- Fractions: `\\frac{a}{b}`
- Geometry: `\\triangle`, `\\angle`, `^\\circ`, `\\parallel`, `\\perp`, `\\sim`, `\\cong`
- Algebra: `\\sqrt{}`, `\\sqrt[3]{}`, `\\log`, `\\ln`, `e^{}`, `i`, `\\pi`
- Inequalities: `\\leq`, `\\geq`, `<`, `>`, `\\neq`
- Trig: `\\sin`, `\\cos`, `\\tan`

## Topics Source
All topics defined in `High School Worksheet Topics List.xlsx`

---

# CONTINUATION PROMPT

Copy everything below this line to continue the session:

---

Continue creating the missing high school worksheet generators. Use parallel Task agents (one per course) for speed.

**Context:**
- Working directory: `c:\Users\Administrator\Documents\GitHub\whymath\worksheet-generator`
- Run `python check_progress.py` for current status
- Topics source: `High School Worksheet Topics List.xlsx`
- Template: See `CLAUDE_SESSION_CONTEXT.md`

**GEOMETRY missing (~41 generators):**

Unit 2: dilation_preserved_properties, properties_definitions_transformations

Unit 3: proofs_with_transformations, transformations_and_congruence, triangle_congruence_from_transformations, theorems_triangle_properties, working_with_triangles, theorems_quadrilateral_properties, proofs_general_theorems

Unit 4: constructing_lines_angles, definitions_of_similarity, intro_triangle_similarity, angle_bisector_theorem, solving_similar_congruent_triangles, proving_relationships_similarity

Unit 5: modeling_similar_congruent_triangles, pythagorean_theorem_proofs, ratios_in_right_triangles, solving_side_right_triangle_trig, solving_angle_right_triangle_trig, sine_cosine_complementary_angles

Unit 6: modeling_right_triangles, dividing_line_segments, problem_solving_distance_coordinate, parallel_perpendicular_lines_coordinate

Unit 7: equations_parallel_perpendicular_lines, graphs_circles_intro, expanded_equation_circle

Unit 8: focus_directrix_parabola, circle_basics, arc_length_degrees, intro_radians, arc_length_radians, sectors, inscribed_angles, inscribed_shapes_problem_solving, proofs_inscribed_shapes, properties_tangents, constructing_regular_polygons_inscribed, constructing_circumcircles_incircles

Unit 9: constructing_line_tangent_circle, 2d_vs_3d_objects, cavalieris_principle

**ALGEBRA 2 missing (~53 generators):**

Unit 1: polynomial_add_subtract, polynomial_mult_div, special_products

Unit 2: the_number_system, imaginary_unit_i, add_sub_complex_numbers, multiplying_complex_numbers, quadratics_complex_solutions

Unit 3: greatest_common_factor, factoring_out_monomials, higher_degree_polynomial_factorization, polynomial_patterns_factorization

Unit 4 (create dir): dividing_polynomials, polynomial_division_linear_factors, dividing_quadratics_linear_factors, polynomial_remainder_theorem

Unit 5 (create dir): graphing_functions, what_are_zeros, intervals_pos_neg, end_behavior_graphs, review_of_graphs

Unit 6: properties_exponents_add_sub, properties_exponents_mult_div, evaluating_exponents_radicals, equivalent_forms_exponents, solving_exponential_equations

Unit 7: rate_of_change_exponential, creating_exponential_graphs

Unit 8: e_constant, natural_log, properties_of_logarithms, change_of_base_formula, solving_exponential_with_logs, real_life_exponential_logs

Unit 9 (create dir): translations_of_graphs, reflection_of_graphs, symmetry_of_graphs, scaling_functions, graphs_square_root, graphs_cube_root, graphs_exponential, graphs_logarithmic

Unit 10 (create dir): rational_equations, square_root_equations, cube_root_equations, quadratics_review, solving_by_graphing

Unit 11: radians, why_radians, pythagorean_identity, graphs_sin_cos_tan, amplitude_midline_period, graphing_trig_functions

Unit 12 (create dir): models_of_functions, interpreting_functions_without_graphing, manipulating_formulas

**IM1 missing (~58 generators):**

Unit 1: parts_of_a_term, expression_vs_equation, circle_expressions_in_equation, expressions_part_of_equation, evaluating_expressions, combining_like_terms_first_power, combining_like_terms_multiple_variables, like_terms_by_powers, combining_like_terms_full, equivalent_expressions, evaluating_after_simplifying

Unit 2: what_is_an_equation, solving_equations_add_sub, solving_equations_mult_div, solving_equations_parenthesis, inverse_operations, equations_variables_both_sides, multi_step_equations_variables_both_sides

Unit 3: what_is_absolute_value, absolute_value_expressions

Unit 4: inequalities_intro, number_of_solutions_inequalities, solving_inequalities_add_sub, solving_inequalities_mult_div, multi_step_inequalities, absolute_value_inequalities

Unit 5 (create dir): rates, dimensional_analysis, word_problems_dimensional_analysis

Unit 6: linear_equations_intro, linear_equations_unknown_coefficients, horizontal_vertical_lines, intercepts, slope_and_intercepts, slope_intercepts_word_problems

Unit 7: graphing_slope_intercept, word_problems_slope_intercept, point_slope_form, graphing_point_slope, word_problems_point_slope, standard_form, graphing_standard_form, word_problems_standard_form, combination_equation_types, when_to_use_which_equation

Unit 8: systems_of_equations_intro, solving_systems_graphing, modeling_systems_graphs, infinite_no_solution, solving_systems_substitution, checking_your_answer, systems_word_problems_basic, systems_word_problems_money, systems_word_problems_rate, checking_answer_plugin_logic

Unit 9 (create dir): graphing_two_variable_inequalities, systems_of_inequalities, modeling_two_variable_inequalities

**Instructions:**
1. Spawn 3 parallel Task agents (one per course)
2. Each generator needs complete implementations for all 4 difficulty levels
3. Use `random.choice()` for varied problem types within each difficulty
4. Generate clean integer answers when possible
5. Include step-by-step LaTeX solutions

---

## Previous Session Summary (December 1, 2025)

### K-2 Difficulty Level Refactoring
- Refactored 103 K-2 generators to remove difficulty levels
- Created `refactor_k2_generators.py` and `generate_k2_worksheets.py`

### K-8 Coverage: Complete (424 generators across 90 units)

### High School Algebra: Complete (112 generators, 19 working topics)

## Key Files Reference
- `batch_generate_worksheets.py` - Main batch generation
- `generate_k2_worksheets.py` - K-2 specific generation
- `check_progress.py` - Visual progress tracker for HS generators
- `pdf_generator.py` - PDF rendering engine
- `equation_generator.py` - Base Equation dataclass
- `High School Worksheet Topics List.xlsx` - Master topic list
