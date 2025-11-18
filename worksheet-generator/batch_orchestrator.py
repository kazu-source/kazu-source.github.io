"""
Batch Generation Orchestrator - Coordinates batch worksheet generation.
Handles progress tracking, error handling, and output management.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional, Callable, Any
from pathlib import Path
import time
from datetime import datetime

from topic_registry import TopicRegistry, TopicMetadata
from excel_config_loader import ExcelConfigLoader, TopicDefinition
from pdf_generator import PDFWorksheetGenerator
from worksheet_config import get_config


@dataclass
class GenerationTask:
    """Represents a single worksheet generation task."""
    unit: float
    type: str
    topic: str
    difficulty: str = "easy"
    num_problems: Optional[int] = None
    course: str = "Algebra 1"

    def __repr__(self):
        return f"Unit {self.unit} | {self.type} | {self.topic} ({self.difficulty})"


@dataclass
class GenerationResult:
    """Result of a worksheet generation attempt."""
    task: GenerationTask
    success: bool
    output_path: Optional[str] = None
    error_message: Optional[str] = None
    duration_seconds: float = 0.0

    def __repr__(self):
        status = "✓" if self.success else "✗"
        return f"{status} {self.task}"


class BatchOrchestrator:
    """
    Orchestrates batch generation of worksheets.
    Coordinates between registry, generators, and output management.
    """

    def __init__(self, registry: TopicRegistry, output_base_dir: str = "output"):
        """
        Initialize the batch orchestrator.

        Args:
            registry: TopicRegistry with registered generators
            output_base_dir: Base directory for output files
        """
        self.registry = registry
        self.output_base_dir = Path(output_base_dir)
        self.pdf_gen = PDFWorksheetGenerator()

        # Progress tracking
        self.total_tasks = 0
        self.completed_tasks = 0
        self.failed_tasks = 0
        self.results: List[GenerationResult] = []

        # Callbacks for progress updates
        self.on_task_start: Optional[Callable[[GenerationTask], None]] = None
        self.on_task_complete: Optional[Callable[[GenerationResult], None]] = None
        self.on_batch_complete: Optional[Callable[[List[GenerationResult]], None]] = None

    def create_tasks_from_excel(
        self,
        excel_loader: ExcelConfigLoader,
        type_filter: Optional[List[str]] = None,
        unit_filter: Optional[float] = None,
        difficulty: str = "easy",
        num_problems: Optional[int] = None
    ) -> List[GenerationTask]:
        """
        Create generation tasks from Excel configuration.

        Args:
            excel_loader: Loaded Excel configuration
            type_filter: Filter by worksheet types (e.g., ["Intro", "Graphing"])
            unit_filter: Filter by unit number
            difficulty: Difficulty level for all tasks
            num_problems: Number of problems (None = use config default)

        Returns:
            List of generation tasks
        """
        # Get filtered topics
        topics = excel_loader.topics
        if type_filter:
            topics = [t for t in topics if t.type in type_filter]
        if unit_filter is not None:
            topics = [t for t in topics if t.unit == unit_filter]

        # Create tasks
        tasks = []
        for topic in topics:
            # Only create task if generator exists
            if self.registry.get_generator(topic.unit, topic.type, topic.topic):
                task = GenerationTask(
                    unit=topic.unit,
                    type=topic.type,
                    topic=topic.topic,
                    difficulty=difficulty,
                    num_problems=num_problems,
                    course=topic.course
                )
                tasks.append(task)

        return tasks

    def create_tasks_from_registry(
        self,
        type_filter: Optional[List[str]] = None,
        unit_filter: Optional[float] = None,
        difficulty: str = "easy",
        num_problems: Optional[int] = None
    ) -> List[GenerationTask]:
        """
        Create generation tasks from all implemented topics in registry.

        Args:
            type_filter: Filter by worksheet types
            unit_filter: Filter by unit number
            difficulty: Difficulty level
            num_problems: Number of problems (None = use config default)

        Returns:
            List of generation tasks
        """
        # Get implemented topics
        topics = self.registry.get_implemented_topics(type_filter=type_filter)

        if unit_filter is not None:
            topics = [t for t in topics if t.unit == unit_filter]

        # Create tasks
        tasks = []
        for topic in topics:
            task = GenerationTask(
                unit=topic.unit,
                type=topic.type.value,
                topic=topic.topic,
                difficulty=difficulty,
                num_problems=num_problems,
                course="Algebra 1"  # Default for now
            )
            tasks.append(task)

        return tasks

    def generate_batch(
        self,
        tasks: List[GenerationTask],
        skip_existing: bool = False
    ) -> List[GenerationResult]:
        """
        Generate worksheets for a batch of tasks.

        Args:
            tasks: List of generation tasks to execute
            skip_existing: If True, skip tasks where output file already exists

        Returns:
            List of generation results
        """
        import sys

        # Use ASCII characters for Windows compatibility
        check_mark = "OK" if sys.platform == 'win32' else "✓"
        cross_mark = "X" if sys.platform == 'win32' else "✗"
        circle_mark = "O" if sys.platform == 'win32' else "⊙"

        self.total_tasks = len(tasks)
        self.completed_tasks = 0
        self.failed_tasks = 0
        self.results = []

        print(f"\n{'='*70}")
        print(f"BATCH GENERATION: {self.total_tasks} tasks")
        print(f"{'='*70}\n")

        for i, task in enumerate(tasks, 1):
            print(f"[{i}/{self.total_tasks}] {task}")

            # Notify task start
            if self.on_task_start:
                self.on_task_start(task)

            # Check if output already exists
            output_path = self._get_output_path(task)
            if skip_existing and output_path.exists():
                print(f"  {circle_mark} Skipping (already exists): {output_path}")
                result = GenerationResult(
                    task=task,
                    success=True,
                    output_path=str(output_path),
                    error_message="Skipped - file exists"
                )
                self.results.append(result)
                self.completed_tasks += 1
                continue

            # Generate worksheet
            result = self._generate_single(task)
            self.results.append(result)

            if result.success:
                self.completed_tasks += 1
                print(f"  {check_mark} Generated: {result.output_path}")
                print(f"  Time: {result.duration_seconds:.2f}s")
            else:
                self.failed_tasks += 1
                print(f"  {cross_mark} Failed: {result.error_message}")

            # Notify task complete
            if self.on_task_complete:
                self.on_task_complete(result)

            print()

        # Notify batch complete
        if self.on_batch_complete:
            self.on_batch_complete(self.results)

        # Print summary
        self._print_summary()

        return self.results

    def _generate_single(self, task: GenerationTask) -> GenerationResult:
        """
        Generate a single worksheet.

        Args:
            task: Generation task

        Returns:
            Generation result
        """
        start_time = time.time()

        try:
            # Get generator
            generator = self.registry.get_generator(task.unit, task.type, task.topic)
            if not generator:
                return GenerationResult(
                    task=task,
                    success=False,
                    error_message="Generator not found in registry"
                )

            # Get topic metadata for config key
            topic_meta = self.registry.get_topic(task.unit, task.type, task.topic)
            if not topic_meta or not topic_meta.config_key:
                return GenerationResult(
                    task=task,
                    success=False,
                    error_message="Config key not found"
                )

            # Get config
            try:
                config = get_config(topic_meta.config_key)
            except KeyError as e:
                return GenerationResult(
                    task=task,
                    success=False,
                    error_message=f"Config not found: {e}"
                )

            # Determine number of problems
            num_problems = task.num_problems if task.num_problems else config.default_num_problems

            # Generate problems (note: generator uses generate_worksheet method)
            problems = generator.generate_worksheet(
                difficulty=task.difficulty,
                num_problems=num_problems
            )

            # Prepare output
            output_path = self._get_output_path(task)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Generate PDF
            title = f"{task.topic}"
            self.pdf_gen.generate_worksheet(
                equations=problems,
                output_path=str(output_path),
                title=title
            )

            duration = time.time() - start_time

            return GenerationResult(
                task=task,
                success=True,
                output_path=str(output_path),
                duration_seconds=duration
            )

        except Exception as e:
            duration = time.time() - start_time
            return GenerationResult(
                task=task,
                success=False,
                error_message=str(e),
                duration_seconds=duration
            )

    def _get_output_path(self, task: GenerationTask) -> Path:
        """
        Generate output path for a task.

        Format: output/{course}/Unit{unit}/{type}/{topic}_{difficulty}_{date}.pdf

        Args:
            task: Generation task

        Returns:
            Path object for output file
        """
        # Sanitize topic name for filename
        safe_topic = task.topic.replace("/", "-").replace("\\", "-")
        safe_topic = "".join(c for c in safe_topic if c.isalnum() or c in "- _")

        # Create filename
        date_str = datetime.now().strftime("%Y%m%d")
        filename = f"{safe_topic}_{task.difficulty}_{date_str}.pdf"

        # Create directory structure
        output_dir = self.output_base_dir / task.course / f"Unit{int(task.unit)}" / task.type

        return output_dir / filename

    def _print_summary(self):
        """Print batch generation summary."""
        import sys
        check_mark = "OK" if sys.platform == 'win32' else "✓"
        cross_mark = "X" if sys.platform == 'win32' else "✗"

        print(f"{'='*70}")
        print("BATCH GENERATION SUMMARY")
        print(f"{'='*70}")
        print(f"Total tasks:      {self.total_tasks}")
        print(f"Completed:        {self.completed_tasks} {check_mark}")
        print(f"Failed:           {self.failed_tasks} {cross_mark}")
        print(f"Success rate:     {self.completed_tasks/self.total_tasks*100:.1f}%")

        # Show failures if any
        if self.failed_tasks > 0:
            print(f"\n{'='*70}")
            print("FAILED TASKS")
            print(f"{'='*70}")
            for result in self.results:
                if not result.success:
                    print(f"{cross_mark} {result.task}")
                    print(f"  Error: {result.error_message}")

    def get_summary_stats(self) -> Dict[str, Any]:
        """
        Get summary statistics.

        Returns:
            Dictionary with summary statistics
        """
        return {
            'total_tasks': self.total_tasks,
            'completed': self.completed_tasks,
            'failed': self.failed_tasks,
            'success_rate': self.completed_tasks / self.total_tasks if self.total_tasks > 0 else 0,
            'results': self.results
        }


if __name__ == "__main__":
    # Example usage
    from topic_registry import get_registry, register_all_generators

    # Initialize
    register_all_generators()
    registry = get_registry()
    orchestrator = BatchOrchestrator(registry, output_base_dir="output")

    # Create tasks for all implemented Intro and Graphing topics
    tasks = orchestrator.create_tasks_from_registry(
        type_filter=["Intro", "Graphing"],
        difficulty="easy"
    )

    print(f"Created {len(tasks)} tasks")

    # Generate (uncomment to actually run)
    # results = orchestrator.generate_batch(tasks)
