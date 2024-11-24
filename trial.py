#========>>>>>> Here is the a mini project whch is ROCK , PAPER AND SCISSORS ==============>>>>>>>>>

import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        master.title("Rock, Paper, Scissors")
        master.configure(bg="#f0f0f0")  # Light gray background

        self.label = tk.Label(master, text="Welcome to Rock, Paper, Scissors!😎", font=("Helvetica", 18), bg="#f0f0f0")
        self.label.pack(pady=20)

        self.result_label = tk.Label(master, text="", font=("Helvetica", 16), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        button_frame = tk.Frame(master, bg="#f0f0f0")
        button_frame.pack(pady=10)

        self.rock_button = tk.Button(button_frame, text="Rock", command=lambda: self.play("rock"), bg="#ffcccb", font=("Helvetica", 14))
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(button_frame, text="Paper", command=lambda: self.play("paper"), bg="#add8e6", font=("Helvetica", 14))
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: self.play("scissors"), bg="#90ee90", font=("Helvetica", 14))
        self.scissors_button.pack(side=tk.LEFT, padx=10)

    def play(self, user_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        result = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n"

        if user_choice == computer_choice:
            result += "It's a tie!"
            self.result_label.config(fg="black")  # Tie color
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            result += "You win!"
            self.result_label.config(fg="green")  # Win color
        else:
            result += "You lose!"
            self.result_label.config(fg="red")  # Lose color

        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
