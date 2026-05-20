import tkinter as tk
from game_logic import play, reset_game

root = tk.Tk()
root.title("Rock Paper Scissors - BFS & DFS")

# Labels
player_label = tk.Label(root, text="Player: ")
player_label.pack()

computer_label = tk.Label(root, text="Computer: ")
computer_label.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0 | Ties: 0")
score_label.pack()

# Buttons
for choice in ["Rock", "Paper", "Scissors"]:
    tk.Button(root, text=choice,
              command=lambda c=choice: play(c, player_label, computer_label, result_label, score_label)
              ).pack()

tk.Button(root, text="Reset", command=reset_game).pack()

root.mainloop()
