"""
Telling Time Generator - Grade 3 Unit 12
Generates problems for reading analog and digital clocks
Focuses on time to the nearest minute using 12-hour format with AM/PM
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class TellingTimeGenerator:
    """Generates telling time problems."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Equation]:
        """
        Generate worksheet problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of Equation objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str) -> Equation:
        """Generate a single problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:
            return self._generate_challenge()

    def _format_time(self, hour: int, minute: int, am_pm: str) -> str:
        """Format time in 12-hour format."""
        return f"{hour}:{minute:02d} {am_pm}"

    def _generate_easy(self) -> Equation:
        """Generate easy problems: reading time to the hour or half hour."""
        hour = random.randint(1, 12)
        minute = random.choice([0, 30])  # On the hour or half hour
        am_pm = random.choice(['AM', 'PM'])

        time_str = self._format_time(hour, minute, am_pm)

        # Different question types
        question_type = random.choice(['analog', 'digital'])

        if question_type == 'analog':
            if minute == 0:
                latex = f"\\text{{What time is shown? The hour hand points to {hour} and the minute hand points to 12.}}"
            else:
                latex = f"\\text{{What time is shown? The hour hand is between {hour} and {(hour % 12) + 1}, and the minute hand points to 6.}}"
        else:
            latex = f"\\text{{Write the time shown on the digital clock: {time_str}}}"

        solution = time_str

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Time: {time_str}}}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: reading time to 5-minute intervals."""
        hour = random.randint(1, 12)
        minute = random.choice([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
        am_pm = random.choice(['AM', 'PM'])

        time_str = self._format_time(hour, minute, am_pm)

        # Different question types
        question_type = random.choice(['read', 'convert'])

        if question_type == 'read':
            minute_marker = minute // 5
            latex = f"\\text{{What time is shown? The hour hand is near {hour} and the minute hand points to {minute_marker}.}}"
            solution = time_str
        else:
            # Convert digital to analog description
            latex = f"\\text{{Where should the clock hands be for {time_str}?}}"
            if minute == 0:
                solution = f"Hour hand at {hour}, minute hand at 12"
            else:
                minute_marker = minute // 5
                solution = f"Hour hand near {hour}, minute hand at {minute_marker}"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Time: {time_str}}}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: reading time to the nearest minute."""
        hour = random.randint(1, 12)
        minute = random.randint(0, 59)
        am_pm = random.choice(['AM', 'PM'])

        time_str = self._format_time(hour, minute, am_pm)

        # Word problem contexts
        contexts = [
            f"\\text{{The clock shows that school starts at what time?}}",
            f"\\text{{What time does the clock show for lunch?}}",
            f"\\text{{When does recess begin according to the clock?}}",
            f"\\text{{What time is shown on the classroom clock?}}"
        ]

        context = random.choice(contexts)
        latex = f"{context} \\text{{ (Answer in format HH:MM AM/PM)}}"
        solution = time_str

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Read the hour hand: {hour}}}",
                f"\\text{{Read the minute hand: {minute} minutes}}",
                f"\\text{{Time: {time_str}}}"
            ],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: comparing times or reasoning."""
        hour1 = random.randint(1, 12)
        minute1 = random.randint(0, 59)
        am_pm1 = random.choice(['AM', 'PM'])

        # Generate second time that's different
        hour2 = random.randint(1, 12)
        minute2 = random.randint(0, 59)
        am_pm2 = am_pm1  # Keep same AM/PM for easier comparison

        time1_str = self._format_time(hour1, minute1, am_pm1)
        time2_str = self._format_time(hour2, minute2, am_pm2)

        # Calculate which is later
        minutes1 = hour1 * 60 + minute1
        minutes2 = hour2 * 60 + minute2

        if minutes1 > minutes2:
            later_time = time1_str
        else:
            later_time = time2_str

        # Different challenge types
        challenge_type = random.choice(['compare', 'reasoning'])

        if challenge_type == 'compare':
            latex = f"\\text{{Which time is later: {time1_str} or {time2_str}?}}"
            solution = later_time
            steps = [f"\\text{{Later time: {later_time}}}"]
        else:
            # Reasoning problem
            minutes_diff = abs(minutes1 - minutes2)
            latex = f"\\text{{How many minutes are between {time1_str} and {time2_str}?}}"
            solution = f"{minutes_diff} minutes"
            steps = [f"\\text{{Difference: {minutes_diff} minutes}}"]

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = TellingTimeGenerator()

    print("Easy:")
    for problem in generator.generate_worksheet('easy', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nMedium:")
    for problem in generator.generate_worksheet('medium', 3):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nHard:")
    for problem in generator.generate_worksheet('hard', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")

    print("\nChallenge:")
    for problem in generator.generate_worksheet('challenge', 2):
        print(f"  {problem.latex}")
        print(f"  Solution: {problem.solution}\n")


if __name__ == '__main__':
    main()
