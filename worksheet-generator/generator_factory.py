"""
Generator Factory - Centralized factory for creating worksheet generators.
Provides clean interface for generator instantiation and discovery.
"""

from typing import Optional, Dict, Type, Any, List
from abc import ABC, abstractmethod


class WorksheetGenerator(ABC):
    """
    Base interface for all worksheet generators.
    All generators should implement this interface.
    """

    @abstractmethod
    def generate_problems(self, num_problems: int, difficulty: str = "easy") -> List[Any]:
        """
        Generate problems for a worksheet.

        Args:
            num_problems: Number of problems to generate
            difficulty: Difficulty level (easy, medium, hard)

        Returns:
            List of problem objects (format varies by generator)
        """
        pass


class GeneratorFactory:
    """
    Factory for creating worksheet generators.
    Centralized registration and instantiation of all generators.
    """

    def __init__(self):
        """Initialize the generator factory."""
        self._generators: Dict[str, Type] = {}
        self._instances: Dict[str, Any] = {}  # Cached instances
        self._metadata: Dict[str, Dict[str, str]] = {}

    def register(
        self,
        name: str,
        generator_class: Type,
        config_key: str,
        description: str = "",
        category: str = "general"
    ) -> None:
        """
        Register a generator class.

        Args:
            name: Unique name for the generator
            generator_class: Generator class to register
            config_key: Configuration key in worksheet_config.py
            description: Human-readable description
            category: Category (e.g., "equations", "graphing", "inequalities")
        """
        self._generators[name] = generator_class
        self._metadata[name] = {
            'config_key': config_key,
            'description': description,
            'category': category,
            'class_name': generator_class.__name__
        }

    def create(self, name: str, cached: bool = True) -> Optional[Any]:
        """
        Create a generator instance.

        Args:
            name: Generator name
            cached: If True, return cached instance; if False, create new instance

        Returns:
            Generator instance or None if not found
        """
        if name not in self._generators:
            return None

        # Return cached instance if requested
        if cached and name in self._instances:
            return self._instances[name]

        # Create new instance
        generator_class = self._generators[name]
        instance = generator_class()

        # Cache if requested
        if cached:
            self._instances[name] = instance

        return instance

    def get_config_key(self, name: str) -> Optional[str]:
        """Get configuration key for a generator."""
        if name not in self._metadata:
            return None
        return self._metadata[name]['config_key']

    def get_metadata(self, name: str) -> Optional[Dict[str, str]]:
        """Get metadata for a generator."""
        return self._metadata.get(name)

    def list_generators(self, category: Optional[str] = None) -> List[str]:
        """
        List all registered generators.

        Args:
            category: Filter by category (optional)

        Returns:
            List of generator names
        """
        if category:
            return [
                name for name, meta in self._metadata.items()
                if meta['category'] == category
            ]
        return list(self._generators.keys())

    def get_categories(self) -> List[str]:
        """Get list of all categories."""
        return sorted(set(meta['category'] for meta in self._metadata.values()))

    def is_registered(self, name: str) -> bool:
        """Check if a generator is registered."""
        return name in self._generators

    def clear_cache(self):
        """Clear all cached generator instances."""
        self._instances.clear()

    def __repr__(self):
        return f"GeneratorFactory({len(self._generators)} generators registered)"


# Global factory instance
_factory = GeneratorFactory()


def get_factory() -> GeneratorFactory:
    """Get the global generator factory instance."""
    return _factory


def register_all_generators():
    """
    Register all implemented generators with the factory.
    This should be called during application initialization.
    """
    factory = get_factory()

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

    # Register equation generators
    factory.register(
        name="linear_equation",
        generator_class=LinearEquationGenerator,
        config_key="linear_equation",
        description="Linear equation solver problems",
        category="equations"
    )

    factory.register(
        name="multistep_equation",
        generator_class=MultiStepEquationGenerator,
        config_key="multistep_equations",
        description="Multi-step equation problems",
        category="equations"
    )

    factory.register(
        name="system_of_equations",
        generator_class=SystemsOfEquationsGenerator,
        config_key="system_of_equations",
        description="Systems of equations (algebraic)",
        category="equations"
    )

    # Register property generators
    factory.register(
        name="properties_add_subtract",
        generator_class=PropertiesOfEqualityGenerator,
        config_key="properties_of_equality",
        description="Properties of equality (add/subtract)",
        category="properties"
    )

    factory.register(
        name="properties_mult_div",
        generator_class=PropertiesMultDivGenerator,
        config_key="properties_mult_div",
        description="Properties of equality (multiply/divide)",
        category="properties"
    )

    # Register inequality generators
    factory.register(
        name="inequality",
        generator_class=InequalityGenerator,
        config_key="inequality",
        description="Inequality problems with number lines",
        category="inequalities"
    )

    # Register word problem generators
    factory.register(
        name="word_problems",
        generator_class=WordProblemsGenerator,
        config_key="word_problems",
        description="Linear equation word problems",
        category="word_problems"
    )

    # Register graphing generators
    factory.register(
        name="graphing_points",
        generator_class=GraphingPointsGenerator,
        config_key="graphing_points",
        description="Graphing points on coordinate plane",
        category="graphing"
    )

    factory.register(
        name="graphing_systems",
        generator_class=GraphingSystemsGenerator,
        config_key="graphing_systems",
        description="Graphing systems of equations",
        category="graphing"
    )

    factory.register(
        name="graphing_parabolas",
        generator_class=ParabolaGraphingGenerator,
        config_key="graphing_parabolas",
        description="Graphing parabolas",
        category="graphing"
    )


if __name__ == "__main__":
    # Example usage
    register_all_generators()
    factory = get_factory()

    print("=" * 70)
    print("GENERATOR FACTORY")
    print("=" * 70)
    print(f"\n{factory}\n")

    print("Registered Generators:")
    print("-" * 70)

    for category in factory.get_categories():
        print(f"\n{category.upper()}:")
        generators = factory.list_generators(category=category)
        for gen_name in generators:
            meta = factory.get_metadata(gen_name)
            print(f"  {gen_name:25s} - {meta['description']}")

    print("\n\nExample: Creating a generator")
    print("-" * 70)
    gen = factory.create("linear_equation")
    print(f"Created: {gen}")
    print(f"Config key: {factory.get_config_key('linear_equation')}")

    # Test generating problems
    print("\n\nExample: Generating problems")
    print("-" * 70)
    problems = gen.generate_problems(num_problems=3, difficulty="easy")
    print(f"Generated {len(problems)} problems")
