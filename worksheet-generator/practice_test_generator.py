"""
Practice Test Generator - Create mixed-problem worksheets
Combines problems from multiple topics at various difficulty levels
Ideal for unit reviews, cumulative assessments, and comprehensive practice
"""

import sys
import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple
import random

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from topic_registry import get_registry, register_all_generators
from pdf_generator import PDFWorksheetGenerator
from worksheet_config import get_config


class PracticeTestGenerator:
    """Generates mixed-problem practice tests from multiple topics."""

    def __init__(self):
        """Initialize the practice test generator."""
        register_all_generators()
        self.registry = get_registry()
        self.pdf_gen = PDFWorksheetGenerator()

    def generate_unit_review(
        self,
        unit: float,
        num_problems: int = 20,
        difficulty_mix: str = 'balanced',
        output_path: str = None
    ) -> str:
        """
        Generate a practice test covering all topics in a unit.

        Args:
            unit: Unit number (e.g., 1.0, 2.0, 5.0)
            num_problems: Total number of problems
            difficulty_mix: 'easy', 'medium', 'hard', 'challenge', 'balanced', or 'progressive'
            output_path: Custom output path (optional)

        Returns:
            Path to generated PDF
        """
        # Get all topics for this unit
        unit_topics = [t for t in self.registry.get_implemented_topics() if t.unit == unit]

        if not unit_topics:
            raise ValueError(f"No implemented topics found for Unit {unit}")

        # Calculate problems per topic
        problems_per_topic = max(1, num_problems // len(unit_topics))

        # Generate problems from each topic
        all_problems = []
        for topic_meta in unit_topics:
            difficulty = self._select_difficulty(difficulty_mix, len(all_problems), num_problems)

            generator = self.registry.get_generator(topic_meta.unit, topic_meta.type.value, topic_meta.topic)
            if generator:
                problems = generator.generate_worksheet(difficulty, problems_per_topic)
                all_problems.extend(problems[:problems_per_topic])

        # Shuffle problems for mixed practice
        random.shuffle(all_problems)

        # Trim to exact number
        all_problems = all_problems[:num_problems]

        # Generate output path
        if not output_path:
            date_str = datetime.now().strftime("%Y%m%d")
            output_dir = Path("output") / f"Unit{int(unit)}" / "Practice_Tests"
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / f"Unit{int(unit)}_Review_{difficulty_mix}_{date_str}.pdf"

        # Generate PDF
        title = f"Algebra 1 - Unit {int(unit)} Review ({difficulty_mix.capitalize()})"
        self.pdf_gen.generate_worksheet(all_problems, str(output_path), title=title)

        return str(output_path)

    def generate_cumulative_test(
        self,
        units: List[float],
        num_problems: int = 30,
        difficulty_mix: str = 'balanced',
        output_path: str = None
    ) -> str:
        """
        Generate a cumulative practice test covering multiple units.

        Args:
            units: List of unit numbers (e.g., [1.0, 2.0, 3.0])
            num_problems: Total number of problems
            difficulty_mix: Difficulty distribution strategy
            output_path: Custom output path (optional)

        Returns:
            Path to generated PDF
        """
        # Get all topics for these units
        all_topics = []
        for unit in units:
            unit_topics = [t for t in self.registry.get_implemented_topics() if t.unit == unit]
            all_topics.extend(unit_topics)

        if not all_topics:
            raise ValueError(f"No implemented topics found for units {units}")

        # Calculate problems per topic
        problems_per_topic = max(1, num_problems // len(all_topics))

        # Generate problems from each topic
        all_problems = []
        for topic_meta in all_topics:
            difficulty = self._select_difficulty(difficulty_mix, len(all_problems), num_problems)

            generator = self.registry.get_generator(topic_meta.unit, topic_meta.type.value, topic_meta.topic)
            if generator:
                problems = generator.generate_worksheet(difficulty, problems_per_topic)
                all_problems.extend(problems[:problems_per_topic])

        # Shuffle problems
        random.shuffle(all_problems)

        # Trim to exact number
        all_problems = all_problems[:num_problems]

        # Generate output path
        if not output_path:
            date_str = datetime.now().strftime("%Y%m%d")
            units_str = "_".join([str(int(u)) for u in units])
            output_dir = Path("output") / "Practice_Tests"
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / f"Units_{units_str}_Cumulative_{difficulty_mix}_{date_str}.pdf"

        # Generate PDF
        units_display = ", ".join([str(int(u)) for u in units])
        title = f"Algebra 1 - Units {units_display} Cumulative Review ({difficulty_mix.capitalize()})"
        self.pdf_gen.generate_worksheet(all_problems, str(output_path), title=title)

        return str(output_path)

    def generate_custom_test(
        self,
        topic_specs: List[Tuple[float, str, str, str, int]],
        output_path: str = None,
        test_name: str = "Custom Practice Test"
    ) -> str:
        """
        Generate a custom practice test with specific topics and difficulties.

        Args:
            topic_specs: List of (unit, type, topic, difficulty, num_problems) tuples
            output_path: Custom output path (optional)
            test_name: Name for the test

        Returns:
            Path to generated PDF

        Example:
            topic_specs = [
                (2.0, "Intro", "Equations", "medium", 5),
                (2.0, "Intro", "Properties of Equality", "hard", 5),
                (5.0, "Intro", "Systems of Equations", "challenge", 3),
            ]
        """
        all_problems = []

        for unit, type_, topic, difficulty, num in topic_specs:
            generator = self.registry.get_generator(unit, type_, topic)
            if generator:
                problems = generator.generate_worksheet(difficulty, num)
                all_problems.extend(problems)
            else:
                print(f"Warning: Generator not found for {topic}")

        # Shuffle for mixed practice
        random.shuffle(all_problems)

        # Generate output path
        if not output_path:
            date_str = datetime.now().strftime("%Y%m%d")
            output_dir = Path("output") / "Practice_Tests"
            output_dir.mkdir(parents=True, exist_ok=True)
            test_name_clean = test_name.replace(" ", "_")
            output_path = output_dir / f"{test_name_clean}_{date_str}.pdf"

        # Generate PDF
        title = f"Algebra 1 - {test_name}"
        self.pdf_gen.generate_worksheet(all_problems, str(output_path), title=title)

        return str(output_path)

    def generate_topic_spiral(
        self,
        topic: Tuple[float, str, str],
        num_problems_per_level: int = 5,
        output_path: str = None
    ) -> str:
        """
        Generate a spiral review worksheet for a single topic across all difficulty levels.

        Args:
            topic: (unit, type, topic_name) tuple
            num_problems_per_level: Problems per difficulty level
            output_path: Custom output path (optional)

        Returns:
            Path to generated PDF
        """
        unit, type_, topic_name = topic
        generator = self.registry.get_generator(unit, type_, topic_name)

        if not generator:
            raise ValueError(f"Generator not found for {topic_name}")

        all_problems = []
        for difficulty in ['easy', 'medium', 'hard', 'challenge']:
            problems = generator.generate_worksheet(difficulty, num_problems_per_level)
            all_problems.extend(problems)

        # Don't shuffle - keep progressive difficulty

        # Generate output path
        if not output_path:
            date_str = datetime.now().strftime("%Y%m%d")
            topic_clean = topic_name.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "").replace("?", "")
            output_dir = Path("output") / f"Unit{int(unit)}" / "Practice_Tests"
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / f"{topic_clean}_Spiral_{date_str}.pdf"

        # Generate PDF
        title = f"Algebra 1 - {topic_name} Spiral Review"
        self.pdf_gen.generate_worksheet(all_problems, str(output_path), title=title)

        return str(output_path)

    def _select_difficulty(self, difficulty_mix: str, current_count: int, total: int) -> str:
        """
        Select difficulty level based on mixing strategy.

        Args:
            difficulty_mix: Strategy name
            current_count: Number of problems generated so far
            total: Total problems to generate

        Returns:
            Difficulty level string
        """
        if difficulty_mix == 'easy':
            return 'easy'
        elif difficulty_mix == 'medium':
            return 'medium'
        elif difficulty_mix == 'hard':
            return 'hard'
        elif difficulty_mix == 'challenge':
            return 'challenge'
        elif difficulty_mix == 'balanced':
            # Equal mix of all four levels
            return random.choice(['easy', 'medium', 'hard', 'challenge'])
        elif difficulty_mix == 'progressive':
            # Start easy, end challenge
            progress = current_count / total
            if progress < 0.25:
                return 'easy'
            elif progress < 0.50:
                return 'medium'
            elif progress < 0.75:
                return 'hard'
            else:
                return 'challenge'
        else:
            return 'medium'


def main():
    """Example usage of the practice test generator."""
    gen = PracticeTestGenerator()

    print("=" * 80)
    print("PRACTICE TEST GENERATOR")
    print("=" * 80)
    print()

    # Example 1: Unit 2 Review
    print("Generating Unit 2 Review (20 problems, balanced difficulty)...")
    path = gen.generate_unit_review(unit=2.0, num_problems=20, difficulty_mix='balanced')
    print(f"  Created: {path}")
    print()

    # Example 2: Cumulative Test (Units 1-2)
    print("Generating Units 1-2 Cumulative Test (30 problems, progressive difficulty)...")
    path = gen.generate_cumulative_test(units=[1.0, 2.0], num_problems=30, difficulty_mix='progressive')
    print(f"  Created: {path}")
    print()

    # Example 3: Custom Test
    print("Generating Custom Test (equations focus)...")
    custom_specs = [
        (2.0, "Intro", "Equations", "medium", 5),
        (2.0, "Intro", "Property of Equality (add/subtract)", "hard", 5),
        (2.0, "Intro", "Solving Multi-Step Equations", "challenge", 3),
    ]
    path = gen.generate_custom_test(custom_specs, test_name="Equations Mastery Test")
    print(f"  Created: {path}")
    print()

    # Example 4: Topic Spiral
    print("Generating Equations Spiral Review (all difficulty levels)...")
    path = gen.generate_topic_spiral((2.0, "Intro", "Equations"), num_problems_per_level=4)
    print(f"  Created: {path}")
    print()

    print("=" * 80)
    print("All practice tests generated successfully!")
    print("=" * 80)


if __name__ == "__main__":
    main()
