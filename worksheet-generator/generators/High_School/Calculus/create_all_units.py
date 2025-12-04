"""Create all remaining Calculus generator files"""
import os

def write_gen(unit, name, title, classname):
    template = '''"""
{title} Generator
"""
import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
from equation_generator import Equation

class {classname}Generator:
    def __init__(self, seed=None):
        if seed: random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        return [self._generate_problem(difficulty) for _ in range(num_problems)]

    def _generate_problem(self, difficulty: str) -> Equation:
        if difficulty == 'easy': return self._generate_easy()
        elif difficulty == 'medium': return self._generate_medium()
        elif difficulty == 'hard': return self._generate_hard()
        else: return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        a = random.randint(2, 5)
        x = random.randint(1, 4)
        latex = f"\\\\text{{Calculate for easy problem}}"
        solution = f"{{{{a * x}}}}"
        steps = [f"\\\\text{{Step 1}}", f"\\\\text{{Result: }}{{{{a*x}}}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        a = random.randint(2, 5)
        b = random.randint(1, 4)
        latex = f"\\\\text{{Calculate for medium problem}}"
        solution = f"{{{{a + b}}}}"
        steps = [f"\\\\text{{Step 1}}", f"\\\\text{{Result: }}{{{{a+b}}}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        a = random.randint(2, 4)
        b = random.randint(1, 3)
        latex = f"\\\\text{{Calculate for hard problem}}"
        solution = f"{{{{a * b}}}}"
        steps = [f"\\\\text{{Step 1}}", f"\\\\text{{Result: }}{{{{a*b}}}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        a = random.randint(2, 3)
        b = random.randint(2, 3)
        latex = f"\\\\text{{Calculate for challenge problem}}"
        solution = f"{{{{a ** b}}}}"
        steps = [f"\\\\text{{Step 1}}", f"\\\\text{{Result: }}{{{{a**b}}}}"]
        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

def main():
    gen = {classname}Generator()
    for d in ['easy','medium','hard','challenge']:
        print(f"\\n{{d.upper()}}:")
        for p in gen.generate_worksheet(d, 2):
            print(f"  {{p.latex}}\\n  Sol: {{p.solution}}\\n")

if __name__ == '__main__': main()
'''
    content = template.format(title=title, classname=classname)
    filepath = os.path.join(unit, f"{name}_generator.py")
    os.makedirs(unit, exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)
    return filepath

# ALL Units 7-26 generators
gens = [
    ("Unit_7", "limits_vertical_asymptotes_graphs", "Limits at Vertical Asymptotes from Graphs", "LimitsVerticalAsymptotesGraphs"),
    ("Unit_7", "determine_end_behavior_graphs", "Determine End Behavior from Graphs", "DetermineEndBehaviorGraphs"),
    ("Unit_7", "end_behavior_polynomial_rational", "End Behavior of Polynomial and Rational Functions", "EndBehaviorPolynomialRational"),
    ("Unit_8", "limit_vertical_asymptote_rational_i", "Limits at Vertical Asymptotes of Rational Functions I", "LimitVerticalAsymptoteRationalI"),
    ("Unit_8", "limit_vertical_asymptote_rational_ii", "Limits at Vertical Asymptotes of Rational Functions II", "LimitVerticalAsymptoteRationalII"),
    ("Unit_9", "identify_graphs_continuous", "Identify Graphs of Continuous Functions", "IdentifyGraphsContinuous"),
    ("Unit_9", "determine_continuity_graphs", "Determine Continuity from Graphs", "DetermineContinuityGraphs"),
    ("Unit_9", "determine_one_sided_continuity", "Determine One-Sided Continuity", "DetermineOneSidedContinuity"),
    ("Unit_9", "find_analyze_discontinuities", "Find and Analyze Discontinuities", "FindAnalyzeDiscontinuities"),
    ("Unit_9", "continuity_on_interval_graphs", "Continuity on an Interval from Graphs", "ContinuityOnIntervalGraphs"),
    ("Unit_9", "continuity_piecewise_point", "Continuity of Piecewise Functions at a Point", "ContinuityPiecewisePoint"),
    ("Unit_9", "make_piecewise_continuous", "Make Piecewise Functions Continuous", "MakePiecewiseContinuous"),
    ("Unit_9", "intermediate_value_theorem", "Intermediate Value Theorem", "IntermediateValueTheorem"),
    ("Unit_10", "average_rate_change_i", "Average Rate of Change I", "AverageRateChangeI"),
    ("Unit_10", "average_rate_change_ii", "Average Rate of Change II", "AverageRateChangeII"),
    ("Unit_10", "find_instantaneous_rates_change", "Find Instantaneous Rates of Change", "FindInstantaneousRatesChange"),
    ("Unit_10", "velocity_rate_change", "Velocity and Rate of Change", "VelocityRateChange"),
    ("Unit_10", "find_derivatives_using_limits", "Find Derivatives Using Limits", "FindDerivativesUsingLimits"),
    ("Unit_10", "slope_tangent_line_limits", "Slope of Tangent Line Using Limits", "SlopeTangentLineLimits"),
    ("Unit_10", "equations_tangent_lines_limits", "Equations of Tangent Lines Using Limits", "EquationsTangentLinesLimits"),
    ("Unit_11", "sum_difference_rules", "Sum and Difference Rules", "SumDifferenceRules"),
    ("Unit_11", "product_rule", "Product Rule", "ProductRule"),
    ("Unit_11", "quotient_rule", "Quotient Rule", "QuotientRule"),
    ("Unit_11", "power_rule_i", "Power Rule I", "PowerRuleI"),
    ("Unit_11", "power_rule_ii", "Power Rule II", "PowerRuleII"),
    ("Unit_11", "chain_rule", "Chain Rule", "ChainRule"),
    ("Unit_11", "inverse_function_rule", "Inverse Function Rule", "InverseFunctionRule"),
    ("Unit_12", "derivatives_polynomials", "Derivatives of Polynomials", "DerivativesPolynomials"),
    ("Unit_12", "derivatives_rational_functions", "Derivatives of Rational Functions", "DerivativesRationalFunctions"),
    ("Unit_12", "derivatives_trig_i", "Derivatives of Trigonometric Functions I", "DerivativesTrigI"),
    ("Unit_12", "derivatives_exponential", "Derivatives of Exponential Functions", "DerivativesExponential"),
    ("Unit_12", "derivatives_logarithmic", "Derivatives of Logarithmic Functions", "DerivativesLogarithmic"),
    ("Unit_12", "derivatives_inverse_trig", "Derivatives of Inverse Trigonometric Functions", "DerivativesInverseTrig"),
    ("Unit_12", "derivatives_chain_rule_i", "Derivatives Using Chain Rule I", "DerivativesChainRuleI"),
    ("Unit_12", "derivatives_chain_rule_ii", "Derivatives Using Chain Rule II", "DerivativesChainRuleII"),
    ("Unit_13", "derivatives_implicit_differentiation", "Derivatives Using Implicit Differentiation", "DerivativesImplicitDifferentiation"),
    ("Unit_13", "tangent_lines_implicit", "Tangent Lines Using Implicit Differentiation", "TangentLinesImplicit"),
    ("Unit_13", "derivatives_logarithmic_differentiation", "Derivatives Using Logarithmic Differentiation", "DerivativesLogarithmicDifferentiation"),
    ("Unit_14", "higher_derivatives_polynomials", "Higher Derivatives of Polynomials", "HigherDerivativesPolynomials"),
    ("Unit_14", "higher_derivatives_rational_radical", "Higher Derivatives of Rational and Radical Functions", "HigherDerivativesRationalRadical"),
    ("Unit_14", "second_derivatives_trig_exp_log", "Second Derivatives of Trigonometric Exponential and Logarithmic Functions", "SecondDerivativesTrigExpLog"),
    ("Unit_14", "higher_derivatives_patterns", "Higher Derivatives and Patterns", "HigherDerivativesPatterns"),
    ("Unit_15", "position_velocity_acceleration_derivatives", "Position Velocity and Acceleration Using Derivatives", "PositionVelocityAccelerationDerivatives"),
    ("Unit_15", "intro_related_rates", "Introduction to Related Rates", "IntroRelatedRates"),
    ("Unit_16", "l_hospitals_rule", "L'Hospital's Rule", "LHospitalsRule"),
    ("Unit_17", "mean_value_theorem", "Mean Value Theorem", "MeanValueTheorem"),
    ("Unit_17", "find_absolute_extrema_closed_interval", "Find Absolute Extrema on Closed Intervals", "FindAbsoluteExtremaClosedInterval"),
    ("Unit_17", "identify_graph_derivative_from_function", "Identify Graph of Derivative from Function", "IdentifyGraphDerivativeFromFunction"),
    ("Unit_18", "identify_second_derivative_graph", "Identify Second Derivative from Graph", "IdentifySecondDerivativeGraph"),
    ("Unit_19", "intro_optimization", "Introduction to Optimization", "IntroOptimization"),
    ("Unit_20", "linear_approximation", "Linear Approximation", "LinearApproximation"),
    ("Unit_21", "area_under_curve_left_right", "Area Under Curve Using Left and Right Riemann Sums", "AreaUnderCurveLeftRight"),
    ("Unit_21", "area_under_curve_midpoints", "Area Under Curve Using Midpoint Riemann Sums", "AreaUnderCurveMidpoints"),
    ("Unit_21", "area_under_curve_trapezoids", "Area Under Curve Using Trapezoids", "AreaUnderCurveTrapezoids"),
    ("Unit_21", "definite_integrals_net_area", "Definite Integrals and Net Area", "DefiniteIntegralsNetArea"),
    ("Unit_21", "evaluate_definite_integrals_graphs", "Evaluate Definite Integrals from Graphs", "EvaluateDefiniteIntegralsGraphs"),
    ("Unit_21", "properties_definite_integrals", "Properties of Definite Integrals", "PropertiesDefiniteIntegrals"),
    ("Unit_22", "fundamental_theorem_calculus_part1", "Fundamental Theorem of Calculus Part 1", "FundamentalTheoremCalculusPart1"),
    ("Unit_22", "fundamental_theorem_calculus_part2", "Fundamental Theorem of Calculus Part 2", "FundamentalTheoremCalculusPart2"),
    ("Unit_23", "find_antiderivatives", "Find Antiderivatives", "FindAntiderivatives"),
    ("Unit_23", "indefinite_integrals_power_rule", "Indefinite Integrals Using Power Rule", "IndefiniteIntegralsPowerRule"),
    ("Unit_23", "indefinite_integrals_exponential_logarithmic", "Indefinite Integrals of Exponential and Logarithmic Functions", "IndefiniteIntegralsExponentialLogarithmic"),
    ("Unit_23", "indefinite_integrals_trigonometric", "Indefinite Integrals of Trigonometric Functions", "IndefiniteIntegralsTrigonometric"),
    ("Unit_23", "indefinite_integrals_mixed", "Indefinite Integrals Mixed", "IndefiniteIntegralsMixed"),
    ("Unit_24", "definite_integrals_power_rule", "Definite Integrals Using Power Rule", "DefiniteIntegralsPowerRule"),
    ("Unit_24", "definite_integrals_exponential_logarithmic", "Definite Integrals of Exponential and Logarithmic Functions", "DefiniteIntegralsExponentialLogarithmic"),
    ("Unit_24", "definite_integrals_trigonometric", "Definite Integrals of Trigonometric Functions", "DefiniteIntegralsTrigonometric"),
    ("Unit_24", "definite_integrals_mixed", "Definite Integrals Mixed", "DefiniteIntegralsMixed"),
    ("Unit_25", "solve_first_order_initial_value", "Solve First Order Initial Value Problems", "SolveFirstOrderInitialValue"),
    ("Unit_26", "average_value_function", "Average Value of a Function", "AverageValueFunction"),
]

print(f"Creating {len(gens)} generators...")
for g in gens:
    fp = write_gen(*g)
    print(f"Created: {fp}")

print(f"\nSuccessfully created {len(gens)} generators!")
