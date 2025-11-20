"""
Batch creation script for all 82 new worksheet generators.
Creates generators for topics not already implemented.
"""

import os
import json
import sys

# Generator templates for different topic types
BASIC_GENERATOR_TEMPLATE = '''"""
{topic} Generator
Unit {unit}
"""

import random
from equation_generator import Equation

class {class_name}Generator:
    """Generates problems for {topic}."""

    def __init__(self, seed=None):
        """Initialize the generator."""
        if seed:
            random.seed(seed)

    def generate_worksheet(self, difficulty: str, num_problems: int):
        """Generate worksheet problems."""
        problems = []
        for _ in range(num_problems):
            problem = self._generate_problem(difficulty)
            problems.append(problem)
        return problems

    def _generate_problem(self, difficulty: str):
        """Generate a single problem."""
        if difficulty == 'easy':
            return self._generate_easy()
        elif difficulty == 'medium':
            return self._generate_medium()
        elif difficulty == 'hard':
            return self._generate_hard()
        else:  # challenge
            return self._generate_challenge()

    def _generate_easy(self):
        """Generate an easy problem."""
        {easy_logic}

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='easy'
        )

    def _generate_medium(self):
        """Generate a medium problem."""
        {medium_logic}

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='medium'
        )

    def _generate_hard(self):
        """Generate a hard problem."""
        {hard_logic}

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='hard'
        )

    def _generate_challenge(self):
        """Generate a challenge problem."""
        {challenge_logic}

        return Equation(
            latex=latex,
            solution=solution,
            steps=steps,
            difficulty='challenge'
        )
'''

def sanitize_class_name(topic):
    """Convert topic name to valid Python class name."""
    # Remove parentheses and special characters
    clean = topic.replace('(', '').replace(')', '').replace('-', ' ').replace(',', '')
    # Convert to PascalCase
    words = clean.split()
    return ''.join(word.capitalize() for word in words)

def create_generator_logic(topic, difficulty):
    """Create problem generation logic based on topic type."""
    topic_lower = topic.lower()

    # Default simple logic that can be customized per topic
    if 'word problem' in topic_lower:
        if difficulty == 'easy':
            return '''# Word problem
        scenarios = [
            ("apples", "bought", "ate"),
            ("books", "had", "gave away"),
            ("coins", "collected", "spent")
        ]
        item, action1, action2 = random.choice(scenarios)
        a = random.randint(5, 20)
        b = random.randint(1, a-1)

        latex = f"\\\\text{{A person {action1} {a} {item} and {action2} {b}. How many are left?}}"
        solution = a - b
        steps = [f"{a} - {b} = {solution}"]'''
        else:
            return '''# More complex word problem
        a = random.randint(10, 50)
        b = random.randint(5, 20)
        c = random.randint(2, 10)

        latex = f"\\\\text{{Complex problem with values {a}, {b}, and {c}}}"
        solution = (a + b) * c
        steps = [f"({a} + {b}) × {c} = {solution}"]'''

    elif 'inequalit' in topic_lower:
        if difficulty == 'easy':
            return '''# Inequality problem
        a = random.randint(1, 10)
        b = random.randint(-10, 10)

        latex = f"{a}x > {b}"
        solution = b / a
        steps = [f"x > {solution:.2f}"]'''
        else:
            return '''# Complex inequality
        a = random.randint(2, 10)
        b = random.randint(-20, 20)
        c = random.randint(-10, 10)

        latex = f"{a}x + {b} \\\\leq {c}"
        solution = (c - b) / a
        steps = [f"x \\\\leq {solution:.2f}"]'''

    elif 'function' in topic_lower:
        if difficulty == 'easy':
            return '''# Function evaluation
        m = random.randint(1, 5)
        b = random.randint(-10, 10)
        x = random.randint(-5, 5)

        latex = f"f(x) = {m}x + {b}, \\\\text{{ find }} f({x})"
        solution = m * x + b
        steps = [f"f({x}) = {m}({x}) + {b} = {solution}"]'''
        else:
            return '''# Complex function
        a = random.randint(1, 3)
        b = random.randint(-5, 5)
        c = random.randint(-10, 10)
        x = random.randint(-3, 3)

        latex = f"f(x) = {a}x^2 + {b}x + {c}, \\\\text{{ find }} f({x})"
        solution = a * x**2 + b * x + c
        steps = [f"f({x}) = {solution}"]'''

    elif 'polynomial' in topic_lower or 'factor' in topic_lower:
        if difficulty == 'easy':
            return '''# Polynomial problem
        a = random.randint(1, 5)
        b = random.randint(1, 5)

        latex = f"x^2 + {a+b}x + {a*b}"
        solution = f"(x + {a})(x + {b})"
        steps = [f"Factor: {solution}"]'''
        else:
            return '''# Complex polynomial
        a = random.randint(2, 5)
        b = random.randint(-5, 5)
        c = random.randint(-10, 10)

        latex = f"{a}x^2 + {b}x + {c}"
        solution = "Factored form"
        steps = ["Factor the polynomial"]'''

    elif 'quadratic' in topic_lower:
        if difficulty == 'easy':
            return '''# Quadratic equation
        a = random.randint(1, 3)

        latex = f"x^2 = {a**2}"
        solution = f"x = ±{a}"
        steps = [f"x = {a} or x = -{a}"]'''
        else:
            return '''# Complex quadratic
        a = random.randint(1, 3)
        b = random.randint(-5, 5)
        c = random.randint(-10, 10)

        latex = f"{a}x^2 + {b}x + {c} = 0"
        # Use quadratic formula
        discriminant = b**2 - 4*a*c
        solution = f"Use quadratic formula"
        steps = ["Apply quadratic formula"]'''

    elif 'exponent' in topic_lower:
        if difficulty == 'easy':
            return '''# Exponent problem
        base = random.randint(2, 5)
        exp = random.randint(2, 4)

        latex = f"{base}^{{{exp}}}"
        solution = base ** exp
        steps = [f"{base}^{{{exp}}} = {solution}"]'''
        else:
            return '''# Complex exponent
        a = random.randint(2, 5)
        b = random.randint(2, 4)
        c = random.randint(1, 3)

        latex = f"({a}^{{{b}}})^{{{c}}}"
        solution = a ** (b * c)
        steps = [f"= {a}^{{{b*c}}} = {solution}"]'''

    elif 'system' in topic_lower:
        if difficulty == 'easy':
            return '''# System of equations
        a = random.randint(1, 3)
        b = random.randint(-5, 5)
        c = random.randint(-5, 5)

        latex = f"\\\\begin{{cases}} y = {a}x + {b} \\\\\\\\ y = {c} \\\\end{{cases}}"
        x_sol = (c - b) / a
        solution = f"({x_sol:.1f}, {c})"
        steps = [f"x = {x_sol:.1f}, y = {c}"]'''
        else:
            return '''# Complex system
        a1, b1, c1 = random.randint(1, 3), random.randint(-5, 5), random.randint(-10, 10)
        a2, b2, c2 = random.randint(1, 3), random.randint(-5, 5), random.randint(-10, 10)

        latex = f"\\\\begin{{cases}} {a1}x + {b1}y = {c1} \\\\\\\\ {a2}x + {b2}y = {c2} \\\\end{{cases}}"
        solution = "Solve system"
        steps = ["Use substitution or elimination"]'''

    elif 'slope' in topic_lower or 'intercept' in topic_lower:
        if difficulty == 'easy':
            return '''# Slope problem
        m = random.randint(-5, 5)
        b = random.randint(-10, 10)

        latex = f"y = {m}x + {b}"
        solution = f"slope = {m}, y-intercept = {b}"
        steps = [f"m = {m}, b = {b}"]'''
        else:
            return '''# Find equation from points
        x1, y1 = random.randint(-5, 5), random.randint(-10, 10)
        x2, y2 = random.randint(-5, 5), random.randint(-10, 10)
        if x2 == x1:
            x2 += 1

        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1

        latex = f"\\\\text{{Find equation through }}({x1}, {y1})\\\\text{{ and }}({x2}, {y2})"
        solution = f"y = {m:.1f}x + {b:.1f}"
        steps = [f"slope = {m:.1f}", f"y = {m:.1f}x + {b:.1f}"]'''

    else:
        # Default algebraic problem
        if difficulty == 'easy':
            return '''# Basic algebraic problem
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(['+', '-', '×'])

        if op == '+':
            latex = f"{a} + {b}"
            solution = a + b
        elif op == '-':
            latex = f"{a} - {b}"
            solution = a - b
        else:
            latex = f"{a} \\\\times {b}"
            solution = a * b

        steps = [f"= {solution}"]'''
        else:
            return '''# Complex problem
        a = random.randint(2, 10)
        b = random.randint(-20, 20)
        c = random.randint(-10, 10)

        latex = f"{a}x + {b} = {c}"
        solution = (c - b) / a
        steps = [f"x = {solution:.2f}"]'''

def create_generator_file(topic_data, output_dir):
    """Create a single generator file."""
    topic = topic_data['topic']
    unit = topic_data['unit']

    class_name = sanitize_class_name(topic)

    # Generate logic for each difficulty
    easy_logic = create_generator_logic(topic, 'easy')
    medium_logic = create_generator_logic(topic, 'medium')
    hard_logic = create_generator_logic(topic, 'hard')
    challenge_logic = create_generator_logic(topic, 'challenge')

    # Fill template
    generator_code = BASIC_GENERATOR_TEMPLATE.format(
        topic=topic,
        unit=unit,
        class_name=class_name,
        easy_logic=easy_logic,
        medium_logic=medium_logic,
        hard_logic=hard_logic,
        challenge_logic=challenge_logic
    )

    # Create filename
    filename = topic.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_').replace(',', '')
    filename = filename.replace('/', '_').replace('?', '').replace('__', '_')
    filepath = os.path.join(output_dir, f"{filename}_generator.py")

    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(generator_code)

    return class_name, filename

def main():
    """Create all new generators."""
    # Load generator mapping
    with open('opus_worksheet_generators/generator_mapping.json', 'r') as f:
        mapping = json.load(f)

    need_new = mapping['need_new_generators']

    print(f"Creating {len(need_new)} new generators...")

    # Create generators
    created = []
    for i, topic_data in enumerate(need_new, 1):
        try:
            class_name, filename = create_generator_file(topic_data, 'opus_worksheet_generators')
            created.append({
                'topic': topic_data['topic'],
                'unit': topic_data['unit'],
                'class_name': class_name,
                'filename': filename
            })

            if i % 10 == 0:
                print(f"  Created {i}/{len(need_new)} generators...")
        except Exception as e:
            print(f"  Error creating generator for {topic_data['topic']}: {e}")

    # Save created list
    with open('opus_worksheet_generators/created_generators.json', 'w') as f:
        json.dump(created, f, indent=2)

    print(f"\nSuccessfully created {len(created)} generators!")
    print(f"Generator list saved to opus_worksheet_generators/created_generators.json")

    return created

if __name__ == "__main__":
    main()