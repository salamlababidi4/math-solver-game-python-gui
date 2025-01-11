import tkinter as tk
import random
from tkinter import messagebox

class MathSolverGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Solver Game")

        # Game variables
        self.score = 0
        self.time_left = 60
        self.current_question = ""
        self.correct_answer = None

        # UI setup
        self.timer_label = tk.Label(root, text=f"Time Left: {self.time_left}s", font=("Helvetica", 16))
        self.timer_label.pack(pady=10)

        self.question_label = tk.Label(root, text="Press 'Start' to begin", font=("Helvetica", 14))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Helvetica", 16), justify="center")  # Center the text
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", self.check_answer)
        self.answer_entry.config(state="disabled")

        self.start_button = tk.Button(root, text="Start", font=("Helvetica", 16), command=self.start_game)
        self.start_button.pack(pady=10)

    def start_game(self):
        self.score = 0
        self.time_left = 60
        self.answer_entry.config(state="normal")
        self.answer_entry.delete(0, tk.END)
        self.start_button.config(state="disabled")
        self.update_timer()
        self.generate_question()

        # Place cursor in the center of the entry field when the game starts
        self.answer_entry.icursor(tk.END)

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def generate_question(self):
        operators = ['+', '-', '*', '/']
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(operators)

        if operator == '/':
            num1 = num1 * num2  # Ensure the division result is an integer

        self.correct_answer = eval(f"{num1} {operator} {num2}")
        if operator == '/':
            self.correct_answer = round(self.correct_answer, 2)  # Handle division rounding

        self.current_question = f"{num1} {operator} {num2}"
        self.question_label.config(text=self.current_question)

    def check_answer(self, event):
        try:
            user_answer = float(self.answer_entry.get())
        except ValueError:
            self.answer_entry.delete(0, tk.END)
            return

        if user_answer == self.correct_answer:
            self.score += 1

        self.answer_entry.delete(0, tk.END)
        self.generate_question()

    def end_game(self):
        self.answer_entry.config(state="disabled")
        self.start_button.config(state="normal")
        self.question_label.config(text=f"Game Over! Your Score: {self.score}")
        messagebox.showinfo("Game Over", f"Time's up! Your final score is: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = MathSolverGame(root)
    root.mainloop()
