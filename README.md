# Unbeatable Tic-Tac-Toe AI (Minimax with Alpha-Beta Pruning)

**Course:** B.Tech Information Technology (Semester V)  
**Subject:** Artificial Intelligence (Course Code: 202044503)  
**Topic:** Unit 3 - Game Playing & Planning / Practical #9  

---

## 1. Project Overview
This project implements an intelligent game-playing agent for Tic-Tac-Toe using the **Minimax Algorithm** enhanced with **Alpha-Beta Cut-offs (Pruning)**. 

Because Tic-Tac-Toe is a zero-sum, complete information game, the AI evaluates all possible states of the game tree. With Minimax and Alpha-Beta pruning, the AI plays optimally: **it is mathematically impossible for a human player to beat the AI (the best possible outcome for the human is a draw).**

---

## 2. Tech Stack
- **Programming Language:** Python 3 (3.8+)
- **GUI Framework:** `tkinter` (Standard library, 0 external packages needed)
- **Dependencies:** None (`pip install` is NOT required)

---

## 3. How to Run the Project
Open terminal or command prompt inside this folder and run:
```bash
python tictactoe_ai.py
```

---

## 4. Key AI Concepts for Viva & Exam

### Q1: What is the Minimax algorithm?
> **Answer:** Minimax is a recursive backtracking algorithm used in two-player, turn-based, zero-sum games. It assumes both players make optimal moves. The AI acts as the **Maximizer** (trying to get the highest score), while the opponent acts as the **Minimizer** (trying to minimize the AI's score).

### Q2: What is Alpha-Beta Pruning?
> **Answer:** Alpha-Beta pruning is an optimization technique for Minimax that eliminates branches of the search tree that cannot influence the final decision.
> - **$\alpha$ (Alpha):** The best (highest) score guaranteed to the Maximizer so far.
> - **$\beta$ (Beta):** The best (lowest) score guaranteed to the Minimizer so far.
> - **Condition:** If $\beta \le \alpha$, the remaining child nodes in that subtree are pruned (cut off).

### Q3: Why does this app display "Nodes explored"?
> **Answer:** The node counter proves that Alpha-Beta pruning is working. Without pruning, Minimax evaluates thousands of nodes; with pruning, it evaluates significantly fewer states while achieving the exact same optimal move.
