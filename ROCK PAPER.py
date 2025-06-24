import tkinter as tk
import random
user_score = 0
computer_score = 0
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

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
    label_user.config(text="You chose: " + user_choice)
    label_computer.config(text="Computer chose: " + computer_choice)
    label_result.config(text="Result: " + result)
    label_score.config(text=f"Score - You: {user_score} | Computer: {computer_score}")
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    label_user.config(text="You chose: ")
    label_computer.config(text="Computer chose: ")
    label_result.config(text="Result: ")
    label_score.config(text="Score - You: 0 | Computer: 0")
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("350x350")
window.config(bg="white")
tk.Label(window, text="Rock, Paper, Scissors", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
tk.Label(window, text="Choose one:", font=("Arial", 12), bg="white").pack()
tk.Button(window, text="Rock", width=12, command=lambda: play("Rock")).pack(pady=5)
tk.Button(window, text="Paper", width=12, command=lambda: play("Paper")).pack(pady=5)
tk.Button(window, text="Scissors", width=12, command=lambda: play("Scissors")).pack(pady=5)
label_user = tk.Label(window, text="You chose: ", font=("Arial", 12), bg="white")
label_user.pack(pady=2)

label_computer = tk.Label(window, text="Computer chose: ", font=("Arial", 12), bg="white")
label_computer.pack(pady=2)

label_result = tk.Label(window, text="Result: ", font=("Arial", 12, "bold"), fg="blue", bg="white")
label_result.pack(pady=5)

label_score = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Arial", 12), bg="white")
label_score.pack(pady=5)

tk.Button(window, text="Reset Game", command=reset_game).pack(pady=10)
window.mainloop()
