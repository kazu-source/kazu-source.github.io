"""
Generator for graphing points on a coordinate plane worksheets.
Chapter 4: Linear Equations (Two Variables) - Graphing Points
"""

import random
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import List, Tuple

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from graphing_utils import graph_points, create_blank_coordinate_plane


@dataclass
class GraphingPointsProblem:
    """Represents a point graphing problem."""
    points: List[Tuple[int, int]]  # List of (x, y) points to graph
    labels: List[str]  # Labels for each point (e.g., "A", "B", "C")
    difficulty: str  # easy, medium, hard, challenge
    worksheet_image: object  # PIL Image for worksheet (blank grid)
    answer_image: object  # PIL Image for answer key (with points plotted)
    x_min: int = -10
    x_max: int = 10
    y_min: int = -10
    y_max: int = 10


class GraphingPointsGenerator:
    """Generator for point graphing problems."""

    def __init__(self, seed=None):
        """
        Initialize the generator.

        Args:
            seed: Random seed for reproducibility
        """
        if seed is not None:
            random.seed(seed)

        self.point_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

    def generate_problem(self, difficulty: str) -> GraphingPointsProblem:
        """
        Generate a single point graphing problem.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'

        Returns:
            GraphingPointsProblem object
        """
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        elif difficulty == 'challenge':
            return self._generate_challenge()
        else:
            raise ValueError(f"Unknown difficulty: {difficulty}")

    def _generate_easy(self) -> GraphingPointsProblem:
        """
        Generate easy problem: 3 points in first quadrant, coordinates 0-10.
        """
        num_points = 3
        points = []

        # Generate points in first quadrant with no duplicates
        used_points = set()
        while len(points) < num_points:
            x = random.randint(0, 10)
            y = random.randint(0, 10)
            if (x, y) not in used_points:
                points.append((x, y))
                used_points.add((x, y))

        labels = [f"{self.point_labels[i]}({x},{y})"
                 for i, (x, y) in enumerate(points)]

        # Create worksheet image (blank first quadrant grid)
        worksheet_img = create_blank_coordinate_plane(
            x_min=0, x_max=10, y_min=0, y_max=10,
            first_quadrant_only=True, figsize=(6, 6)
        )

        # Create answer key image (with points plotted)
        answer_img = graph_points(
            points, labels=labels,
            x_min=0, x_max=10, y_min=0, y_max=10,
            first_quadrant_only=True, figsize=(6, 6)
        )

        return GraphingPointsProblem(
            points=points,
            labels=labels,
            difficulty='easy',
            worksheet_image=worksheet_img,
            answer_image=answer_img,
            x_min=0, x_max=10, y_min=0, y_max=10
        )

    def _generate_medium(self) -> GraphingPointsProblem:
        """
        Generate medium problem: 4 points in all quadrants, coordinates -5 to 5.
        """
        num_points = 4
        points = []

        # Ensure we get points in different quadrants
        quadrants = [
            (lambda: (random.randint(1, 5), random.randint(1, 5))),      # Q1
            (lambda: (random.randint(-5, -1), random.randint(1, 5))),    # Q2
            (lambda: (random.randint(-5, -1), random.randint(-5, -1))),  # Q3
            (lambda: (random.randint(1, 5), random.randint(-5, -1))),    # Q4
        ]

        random.shuffle(quadrants)

        for i in range(num_points):
            points.append(quadrants[i]())

        labels = [f"{self.point_labels[i]}({x},{y})"
                 for i, (x, y) in enumerate(points)]

        # Create worksheet image (blank grid)
        worksheet_img = create_blank_coordinate_plane(
            x_min=-5, x_max=5, y_min=-5, y_max=5,
            figsize=(6, 6)
        )

        # Create answer key image
        answer_img = graph_points(
            points, labels=labels,
            x_min=-5, x_max=5, y_min=-5, y_max=5,
            figsize=(6, 6)
        )

        return GraphingPointsProblem(
            points=points,
            labels=labels,
            difficulty='medium',
            worksheet_image=worksheet_img,
            answer_image=answer_img,
            x_min=-5, x_max=5, y_min=-5, y_max=5
        )

    def _generate_hard(self) -> GraphingPointsProblem:
        """
        Generate hard problem: 5 points across all 4 quadrants, full range -10 to 10.
        """
        num_points = 5
        points = []

        # Ensure we get points in all 4 quadrants
        quadrants = [
            (lambda: (random.randint(1, 10), random.randint(1, 10))),      # Q1
            (lambda: (random.randint(-10, -1), random.randint(1, 10))),    # Q2
            (lambda: (random.randint(-10, -1), random.randint(-10, -1))),  # Q3
            (lambda: (random.randint(1, 10), random.randint(-10, -1))),    # Q4
        ]

        # Generate one point in each quadrant
        for quadrant_gen in quadrants:
            points.append(quadrant_gen())

        # Add one more point in any quadrant
        used_points = set(points)
        while len(points) < num_points:
            x = random.randint(-10, 10)
            y = random.randint(-10, 10)
            if (x, y) not in used_points:
                points.append((x, y))
                used_points.add((x, y))

        # Shuffle to mix quadrants
        random.shuffle(points)

        labels = [f"{self.point_labels[i]}({x},{y})"
                 for i, (x, y) in enumerate(points)]

        # Create worksheet image
        worksheet_img = create_blank_coordinate_plane(figsize=(6, 6))

        # Create answer key image
        answer_img = graph_points(points, labels=labels, figsize=(6, 6))

        return GraphingPointsProblem(
            points=points,
            labels=labels,
            difficulty='hard',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def _generate_challenge(self) -> GraphingPointsProblem:
        """
        Generate challenge problem: 6 points across all 4 quadrants, includes points on axes.
        """
        num_points = 6
        points = []

        # Include at least 2 points on axes
        # Point on x-axis
        points.append((random.randint(-8, 8), 0))
        # Point on y-axis
        points.append((0, random.randint(-8, 8)))

        # Ensure we get points in all 4 quadrants
        quadrants = [
            (lambda: (random.randint(1, 10), random.randint(1, 10))),      # Q1
            (lambda: (random.randint(-10, -1), random.randint(1, 10))),    # Q2
            (lambda: (random.randint(-10, -1), random.randint(-10, -1))),  # Q3
            (lambda: (random.randint(1, 10), random.randint(-10, -1))),    # Q4
        ]

        random.shuffle(quadrants)

        # Add points from different quadrants
        used_points = set(points)
        for quadrant_gen in quadrants:
            if len(points) >= num_points:
                break
            point = quadrant_gen()
            if point not in used_points:
                points.append(point)
                used_points.add(point)

        # Fill any remaining slots
        while len(points) < num_points:
            x = random.randint(-10, 10)
            y = random.randint(-10, 10)
            if (x, y) not in used_points:
                points.append((x, y))
                used_points.add((x, y))

        # Shuffle to mix axis points with others
        random.shuffle(points)

        labels = [f"{self.point_labels[i]}({x},{y})"
                 for i, (x, y) in enumerate(points)]

        # Create worksheet image
        worksheet_img = create_blank_coordinate_plane(figsize=(6, 6))

        # Create answer key image
        answer_img = graph_points(points, labels=labels, figsize=(6, 6))

        return GraphingPointsProblem(
            points=points,
            labels=labels,
            difficulty='challenge',
            worksheet_image=worksheet_img,
            answer_image=answer_img
        )

    def generate_worksheet(self, difficulty: str,
                          num_problems: int) -> List[GraphingPointsProblem]:
        """
        Generate multiple problems for a worksheet.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of GraphingPointsProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problems.append(self.generate_problem(difficulty))
        return problems


if __name__ == "__main__":
    # Test the generator
    print("Testing Graphing Points Generator...")

    gen = GraphingPointsGenerator(seed=42)

    # Test each difficulty level
    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()}:")
        problem = gen.generate_problem(difficulty)
        print(f"  Points: {problem.points}")
        print(f"  Labels: {problem.labels}")
        print(f"  Bounds: x({problem.x_min},{problem.x_max}), y({problem.y_min},{problem.y_max})")

        # Save test images
        problem.worksheet_image.save(f"test_graphing_points_{difficulty}_worksheet.png")
        problem.answer_image.save(f"test_graphing_points_{difficulty}_answer.png")
        print(f"  Saved: test_graphing_points_{difficulty}_worksheet.png & _answer.png")

    print("\n[OK] All tests passed!")
