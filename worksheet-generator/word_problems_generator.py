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
            'hard': (1, 100),     # Numbers 1-100
            'challenge': (1, 200) # Numbers 1-200
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

        # Challenge multi-step problem templates
        # {x} = unknown variable, {a}, {b}, {c} = coefficients/constants
        self.challenge_templates = [
            ("A store had {x} shirts. On Monday, they sold {a} shirts. On Tuesday, they received a shipment of {b} more shirts. Now they have {total} shirts. How many shirts did they start with?", "two-step"),
            ("Maria saves ${x} per month. She already has ${a} in her savings account. After {b} months of saving, she will have ${total}. How much does she save per month?", "two-step"),
            ("A school has {x} students. {a} students joined the school this year, and {b} students left. Now the school has {total} students. How many students were there originally?", "two-step"),
            ("Jake is collecting baseball cards. He started with {x} cards. He bought {a} packs with {b} cards each, then gave {c} cards to his friend. Now he has {total} cards. How many cards did he start with?", "multi-step"),
            ("A farm has chickens and cows. There are {x} chickens. The number of cows is {a} less than the chickens. Together, there are {total} animals. How many chickens are there?", "multi-step"),
            ("Emma is reading a book with {total} pages. She read {a} pages on Saturday and {b} pages on Sunday. She has {result} pages left to read. How many pages are left?", "multi-step"),
            ("A theater sold tickets for a show. Adult tickets cost ${a} each and they sold {x} adult tickets. They also sold {b} child tickets at ${c} each. They made ${total} in total. How many adult tickets did they sell?", "complex"),
            ("A bakery makes cookies. They start with {x} cookies in the morning. They sell {a} cookies in the morning and {b} cookies in the afternoon. Then they bake {c} more cookies. Now they have {total} cookies. How many cookies did they start with?", "complex"),
            ("Tom has {x} dollars. He spent {a} dollars on lunch and {b} dollars on a book. His friend gave him ${c}. Now he has ${total}. How much money did Tom start with?", "multi-step"),
            ("A garden has roses and tulips. There are {x} roses. The number of tulips is {a} times the number of roses. Together there are {total} flowers. How many roses are there?", "multi-step"),
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

    def _generate_challenge_problem(self, difficulty: str) -> WordProblem:
        """
        Generate a multi-step challenge word problem.

        These problems require multiple operations and setting up
        more complex equations.

        Args:
            difficulty: Difficulty level (typically 'challenge')

        Returns:
            WordProblem object
        """
        min_val, max_val = self.difficulty_ranges.get(difficulty, (1, 200))

        # Choose a random template
        template, context_type = random.choice(self.challenge_templates)

        # Generate values based on context type
        if context_type == "two-step":
            # Format: x - a + b = total, so x = total - b + a
            x = random.randint(min_val, max_val)
            a = random.randint(10, min(50, max_val // 2))
            b = random.randint(10, min(50, max_val // 2))
            total = x - a + b

            problem_text = template.format(x="x", a=a, b=b, total=total)
            equation = f"x - {a} + {b} = {total}"
            latex = f"x - {a} + {b} = {total}"

        elif context_type == "multi-step":
            # Format: x + a*b - c = total or similar variations
            x = random.randint(min_val // 2, max_val // 2)
            a = random.randint(2, 10)
            b = random.randint(2, 10)
            c = random.randint(5, min(30, max_val // 4))

            # Randomly choose operation pattern
            if "packs with" in template:
                # x + a*b - c = total
                total = x + a * b - c
                problem_text = template.format(x="x", a=a, b=b, c=c, total=total)
                equation = f"x + {a}*{b} - {c} = {total}"
                latex = f"x + {a} \\times {b} - {c} = {total}"
            elif "times the number" in template:
                # x + a*x = total, so x(1 + a) = total
                total = x + a * x
                problem_text = template.format(x="x", a=a, total=total)
                equation = f"x + {a}x = {total}"
                latex = f"x + {a}x = {total}"
            else:
                # x - a - b = result or similar
                result = x - a - b
                if result < 0:
                    result = abs(result)
                    x = a + b + result
                # Check if template needs 'c' parameter
                if "{c}" in template:
                    c = random.randint(5, 20)
                    problem_text = template.format(x="x", a=a, b=b, c=c, result=result, total=x)
                else:
                    problem_text = template.format(x="x", a=a, b=b, result=result, total=x)
                equation = f"x - {a} - {b} = {result}"
                latex = f"x - {a} - {b} = {result}"

        else:  # complex
            # Format: a*x + b*c = total
            x = random.randint(5, min(50, max_val // 10))
            a = random.randint(5, 20)  # Price or multiplier
            b = random.randint(10, min(50, max_val // 10))
            c = random.randint(2, 15)  # Price or multiplier

            total = a * x + b * c

            problem_text = template.format(x="x", a=a, b=b, c=c, total=total)
            equation = f"{a}x + {b}*{c} = {total}"
            latex = f"{a}x + {b} \\times {c} = {total}"

        return WordProblem(
            problem_text=problem_text,
            equation=equation,
            latex=latex,
            solution=x,
            operation="multi-step"
        )

    def generate_problem(self, difficulty: str = 'medium',
                        operation: str = 'mixed') -> WordProblem:
        """
        Generate a single word problem.

        Args:
            difficulty: 'easy', 'medium', 'hard', or 'challenge'
            operation: 'addition', 'subtraction', or 'mixed'

        Returns:
            WordProblem object
        """
        # For challenge difficulty, use multi-step problems
        if difficulty == 'challenge':
            return self._generate_challenge_problem(difficulty)

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
            difficulty: 'easy', 'medium', 'hard', or 'challenge'
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

    print("\n" + "=" * 80)
    print("\nCHALLENGE Problems (Multi-step real-world scenarios):")
    problems = generator.generate_worksheet('challenge', 3, 'mixed')
    for i, prob in enumerate(problems, 1):
        print(f"\n{i}. {prob.problem_text}")
        print(f"   Equation: {prob.equation}")
        print(f"   Solution: x = {prob.solution}")
        print(f"   Operation: {prob.operation.title()}")
