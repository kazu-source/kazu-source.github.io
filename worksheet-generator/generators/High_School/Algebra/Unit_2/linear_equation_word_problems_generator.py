"""
Linear Equation Word Problems Generator
Generates word problems that require solving linear equations
"""

import random
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from equation_generator import Equation


class LinearEquationWordProblemsGenerator:
    """Generates linear equation word problems."""

    def __init__(self, seed=None):
        """Initialize the linear equation word problems generator."""
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
        """Generate a single word problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self) -> Equation:
        """Generate simple word problems with direct relationships"""
        problem_types = ['age', 'money', 'collection', 'total_cost']
        problem_type = random.choice(problem_types)

        if problem_type == 'age':
            x = random.randint(8, 15)
            years = random.randint(3, 8)
            future_age = x + years

            latex = f"\\text{{Sarah is }} x \\text{{ years old. In }} {years} \\text{{ years, she will be }} {future_age}. \\text{{ How old is Sarah now?}}"
            solution = x
            steps = [f"x + {years} = {future_age}", f"x = {x}"]

        elif problem_type == 'money':
            x = random.randint(10, 50)
            spent = random.randint(5, min(x - 2, 25))
            remaining = x - spent

            latex = f"\\text{{Maria had }} \\${x}. \\text{{ She spent }} \\${spent}. \\text{{ How much does she have left?}}"
            solution = remaining
            steps = [f"{x} - {spent} = x", f"x = {remaining}"]

        elif problem_type == 'collection':
            x = random.randint(15, 50)
            bought = random.randint(5, 20)
            total = x + bought

            latex = f"\\text{{Tom had }} {x} \\text{{ cards. He bought }} {bought} \\text{{ more. How many cards does he have now?}}"
            solution = total
            steps = [f"{x} + {bought} = x", f"x = {total}"]

        else:  # total_cost
            price = random.randint(3, 15)
            quantity = random.randint(3, 8)
            total = price * quantity

            latex = f"\\text{{Each book costs }} \\${price}. \\text{{ If you buy }} {quantity} \\text{{ books, what is the total cost?}}"
            solution = total
            steps = [f"{price} \\times {quantity} = x", f"x = {total}"]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='easy')

    def _generate_medium(self) -> Equation:
        """Generate word problems requiring equation setup"""
        problem_types = ['consecutive_numbers', 'perimeter', 'shared_items', 'two_step']
        problem_type = random.choice(problem_types)

        if problem_type == 'consecutive_numbers':
            x = random.randint(10, 30)
            total = x + (x + 1)

            latex = f"\\text{{Two consecutive numbers add up to }} {total}. \\text{{ What are the numbers?}}"
            solution = x
            steps = [
                f"\\text{{Let first number be }} x",
                f"x + (x + 1) = {total}",
                f"2x + 1 = {total}",
                f"x = {x}, \\text{{ second number is }} {x + 1}"
            ]

        elif problem_type == 'perimeter':
            width = random.randint(5, 15)
            length = random.randint(width + 3, 25)
            perimeter = 2 * (length + width)

            latex = f"\\text{{A rectangle has a width of }} {width} \\text{{ cm and perimeter of }} {perimeter} \\text{{ cm. Find the length.}}"
            solution = length
            steps = [
                f"2({width} + l) = {perimeter}",
                f"{2 * width} + 2l = {perimeter}",
                f"2l = {perimeter - 2 * width}",
                f"l = {length}"
            ]

        elif problem_type == 'shared_items':
            per_person = random.randint(3, 8)
            people = random.randint(4, 10)
            total = per_person * people

            latex = f"\\text{{If }} {total} \\text{{ candies are shared equally among }} {people} \\text{{ people, how many does each person get?}}"
            solution = per_person
            steps = [
                f"\\text{{Let }} x \\text{{ be candies per person}}",
                f"{people}x = {total}",
                f"x = {per_person}"
            ]

        else:  # two_step
            x = random.randint(10, 40)
            multiplier = random.randint(2, 5)
            added = random.randint(5, 15)
            result = multiplier * x + added

            latex = f"\\text{{A number is multiplied by }} {multiplier} \\text{{ and }} {added} \\text{{ is added. The result is }} {result}. \\text{{ What is the number?}}"
            solution = x
            steps = [
                f"\\text{{Let the number be }} x",
                f"{multiplier}x + {added} = {result}",
                f"{multiplier}x = {result - added}",
                f"x = {x}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='medium')

    def _generate_hard(self) -> Equation:
        """Generate complex word problems with multiple variables or constraints"""
        problem_types = ['age_relation', 'money_split', 'work_rate', 'mixture']
        problem_type = random.choice(problem_types)

        if problem_type == 'age_relation':
            current_age = random.randint(10, 25)
            years_ago = random.randint(3, 8)
            past_age = current_age - years_ago
            relation_mult = random.randint(2, 4)
            parent_past_age = relation_mult * past_age

            latex = f"\\text{{{years_ago} years ago, a mother was }} {relation_mult} \\text{{ times as old as her daughter.}}"
            latex += f"\\text{{ The daughter is now }} {current_age}. \\text{{ How old is the mother now?}}"
            solution = parent_past_age + years_ago
            steps = [
                f"\\text{{Daughter's age {years_ago} years ago: }} {past_age}",
                f"\\text{{Mother's age then: }} {relation_mult} \\times {past_age} = {parent_past_age}",
                f"\\text{{Mother's age now: }} {parent_past_age} + {years_ago} = {solution}"
            ]

        elif problem_type == 'money_split':
            total = random.randint(50, 150)
            ratio_a = random.randint(2, 4)
            ratio_b = random.randint(2, 4)
            unit = total // (ratio_a + ratio_b)
            amount_a = ratio_a * unit

            latex = f"\\text{{Two people split }} \\${total} \\text{{ in the ratio }} {ratio_a}:{ratio_b}. \\text{{ How much does the first person get?}}"
            solution = amount_a
            steps = [
                f"\\text{{Total parts: }} {ratio_a} + {ratio_b} = {ratio_a + ratio_b}",
                f"\\text{{Each part: }} \\${total} \\div {ratio_a + ratio_b} = \\${unit}",
                f"\\text{{First person: }} {ratio_a} \\times \\${unit} = \\${amount_a}"
            ]

        elif problem_type == 'work_rate':
            hours = random.randint(4, 12)
            pages_per_hour = random.randint(8, 20)
            total_pages = hours * pages_per_hour

            latex = f"\\text{{A printer prints }} {pages_per_hour} \\text{{ pages per hour. How many hours to print }} {total_pages} \\text{{ pages?}}"
            solution = hours
            steps = [
                f"\\text{{Let }} h \\text{{ be hours needed}}",
                f"{pages_per_hour}h = {total_pages}",
                f"h = {hours}"
            ]

        else:  # mixture
            total_students = random.randint(30, 60)
            boys = random.randint(15, total_students - 5)
            girls = total_students - boys

            latex = f"\\text{{A class has }} {total_students} \\text{{ students. If there are }} {boys} \\text{{ boys, how many girls are there?}}"
            solution = girls
            steps = [
                f"\\text{{Let }} g \\text{{ be number of girls}}",
                f"{boys} + g = {total_students}",
                f"g = {girls}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='hard')

    def _generate_challenge(self) -> Equation:
        """Generate very complex word problems with multiple steps"""
        problem_types = ['investment', 'speed_distance', 'percent_change', 'multi_step']
        problem_type = random.choice(problem_types)

        if problem_type == 'investment':
            principal = random.randint(1000, 5000)
            rate = random.randint(3, 8)
            years = random.randint(2, 5)
            interest = (principal * rate * years) // 100
            total = principal + interest

            latex = f"\\text{{An investment of }} \\${principal} \\text{{ earns }} {rate}\\% \\text{{ simple interest per year.}}"
            latex += f"\\text{{ What is the total after }} {years} \\text{{ years?}}"
            solution = total
            steps = [
                f"\\text{{Interest: }} \\${principal} \\times {rate}\\% \\times {years}",
                f"\\text{{Interest: }} \\${interest}",
                f"\\text{{Total: }} \\${principal} + \\${interest} = \\${total}"
            ]

        elif problem_type == 'speed_distance':
            speed = random.randint(40, 80)
            time = random.randint(2, 6)
            distance = speed * time

            latex = f"\\text{{A car travels at }} {speed} \\text{{ mph for }} {time} \\text{{ hours. How far does it travel?}}"
            solution = distance
            steps = [
                f"\\text{{Distance = Speed }} \\times \\text{{ Time}}",
                f"d = {speed} \\times {time}",
                f"d = {distance} \\text{{ miles}}"
            ]

        elif problem_type == 'percent_change':
            original = random.randint(100, 500)
            percent = random.randint(10, 40)
            increase = (original * percent) // 100
            new_value = original + increase

            latex = f"\\text{{A price of }} \\${original} \\text{{ increases by }} {percent}\\%. \\text{{ What is the new price?}}"
            solution = new_value
            steps = [
                f"\\text{{Increase: }} \\${original} \\times {percent}\\% = \\${increase}",
                f"\\text{{New price: }} \\${original} + \\${increase} = \\${new_value}"
            ]

        else:  # multi_step
            # Complex scenario: buying multiple items with discount
            item_price = random.randint(15, 40)
            quantity = random.randint(3, 6)
            discount_per_item = random.randint(2, 8)
            final_price = (item_price - discount_per_item) * quantity

            latex = f"\\text{{Items cost }} \\${item_price} \\text{{ each. With a }} \\${discount_per_item} \\text{{ discount per item,}}"
            latex += f"\\text{{ what is the total cost for }} {quantity} \\text{{ items?}}"
            solution = final_price
            steps = [
                f"\\text{{Discounted price: }} \\${item_price} - \\${discount_per_item} = \\${item_price - discount_per_item}",
                f"\\text{{Total: }} \\${item_price - discount_per_item} \\times {quantity} = \\${final_price}"
            ]

        return Equation(latex=latex, solution=solution, steps=steps, difficulty='challenge')

