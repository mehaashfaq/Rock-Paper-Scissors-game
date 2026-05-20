🎮 Rock Paper Scissors Game with BFS & DFS (Tkinter Python Project)

A Python-based Rock Paper Scissors game built using Tkinter GUI, enhanced with Graph Theory concepts (BFS & DFS) to explore possible move transitions.

This project demonstrates both:

🎨 GUI development using Tkinter
🧠 Graph traversal algorithms (Breadth First Search & Depth First Search)
🎲 Randomized game logic
📊 Score tracking system
📌 Project Overview

This game allows a user to play Rock, Paper, Scissors against the computer. Each move is part of a graph structure, where moves are connected to each other.

Even though Rock Paper Scissors is simple, this project adds a computer science twist by modeling the moves as a graph and applying:

Breadth First Search (BFS)
Depth First Search (DFS)

These algorithms explore all possible moves starting from a chosen move.

🧠 Key Concepts Used
1. 🎲 Game Logic
Player selects: Rock / Paper / Scissors
Computer randomly selects a move
Winner is decided using standard rules:
Rock beats Scissors
Scissors beats Paper
Paper beats Rock
2. 🌐 Graph Representation

Moves are represented as a graph:

move_graph = {
    "Rock": ["Paper", "Scissors"],
    "Paper": ["Rock", "Scissors"],
    "Scissors": ["Rock", "Paper"]
}
📌 Meaning:
Each move is connected to the other possible moves
This forms a fully connected directed graph
3. 🔍 Breadth First Search (BFS)

BFS explores moves level by level using a queue.

📌 Idea:
Start from a move
Visit all directly connected moves first
Then explore deeper connections
🧾 Output Example:

If start = "Rock"

Rock → Paper → Scissors
4. 🌲 Depth First Search (DFS)

DFS explores as deep as possible before backtracking.

📌 Idea:
Start from a move
Go deep into one path first
Then backtrack and explore others
🧾 Output Example:

If start = "Rock"

Rock → Paper → Scissors
5. 🖥️ Tkinter GUI

The game uses Python’s built-in GUI library:

Features:
Buttons for Rock, Paper, Scissors
Labels showing:
Player choice
Computer choice
Result
Scoreboard
Reset button to restart game
📊 Features

✔ Simple and interactive GUI
✔ Real-time score tracking
✔ Random computer opponent
✔ BFS and DFS integration
✔ Console output for graph traversal
✔ Reset game functionality
✔ Clean modular Python structure

📁 Project Structure
rock-paper-scissors-bfs-dfs/
│
├── main.py        # Full game code (GUI + logic + BFS + DFS)
└── README.md      # Project documentation
🚀 How to Run the Project
1. Install Python

Make sure Python 3 is installed.

Check version:

python --version
2. Run the Game
python main.py
🎮 How to Play
Run the program
Click one of the buttons:
Rock ✊
Paper 📄
Scissors ✂️
Computer will randomly choose its move
Result will be displayed:
Win 🎉
Lose 😢
Tie 🤝
Score updates automatically
Click “Reset Game” to restart
🧠 BFS & DFS Output (Console)

Every move also triggers graph traversal:

Example output:

BFS: {'Rock', 'Paper', 'Scissors'}
DFS: {'Rock', 'Paper', 'Scissors'}

These outputs show all reachable nodes from the selected move.

📌 Learning Outcomes

After building this project, you will understand:

How to build GUI apps in Python (Tkinter)
How to implement game logic
How BFS works in real applications
How DFS works recursively
How graphs can represent real-world problems
How to combine algorithms + GUI programming
🔥 Possible Improvements

You can upgrade this project by adding:

🎨 UI Improvements
Images instead of text buttons
Animations for moves
Better layout using frames
🤖 AI Enhancements
Smart computer opponent (pattern prediction)
Minimax-style strategy
📊 Features
Win percentage tracking
Match history log
Sound effects
🌐 Web Version
Convert into Flask or Django app
Or React frontend with Python backend
👨‍💻 Author

Created as a learning project for:

Python programming
GUI development
Data structures (Graph theory)
Algorithm visualization
📌 License

This project is open-source and free to use for learning purposes.
