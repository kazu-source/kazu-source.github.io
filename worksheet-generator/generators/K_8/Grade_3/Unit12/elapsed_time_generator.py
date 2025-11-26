"""
Elapsed Time Generator - Grade 3 Unit 12
Generates problems for calculating time intervals
Focuses on finding elapsed time and determining start/end times
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
from equation_generator import Equation


class ElapsedTimeGenerator:
    """Generates elapsed time problems."""

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

    def _format_time(self, hour: int, minute: int, am_pm: str = None) -> str:
        """Format time in 12-hour format."""
        if am_pm:
            return f"{hour}:{minute:02d} {am_pm}"
        return f"{hour}:{minute:02d}"

    def _add_minutes(self, hour: int, minute: int, add_minutes: int) -> tuple:
        """Add minutes to a time and return new hour and minute."""
        total_minutes = hour * 60 + minute + add_minutes
        new_hour = (total_minutes // 60) % 12
        if new_hour == 0:
            new_hour = 12
        new_minute = total_minutes % 60
        return new_hour, new_minute

    def _generate_easy(self) -> Equation:
        """Generate easy problems: elapsed time with simple hour intervals."""
        start_hour = random.randint(1, 11)
        elapsed_hours = random.randint(1, 3)
        end_hour = start_hour + elapsed_hours
        if end_hour > 12:
            end_hour = end_hour - 12

        am_pm = random.choice(['AM', 'PM'])
        start_time = f"{start_hour}:00 {am_pm}"
        end_time = f"{end_hour}:00 {am_pm}"

        contexts = [
            f"\\text{{A movie starts at {start_time} and ends at {end_time}.}}",
            f"\\text{{School begins at {start_time} and lunch is at {end_time}.}}",
            f"\\text{{Practice starts at {start_time} and finishes at {end_time}.}}",
        ]

        context = random.choice(contexts)
        latex = f"{context} \\text{{ How long is that?}}"
        solution = f"{elapsed_hours} hours"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{{end_hour} - {start_hour} = {elapsed_hours} hours}}"],
            difficulty='easy'
        )

    def _generate_medium(self) -> Equation:
        """Generate medium problems: elapsed time with minutes."""
        start_hour = random.randint(1, 12)
        start_minute = random.choice([0, 15, 30, 45])
        elapsed_minutes = random.choice([15, 30, 45, 60, 75, 90])

        am_pm = random.choice(['AM', 'PM'])
        end_hour, end_minute = self._add_minutes(start_hour, start_minute, elapsed_minutes)

        start_time = self._format_time(start_hour, start_minute, am_pm)
        end_time = self._format_time(end_hour, end_minute, am_pm)

        contexts = [
            f"\\text{{Reading time is from {start_time} to {end_time}.}}",
            f"\\text{{The game starts at {start_time} and ends at {end_time}.}}",
            f"\\text{{Math class begins at {start_time} and finishes at {end_time}.}}",
        ]

        context = random.choice(contexts)
        latex = f"{context} \\text{{ How much time elapsed?}}"

        # Format solution
        hours = elapsed_minutes // 60
        minutes = elapsed_minutes % 60
        if hours > 0 and minutes > 0:
            solution = f"{hours} hour {minutes} minutes"
        elif hours > 0:
            solution = f"{hours} hour"
        else:
            solution = f"{minutes} minutes"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Elapsed time: {solution}}}"],
            difficulty='medium'
        )

    def _generate_hard(self) -> Equation:
        """Generate hard problems: finding start or end time given elapsed time."""
        problem_type = random.choice(['find_start', 'find_end'])

        if problem_type == 'find_start':
            end_hour = random.randint(2, 12)
            end_minute = random.randint(0, 59)
            elapsed_minutes = random.randint(30, 120)

            # Calculate start time
            total_end_minutes = end_hour * 60 + end_minute
            total_start_minutes = total_end_minutes - elapsed_minutes
            start_hour = (total_start_minutes // 60) % 12
            if start_hour == 0:
                start_hour = 12
            start_minute = total_start_minutes % 60

            am_pm = random.choice(['AM', 'PM'])
            end_time = self._format_time(end_hour, end_minute, am_pm)
            start_time = self._format_time(start_hour, start_minute, am_pm)

            hours = elapsed_minutes // 60
            minutes = elapsed_minutes % 60
            if hours > 0 and minutes > 0:
                elapsed_str = f"{hours} hour {minutes} minutes"
            elif hours > 0:
                elapsed_str = f"{hours} hour"
            else:
                elapsed_str = f"{minutes} minutes"

            latex = f"\\text{{A soccer game lasted {elapsed_str} and ended at {end_time}. What time did it start?}}"
            solution = start_time

        else:  # find_end
            start_hour = random.randint(1, 11)
            start_minute = random.randint(0, 59)
            elapsed_minutes = random.randint(30, 120)

            end_hour, end_minute = self._add_minutes(start_hour, start_minute, elapsed_minutes)

            am_pm = random.choice(['AM', 'PM'])
            start_time = self._format_time(start_hour, start_minute, am_pm)
            end_time = self._format_time(end_hour, end_minute, am_pm)

            hours = elapsed_minutes // 60
            minutes = elapsed_minutes % 60
            if hours > 0 and minutes > 0:
                elapsed_str = f"{hours} hour {minutes} minutes"
            elif hours > 0:
                elapsed_str = f"{hours} hour"
            else:
                elapsed_str = f"{minutes} minutes"

            latex = f"\\text{{A piano lesson starts at {start_time} and lasts {elapsed_str}. What time does it end?}}"
            solution = end_time

        return Equation(
            latex=latex,
            solution=solution,
            steps=[f"\\text{{Answer: {solution}}}"],
            difficulty='hard'
        )

    def _generate_challenge(self) -> Equation:
        """Generate challenge problems: multi-step time problems."""
        # Problem with multiple activities
        start_hour = random.randint(1, 10)
        start_minute = 0
        am_pm = random.choice(['AM', 'PM'])

        activity1_minutes = random.randint(20, 45)
        activity2_minutes = random.randint(15, 40)
        activity3_minutes = random.randint(10, 30)

        total_minutes = activity1_minutes + activity2_minutes + activity3_minutes
        end_hour, end_minute = self._add_minutes(start_hour, start_minute, total_minutes)

        start_time = self._format_time(start_hour, start_minute, am_pm)
        end_time = self._format_time(end_hour, end_minute, am_pm)

        activities = [
            ['homework', 'reading', 'playing'],
            ['breakfast', 'getting dressed', 'walking to school'],
            ['warm-up', 'practice', 'cool-down']
        ]

        chosen_activities = random.choice(activities)

        latex = (f"\\text{{Sarah started at {start_time}. She spent {activity1_minutes} minutes on {chosen_activities[0]}, "
                f"{activity2_minutes} minutes on {chosen_activities[1]}, and {activity3_minutes} minutes on {chosen_activities[2]}. "
                f"What time did she finish?}}")

        solution = end_time

        total_hours = total_minutes // 60
        remaining_minutes = total_minutes % 60
        if total_hours > 0:
            total_str = f"{total_hours} hour {remaining_minutes} minutes"
        else:
            total_str = f"{remaining_minutes} minutes"

        return Equation(
            latex=latex,
            solution=solution,
            steps=[
                f"\\text{{Total time: {activity1_minutes} + {activity2_minutes} + {activity3_minutes} = {total_minutes} minutes}}",
                f"\\text{{End time: {solution}}}"
            ],
            difficulty='challenge'
        )


def main():
    """Test the generator."""
    generator = ElapsedTimeGenerator()

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
