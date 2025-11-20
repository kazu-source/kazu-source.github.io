"""
Desktop GUI for the Math Worksheet Generator using Tkinter.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from datetime import datetime

from equation_generator import LinearEquationGenerator
from systems_generator import SystemsOfEquationsGenerator
from inequalities_generator import InequalityGenerator
from properties_generator import PropertiesOfEqualityGenerator
from properties_mult_div_generator import PropertiesMultDivGenerator
from word_problems_generator import WordProblemsGenerator
from multistep_generator import MultiStepEquationGenerator
from generators.chapter04.graphing_points import GraphingPointsGenerator
from generators.chapter03.compound_inequalities_generator import CompoundInequalityGenerator
from pdf_generator import PDFWorksheetGenerator
from worksheet_config import get_config


class WorksheetGeneratorGUI:
    """Main GUI application for generating math worksheets."""

    def __init__(self, root):
        """
        Initialize the GUI application.

        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("Math Worksheet Generator")
        self.root.geometry("550x480")
        self.root.resizable(False, False)

        # Initialize generators
        self.equation_gen = LinearEquationGenerator()
        self.systems_gen = SystemsOfEquationsGenerator()
        self.inequality_gen = InequalityGenerator()
        self.compound_inequality_gen = CompoundInequalityGenerator()
        self.properties_gen = PropertiesOfEqualityGenerator()
        self.properties_mult_div_gen = PropertiesMultDivGenerator()
        self.word_problems_gen = WordProblemsGenerator()
        self.multistep_gen = MultiStepEquationGenerator()
        self.graphing_points_gen = GraphingPointsGenerator()

        # Import systems graphing generator
        from generators.chapter05.graphing_systems import GraphingSystemsGenerator
        self.graphing_systems_gen = GraphingSystemsGenerator()

        # Import parabola graphing generator
        from generators.chapter11.graphing_parabolas import ParabolaGraphingGenerator
        self.parabola_gen = ParabolaGraphingGenerator()

        self.pdf_gen = PDFWorksheetGenerator()

        # Map chapters to topics
        # Structure: {chapter_name: {topic_display_name: (generator_name, config_key)}}
        self.chapter_topics = {
            'Chapter 2: Solving Simple Equations': {
                'Properties of Equality - Add/Subtract': ('properties', 'properties_of_equality'),
                'Properties of Equality - Mult/Div': ('properties_mult_div', 'properties_mult_div'),
                'Multi-Step Equations': ('multistep', 'multistep_equations'),
                'Linear Equations': ('linear', 'linear_equation'),
            },
            'Chapter 3: Inequalities': {
                'Inequalities': ('inequality', 'inequality'),
                'Compound Inequalities - Mixed': ('compound_inequality', 'compound_inequality'),
                'Compound Inequalities - AND': ('compound_inequality_and', 'compound_inequality_and'),
                'Compound Inequalities - OR': ('compound_inequality_or', 'compound_inequality_or'),
            },
            'Chapter 4: Linear Equations - Two Variables': {
                'Graphing Points': ('graphing_points', 'graphing_points'),
            },
            'Chapter 5: Systems of Equations': {
                'Systems of Equations - Algebraic': ('systems', 'system_of_equations'),
                'Systems of Equations - Graphing': ('graphing_systems', 'graphing_systems'),
            },
            'Chapter 6: Systems of Inequalities': {
                'Word Problems - Add/Subtract': ('word_problems', 'word_problems'),
            },
            'Chapter 11: Quadratic Functions and Parabolas': {
                'Graphing Parabolas': ('graphing_parabolas', 'graphing_parabolas'),
            },
        }

        # Legacy map for backwards compatibility
        self.problem_type_map = {
            'Linear Equations': 'linear_equation',
            'Systems of Equations - Algebraic': 'system_of_equations',
            'Systems of Equations - Graphing': 'graphing_systems',
            'Inequalities': 'inequality',
            'Compound Inequalities - Mixed': 'compound_inequality',
            'Compound Inequalities - AND': 'compound_inequality_and',
            'Compound Inequalities - OR': 'compound_inequality_or',
            'Properties of Equality - Add/Subtract': 'properties_of_equality',
            'Properties of Equality - Mult/Div': 'properties_mult_div',
            'Word Problems - Add/Subtract': 'word_problems',
            'Multi-Step Equations': 'multistep_equations',
            'Graphing Points': 'graphing_points',
            'Graphing Parabolas': 'graphing_parabolas'
        }

        # Setup UI
        self._create_widgets()

    def _create_widgets(self):
        """Create and layout all GUI widgets."""
        # Main frame with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Title
        title_label = ttk.Label(main_frame, text="Math Worksheet Generator",
                               font=("Helvetica", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 15))

        # Chapter selection
        chapter_label = ttk.Label(main_frame, text="Chapter:",
                                 font=("Helvetica", 11))
        chapter_label.grid(row=1, column=0, sticky=tk.W, pady=10)

        self.chapter_var = tk.StringVar(value="Chapter 2: Solving Simple Equations")
        self.chapter_combo = ttk.Combobox(main_frame, textvariable=self.chapter_var,
                                         state="readonly", width=25)
        self.chapter_combo['values'] = tuple(self.chapter_topics.keys())
        self.chapter_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=10, padx=(10, 0))

        # Topic selection
        topic_label = ttk.Label(main_frame, text="Topic:",
                               font=("Helvetica", 11))
        topic_label.grid(row=2, column=0, sticky=tk.W, pady=10)

        self.topic_var = tk.StringVar(value="Linear Equations")
        self.topic_combo = ttk.Combobox(main_frame, textvariable=self.topic_var,
                                       state="readonly", width=25)
        # Initialize with topics from first chapter
        first_chapter = list(self.chapter_topics.keys())[0]
        self.topic_combo['values'] = tuple(self.chapter_topics[first_chapter].keys())
        self.topic_combo.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=10, padx=(10, 0))

        # Update topics when chapter changes
        def update_chapter(event=None):
            chapter = self.chapter_var.get()
            topics = list(self.chapter_topics[chapter].keys())
            self.topic_combo['values'] = topics
            if topics:
                self.topic_var.set(topics[0])
            self._update_difficulty_descriptions()
            self._update_worksheet_title()
            self._update_default_num_problems()

        self.chapter_combo.bind('<<ComboboxSelected>>', update_chapter)

        # Update when topic changes
        def update_topic(event=None):
            self._update_difficulty_descriptions()
            self._update_worksheet_title()
            self._update_default_num_problems()

        self.topic_combo.bind('<<ComboboxSelected>>', update_topic)

        # Difficulty level selection
        difficulty_label = ttk.Label(main_frame, text="Difficulty Level:",
                                     font=("Helvetica", 11))
        difficulty_label.grid(row=3, column=0, sticky=tk.W, pady=10)

        self.difficulty_var = tk.StringVar(value="medium")
        difficulty_combo = ttk.Combobox(main_frame, textvariable=self.difficulty_var,
                                        state="readonly", width=25)
        difficulty_combo['values'] = ('easy', 'medium', 'hard', 'challenge')
        difficulty_combo.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=10, padx=(10, 0))

        # Difficulty descriptions - store for later updates
        self.difficulty_descriptions = {
            'Linear Equations': {
                'easy': 'One-step equations (x + 5 = 12)',
                'medium': 'Two-step equations (2x + 3 = 11)',
                'hard': 'Multi-step with parentheses',
                'challenge': 'Variables on both sides'
            },
            'Systems of Equations': {
                'easy': 'One variable already solved',
                'medium': 'Standard form, elimination/substitution',
                'hard': 'Larger coefficients',
                'challenge': 'May have fraction solutions'
            },
            'Inequalities': {
                'easy': 'One-step inequalities (x + 5 < 12)',
                'medium': 'Two-step inequalities (2x + 3 > 11)',
                'hard': 'Multi-step with parentheses',
                'challenge': 'Variables on both sides (direction may flip)'
            },
            'Compound Inequalities - Mixed': {
                'easy': 'Simple compound (3 < x < 7 or x < 2)',
                'medium': 'One-step solving (5 < x + 2 < 9)',
                'hard': 'Two-step solving (1 < 2x + 3 < 11)',
                'challenge': 'Negative coefficients (flip directions)'
            },
            'Compound Inequalities - AND': {
                'easy': 'Simple AND (3 < x < 7)',
                'medium': 'One-step solving (5 < x + 2 < 9)',
                'hard': 'Two-step solving (1 < 2x + 3 < 11)',
                'challenge': 'Negative coefficients (flip directions)'
            },
            'Compound Inequalities - OR': {
                'easy': 'Simple OR (x < 2 or x > 5)',
                'medium': 'One-step solving (x + 2 < 3 or x + 2 > 7)',
                'hard': 'Two-step solving (2x + 3 < 1 or 2x + 3 > 11)',
                'challenge': 'Negative coefficients (flip directions)'
            },
            'Properties of Equality - Add/Subtract': {
                'easy': 'Numbers 1-10 (x + 3 = 8, x - 5 = 2)',
                'medium': 'Numbers 1-20 (x + 12 = 25, x - 8 = 14)',
                'hard': 'Numbers 1-50 (may result in negatives)',
                'challenge': 'Numbers 1-50 (may result in negatives)'
            },
            'Properties of Equality - Mult/Div': {
                'easy': 'Numbers 1-10 (3x = 12, x/2 = 5)',
                'medium': 'Numbers 1-20 (7x = 42, x/4 = 9)',
                'hard': 'Numbers 1-50 (larger products/quotients)',
                'challenge': 'Numbers 1-50 (larger products/quotients)'
            },
            'Word Problems - Add/Subtract': {
                'easy': 'Numbers 1-20 (simple contexts)',
                'medium': 'Numbers 1-50 (varied contexts)',
                'hard': 'Numbers 1-100 (complex scenarios)',
                'challenge': 'Numbers 1-100 (complex scenarios)'
            },
            'Graphing Points': {
                'easy': '3 points, first quadrant only (0-10)',
                'medium': '4 points, all 4 quadrants (-5 to 5)',
                'hard': '5 points, all 4 quadrants (-10 to 10)',
                'challenge': '6 points, all 4 quadrants + axes'
            },
            'Systems of Equations - Graphing': {
                'easy': 'Integer slopes (±1, ±2), integer solution',
                'medium': 'Fractional slopes, mixed forms',
                'hard': 'Standard form, may have fractional solution',
                'challenge': 'Complex forms, fractional solutions'
            },
            'Graphing Parabolas': {
                'easy': 'y = x² or y = -x² (vertex at origin)',
                'medium': 'y = (x - h)² + k (integer h, k)',
                'hard': 'y = a(x - h)² + k (a ≠ 1, stretch/compress)',
                'challenge': 'Fractional a, h, or k values'
            }
        }

        self.desc_var = tk.StringVar(value=self.difficulty_descriptions['Linear Equations']['medium'])
        desc_label = ttk.Label(main_frame, textvariable=self.desc_var,
                              font=("Helvetica", 9), foreground="gray")
        desc_label.grid(row=4, column=1, sticky=tk.W, padx=(10, 0))

        # Update description when difficulty changes
        def update_description(event=None):
            topic = self.topic_var.get()
            difficulty = self.difficulty_var.get()
            if topic in self.difficulty_descriptions:
                self.desc_var.set(self.difficulty_descriptions[topic][difficulty])
            self._update_worksheet_title()

        difficulty_combo.bind('<<ComboboxSelected>>', update_description)

        # Number of problems
        num_problems_label = ttk.Label(main_frame, text="Number of Problems:",
                                       font=("Helvetica", 11))
        num_problems_label.grid(row=5, column=0, sticky=tk.W, pady=10)

        self.num_problems_var = tk.StringVar(value="10")
        num_problems_spinbox = ttk.Spinbox(main_frame, from_=4, to=16,
                                          textvariable=self.num_problems_var,
                                          width=25)
        num_problems_spinbox.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=10, padx=(10, 0))

        # Include answer key checkbox
        self.answer_key_var = tk.BooleanVar(value=True)
        answer_key_check = ttk.Checkbutton(main_frame, text="Include Answer Key",
                                          variable=self.answer_key_var)
        answer_key_check.grid(row=6, column=0, columnspan=2, pady=10)

        # Worksheet title
        title_input_label = ttk.Label(main_frame, text="Worksheet Title:",
                                      font=("Helvetica", 11))
        title_input_label.grid(row=7, column=0, sticky=tk.W, pady=10)

        self.title_var = tk.StringVar(value="Linear Equations - Medium")
        title_entry = ttk.Entry(main_frame, textvariable=self.title_var, width=27)
        title_entry.grid(row=7, column=1, sticky=(tk.W, tk.E), pady=10, padx=(10, 0))

        # Generate button
        generate_btn = ttk.Button(main_frame, text="Generate Worksheet",
                                 command=self.generate_worksheet)
        generate_btn.grid(row=8, column=0, columnspan=2, pady=30)

        # Status label
        self.status_var = tk.StringVar(value="Ready to generate worksheet")
        status_label = ttk.Label(main_frame, textvariable=self.status_var,
                                font=("Helvetica", 9), foreground="blue")
        status_label.grid(row=9, column=0, columnspan=2)

        # Configure grid weights for responsive layout
        main_frame.columnconfigure(1, weight=1)

    def _update_difficulty_descriptions(self):
        """Update the difficulty description based on problem type."""
        topic = self.topic_var.get()
        difficulty = self.difficulty_var.get()
        if topic in self.difficulty_descriptions:
            self.desc_var.set(self.difficulty_descriptions[topic][difficulty])

    def _update_worksheet_title(self):
        """Update the worksheet title based on selected problem type and difficulty."""
        topic = self.topic_var.get()
        difficulty = self.difficulty_var.get()
        # Capitalize difficulty level for display
        difficulty_capitalized = difficulty.capitalize()
        self.title_var.set(f"{topic} - {difficulty_capitalized}")

    def _update_default_num_problems(self):
        """Update the default number of problems based on problem type."""
        topic = self.topic_var.get()
        # Get the config key from the display name
        config_key = self.problem_type_map.get(topic)
        if config_key:
            config = get_config(config_key)
            self.num_problems_var.set(str(config.default_num_problems))

    def generate_worksheet(self):
        """Generate the worksheet PDF based on user inputs."""
        try:
            # Validate inputs
            num_problems = int(self.num_problems_var.get())
            if num_problems < 4 or num_problems > 16:
                messagebox.showerror("Invalid Input",
                                   "Number of problems must be between 4 and 16")
                return

            difficulty = self.difficulty_var.get()
            topic = self.topic_var.get()
            title = self.title_var.get()
            include_answer_key = self.answer_key_var.get()

            # Update status
            if topic == "Systems of Equations - Algebraic":
                status_text = "Generating systems..."
            elif topic == "Systems of Equations - Graphing":
                status_text = "Generating system graphs..."
            elif topic == "Inequalities":
                status_text = "Generating inequalities..."
            elif topic == "Compound Inequalities - Mixed":
                status_text = "Generating compound inequalities (mixed)..."
            elif topic == "Compound Inequalities - AND":
                status_text = "Generating compound inequalities (AND)..."
            elif topic == "Compound Inequalities - OR":
                status_text = "Generating compound inequalities (OR)..."
            elif topic == "Properties of Equality - Add/Subtract":
                status_text = "Generating properties (add/subtract)..."
            elif topic == "Properties of Equality - Mult/Div":
                status_text = "Generating properties (mult/div)..."
            elif topic == "Word Problems - Add/Subtract":
                status_text = "Generating word problems..."
            elif topic == "Multi-Step Equations":
                status_text = "Generating multi-step equations..."
            elif topic == "Graphing Points":
                status_text = "Generating graphs..."
            elif topic == "Graphing Parabolas":
                status_text = "Generating parabola graphs..."
            else:
                status_text = "Generating equations..."
            self.status_var.set(status_text)
            self.root.update()

            # Generate problems based on type
            if topic == "Systems of Equations - Algebraic":
                equations = self.systems_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Systems of Equations - Graphing":
                equations = self.graphing_systems_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Inequalities":
                equations = self.inequality_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Compound Inequalities - Mixed":
                equations = self.compound_inequality_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Compound Inequalities - AND":
                equations = self.compound_inequality_gen.generate_worksheet(difficulty, num_problems, compound_type='and')
            elif topic == "Compound Inequalities - OR":
                equations = self.compound_inequality_gen.generate_worksheet(difficulty, num_problems, compound_type='or')
            elif topic == "Properties of Equality - Add/Subtract":
                equations = self.properties_gen.generate_worksheet(difficulty, num_problems, 'mixed')
            elif topic == "Properties of Equality - Mult/Div":
                equations = self.properties_mult_div_gen.generate_worksheet(difficulty, num_problems, 'mixed')
            elif topic == "Word Problems - Add/Subtract":
                equations = self.word_problems_gen.generate_worksheet(difficulty, num_problems, 'mixed')
            elif topic == "Multi-Step Equations":
                equations = self.multistep_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Graphing Points":
                equations = self.graphing_points_gen.generate_worksheet(difficulty, num_problems)
            elif topic == "Graphing Parabolas":
                equations = self.parabola_gen.generate_worksheet(difficulty, num_problems)
            else:
                equations = self.equation_gen.generate_worksheet(difficulty, num_problems)

            # Ask user where to save
            # Get the config key for the problem type
            config_key = self.problem_type_map.get(topic)
            default_filename = f"{config_key}_{difficulty}.pdf"
            # Uncomment below to include timestamp in filename:
            # default_filename = f"{config_key}_{difficulty}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            output_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
                initialfile=default_filename
            )

            if not output_path:
                # User cancelled
                self.status_var.set("Ready to generate worksheet")
                return

            # Update status
            self.status_var.set("Creating PDF...")
            self.root.update()

            # Generate PDF
            self.pdf_gen.generate_worksheet(equations, output_path, title, include_answer_key)

            # Success message
            self.status_var.set(f"Worksheet saved successfully!")
            messagebox.showinfo("Success",
                              f"Worksheet generated successfully!\n\nSaved to:\n{output_path}")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)}")
            self.status_var.set("Error generating worksheet")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
            self.status_var.set("Error generating worksheet")


def main():
    """Main entry point for the GUI application."""
    root = tk.Tk()
    app = WorksheetGeneratorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
