"""Replacement functions for solutions_generator hard and challenge"""

# Hard function replacement
hard_func = '''    def _generate_hard(self) -> Equation:
        """Generate hard equations - mix of one solution, no solution, and infinite solutions."""
        problem_type = random.choice(['one_solution', 'no_solution', 'infinite'])

        if problem_type == 'one_solution':
            # Variables on both sides with one solution
            left_coef = random.randint(4, 9)
            right_coef = random.randint(2, left_coef - 1)
            const1 = random.randint(2, 12)
            const2 = random.randint(5, 20)

            latex = f"{left_coef}x + {const1} = {right_coef}x + {const2}"
            solution = 1  # One solution

        elif problem_type == 'no_solution':
            # Same coefficients, different constants = no solution
            coef = random.randint(2, 6)
            const1 = random.randint(5, 15)
            const2 = const1 + random.randint(1, 5)

            latex = f"{coef}x + {const1} = {coef}x + {const2}"
            solution = 0  # No solutions

        else:  # infinite
            # Identical both