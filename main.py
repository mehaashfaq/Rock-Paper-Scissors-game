import tkinter as tk
import random
from collections import deque

# ---------------- GRAPH REPRESENTATION ---------------- #
move_graph = {
    "Rock": ["Paper", "Scissors"],
    "Paper": ["Rock", "Scissors"],
    "Scissors": ["Rock", "Paper"]
}

# ---------------- BFS ALGORITHM ---------------- #
def bfs(start_move):
    visited = set()
    queue = deque([start_move])

    while queue:
        move = queue.popleft()
        if move not in visited:
            visited.add(move)
            queue.extend(move_graph[move])

    return visited


# ---------------- DFS ALGORITHM ---------------- #
def dfs(start_move, visited=None):
    if visited is None:
        visited = set()

    visited.add(start_move)

    for next_move in move_graph[start_move]:
        if next_move not in visited:
            dfs(next_move, visited)

    return visited


# ---------------- GAME LOGIC ---------------- #
def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])


def determine_winner(player, computer):
    if player == computer:
        return "Tie"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Scissors" and computer == "Paper") or \
         (player == "Paper" and computer == "Rock"):
        return "Win"
    else:
        return "Lose"


# ---------------- INITIAL SCORES ---------------- #
player_score = 0
computer_score = 0
ties = 0


# ---------------- PLAY FUNCTION ---------------- #
def play(player_choice):
    global player_score, computer_score, ties

    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)

    player_label.config(text=f"Player: {player_choice}")
    computer_label.config(text=f"Computer: {computer_choice}")
    result_label.config(text=f"Result: {result}")

    if result == "Win":
        player_score += 1
    elif result == "Lose":
        computer_score += 1
    else:
        ties += 1

    score_label.config(
        text=f"Score - You: {player_score} | Computer: {computer_score} | Ties: {ties}"
    )

    # BFS & DFS (printed in console)
    print("BFS:", bfs(player_choice))
    print("DFS:", dfs(player_choice))


# ---------------- RESET FUNCTION ---------------- #
def reset_game():
    global player_score, computer_score, ties
    player_score = 0
    computer_score = 0
    ties = 0

    player_label.config(text="Player: ")
    computer_label.config(text="Computer: ")
    result_label.config(text="Result: ")
    score_label.config(text="Score - You: 0 | Computer: 0 | Ties: 0")


# ---------------- GUI SETUP ---------------- #
root = tk.Tk()
root.title("Rock Paper Scissors - BFS & DFS")
root.geometry("400x400")

player_label = tk.Label(root, text="Player: ")
player_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer: ")
computer_label.pack(pady=5)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=5)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0 | Ties: 0")
score_label.pack(pady=10)

# Buttons
tk.Button(root, text="Rock", width=10, command=lambda: play("Rock")).pack(pady=2)
tk.Button(root, text="Paper", width=10, command=lambda: play("Paper")).pack(pady=2)
tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors")).pack(pady=2)

tk.Button(root, text="Reset Game", width=15, command=reset_game).pack(pady=10)

# Run app
root.mainloop()
