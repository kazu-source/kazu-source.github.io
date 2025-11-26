"""
Topic Registry System - Maps topics to worksheet generators.
Provides a centralized registry for all worksheet generators organized by unit, type, and topic.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Callable, Any
from enum import Enum


class WorksheetType(Enum):
    """Types of worksheets that can be generated."""
    INTRO = "Intro"
    GRAPHING = "Graphing"
    SOLVING = "Solving"
    EXPANSION = "Expansion"
    REVIEW = "Review"
    IDENTIFYING = "Identifying"
    INTRODUCTION = "Introduction"


@dataclass
class TopicMetadata:
    """Metadata for a worksheet topic."""
    unit: float
    type: WorksheetType
    topic: str
    generator_class: Optional[type] = None
    config_key: Optional[str] = None
    implemented: bool = False

    def __repr__(self):
        status = "✓" if self.implemented else "✗"
        return f"{status} Unit {self.unit} | {self.type.value} | {self.topic}"


class TopicRegistry:
    """
    Central registry for all worksheet topics and their generators.
    Maps topics from the Excel configuration to actual generator implementations.
    """

    def __init__(self):
        """Initialize the topic registry."""
        self._topics: Dict[str, TopicMetadata] = {}
        self._generator_cache: Dict[str, Any] = {}

    def register_topic(
        self,
        unit: float,
        type: str,
        topic: str,
        generator_class: Optional[type] = None,
        config_key: Optional[str] = None
    ) -> None:
        """
        Register a topic with optional generator implementation.

        Args:
            unit: Unit number (e.g., 1.0, 2.0, 11.0)
            type: Worksheet type (Intro, Graphing, etc.)
            topic: Topic name
            generator_class: Generator class (if implemented)
            config_key: Configuration key in worksheet_config.py
        """
        # Parse type to enum
        try:
            worksheet_type = WorksheetType(type)
        except ValueError:
            worksheet_type = WorksheetType.INTRO  # Default fallback

        # Create unique key for topic
        topic_key = self._make_key(unit, type, topic)

        # Register the topic
        self._topics[topic_key] = TopicMetadata(
            unit=unit,
            type=worksheet_type,
            topic=topic,
            generator_class=generator_class,
            config_key=config_key,
            implemented=(generator_class is not None)
        )

    def get_topic(self, unit: float, type: str, topic: str) -> Optional[TopicMetadata]:
        """Get topic metadata by unit, type, and topic name."""
        key = self._make_key(unit, type, topic)
        return self._topics.get(key)

    def get_generator(self, unit: float, type: str, topic: str) -> Optional[Any]:
        """
        Get generator instance for a topic.
        Uses cached instances to avoid recreating generators.

        Args:
            unit: Unit number
            type: Worksheet type
            topic: Topic name

        Returns:
            Generator instance or None if not implemented
        """
        key = self._make_key(unit, type, topic)

        # Check cache first
        if key in self._generator_cache:
            return self._generator_cache[key]

        # Get topic metadata
        topic_meta = self._topics.get(key)
        if not topic_meta or not topic_meta.generator_class:
            return None

        # Instantiate and cache
        generator = topic_meta.generator_class()
        self._generator_cache[key] = generator
        return generator

    def get_all_topics(self, unit_filter: Optional[float] = None,
                       type_filter: Optional[List[str]] = None) -> List[TopicMetadata]:
        """
        Get all topics, optionally filtered by unit and/or type.

        Args:
            unit_filter: Filter by specific unit number
            type_filter: Filter by worksheet types (e.g., ["Intro", "Graphing"])

        Returns:
            List of matching topic metadata
        """
        topics = list(self._topics.values())

        # Apply unit filter
        if unit_filter is not None:
            topics = [t for t in topics if t.unit == unit_filter]

        # Apply type filter
        if type_filter:
            type_enums = [WorksheetType(t) for t in type_filter if t]
            topics = [t for t in topics if t.type in type_enums]

        return sorted(topics, key=lambda t: (t.unit, t.type.value, t.topic))

    def get_implemented_topics(self, type_filter: Optional[List[str]] = None) -> List[TopicMetadata]:
        """
        Get all topics that have generator implementations.

        Args:
            type_filter: Filter by worksheet types

        Returns:
            List of implemented topic metadata
        """
        all_topics = self.get_all_topics(type_filter=type_filter)
        return [t for t in all_topics if t.implemented]

    def get_unimplemented_topics(self, type_filter: Optional[List[str]] = None) -> List[TopicMetadata]:
        """
        Get all topics that don't have generator implementations yet.

        Args:
            type_filter: Filter by worksheet types

        Returns:
            List of unimplemented topic metadata
        """
        all_topics = self.get_all_topics(type_filter=type_filter)
        return [t for t in all_topics if not t.implemented]

    def get_units(self) -> List[float]:
        """Get list of all unique units."""
        return sorted(set(t.unit for t in self._topics.values()))

    def get_types(self) -> List[str]:
        """Get list of all unique worksheet types."""
        return sorted(set(t.type.value for t in self._topics.values()))

    def get_coverage_stats(self) -> Dict[str, Any]:
        """
        Get statistics about topic coverage.

        Returns:
            Dictionary with coverage statistics
        """
        all_topics = list(self._topics.values())
        implemented = [t for t in all_topics if t.implemented]

        # By type
        type_stats = {}
        for wtype in WorksheetType:
            type_topics = [t for t in all_topics if t.type == wtype]
            type_implemented = [t for t in type_topics if t.implemented]
            if type_topics:
                type_stats[wtype.value] = {
                    'total': len(type_topics),
                    'implemented': len(type_implemented),
                    'percentage': len(type_implemented) / len(type_topics) * 100
                }

        return {
            'total_topics': len(all_topics),
            'implemented': len(implemented),
            'unimplemented': len(all_topics) - len(implemented),
            'percentage': len(implemented) / len(all_topics) * 100 if all_topics else 0,
            'by_type': type_stats
        }

    def _make_key(self, unit: float, type: str, topic: str) -> str:
        """Create unique key for a topic."""
        return f"{unit}|{type}|{topic}"

    def __len__(self) -> int:
        """Return number of registered topics."""
        return len(self._topics)

    def __repr__(self):
        stats = self.get_coverage_stats()
        return f"TopicRegistry({stats['implemented']}/{stats['total_topics']} topics implemented)"


# Global registry instance
_registry = TopicRegistry()


def get_registry() -> TopicRegistry:
    """Get the global topic registry instance."""
    return _registry


def register_all_generators():
    """
    Register all implemented generators with the topic registry.
    This function should be called during application initialization.
    """
    registry = get_registry()

    # Import generators
    from equation_generator import LinearEquationGenerator
    from systems_generator import SystemsOfEquationsGenerator
    from inequalities_generator import InequalityGenerator
    from properties_generator import PropertiesOfEqualityGenerator
    from properties_mult_div_generator import PropertiesMultDivGenerator
    from word_problems_generator import WordProblemsGenerator
    from multistep_generator import MultiStepEquationGenerator
    from generators.chapter04.graphing_points import GraphingPointsGenerator
    from generators.chapter05.graphing_systems import GraphingSystemsGenerator
    from generators.chapter11.graphing_parabolas import ParabolaGraphingGenerator
    from generators.chapter01.variables_generator import VariablesGenerator
    from generators.chapter01.exponents_generator import ExponentsGenerator
    from generators.chapter01.evaluating_expressions_generator import EvaluatingExpressionsGenerator
    from generators.chapter01.substitution_generator import SubstitutionGenerator
    from generators.chapter01.combining_like_terms_generator import CombiningLikeTermsGenerator
    from generators.chapter01.absolute_value_generator import AbsoluteValueGenerator
    from generators.chapter01.square_roots_generator import SquareRootsGenerator
    from generators.chapter02.equations_intro_generator import EquationsIntroGenerator
    from generators.chapter02.inputs_outputs_generator import InputsOutputsGenerator
    from generators.chapter02.solutions_generator import SolutionsGenerator
    from generators.chapter02.variables_both_sides_generator import VariablesBothSidesGenerator
    from generators.chapter03.compound_inequalities_generator import CompoundInequalityGenerator
    from generators.chapter04.graphing_lines import GraphingLinesGenerator
    from generators.chapter04.graphing_slope_intercept import SlopeInterceptGenerator
    from generators.chapter04.graphing_point_slope import PointSlopeGenerator
    from generators.chapter04.graphing_standard_form import StandardFormGenerator

    # Chapter 1: Basics
    registry.register_topic(1.0, "Intro", "Variables",
                           VariablesGenerator, "variables")
    registry.register_topic(1.0, "Intro", "Exponents",
                           ExponentsGenerator, "exponents")
    registry.register_topic(1.0, "Intro", "Evaluating an Expression",
                           EvaluatingExpressionsGenerator, "evaluating_expressions")
    registry.register_topic(1.0, "Intro", "Substitution of Variables",
                           SubstitutionGenerator, "substitution")
    registry.register_topic(1.0, "Intro", "Combining Like Terms",
                           CombiningLikeTermsGenerator, "combining_like_terms")
    registry.register_topic(1.0, "Intro", "Absolute Value",
                           AbsoluteValueGenerator, "absolute_value")
    registry.register_topic(1.0, "Intro", "Square Roots",
                           SquareRootsGenerator, "square_roots")

    # Chapter 2: Equations
    registry.register_topic(2.0, "Intro", "Equations",
                           EquationsIntroGenerator, "equations_intro")
    registry.register_topic(2.0, "Intro", "Inputs and Outputs",
                           InputsOutputsGenerator, "inputs_outputs")
    registry.register_topic(2.0, "Intro", "What Are Solutions?",
                           SolutionsGenerator, "solutions")
    registry.register_topic(2.0, "Intro", "Solving Equations with Variables on Both Sides",
                           VariablesBothSidesGenerator, "variables_both_sides")
    registry.register_topic(2.0, "Intro", "Property of Equality (add/subtract)",
                           PropertiesOfEqualityGenerator, "properties_of_equality")
    registry.register_topic(2.0, "Intro", "Property of Equality (mult/div)",
                           PropertiesMultDivGenerator, "properties_mult_div")
    registry.register_topic(2.0, "Intro", "Solving Multi-Step Equations",
                           MultiStepEquationGenerator, "multistep_equations")
    registry.register_topic(2.0, "Intro", "Linear Equations",
                           LinearEquationGenerator, "linear_equation")
    registry.register_topic(2.0, "Intro", "Linear Equation Word Problems",
                           WordProblemsGenerator, "word_problems")

    # Chapter 3: Inequalities
    registry.register_topic(3.0, "Graphing", "One-Step Inequalities",
                           InequalityGenerator, "inequality")
    registry.register_topic(3.0, "Graphing", "Compound Inequalities - Mixed",
                           CompoundInequalityGenerator, "compound_inequality")
    registry.register_topic(3.0, "Graphing", "Compound Inequalities - AND",
                           CompoundInequalityGenerator, "compound_inequality_and")
    registry.register_topic(3.0, "Graphing", "Compound Inequalities - OR",
                           CompoundInequalityGenerator, "compound_inequality_or")

    # Chapter 4: Linear Equations - Two Variables
    registry.register_topic(4.0, "Graphing", "Points on a Coordinate Plane",
                           GraphingPointsGenerator, "graphing_points")
    registry.register_topic(4.0, "Graphing", "Line on a Coordinate Plane",
                           GraphingLinesGenerator, "graphing_lines")
    registry.register_topic(4.0, "Graphing", "Slope-Intercept Form",
                           SlopeInterceptGenerator, "slope_intercept")
    registry.register_topic(4.0, "Graphing", "Point-Slope Form",
                           PointSlopeGenerator, "point_slope")
    registry.register_topic(4.0, "Graphing", "Standard Form",
                           StandardFormGenerator, "standard_form")

    # Chapter 5: Systems of Equations
    registry.register_topic(5.0, "Intro", "Systems of Equations",
                           SystemsOfEquationsGenerator, "system_of_equations")
    registry.register_topic(5.0, "Graphing", "Systems of Equations",
                           GraphingSystemsGenerator, "graphing_systems")

    # Chapter 11: Quadratic Functions
    registry.register_topic(11.0, "Graphing", "Using Vertex Form",
                           ParabolaGraphingGenerator, "graphing_parabolas")

    # Add new Unit 11-13 generators
    try:
        from generators.chapter11.completing_square_simple import CompletingSquareSimpleGenerator
        from generators.chapter11.quadratic_formula_simple import QuadraticFormulaSimpleGenerator
        from generators.chapter12.quadratic_functions_simple import QuadraticFunctionsSimpleGenerator
        from generators.chapter13.arithmetic_sequences_simple import ArithmeticSequencesSimpleGenerator
        from generators.chapter13.geometric_sequences_simple import GeometricSequencesSimpleGenerator

        # Unit 11: More Quadratics
        registry.register_topic(11.0, "Intro", "Completing the Square",
                               CompletingSquareSimpleGenerator, "completing_the_square")
        registry.register_topic(11.0, "Intro", "Quadratic Formula",
                               QuadraticFormulaSimpleGenerator, "quadratic_formula")

        # Unit 12: Quadratic Functions
        registry.register_topic(12.0, "Intro", "Quadratic Functions",
                               QuadraticFunctionsSimpleGenerator, "quadratic_functions")

        # Unit 13: Sequences and More
        registry.register_topic(13.0, "Intro", "Arithmetic Sequences",
                               ArithmeticSequencesSimpleGenerator, "arithmetic_sequences")
        registry.register_topic(13.0, "Intro", "Geometric Sequences",
                               GeometricSequencesSimpleGenerator, "geometric_sequences")
    except ImportError as e:
        print(f"Warning: Could not import new generators: {e}")


if __name__ == "__main__":
    # Example usage
    register_all_generators()
    registry = get_registry()

    print("=" * 60)
    print("TOPIC REGISTRY")
    print("=" * 60)
    print(f"\n{registry}\n")

    print("Implemented Topics:")
    print("-" * 60)
    for topic in registry.get_implemented_topics():
        print(topic)

    print("\n\nCoverage Statistics:")
    print("-" * 60)
    stats = registry.get_coverage_stats()
    print(f"Overall: {stats['implemented']}/{stats['total_topics']} ({stats['percentage']:.1f}%)")
    print("\nBy Type:")
    for type_name, type_stats in stats['by_type'].items():
        print(f"  {type_name}: {type_stats['implemented']}/{type_stats['total']} ({type_stats['percentage']:.1f}%)")
