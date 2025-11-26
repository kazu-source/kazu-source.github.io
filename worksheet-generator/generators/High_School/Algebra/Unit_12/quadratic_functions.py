"""
Generator for Quadratic Functions problems.
"""

import random
from generators.base import Problem, BaseGenerator
from typing import List


class QuadraticFunctionsGenerator(BaseGenerator):
    """Generator for quadratic functions problems."""

    def __init__(self):
        """Initialize the generator."""
        super().__init__()

    def generate_worksheet(self, difficulty: str, num_problems: int) -> List[Problem]:
        """
        Generate a worksheet of quadratic functions problems.

        Args:
            difficulty: One of 'easy', 'medium', 'hard', 'challenge'
            num_problems: Number of problems to generate

        Returns:
            List of Problem objects
        """
        problems = []
        for _ in range(num_problems):
            problem = self.generate_problem(difficulty)
            if problem:
                problems.append(problem)
        return problems

    def generate_problem(self, difficulty: str) -> Problem:
        """
        Generate a single quadratic functions problem.

        Args:
            difficulty: Problem difficulty level

        Returns:
            Problem object
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

    def _generate_easy(self) -> Problem:
        """
        Generate an easy quadratic functions problem.
        Identify vertex, axis of symmetry, or direction of opening.
        """
        problem_type = random.choice(['vertex', 'axis', 'direction'])

        # Generate a simple quadratic in vertex form
        h = random.randint(-5, 5)
        k = random.randint(-10, 10)
        a = random.choice([-3, -2, -1, 1, 2, 3])

        # Format the function
        if a == 1:
            func = f"f(x) = (x"
        elif a == -1:
            func = f"f(x) = -(x"
        else:
            func = f"f(x) = {a}(x"

        if h > 0:
            func += f" - {h})²"
        elif h < 0:
            func += f" + {abs(h)})²"
        else:
            func += ")²"

        if k > 0:
            func += f" + {k}"
        elif k < 0:
            func += f" - {abs(k)}"

        if problem_type == 'vertex':
            question = f"Find the vertex of {func}"
            answer = f"({h}, {k})"
        elif problem_type == 'axis':
            question = f"Find the axis of symmetry of {func}"
            answer = f"x = {h}"
        else:  # direction
            question = f"Does {func} open upward or downward?"
            answer = "Upward" if a > 0 else "Downward"

        return Problem(
            problem_type="quadratic_functions",
            question=question,
            answer=answer,
            difficulty=1
        )

    def _generate_medium(self) -> Problem:
        """
        Generate a medium quadratic functions problem.
        Find x-intercepts, y-intercept, or convert forms.
        """
        problem_type = random.choice(['x_intercepts', 'y_intercept', 'convert'])

        if problem_type == 'x_intercepts':
            # Generate factored form
            root1 = random.randint(-8, 8)
            root2 = random.randint(-8, 8)
            a = random.choice([1, -1, 2, -2])

            if a == 1:
                func = f"f(x) = (x"
            else:
                func = f"f(x) = {a}(x"

            if root1 > 0:
                func += f" - {root1})(x"
            elif root1 < 0:
                func += f" + {abs(root1)})(x"
            else:
                func += ")(x"

            if root2 > 0:
                func += f" - {root2})"
            elif root2 < 0:
                func += f" + {abs(root2)})"
            else:
                func += ")"

            question = f"Find the x-intercepts of {func}"
            answer = f"x = {root1} and x = {root2}"

        elif problem_type == 'y_intercept':
            # Generate standard form
            a = random.choice([1, -1, 2, -2, 3, -3])
            b = random.randint(-10, 10)
            c = random.randint(-15, 15)

            func = f"f(x) = "
            if a == 1:
                func += "x²"
            elif a == -1:
                func += "-x²"
            else:
                func += f"{a}x²"

            if b > 0:
                func += f" + {b}x"
            elif b < 0:
                func += f" - {abs(b)}x"

            if c > 0:
                func += f" + {c}"
            elif c < 0:
                func += f" - {abs(c)}"

            question = f"Find the y-intercept of {func}"
            answer = f"(0, {c})"

        else:  # convert
            # Generate vertex form and ask to convert to standard
            h = random.randint(-4, 4)
            k = random.randint(-8, 8)
            a = random.choice([1, -1, 2])

            if a == 1:
                vertex_form = f"f(x) = (x"
            elif a == -1:
                vertex_form = f"f(x) = -(x"
            else:
                vertex_form = f"f(x) = {a}(x"

            if h > 0:
                vertex_form += f" - {h})²"
            elif h < 0:
                vertex_form += f" + {abs(h)})²"
            else:
                vertex_form += ")²"

            if k > 0:
                vertex_form += f" + {k}"
            elif k < 0:
                vertex_form += f" - {abs(k)}"

            # Calculate standard form coefficients
            b = -2 * a * h
            c = a * h * h + k

            standard_form = f"f(x) = "
            if a == 1:
                standard_form += "x²"
            elif a == -1:
                standard_form += "-x²"
            else:
                standard_form += f"{a}x²"

            if b > 0:
                standard_form += f" + {b}x"
            elif b < 0:
                standard_form += f" - {abs(b)}x"

            if c > 0:
                standard_form += f" + {c}"
            elif c < 0:
                standard_form += f" - {abs(c)}"

            question = f"Convert {vertex_form} to standard form"
            answer = standard_form

        return Problem(
            problem_type="quadratic_functions",
            question=question,
            answer=answer,
            difficulty=2
        )

    def _generate_hard(self) -> Problem:
        """
        Generate a hard quadratic functions problem.
        Find maximum/minimum values, domain/range, or transformations.
        """
        problem_type = random.choice(['max_min', 'range', 'transformation'])

        if problem_type == 'max_min':
            # Generate a word problem about maximum/minimum
            a = random.choice([-2, -1, 1, 2])
            h = random.randint(-5, 5)
            k = random.randint(-10, 10)

            if a > 0:
                question = f"Find the minimum value of f(x) = {a}(x - {h})² + {k}"
                answer = f"Minimum value is {k} at x = {h}"
            else:
                question = f"Find the maximum value of f(x) = {a}(x - {h})² + {k}"
                answer = f"Maximum value is {k} at x = {h}"

        elif problem_type == 'range':
            # Find the range of a quadratic function
            a = random.choice([-3, -2, -1, 1, 2, 3])
            h = random.randint(-5, 5)
            k = random.randint(-10, 10)

            if a == 1:
                func = f"f(x) = (x"
            elif a == -1:
                func = f"f(x) = -(x"
            else:
                func = f"f(x) = {a}(x"

            if h > 0:
                func += f" - {h})²"
            elif h < 0:
                func += f" + {abs(h)})²"
            else:
                func += ")²"

            if k > 0:
                func += f" + {k}"
            elif k < 0:
                func += f" - {abs(k)}"

            question = f"Find the range of {func}"
            if a > 0:
                answer = f"[{k}, ∞)"
            else:
                answer = f"(-∞, {k}]"

        else:  # transformation
            # Describe transformation from parent function
            h = random.randint(-5, 5)
            k = random.randint(-10, 10)
            a = random.choice([-3, -2, -0.5, 0.5, 2, 3])

            if a == 1:
                func = f"f(x) = (x"
            elif a == -1:
                func = f"f(x) = -(x"
            else:
                func = f"f(x) = {a}(x"

            if h > 0:
                func += f" - {h})²"
            elif h < 0:
                func += f" + {abs(h)})²"
            else:
                func += ")²"

            if k > 0:
                func += f" + {k}"
            elif k < 0:
                func += f" - {abs(k)}"

            question = f"Describe the transformations of {func} from y = x²"

            transformations = []
            if abs(a) != 1:
                if abs(a) > 1:
                    transformations.append(f"Vertical stretch by factor {abs(a)}")
                else:
                    transformations.append(f"Vertical compression by factor {abs(a)}")
            if a < 0:
                transformations.append("Reflection over x-axis")
            if h != 0:
                if h > 0:
                    transformations.append(f"Shift right {h} units")
                else:
                    transformations.append(f"Shift left {abs(h)} units")
            if k != 0:
                if k > 0:
                    transformations.append(f"Shift up {k} units")
                else:
                    transformations.append(f"Shift down {abs(k)} units")

            answer = ", ".join(transformations)

        return Problem(
            problem_type="quadratic_functions",
            question=question,
            answer=answer,
            difficulty=3
        )

    def _generate_challenge(self) -> Problem:
        """
        Generate a challenge quadratic functions problem.
        Complex word problems or multiple functions.
        """
        problem_type = random.choice(['word_problem', 'composite', 'system'])

        if problem_type == 'word_problem':
            # Projectile motion problem
            v0 = random.choice([20, 30, 40, 50, 60])  # initial velocity
            h0 = random.choice([0, 10, 20, 30])  # initial height

            question = f"A ball is thrown upward with initial velocity {v0} ft/s from a height of {h0} ft. "
            question += f"The height function is h(t) = -16t² + {v0}t + {h0}. "
            question += "When does the ball hit the ground?"

            # Solve -16t² + v0*t + h0 = 0
            import math
            discriminant = v0**2 + 64*h0
            t = (v0 + math.sqrt(discriminant)) / 32
            answer = f"t = {t:.2f} seconds"

        elif problem_type == 'composite':
            # Find composite of functions
            # f(x) = ax² + b, g(x) = cx + d
            a = random.choice([1, 2, -1])
            b = random.randint(-5, 5)
            c = random.choice([1, 2, 3])
            d = random.randint(-5, 5)

            f_func = f"f(x) = {a}x²" if a != 1 else "f(x) = x²"
            if b > 0:
                f_func += f" + {b}"
            elif b < 0:
                f_func += f" - {abs(b)}"

            g_func = f"g(x) = {c}x" if c != 1 else "g(x) = x"
            if d > 0:
                g_func += f" + {d}"
            elif d < 0:
                g_func += f" - {abs(d)}"

            question = f"Given {f_func} and {g_func}, find f(g(x))"

            # Calculate f(g(x)) = a(cx + d)² + b
            # = ac²x² + 2acdx + ad² + b
            coef_x2 = a * c * c
            coef_x = 2 * a * c * d
            const = a * d * d + b

            answer = f"f(g(x)) = {coef_x2}x²"
            if coef_x > 0:
                answer += f" + {coef_x}x"
            elif coef_x < 0:
                answer += f" - {abs(coef_x)}x"
            if const > 0:
                answer += f" + {const}"
            elif const < 0:
                answer += f" - {abs(const)}"

        else:  # system
            # System with quadratic and linear
            # y = x² + bx + c
            # y = mx + n
            b = random.randint(-4, 4)
            c = random.randint(-5, 5)
            m = random.randint(-3, 3)
            n = random.randint(-5, 5)

            quad = f"y = x²"
            if b > 0:
                quad += f" + {b}x"
            elif b < 0:
                quad += f" - {abs(b)}x"
            if c > 0:
                quad += f" + {c}"
            elif c < 0:
                quad += f" - {abs(c)}"

            linear = f"y = {m}x" if m != 1 else "y = x"
            if n > 0:
                linear += f" + {n}"
            elif n < 0:
                linear += f" - {abs(n)}"

            question = f"Find the intersection points of {quad} and {linear}"

            # Solve x² + bx + c = mx + n
            # x² + (b-m)x + (c-n) = 0
            a_coef = 1
            b_coef = b - m
            c_coef = c - n

            discriminant = b_coef**2 - 4*c_coef

            if discriminant > 0:
                import math
                x1 = (-b_coef + math.sqrt(discriminant)) / 2
                x2 = (-b_coef - math.sqrt(discriminant)) / 2
                y1 = m * x1 + n
                y2 = m * x2 + n
                answer = f"({x1:.2f}, {y1:.2f}) and ({x2:.2f}, {y2:.2f})"
            elif discriminant == 0:
                x = -b_coef / 2
                y = m * x + n
                answer = f"({x}, {y})"
            else:
                answer = "No intersection points"

        return Problem(
            problem_type="quadratic_functions",
            question=question,
            answer=answer,
            difficulty=4
        )