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
from pdf_generator import PDFWorksheetGenerator


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
        self.pdf_gen = PDFWorksheetGenerator()

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

        # Problem Type selection
        type_label = ttk.Label(main_frame, text="Problem Type:",
                              font=("Helvetica", 11))
        type_label.grid(row=1, column=0, sticky=tk.W, pady=10)

        self.problem_type_var = tk.StringVar(value="Linear Equations")
        type_combo = ttk.Combobox(main_frame, textvariable=self.problem_type_var,
                                 state="readonly", width=25)
        type_combo['values'] = ('Linear Equations', 'Systems of Equations', 'Inequalities')
        type_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=10, padx=(10, 0))

        # Update difficulty descriptions when problem type changes
        def update_problem_type(event=None):
            self._update_difficulty_descriptions()
            self._update_worksheet_title()

        type_combo.bind('<<ComboboxSelected>>', update_problem_type)

        # Difficulty level selection
        difficulty_label = ttk.Label(main_frame, text="Difficulty Level:",
                                     font=("Helvetica", 11))
        difficulty_label.grid(row=2, column=0, sticky=tk.W, pady=10)

        self.difficulty_var = tk.StringVar(value="medium")
        difficulty_combo = ttk.Combobox(main_frame, textvariable=self.difficulty_var,
                                        state="readonly", width=25)
        difficulty_combo['values'] = ('easy', 'medium', 'hard', 'challenge')
        difficulty_combo.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=10, padx=(10, 0))

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
            }
        }

        self.desc_var = tk.StringVar(value=self.difficulty_descriptions['Linear Equations']['medium'])
        desc_label = ttk.Label(main_frame, textvariable=self.desc_var,
                              font=("Helvetica", 9), foreground="gray")
        desc_label.grid(row=3, column=1, sticky=tk.W, padx=(10, 0))

        # Update description when difficulty changes
        def update_description(event=None):
            problem_type = self.problem_type_var.get()
            difficulty = self.difficulty_var.get()
            self.desc_var.set(self.difficulty_descriptions[problem_type][difficulty])
            self._update_worksheet_title()

        difficulty_combo.bind('<<ComboboxSelected>>', update_description)

        # Number of problems
        num_problems_label = ttk.Label(main_frame, text="Number of Problems:",
                                       font=("Helvetica", 11))
        num_problems_label.grid(row=4, column=0, sticky=tk.W, pady=10)

        self.num_problems_var = tk.StringVar(value="10")
        num_problems_spinbox = ttk.Spinbox(main_frame, from_=5, to=20,
                                          textvariable=self.num_problems_var,
                                          width=25)
        num_problems_spinbox.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=10, padx=(10, 0))

        # Include answer key checkbox
        self.answer_key_var = tk.BooleanVar(value=True)
        answer_key_check = ttk.Checkbutton(main_frame, text="Include Answer Key",
                                          variable=self.answer_key_var)
        answer_key_check.grid(row=5, column=0, columnspan=2, pady=10)

        # Worksheet title
        title_input_label = ttk.Label(main_frame, text="Worksheet Title:",
                                      font=("Helvetica", 11))
        title_input_label.grid(row=6, column=0, sticky=tk.W, pady=10)

        self.title_var = tk.StringVar(value="Linear Equations - Medium")
        title_entry = ttk.Entry(main_frame, textvariable=self.title_var, width=27)
        title_entry.grid(row=6, column=1, sticky=(tk.W, tk.E), pady=10, padx=(10, 0))

        # Generate button
        generate_btn = ttk.Button(main_frame, text="Generate Worksheet",
                                 command=self.generate_worksheet)
        generate_btn.grid(row=7, column=0, columnspan=2, pady=30)

        # Status label
        self.status_var = tk.StringVar(value="Ready to generate worksheet")
        status_label = ttk.Label(main_frame, textvariable=self.status_var,
                                font=("Helvetica", 9), foreground="blue")
        status_label.grid(row=8, column=0, columnspan=2)

        # Configure grid weights for responsive layout
        main_frame.columnconfigure(1, weight=1)

    def _update_difficulty_descriptions(self):
        """Update the difficulty description based on problem type."""
        problem_type = self.problem_type_var.get()
        difficulty = self.difficulty_var.get()
        self.desc_var.set(self.difficulty_descriptions[problem_type][difficulty])

    def _update_worksheet_title(self):
        """Update the worksheet title based on selected problem type and difficulty."""
        problem_type = self.problem_type_var.get()
        difficulty = self.difficulty_var.get()
        # Capitalize difficulty level for display
        difficulty_capitalized = difficulty.capitalize()
        self.title_var.set(f"{problem_type} - {difficulty_capitalized}")

    def generate_worksheet(self):
        """Generate the worksheet PDF based on user inputs."""
        try:
            # Validate inputs
            num_problems = int(self.num_problems_var.get())
            if num_problems < 1 or num_problems > 20:
                messagebox.showerror("Invalid Input",
                                   "Number of problems must be between 1 and 20")
                return

            difficulty = self.difficulty_var.get()
            problem_type = self.problem_type_var.get()
            title = self.title_var.get()
            include_answer_key = self.answer_key_var.get()

            # Update status
            if problem_type == "Systems of Equations":
                status_text = "Generating systems..."
            elif problem_type == "Inequalities":
                status_text = "Generating inequalities..."
            else:
                status_text = "Generating equations..."
            self.status_var.set(status_text)
            self.root.update()

            # Generate problems based on type
            if problem_type == "Systems of Equations":
                equations = self.systems_gen.generate_worksheet(difficulty, num_problems)
            elif problem_type == "Inequalities":
                equations = self.inequality_gen.generate_worksheet(difficulty, num_problems)
            else:
                equations = self.equation_gen.generate_worksheet(difficulty, num_problems)

            # Ask user where to save
            default_filename = f"worksheet_{difficulty}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
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
