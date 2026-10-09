# Unbeatable Tic-Tac-Toe AI (Minimax with Alpha-Beta Pruning)

**Course:** B.Tech Information Technology (Semester V)  
**Subject:** Artificial Intelligence (Course Code: 202044503)  
**Topic:** Unit 3 - Game Playing & Planning / Practical #9  
**Team:** Vishrut Sharma(12402080601153), Yatharth Metha(12402080601160), Ved Tailor(12402080601145)

---

## 1. Project Overview

This project implements an intelligent game-playing agent for Tic-Tac-Toe using the **Minimax Algorithm** enhanced with **Alpha-Beta Cut-offs (Pruning)**.

Because Tic-Tac-Toe is a zero-sum, complete information game, the AI evaluates all possible states of the game tree. With Minimax and Alpha-Beta pruning, the AI plays optimally: **it is mathematically impossible for a human player to beat the AI (the best possible outcome for the human is a draw).**

---

## 2. Features
- **Unbeatable AI:** Minimax algorithm ensures the computer plays optimally.
- **Alpha-Beta Pruning:** Reduces search state space dramatically for fast decisions.
- **🔄 Reset / Play Again Button:** Prominently placed at the bottom so the player can restart or retry anytime.
- **Instant Replay Dialog:** Asks `"Would you like to retry and play again?"` immediately when a match finishes.
- **Scoreboard:** Keeps track of Human Wins, AI Wins, and Draws across rounds.
- **Live Node Counter:** Demonstrates search tree pruning live in front of the evaluator.

---

## 3. Tech Stack

- **Programming Language:** Python 3 (3.8+)
- **GUI Framework:** `tkinter` (Standard library, 0 external packages needed)
- **Dependencies:** None (`pip install` is NOT required)

---

## 3. How to Run the Project

> - Step 1 Download the file
> - Step 2 open the folder in VS Code
> - Step 3 open the terminal and run the command below
>   Open terminal or command prompt inside this folder and run:

```bash
python tictactoe_ai.py
```
