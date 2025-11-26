"""
Inequality Word Problems Generator - Real-world inequality applications
Generates word problems that require setting up and solving inequalities
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class InequalityWordProblemsGenerator:
    """Generates inequality word problems."""

    def __init__(self, seed=None):
        """Initialize the inequality word problems generator."""
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
        """Generate a single inequality word problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate simple inequality word problem"""
        templates = [
            {
                'problem': "Sarah has ${budget}. Each book costs ${cost}. What is the maximum number of books she can buy?",
                'setup': lambda: {
                    'budget': random.randint(20, 50),
                    'cost': random.randint(3, 8)
                },
                'inequality': lambda v: f"{v['cost']}x \\leq {v['budget']}",
                'solution': lambda v: f"x \\leq {v['budget'] // v['cost']}"
            },
            {
                'problem': "A parking garage charges ${fee} per hour. If you have ${money}, how many hours can you park?",
                'setup': lambda: {
                    'fee': random.randint(3, 6),
                    'money': random.randint(15, 30)
                },
                'inequality': lambda v: f"{v['fee']}x \\leq {v['money']}",
                'solution': lambda v: f"x \\leq {v['money'] // v['fee']}"
            },
            {
                'problem': "To pass the class, you need at least {min_score} points. You have {current} points. How many more points do you need?",
                'setup': lambda: {
                    'min_score': random.randint(70, 90),
                    'current': random.randint(50, 65)
                },
                'inequality': lambda v: f"{v['current']} + x \\geq {v['min_score']}",
                'solution': lambda v: f"x \\geq {v['min_score'] - v['current']}"
            }
        ]

        template = random.choice(templates)
        values = template['setup']()
        problem_text = template['problem'].format(**values)

        latex = f"\\text{{{problem_text}}}"
        solution = template['solution'](values)

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate two-step inequality word problem"""
        templates = [
            {
                'problem': "A phone plan costs ${base} per month plus ${per_gb} per GB. You can spend at most ${budget}. How many GB can you use?",
                'setup': lambda: {
                    'base': random.randint(20, 40),
                    'per_gb': random.randint(5, 10),
                    'budget': random.randint(60, 100)
                },
                'inequality': lambda v: f"{v['base']} + {v['per_gb']}x \\leq {v['budget']}",
                'solution': lambda v: f"x \\leq {(v['budget'] - v['base']) // v['per_gb']}"
            },
            {
                'problem': "A taxi charges ${base} plus ${per_mile} per mile. You have ${money}. What's the maximum distance you can travel?",
                'setup': lambda: {
                    'base': random.randint(3, 5),
                    'per_mile': random.randint(2, 4),
                    'money': random.randint(20, 40)
                },
                'inequality': lambda v: f"{v['base']} + {v['per_mile']}x \\leq {v['money']}",
                'solution': lambda v: f"x \\leq {(v['money'] - v['base']) / v['per_mile']:.1f}"
            },
            {
                'problem': "You need at least {min_points} points. Each test is worth {test_points} points. You have {current} points from {num_tests} tests. How many more tests to pass?",
                'setup': lambda: {
                    'min_points': random.randint(200, 300),
                    'test_points': random.randint(25, 50),
                    'current': random.randint(100, 150),
                    'num_tests': random.randint(3, 5)
                },
                'inequality': lambda v: f"{v['current']} + {v['test_points']}x \\geq {v['min_points']}",
                'solution': lambda v: f"x \\geq {(v['min_points'] - v['current']) / v['test_points']:.0f}"
            }
        ]

        template = random.choice(templates)
        values = template['setup']()
        problem_text = template['problem'].format(**values)

        latex = f"\\text{{{problem_text[:60]}}}\\\\ \\text{{{problem_text[60:]}}}" if len(problem_text) > 60 else f"\\text{{{problem_text}}}"
        solution = template['solution'](values)

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate complex inequality word problem"""
        templates = [
            {
                'problem': "A company makes ${profit} profit per item after ${fixed} in fixed costs. How many items for at least ${target} profit?",
                'setup': lambda: {
                    'profit': random.randint(8, 15),
                    'fixed': random.randint(200, 500),
                    'target': random.randint(1000, 2000)
                },
                'inequality': lambda v: f"{v['profit']}x - {v['fixed']} \\geq {v['target']}",
                'solution': lambda v: f"x \\geq {(v['target'] + v['fixed']) / v['profit']:.0f}"
            },
            {
                'problem': "Theater tickets: ${adult} for adults, ${child} for children. At least {min_people} people, budget ${budget}. Max adults if {children} children attend?",
                'setup': lambda: {
                    'adult': random.randint(12, 20),
                    'child': random.randint(6, 10),
                    'min_people': random.randint(10, 20),
                    'budget': random.randint(150, 250),
                    'children': random.randint(3, 7)
                },
                'inequality': lambda v: f"{v['adult']}x + {v['child'] * v['children']} \\leq {v['budget']}",
                'solution': lambda v: f"x \\leq {(v['budget'] - v['child'] * v['children']) // v['adult']}"
            }
        ]

        template = random.choice(templates)
        values = template['setup']()
        problem_text = template['problem'].format(**values)

        latex = f"\\text{{{problem_text[:50]}}}\\\\ \\text{{{problem_text[50:]}}}" if len(problem_text) > 50 else f"\\text{{{problem_text}}}"
        solution = template['solution'](values)

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate multi-constraint inequality word problem"""
        templates = [
            {
                'problem': "Concert venue: capacity {capacity}, tickets ${price} each, costs ${fixed} + ${per} per person. Min tickets for profit?",
                'setup': lambda: {
                    'capacity': random.randint(200, 500),
                    'price': random.randint(20, 40),
                    'fixed': random.randint(1000, 2000),
                    'per': random.randint(5, 10)
                },
                'inequality': lambda v: f"{v['price']}x - ({v['fixed']} + {v['per']}x) > 0",
                'solution': lambda v: f"x > {v['fixed'] / (v['price'] - v['per']):.0f}"
            },
            {
                'problem': "Fundraiser: sell items at ${price}, buy at ${cost}, goal ${goal}, max {max_items} items. Required sales range?",
                'setup': lambda: {
                    'price': random.randint(15, 25),
                    'cost': random.randint(8, 12),
                    'goal': random.randint(500, 1000),
                    'max_items': random.randint(100, 150)
                },
                'inequality': lambda v: f"{v['goal'] / (v['price'] - v['cost']):.0f} \\leq x \\leq {v['max_items']}",
                'solution': lambda v: f"{v['goal'] // (v['price'] - v['cost'])} \\leq x \\leq {v['max_items']}"
            }
        ]

        template = random.choice(templates)
        values = template['setup']()
        problem_text = template['problem'].format(**values)

        latex = f"\\text{{{problem_text[:45]}}}\\\\ \\text{{{problem_text[45:]}}}" if len(problem_text) > 45 else f"\\text{{{problem_text}}}"
        solution = template['solution'](values)

        return Equation(latex=latex, solution=solution, steps=[solution], difficulty='challenge')


if __name__ == "__main__":
    # Test the generator
    gen = InequalityWordProblemsGenerator()

    print("Testing Inequality Word Problems Generator")
    print("=" * 60)

    for difficulty in ['easy', 'medium', 'hard', 'challenge']:
        print(f"\n{difficulty.upper()} Problems:")
        print("-" * 60)
        problems = gen.generate_worksheet(difficulty=difficulty, num_problems=3)
        for i, problem in enumerate(problems, 1):
            print(f"{i}. {problem.latex}")
            print(f"   Solution: {problem.solution}\n")