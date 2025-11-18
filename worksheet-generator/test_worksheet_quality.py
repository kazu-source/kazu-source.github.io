"""
Worksheet Quality Testing Tool
Tests generators and checks for common issues in generated PDFs.
"""

import sys
import os
from pathlib import Path
from typing import List, Dict, Any
import random

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from topic_registry import get_registry, register_all_generators
from worksheet_config import get_config


class WorksheetQualityChecker:
    """Tests worksheet generators for quality issues."""

    def __init__(self):
        """Initialize the quality checker."""
        register_all_generators()
        self.registry = get_registry()
        self.issues = []

    def check_generator(self, unit: float, topic_type: str, topic: str,
                       difficulties: List[str] = None) -> Dict[str, Any]:
        """
        Check a specific generator for quality issues.

        Args:
            unit: Unit number
            topic_type: Type of worksheet (Intro, Graphing, etc.)
            topic: Topic name
            difficulties: List of difficulties to test (default: all)

        Returns:
            Dictionary with test results
        """
        if difficulties is None:
            difficulties = ['easy', 'medium', 'hard']

        results = {
            'topic': f"Unit {unit} | {topic_type} | {topic}",
            'passed': True,
            'issues': [],
            'samples': {}
        }

        # Get generator
        generator = self.registry.get_generator(unit, topic_type, topic)
        if not generator:
            results['passed'] = False
            results['issues'].append("Generator not found or not implemented")
            return results

        # Test each difficulty
        for difficulty in difficulties:
            try:
                # Generate sample problems
                problems = generator.generate_worksheet(difficulty, 3)

                # Check each problem
                difficulty_issues = []
                for i, problem in enumerate(problems, 1):
                    # Check 1: Has latex attribute (or equation_latex for graphing, or labels for point graphing)
                    has_text = (hasattr(problem, 'latex') or
                               hasattr(problem, 'equation_latex') or
                               hasattr(problem, 'labels') or
                               hasattr(problem, 'equation1_latex'))  # for systems

                    if not has_text:
                        difficulty_issues.append(f"Problem {i}: Missing text representation (latex/equation_latex/labels)")
                        continue

                    latex = (getattr(problem, 'latex', None) or
                            getattr(problem, 'equation_latex', None) or
                            ', '.join(getattr(problem, 'labels', [])) or
                            getattr(problem, 'equation1_latex', 'N/A'))

                    # Check 2: LaTeX should not have unprocessed \text{} commands for math problems
                    if '\\text{' in latex and topic_type == 'Intro':
                        # Count ratio of text to math
                        text_content = latex.count('\\text{')
                        if text_content > 3:  # Too much text in a math problem
                            difficulty_issues.append(
                                f"Problem {i}: Excessive \\text{{}} usage (may not render as equation)\n"
                                f"   LaTeX: {latex[:100]}..."
                            )

                    # Check 3: Solution should be numeric for non-graphing problems
                    if hasattr(problem, 'solution'):
                        if topic_type != 'Graphing' and not isinstance(problem.solution, (int, float)):
                            # Check if it's stored in steps
                            if not hasattr(problem, 'steps') or not problem.steps:
                                difficulty_issues.append(
                                    f"Problem {i}: Non-numeric solution without steps\n"
                                    f"   Solution type: {type(problem.solution)}"
                                )

                    # Check 4: Graphing problems should have images
                    if topic_type == 'Graphing':
                        if not hasattr(problem, 'worksheet_image') or not hasattr(problem, 'answer_image'):
                            difficulty_issues.append(f"Problem {i}: Missing worksheet/answer images")

                # Store sample for manual inspection
                results['samples'][difficulty] = [
                    {
                        'latex': (getattr(p, 'latex', None) or
                                 getattr(p, 'equation_latex', None) or
                                 ', '.join(getattr(p, 'labels', [])) or
                                 'N/A'),
                        'solution': getattr(p, 'solution', 'N/A'),
                        'steps': getattr(p, 'steps', [])
                    }
                    for p in problems[:2]  # First 2 problems
                ]

                if difficulty_issues:
                    results['issues'].extend([f"[{difficulty.upper()}] {issue}" for issue in difficulty_issues])
                    results['passed'] = False

            except Exception as e:
                results['passed'] = False
                results['issues'].append(f"[{difficulty.upper()}] Exception: {str(e)}")

        return results

    def check_all_implemented(self) -> List[Dict[str, Any]]:
        """Check all implemented generators."""
        all_results = []
        implemented = self.registry.get_implemented_topics(type_filter=['Intro', 'Graphing'])

        print(f"Testing {len(implemented)} implemented topics...\n")

        for topic_meta in implemented:
            print(f"Testing: Unit {topic_meta.unit} | {topic_meta.type.value} | {topic_meta.topic}")

            result = self.check_generator(
                topic_meta.unit,
                topic_meta.type.value,
                topic_meta.topic
            )

            all_results.append(result)

            if result['passed']:
                print("  OK PASSED\n")
            else:
                print(f"  X FAILED ({len(result['issues'])} issues)")
                for issue in result['issues'][:3]:  # Show first 3 issues
                    print(f"    - {issue}")
                if len(result['issues']) > 3:
                    print(f"    ... and {len(result['issues']) - 3} more issues")
                print()

        return all_results

    def generate_report(self, results: List[Dict[str, Any]]) -> str:
        """Generate a quality report."""
        passed = sum(1 for r in results if r['passed'])
        failed = len(results) - passed

        report = []
        report.append("=" * 80)
        report.append("WORKSHEET QUALITY REPORT")
        report.append("=" * 80)
        report.append(f"\nTotal Tested: {len(results)}")
        report.append(f"Passed: {passed} ({passed/len(results)*100:.1f}%)")
        report.append(f"Failed: {failed} ({failed/len(results)*100:.1f}%)")

        if failed > 0:
            report.append("\n" + "=" * 80)
            report.append("FAILED TOPICS")
            report.append("=" * 80)

            for result in results:
                if not result['passed']:
                    report.append(f"\nX {result['topic']}")
                    for issue in result['issues']:
                        report.append(f"  - {issue}")

        report.append("\n" + "=" * 80)
        report.append("SAMPLE PROBLEMS")
        report.append("=" * 80)

        # Show samples from failed topics
        for result in results:
            if not result['passed']:
                report.append(f"\n{result['topic']}:")
                for difficulty, samples in result['samples'].items():
                    report.append(f"  [{difficulty.upper()}]")
                    for i, sample in enumerate(samples, 1):
                        report.append(f"    {i}. {sample['latex'][:80]}...")
                        report.append(f"       Solution: {sample['solution']}, Steps: {sample['steps']}")

        return "\n".join(report)


def main():
    """Run quality checks."""
    checker = WorksheetQualityChecker()

    print("=" * 80)
    print("WORKSHEET QUALITY CHECKER")
    print("=" * 80)
    print()

    # Check all implemented topics
    results = checker.check_all_implemented()

    # Generate report
    report = checker.generate_report(results)
    print("\n" + report)

    # Save report to file
    report_path = Path("quality_report.txt")
    with open(report_path, 'w') as f:
        f.write(report)

    print(f"\nReport saved to: {report_path}")


if __name__ == "__main__":
    main()
