import tkinter as tk
import random


user_score = 0
computer_score = 0

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    result = ""

 
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

   
    result_label.config(text=f"You chose {user_choice}.\nComputer chose {computer_choice}.\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")


def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_label.config(text="Score - You: 0 | Computer: 0")
    result_label.config(text="Choose Rock, Paper, or Scissors to start!")


root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

instruction = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=('Helvetica', 14))
instruction.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

for choice in choices:
    tk.Button(button_frame, text=choice, width=10, font=('Helvetica', 12),
              command=lambda c=choice: play(c)).pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors to start!", font=('Helvetica', 12), fg="blue")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=('Helvetica', 12))
score_label.pack()

reset_button = tk.Button(root, text="Play Again", font=('Helvetica', 12), command=reset_game)
reset_button.pack(pady=10)

root.mainloop()
