"""
Generator for One-Step Addition/Subtraction Word Problems.
Creates word problems that require students to set up and solve one-step equations.
"""

import random
from dataclasses import dataclass
from typing import List


@dataclass
class WordProblem:
    """Represents a one-step word problem."""
    problem_text: str  # The word problem
    equation: str  # The equation students should set up (e.g., "x + 5 = 12")
    latex: str  # LaTeX format for display
    solution: int  # The solution value
    operation: str  # "addition" or "subtraction"


class WordProblemsGenerator:
    """Generates one-step addition/subtraction word problems."""

    def __init__(self):
        """Initialize the generator with word problem templates."""
        self.difficulty_ranges = {
            'easy': (1, 20),      # Numbers 1-20
            'medium': (1, 50),    # Numbers 1-50
            'hard': (1, 100)      # Numbers 1-100
        }

        # Addition problem templates: (template, context)
        # {x} = unknown variable, {a} = known addend, {total} = total
        self.addition_templates = [
            ("Maria had {x} apples. She bought {a} more apples. Now she has {total} apples. How many apples did Maria have at first?", "apples"),
            ("A book has {total} pages. John has already read {a} pages. How many pages does he have left to read?", "pages"),
            ("In a parking lot, there are {x} cars. Then {a} more cars arrive. Now there are {total} cars total. How many cars were there at first?", "cars"),
            ("Emma saved ${x}. She earned ${a} more doing chores. Now she has ${total}. How much money did she have at first?", "dollars"),
            ("A basketball team scored {x} points in the first half. They scored {a} points in the second half. They scored {total} points total. How many points did they score in the first half?", "points"),
            ("There are {total} students in class today. {a} students are wearing glasses. How many students are not wearing glasses?", "students"),
            ("A farm has {x} chickens and {a} ducks. There are {total} birds total. How many chickens are there?", "chickens"),
            ("Jake collected {x} baseball cards. His friend gave him {a} more cards. Now he has {total} cards. How many cards did he start with?", "cards"),
            ("A recipe needs {total} cups of flour. You already added {a} cups. How many more cups do you need?", "cups"),
            ("The temperature was {x} degrees in the morning. It rose {a} degrees by afternoon. The afternoon temperature was {total} degrees. What was the morning temperature?", "degrees"),
        ]

        # Subtraction problem templates: (template, context)
        # {x} = unknown variable, {s} = amount subtracted, {result} = result after subtraction
        self.subtraction_templates = [
            ("Carlos had {x} stickers. He gave {s} stickers to his friend. Now he has {result} stickers left. How many stickers did Carlos have at first?", "stickers"),
            ("There were {x} cookies in a jar. Sarah ate {s} cookies. Now there are {result} cookies left. How many cookies were there at first?", "cookies"),
            ("A store had {x} video games. They sold {s} games on Monday. They have {result} games left. How many games did they start with?", "games"),
            ("Lisa had ${x}. She spent ${s} on a book. She has ${result} left. How much money did she have at first?", "dollars"),
            ("A theater had {x} people inside. {s} people left during intermission. There are {result} people still in the theater. How many people were there at first?", "people"),
            ("There were {x} birds on a fence. {s} birds flew away. Now there are {result} birds on the fence. How many birds were there at first?", "birds"),
            ("A library had {x} books checked out. {s} books were returned. Now {result} books are still checked out. How many books were checked out at first?", "books"),
            ("Tom had {x} marbles. He lost {s} marbles at the park. He has {result} marbles now. How many marbles did he have at first?", "marbles"),
            ("A class had {x} students. {s} students were absent today. There are {result} students in class. How many students are in the class total?", "students"),
            ("A garden had {x} flowers. The gardener picked {s} flowers. There are {result} flowers left in the garden. How many flowers were there at first?", "flowers"),
        ]

    def _generate_addition_problem(self, difficulty: str) -> WordProblem:
        """
        Generate an addition word problem.

        Format: x + a = total (or total - a = x for reverse)

        Args:
            difficulty: Difficulty level ('easy', 'medium', 'hard')

        Returns:
            WordProblem object
        """
        min_val, max_val = self.difficulty_ranges.get(difficulty, (1, 20))

        # Generate the unknown and known addend
        x = random.randint(min_val, max_val)
        a = random.randint(min_val, max_val)
        total = x + a

        # Choose a random template
        template, context = random.choice(self.addition_templates)

        # Fill in the template
        problem_text = template.format(x="x", a=a, total=total)

        # Create equation: x + a = total
        equation = f"x + {a} = {total}"
        latex = f"x + {a} = {total}"

        return WordProblem(
            problem_text=problem_text,
            equation=equation,
            latex=latex,
            solution=x,
            operation="addition"
        )

    def _generate_subtraction_problem(self, difficulty: str) -> WordProblem:
        """
        Generate a subtraction word problem.

        Format: x - s = result

        Args:
            difficulty: Difficulty level ('easy', 'medium', 'hard')

        Returns:
            WordProblem object
        """
        min_val, max_val = self.difficulty_ranges.get(difficulty, (1, 20))

        # Generate the unknown and subtracted amount
        # Make sure result is positive
        s = random.randint(1, max_val // 2)  # Amount subtracted (smaller)
        result = random.randint(1, max_val)  # Result after subtraction
        x = s + result  # Original amount

        # Choose a random template
        template, context = random.choice(self.subtraction_templates)

        # Fill in the template
        problem_text = template.format(x="x", s=s, result=result)

        # Create equation: x - s = result
        equation = f"x - {s} = {result}"
        latex = f"x - {s} = {result}"

        return WordProblem(
            problem_text=problem_text,
            equation=equation,
            latex=latex,
            solution=x,
            operation="subtraction"
        )

    def generate_problem(self, difficulty: str = 'medium',
                        operation: str = 'mixed') -> WordProblem:
        """
        Generate a single word problem.

        Args:
            difficulty: 'easy', 'medium', or 'hard'
            operation: 'addition', 'subtraction', or 'mixed'

        Returns:
            WordProblem object
        """
        if operation == 'mixed':
            # Randomly choose between addition and subtraction
            operation = random.choice(['addition', 'subtraction'])

        if operation == 'addition':
            return self._generate_addition_problem(difficulty)
        else:  # subtraction
            return self._generate_subtraction_problem(difficulty)

    def generate_worksheet(self, difficulty: str = 'medium',
                          num_problems: int = 8,
                          operation: str = 'mixed') -> List[WordProblem]:
        """
        Generate a complete worksheet of word problems.

        Args:
            difficulty: 'easy', 'medium', or 'hard'
            num_problems: Number of problems to generate
            operation: 'addition', 'subtraction', or 'mixed'

        Returns:
            List of WordProblem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty, operation)
            problems.append(problem)

        return problems


# Example usage and testing
if __name__ == "__main__":
    generator = WordProblemsGenerator()

    print("=" * 80)
    print("One-Step Addition/Subtraction Word Problems")
    print("=" * 80)
    print()

    # Generate sample problems
    print("EASY Problems (Mixed):")
    problems = generator.generate_worksheet('easy', 5, 'mixed')
    for i, prob in enumerate(problems, 1):
        print(f"\n{i}. {prob.problem_text}")
        print(f"   Equation: {prob.equation}")
        print(f"   Solution: x = {prob.solution}")
        print(f"   Operation: {prob.operation.title()}")

    print("\n" + "=" * 80)
    print("\nMEDIUM Problems (Addition only):")
    problems = generator.generate_worksheet('medium', 3, 'addition')
    for i, prob in enumerate(problems, 1):
        print(f"\n{i}. {prob.problem_text}")
        print(f"   Equation: {prob.equation}")
        print(f"   Solution: x = {prob.solution}")

    print("\n" + "=" * 80)
    print("\nHARD Problems (Subtraction only):")
    problems = generator.generate_worksheet('hard', 3, 'subtraction')
    for i, prob in enumerate(problems, 1):
        print(f"\n{i}. {prob.problem_text}")
        print(f"   Equation: {prob.equation}")
        print(f"   Solution: x = {prob.solution}")
