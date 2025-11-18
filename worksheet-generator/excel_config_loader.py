"""
Excel Configuration Loader - Loads worksheet topics from Excel files.
Supports multiple grade levels and courses with extensible structure.
"""

import openpyxl
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Optional, Set
from topic_registry import TopicRegistry, WorksheetType


@dataclass
class TopicDefinition:
    """Definition of a topic from Excel configuration."""
    course: str  # e.g., "Algebra 1", "Geometry", "Grade 6"
    unit: float
    type: str
    topic: str

    def __repr__(self):
        return f"{self.course} - Unit {self.unit} | {self.type} | {self.topic}"


class ExcelConfigLoader:
    """
    Loads worksheet topic configurations from Excel files.
    Designed to handle multiple courses and grade levels.
    """

    def __init__(self, excel_path: str):
        """
        Initialize the Excel configuration loader.

        Args:
            excel_path: Path to Excel file containing topic definitions
        """
        self.excel_path = Path(excel_path)
        self.topics: List[TopicDefinition] = []
        self.course_name: str = ""

    def load(self) -> List[TopicDefinition]:
        """
        Load topic definitions from Excel file.

        Returns:
            List of TopicDefinition objects

        Raises:
            FileNotFoundError: If Excel file doesn't exist
            ValueError: If Excel format is invalid
        """
        if not self.excel_path.exists():
            raise FileNotFoundError(f"Excel file not found: {self.excel_path}")

        # Infer course name from filename
        self.course_name = self._infer_course_name()

        # Load workbook
        wb = openpyxl.load_workbook(self.excel_path)
        ws = wb.active

        # Parse topics
        self.topics = []
        header_row = True

        for row in ws.iter_rows(values_only=True):
            # Skip header row
            if header_row:
                header_row = False
                continue

            # Extract values (Unit, Type, Topic, ...)
            unit_val = row[0] if len(row) > 0 else None
            type_val = row[1] if len(row) > 1 else None
            topic_val = row[2] if len(row) > 2 else None

            # Skip empty rows
            if not unit_val or not type_val or not topic_val:
                continue

            # Handle unit number (could be float or int)
            try:
                unit = float(unit_val)
            except (ValueError, TypeError):
                continue  # Skip rows with invalid unit numbers

            # Create topic definition
            topic_def = TopicDefinition(
                course=self.course_name,
                unit=unit,
                type=str(type_val).strip(),
                topic=str(topic_val).strip()
            )

            self.topics.append(topic_def)

        wb.close()
        return self.topics

    def get_topics_by_type(self, types: List[str]) -> List[TopicDefinition]:
        """
        Filter topics by worksheet type(s).

        Args:
            types: List of worksheet types (e.g., ["Intro", "Graphing"])

        Returns:
            Filtered list of topics
        """
        if not self.topics:
            self.load()

        return [t for t in self.topics if t.type in types]

    def get_topics_by_unit(self, unit: float) -> List[TopicDefinition]:
        """
        Filter topics by unit number.

        Args:
            unit: Unit number to filter by

        Returns:
            Filtered list of topics
        """
        if not self.topics:
            self.load()

        return [t for t in self.topics if t.unit == unit]

    def get_all_units(self) -> List[float]:
        """Get sorted list of all unique unit numbers."""
        if not self.topics:
            self.load()

        return sorted(set(t.unit for t in self.topics))

    def get_all_types(self) -> List[str]:
        """Get sorted list of all unique worksheet types."""
        if not self.topics:
            self.load()

        return sorted(set(t.type for t in self.topics))

    def sync_to_registry(self, registry: TopicRegistry,
                        type_filter: Optional[List[str]] = None) -> Dict[str, int]:
        """
        Synchronize topics from Excel to the TopicRegistry.
        This registers all topics from Excel, even if they don't have generators yet.

        Args:
            registry: TopicRegistry instance to sync to
            type_filter: Only sync topics of these types (e.g., ["Intro", "Graphing"])

        Returns:
            Dictionary with sync statistics
        """
        if not self.topics:
            self.load()

        # Apply filter if needed
        topics_to_sync = self.topics
        if type_filter:
            topics_to_sync = self.get_topics_by_type(type_filter)

        # Track what we sync
        new_topics = 0
        existing_topics = 0

        for topic_def in topics_to_sync:
            # Check if already exists in registry
            existing = registry.get_topic(topic_def.unit, topic_def.type, topic_def.topic)

            if existing:
                existing_topics += 1
            else:
                # Register new topic (without generator - will be added later)
                registry.register_topic(
                    unit=topic_def.unit,
                    type=topic_def.type,
                    topic=topic_def.topic,
                    generator_class=None,
                    config_key=None
                )
                new_topics += 1

        return {
            'total_in_excel': len(self.topics),
            'synced': len(topics_to_sync),
            'new_topics': new_topics,
            'existing_topics': existing_topics
        }

    def _infer_course_name(self) -> str:
        """Infer course name from Excel filename."""
        filename = self.excel_path.stem  # Get filename without extension

        # Map filename patterns to course names
        if "algebra" in filename.lower() and "1" in filename:
            return "Algebra 1"
        elif "algebra" in filename.lower() and "2" in filename:
            return "Algebra 2"
        elif "geometry" in filename.lower():
            return "Geometry"
        elif "calculus" in filename.lower():
            return "Calculus"
        elif "grade" in filename.lower():
            # Extract grade number
            import re
            match = re.search(r'grade[\s_-]*(\d+)', filename.lower())
            if match:
                return f"Grade {match.group(1)}"

        # Default to filename
        return filename.replace("_", " ").title()

    def generate_report(self) -> str:
        """
        Generate a human-readable report of loaded topics.

        Returns:
            Formatted report string
        """
        if not self.topics:
            self.load()

        lines = []
        lines.append("=" * 70)
        lines.append(f"EXCEL CONFIGURATION REPORT: {self.course_name}")
        lines.append("=" * 70)
        lines.append(f"Source: {self.excel_path}")
        lines.append(f"Total Topics: {len(self.topics)}")
        lines.append("")

        # Summary by type
        lines.append("Topics by Type:")
        lines.append("-" * 70)
        type_counts = {}
        for topic in self.topics:
            type_counts[topic.type] = type_counts.get(topic.type, 0) + 1

        for type_name in sorted(type_counts.keys()):
            lines.append(f"  {type_name:20s}: {type_counts[type_name]:3d} topics")

        lines.append("")

        # Summary by unit
        lines.append("Topics by Unit:")
        lines.append("-" * 70)
        unit_counts = {}
        for topic in self.topics:
            unit_counts[topic.unit] = unit_counts.get(topic.unit, 0) + 1

        for unit in sorted(unit_counts.keys()):
            lines.append(f"  Unit {unit:4.1f}: {unit_counts[unit]:3d} topics")

        return "\n".join(lines)


class MultiCourseLoader:
    """
    Manages loading configurations from multiple Excel files.
    Supports different grade levels and courses.
    """

    def __init__(self, base_dir: str = "worksheet-generator"):
        """
        Initialize multi-course loader.

        Args:
            base_dir: Base directory to search for Excel files
        """
        self.base_dir = Path(base_dir)
        self.loaders: Dict[str, ExcelConfigLoader] = {}

    def discover_configs(self) -> List[Path]:
        """
        Discover all Excel configuration files in base directory.

        Returns:
            List of paths to Excel files
        """
        excel_files = []

        # Look for .xlsx files that match topic list pattern
        for pattern in ["*Topic*.xlsx", "*Worksheet*.xlsx", "*topics*.xlsx"]:
            excel_files.extend(self.base_dir.glob(pattern))

        return sorted(set(excel_files))

    def load_all(self) -> Dict[str, ExcelConfigLoader]:
        """
        Load all discovered Excel configuration files.

        Returns:
            Dictionary mapping course names to loaders
        """
        config_files = self.discover_configs()

        for config_file in config_files:
            loader = ExcelConfigLoader(str(config_file))
            loader.load()
            self.loaders[loader.course_name] = loader

        return self.loaders

    def sync_all_to_registry(self, registry: TopicRegistry,
                            type_filter: Optional[List[str]] = None) -> Dict[str, Dict]:
        """
        Sync all courses to the registry.

        Args:
            registry: TopicRegistry to sync to
            type_filter: Only sync topics of these types

        Returns:
            Dictionary of sync statistics per course
        """
        if not self.loaders:
            self.load_all()

        stats = {}
        for course_name, loader in self.loaders.items():
            stats[course_name] = loader.sync_to_registry(registry, type_filter)

        return stats


if __name__ == "__main__":
    # Example usage
    import sys

    # Load Algebra 1 configuration
    loader = ExcelConfigLoader("worksheet-generator/High School Worksheet Topics List.xlsx")
    topics = loader.load()

    print(loader.generate_report())
    print("\n")

    # Show Intro and Graphing topics only
    print("=" * 70)
    print("INTRO AND GRAPHING TOPICS (Current Focus)")
    print("=" * 70)

    intro_graphing = loader.get_topics_by_type(["Intro", "Graphing"])
    for topic in intro_graphing:
        print(f"Unit {topic.unit:4.1f} | {topic.type:10s} | {topic.topic}")

    print(f"\nTotal Intro + Graphing: {len(intro_graphing)}")
