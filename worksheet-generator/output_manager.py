"""
Output Manager - Manages organization and tracking of generated worksheets.
Provides structured output directories and manifest tracking.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict


@dataclass
class WorksheetManifestEntry:
    """Entry in the worksheet manifest."""
    timestamp: str
    course: str
    unit: float
    type: str
    topic: str
    difficulty: str
    num_problems: int
    file_path: str
    file_size_bytes: int

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)


class OutputManager:
    """
    Manages output directory structure and file tracking.
    Provides organized storage and manifest generation.
    """

    def __init__(self, base_dir: str = "output"):
        """
        Initialize output manager.

        Args:
            base_dir: Base directory for all output files
        """
        self.base_dir = Path(base_dir)
        self.manifest_file = self.base_dir / "manifest.json"
        self.manifest: List[WorksheetManifestEntry] = []

        # Create base directory
        self.base_dir.mkdir(parents=True, exist_ok=True)

        # Load existing manifest if it exists
        self._load_manifest()

    def get_output_path(
        self,
        course: str,
        unit: float,
        type: str,
        topic: str,
        difficulty: str,
        date: Optional[str] = None
    ) -> Path:
        """
        Generate output path following standardized structure.

        Structure: {base}/{course}/Unit{unit}/{type}/{topic}_{difficulty}_{date}.pdf

        Args:
            course: Course name (e.g., "Algebra 1")
            unit: Unit number
            type: Worksheet type
            topic: Topic name
            difficulty: Difficulty level
            date: Date string (defaults to today in YYYYMMDD format)

        Returns:
            Path object for output file
        """
        # Default date to today
        if date is None:
            date = datetime.now().strftime("%Y%m%d")

        # Sanitize topic name for filesystem
        safe_topic = self._sanitize_filename(topic)

        # Build directory structure
        course_dir = self._sanitize_filename(course)
        unit_dir = f"Unit{int(unit):02d}"
        type_dir = self._sanitize_filename(type)

        # Create filename
        filename = f"{safe_topic}_{difficulty}_{date}.pdf"

        # Full path
        output_dir = self.base_dir / course_dir / unit_dir / type_dir
        output_dir.mkdir(parents=True, exist_ok=True)

        return output_dir / filename

    def register_worksheet(
        self,
        course: str,
        unit: float,
        type: str,
        topic: str,
        difficulty: str,
        num_problems: int,
        file_path: str
    ) -> WorksheetManifestEntry:
        """
        Register a generated worksheet in the manifest.

        Args:
            course: Course name
            unit: Unit number
            type: Worksheet type
            topic: Topic name
            difficulty: Difficulty level
            num_problems: Number of problems in worksheet
            file_path: Path to generated PDF

        Returns:
            Manifest entry for the worksheet
        """
        # Get file info
        path = Path(file_path)
        file_size = path.stat().st_size if path.exists() else 0

        # Create manifest entry
        entry = WorksheetManifestEntry(
            timestamp=datetime.now().isoformat(),
            course=course,
            unit=unit,
            type=type,
            topic=topic,
            difficulty=difficulty,
            num_problems=num_problems,
            file_path=str(file_path),
            file_size_bytes=file_size
        )

        # Add to manifest
        self.manifest.append(entry)

        # Save manifest
        self._save_manifest()

        return entry

    def get_worksheets(
        self,
        course: Optional[str] = None,
        unit: Optional[float] = None,
        type: Optional[str] = None,
        difficulty: Optional[str] = None
    ) -> List[WorksheetManifestEntry]:
        """
        Query worksheets from manifest with optional filters.

        Args:
            course: Filter by course
            unit: Filter by unit
            type: Filter by worksheet type
            difficulty: Filter by difficulty level

        Returns:
            List of matching worksheet entries
        """
        results = self.manifest

        if course:
            results = [e for e in results if e.course == course]
        if unit is not None:
            results = [e for e in results if e.unit == unit]
        if type:
            results = [e for e in results if e.type == type]
        if difficulty:
            results = [e for e in results if e.difficulty == difficulty]

        return results

    def generate_index_html(self, output_path: Optional[str] = None) -> str:
        """
        Generate an HTML index of all worksheets.

        Args:
            output_path: Path to save HTML file (defaults to base_dir/index.html)

        Returns:
            Path to generated HTML file
        """
        if output_path is None:
            output_path = str(self.base_dir / "index.html")

        # Group worksheets by course and unit
        by_course: Dict[str, Dict[float, List[WorksheetManifestEntry]]] = {}

        for entry in self.manifest:
            if entry.course not in by_course:
                by_course[entry.course] = {}
            if entry.unit not in by_course[entry.course]:
                by_course[entry.course][entry.unit] = []
            by_course[entry.course][entry.unit].append(entry)

        # Generate HTML
        html_lines = [
            "<!DOCTYPE html>",
            "<html lang='en'>",
            "<head>",
            "    <meta charset='UTF-8'>",
            "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>",
            "    <title>Worksheet Library</title>",
            "    <style>",
            "        body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }",
            "        h1 { color: #333; }",
            "        h2 { color: #666; margin-top: 30px; }",
            "        h3 { color: #888; margin-top: 20px; }",
            "        .worksheet { background: white; padding: 10px; margin: 5px 0; border-radius: 5px; }",
            "        .worksheet a { text-decoration: none; color: #0066cc; font-weight: bold; }",
            "        .worksheet a:hover { text-decoration: underline; }",
            "        .meta { color: #666; font-size: 0.9em; margin-left: 20px; }",
            "        .stats { background: #e8f4f8; padding: 15px; border-radius: 5px; margin: 20px 0; }",
            "    </style>",
            "</head>",
            "<body>",
            "    <h1>📚 Worksheet Library</h1>",
            f"    <div class='stats'>",
            f"        <strong>Total Worksheets:</strong> {len(self.manifest)}<br>",
            f"        <strong>Courses:</strong> {len(by_course)}<br>",
            f"        <strong>Last Updated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "    </div>",
        ]

        # Add courses
        for course in sorted(by_course.keys()):
            html_lines.append(f"    <h2>{course}</h2>")

            # Add units
            for unit in sorted(by_course[course].keys()):
                html_lines.append(f"    <h3>Unit {int(unit)}</h3>")

                # Add worksheets
                for entry in sorted(by_course[course][unit], key=lambda e: (e.type, e.topic)):
                    rel_path = Path(entry.file_path).relative_to(self.base_dir)
                    html_lines.append(f"    <div class='worksheet'>")
                    html_lines.append(f"        <a href='{rel_path}'>{entry.topic}</a>")
                    html_lines.append(f"        <span class='meta'>")
                    html_lines.append(f"            {entry.type} | {entry.difficulty} | {entry.num_problems} problems")
                    html_lines.append(f"        </span>")
                    html_lines.append(f"    </div>")

        html_lines.extend([
            "</body>",
            "</html>"
        ])

        # Write HTML file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(html_lines))

        return output_path

    def get_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about generated worksheets.

        Returns:
            Dictionary with statistics
        """
        if not self.manifest:
            return {
                'total_worksheets': 0,
                'total_size_mb': 0,
                'by_course': {},
                'by_type': {},
                'by_difficulty': {}
            }

        # Calculate statistics
        total_size = sum(e.file_size_bytes for e in self.manifest)

        # By course
        by_course = {}
        for entry in self.manifest:
            by_course[entry.course] = by_course.get(entry.course, 0) + 1

        # By type
        by_type = {}
        for entry in self.manifest:
            by_type[entry.type] = by_type.get(entry.type, 0) + 1

        # By difficulty
        by_difficulty = {}
        for entry in self.manifest:
            by_difficulty[entry.difficulty] = by_difficulty.get(entry.difficulty, 0) + 1

        return {
            'total_worksheets': len(self.manifest),
            'total_size_mb': total_size / (1024 * 1024),
            'by_course': by_course,
            'by_type': by_type,
            'by_difficulty': by_difficulty
        }

    def _sanitize_filename(self, name: str) -> str:
        """
        Sanitize a string for use in filenames.

        Args:
            name: String to sanitize

        Returns:
            Sanitized string safe for filesystem
        """
        # Replace problematic characters
        safe = name.replace("/", "-").replace("\\", "-")
        safe = safe.replace(":", "-").replace("*", "-")
        safe = safe.replace("?", "").replace('"', "")
        safe = safe.replace("<", "").replace(">", "")
        safe = safe.replace("|", "-")

        # Remove multiple spaces and dashes
        safe = " ".join(safe.split())
        safe = "-".join(safe.split("-"))

        # Keep only alphanumeric, spaces, dashes, and underscores
        safe = "".join(c for c in safe if c.isalnum() or c in " -_")

        return safe.strip()

    def _load_manifest(self):
        """Load manifest from JSON file."""
        if not self.manifest_file.exists():
            self.manifest = []
            return

        try:
            with open(self.manifest_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.manifest = [
                    WorksheetManifestEntry(**entry) for entry in data
                ]
        except Exception as e:
            print(f"Warning: Could not load manifest: {e}")
            self.manifest = []

    def _save_manifest(self):
        """Save manifest to JSON file."""
        try:
            with open(self.manifest_file, 'w', encoding='utf-8') as f:
                data = [entry.to_dict() for entry in self.manifest]
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Warning: Could not save manifest: {e}")

    def clear_manifest(self):
        """Clear the manifest (does not delete files)."""
        self.manifest = []
        self._save_manifest()

    def __repr__(self):
        return f"OutputManager({len(self.manifest)} worksheets tracked)"


if __name__ == "__main__":
    # Example usage
    manager = OutputManager(base_dir="output")

    print("=" * 70)
    print("OUTPUT MANAGER")
    print("=" * 70)
    print(f"\n{manager}\n")

    # Example: Register a worksheet
    path = manager.get_output_path(
        course="Algebra 1",
        unit=2.0,
        type="Intro",
        topic="Linear Equations",
        difficulty="easy"
    )
    print(f"Output path example: {path}")

    # Show statistics
    print("\n\nStatistics:")
    print("-" * 70)
    stats = manager.get_statistics()
    print(f"Total worksheets: {stats['total_worksheets']}")
    print(f"Total size: {stats['total_size_mb']:.2f} MB")

    if stats['by_course']:
        print("\nBy course:")
        for course, count in stats['by_course'].items():
            print(f"  {course}: {count}")
