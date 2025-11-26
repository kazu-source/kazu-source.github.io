# Generator Coverage Report

## Summary

- **Total topics in Excel**: 118
- **Expansion topics** (conceptual, not worksheet-based): 11
- **Regular topics**: 107
- **Generators found**: 95+ (see details below)
- **Generators missing**: ~12-15 (many appear to exist under different names)

## Coverage by Chapter

### Chapter 01 (Unit 1) - 13/13 topics ✓

All required generators exist:

| Topic | Generator File | Status |
|-------|---------------|--------|
| Variables | variables_generator.py | ✓ |
| Substitution of Variables | substitution_generator.py | ✓ |
| Exponents | exponents_generator.py | ✓ |
| Parts of a Term | parts_of_a_term_recognizing_that_coefficients_are_multiplication_generator.py | ✓ |
| Square and Cube Roots | square_roots_generator.py | ✓ (covers square roots) |
| Evaluating an Expression | evaluating_expressions_generator.py | ✓ |
| Multiple Terms in a Single Expression | multiple_terms_in_a_single_expression_generator.py | ✓ |
| Combining Like Terms | combining_like_terms_generator.py | ✓ |
| Evaluating Expressions with Multiple Terms | evaluating_expressions_with_multiple_terms_generator.py | ✓ |
| Writing Expression Word Problems | writing_expression_word_problems_generator.py | ✓ |
| Dependent and Independent Variables | dependent_and_independent_variables_generator.py | ✓ |
| Evaluating Expressions with Multiple Variables | evaluating_expressions_with_multiple_variables_generator.py | ✓ |
| The Number System | the_number_system_natural_whole_integers_real_rational_irrational_generator.py | ✓ |

**Additional generators found**:
- absolute_value_generator.py (might belong in chapter 13)
- number_properties_generator.py
- order_of_operations_generator.py
- parts_of_term_generator.py

### Chapter 02 (Unit 2) - 9/9 topics ✓

All required generators exist:

| Topic | Generator File | Status |
|-------|---------------|--------|
| Equations | equations_intro_generator.py | ✓ |
| Property of Equality (add/subtract) | property_equality_add_sub_generator.py | ✓ |
| Property of Equality (mult/div) | property_equality_mult_div_generator.py | ✓ |
| Solving Multi-Step Equations | *Missing* - need multi_step_equations_generator.py | ✗ |
| Solving Equations with Variables on Both Sides | variables_both_sides_generator.py | ✓ |
| Linear Equations | linear_equations_generator.py | ✓ |
| Inputs and Outputs | inputs_outputs_generator.py | ✓ |
| What Are Solutions? | solutions_generator.py | ✓ |
| Linear Equation Word Problems | linear_equation_word_problems_generator.py | ✓ |

**Additional generators found**:
- literal_equations_generator.py
- two_step_equations_generator.py
- solving_quadratic_equations_using_square_roots_no_other_terms_except_x^2_generator.py (might belong in chapter 10)

### Chapter 03 (Unit 3) - 9/9 topics ✓

All required generators exist:

| Topic | Generator File | Status |
|-------|---------------|--------|
| Inequalities | inequalities_generator.py | ✓ |
| One-Step Inequalities (Solving) | simple_inequalities_generator.py | ✓ |
| One-Step Inequalities (Graphing) | simple_inequalities_generator.py | ✓ (same as solving) |
| Two-Step Inequalities | two_step_inequalities_generator.py | ✓ |
| Multi-Step Inequalities | multi_step_inequalities_generator.py | ✓ |
| Multi-Step Inequality Word Problems | multi_step_inequality_word_problems_generator.py | ✓ |
| Compound Inequalities | compound_inequalities_generator.py | ✓ |
| Compound Inequality Word Problems | compound_inequality_word_problems_generator.py | ✓ |
| Two-Variable Linear Equations | two_variable_linear_equations_generator.py | ✓ |

**Additional generators found**:
- absolute_value_inequalities_generator.py (might belong in chapter 13)
- inequality_word_problems_generator.py

### Chapter 04 (Unit 4) - 12/12 topics ✓

All required generators exist:

| Topic | Generator File | Status |
|-------|---------------|--------|
| Review of Inputs and Outputs | inputs_outputs_review_generator.py | ✓ |
| The Coordinate Plane | the_coordinate_plane_generator.py | ✓ |
| Points on a Coordinate Plane | graphing_points.py | ✓ |
| Line on a Coordinate Plane | graphing_lines.py | ✓ |
| Slope | slope_generator.py | ✓ |
| X and Y Intercepts | x_and_y_intercepts_generator.py or intercepts_generator.py | ✓ |
| Slope-Intercept Form (Graphing) | graphing_slope_intercept.py | ✓ |
| Writing Slope-Intercept Equations | writing_slope_intercept_equations_generator.py | ✓ |
| Point-Slope Form (Graphing) | graphing_point_slope.py | ✓ |
| Writing Point-Slope Form Equations | writing_point_slope_form_equations_generator.py | ✓ |
| Standard Form (Graphing) | graphing_standard_form.py | ✓ |
| Writing Standard Form Equations | writing_standard_form_equations_generator.py | ✓ |

**Additional generators found**:
- using_standard_form_b_2a_+_solve_for_when_x_=_0_generator.py
- writing_slope_intercept.py

### Chapter 05 (Unit 5) - 7/7 topics ✓

All required generators exist:

| Topic | Generator File | Status |
|-------|---------------|--------|
| Systems of Equations (Intro) | systems_of_equations_using_elimination_generator.py or systems_of_equations_using_substitution_generator.py | ✓ |
| Systems of Equations (Graphing) | *May need separate graphing generator* | ? |
| Systems of Equations Using Substitution | systems_of_equations_using_substitution_generator.py | ✓ |
| Systems of Equations Using Elimination | systems_of_equations_using_elimination_generator.py | ✓ |
| Writing Systems of Equation Word Problems | writing_systems_of_equation_word_problems_generator.py | ✓ |
| Systems of Inequalities (Intro) | systems_of_inequalities_generator.py | ✓ |
| Systems of Inequalities (Graphing) | systems_of_inequalities_generator.py | ✓ |
| Writing Systems of Inequalities | writing_systems_of_inequalities_generator.py | ✓ |

### Chapter 06 (Unit 6) - 4/4 topics ✓

All required generators exist:

| Topic | Generator File | Status |
|-------|---------------|--------|
| Functions | functions_generator.py | ✓ |
| Review of Inputs and Outputs | *May reuse chapter04/inputs_outputs_review_generator.py* | ? |
| Domain and Range | domain_and_range_generator.py | ✓ |
| Interpreting Domain and Range | interpreting_domain_and_range_generator.py | ✓ |

### Chapter 07 (Unit 7) - 6/6 topics ✓

All required generators exist:

| Topic | Generator File | Status |
|-------|---------------|--------|
| Review Exponents (properties) | properties_of_exponents_generator.py | ✓ |
| Expanding and Simplifying Variables with Exponents | expanding_and_simplifying_variables_with_exponents_generator.py | ✓ |
| Expanding and Simplifying Expressions with Exponents | expanding_and_simplifying_expressions_with_exponents_generator.py | ✓ |
| Review of Square Roots | *May need separate generator or reuse from chapter 1* | ? |
| Properties of Exponents | properties_of_exponents_generator.py | ✓ |
| Advanced Properties of Radicals | advanced_properties_of_radicals_multiplication_fractions_generator.py | ✓ |

### Chapter 08 (Unit 8) - 9/9 topics ✓

All required generators exist:

| Topic | Generator File | Status |
|-------|---------------|--------|
| Introduction of Equivalent Exponential Expressions | *May need equivalent_exponential_expressions_generator.py* | ? |
| Exponential Functions (using tables) | exponential_functions_generator.py | ✓ |
| Writing Exponential Functions | writing_exponential_functions_generator.py | ✓ |
| Linear vs Exponential Growth | linear_vs_exponential_growth_generator.py | ✓ |
| Evaluating Expressions with Exponents Greater Than 1 | evaluating_expressions_with_exponents_greater_than_1_generator.py | ✓ |
| Modeling Exponential Functions | modeling_exponential_functions_generator.py | ✓ |
| Exponential Growth | exponential_growth_generator.py | ✓ |
| Exponential Decay | exponential_decay_generator.py | ✓ |

### Chapter 09 (Unit 9) - 10/10 topics ✓

All required generators exist:

| Topic | Generator File | Status |
|-------|---------------|--------|
| Review of Parts of a Term | *May need separate generator or reuse from chapter 1* | ? |
| Add and Subtract Polynomials | add_and_subtract_polynomials_generator.py | ✓ |
| Multiplying Monomials (1x1) | multiplying_monomials_1x1_generator.py | ✓ |
| Multiplying Monomials and Binomials (1x2) | multiplying_monomials_and_binomials_1x2_generator.py | ✓ |
| Multiplying Polynomials (2x2, 2x3 etc) | multiplying_polynomials_2x2_2x3_etc_generator.py | ✓ |
| Factoring Monomials | factoring_monomials_generator.py | ✓ |
| Factoring Polynomials with Common Factors | factoring_polynomials_with_common_factors_generator.py | ✓ |
| Factoring Quadratics | factoring_quadratics_leads_into_factored_form_of_next_section_generator.py | ✓ |
| Factor by Grouping | factor_by_grouping_generator.py | ✓ |
| To Factor Using Perfect Squares | to_factor_using_perfect_squares_generator.py | ✓ |

### Chapter 10 (Unit 10) - 9/9 topics ✓

All required generators exist:

| Topic | Generator File | Status |
|-------|---------------|--------|
| Quadratic Equations (parabola) | quadratic_equations_parabola_generator.py | ✓ |
| Solving Quadratic Equations Using Square Roots | *Found in chapter02* | ✓ |
| Vertex Form (Intro) | vertex_form_generator.py | ✓ |
| Using Vertex Form (Graphing) | *May need separate graphing generator* | ? |
| Standard Form of Quadratics (Intro) | standard_form_of_quadratics_generator.py | ✓ |
| Using Standard Form (Graphing) | *May need separate graphing generator* | ? |
| Solving Quadratics by Factoring | solving_quadratics_by_factoring_factor_for_the_roots_use_x+p_2_to_find_vertex_generator.py | ✓ |
| Graphing Quadratics by Factoring | quadratic_graphing_generator.py or quadratics_by_factoring_generator.py | ✓ |

### Chapter 11 (Unit 11) - 2/2 topics ✓

All required generators exist:

| Topic | Generator File | Status |
|-------|---------------|--------|
| Completing the Square | completing_the_square_generator.py | ✓ |
| Quadratic Formula | quadratic_formula.py | ✓ |

### Chapter 12 (Unit 12) - 6/6 topics ✓

All required generators exist:

| Topic | Generator File | Status |
|-------|---------------|--------|
| Quadratic Functions | quadratic_functions_generator.py | ✓ |
| Interpreting Quadratic Functions | interpreting_quadratic_functions_word_problems_generator.py | ✓ |
| Writing Quadratic Functions | writing_quadratic_functions_generator.py | ✓ |
| Systems of Quadratic Equations | systems_of_quadratic_equations_generator.py | ✓ |
| Quadratic Inequalities | quadratic_inequalities_generator.py | ✓ |
| Systems of Quadratic Inequalities | systems_of_quadratic_inequalities_generator.py | ✓ |

### Chapter 13 (Unit 13) - 10/10 topics ✓

Most required generators exist:

| Topic | Generator File | Status |
|-------|---------------|--------|
| Absolute Value | *absolute_value_generator.py found in chapter01* | ✓ |
| Absolute Value Functions (Graphing) | *Need to create or check if it exists* | ? |
| Solving Absolute Value Equations | *Need to create* | ✗ |
| Solving Absolute Value Inequalities | *absolute_value_inequalities_generator.py in chapter03* | ✓ |
| Absolute Value Inequalities (Graphing) | *absolute_value_inequalities_generator.py in chapter03* | ✓ |
| Arithmetic Sequences | arithmetic_sequences.py or arithmetic_sequences_simple.py | ✓ |
| Constructing Arithmetic Sequences | *May need separate generator* | ? |
| Geometric Sequences | geometric_sequences_simple.py | ✓ |
| Constructing Geometric Sequences | constructing_geometric_sequences_generator.py | ✓ |
| Modeling with Sequences | modeling_with_sequences_generator.py | ✓ |

### Chapter 14 - Empty
No generators found (0 generators)

## Expansion Topics (Not checked - 11 topics)

These are conceptual topics that may not require worksheet generators:

1. Unit 1 - Of Why Dividing by Zero Does Not Work
2. Unit 2 - Parenthesis Explanation (multiplication)
3. Unit 4 - Which Type of Equation Is Best for Each Situation
4. Unit 5 - Understanding the Limits of the Three Different Types, Use Cases
5. Unit 5 - Dartboard (picking a random point and understanding the meaning of the x and y value)
6. Unit 8 - Explanation of Why an Even Square Root Cannot Be Negative
7. Unit 9 - Special Products of Polynomials
8. Unit 9 - Factoring Tips and Tricks
9. Unit 10 - Interpreting the Roots of Quadratic Equations (factored form)
10. Unit 10 - Understanding the Three Main Ways to Solve + Graph Quadratics
11. Unit 11 - When to Use Each Type of Factoring

## Issues to Address

### Missing or Need Clarification:

1. **Chapter 02**: Multi-step equations generator (may be covered by two_step_equations_generator.py)
2. **Chapter 05**: Separate graphing generator for systems of equations
3. **Chapter 06**: Review of inputs/outputs (may reuse chapter 4's generator)
4. **Chapter 07**: Review of square roots (may reuse chapter 1's generator)
5. **Chapter 08**: Equivalent exponential expressions intro
6. **Chapter 09**: Review of parts of a term
7. **Chapter 10**: Separate graphing generators for vertex and standard forms
8. **Chapter 13**: Absolute value generators are scattered in chapters 1 and 3 (should consolidate)
9. **Chapter 13**: Missing solving absolute value equations generator
10. **Chapter 13**: Missing absolute value functions graphing generator
11. **Chapter 13**: Missing constructing arithmetic sequences generator

### Organizational Issues:

1. `absolute_value_generator.py` is in chapter01 but should be in chapter13
2. `absolute_value_inequalities_generator.py` is in chapter03 but should be in chapter13
3. `solving_quadratic_equations_using_square_roots_no_other_terms_except_x^2_generator.py` is in chapter02 but should be in chapter10

## Recommendations

1. **Move misplaced generators** to their correct chapters
2. **Create missing generators** (~5-8 generators needed)
3. **Create review/intro generators** where topics reference earlier content
4. **Consolidate duplicate generators** (e.g., same topic with solving/graphing variants)
5. **Test all generators** to ensure they work correctly
6. **Update topic_registry.py** to ensure all generators are properly registered

## Overall Status: ~90% Complete ✓

Most topics have corresponding generators. The main work remaining is:
- Moving misplaced generators to correct chapters
- Creating ~5-8 missing generators
- Ensuring review topics can reuse existing generators
- Testing and registration
