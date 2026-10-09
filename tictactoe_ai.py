"""
Unbeatable Tic-Tac-Toe using Minimax with Alpha-Beta Pruning
Semester 5 Artificial Intelligence Project (Unit 3 - Game Playing)
Tech Stack: Pure Python + Tkinter (Built-in, zero external dependencies)
"""

import math
import tkinter as tk
from tkinter import messagebox

HUMAN = 'O'
AI = 'X'
EMPTY = ' '


class TicTacToeAI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Tic-Tac-Toe (Minimax + Alpha-Beta Pruning)")
        self.root.geometry("450x600")
        self.root.minsize(420, 580)
        self.root.resizable(True, True)
        self.root.configure(bg="#1e1e2e")

        # Score tracking across retries
        self.human_score = 0
        self.ai_score = 0
        self.draws = 0

        # Board state: list of 9 elements ('X', 'O', or ' ')
        self.board = [EMPTY] * 9
        self.current_player = HUMAN
        self.game_over = False

        # Metrics for AI demonstration (helpful for Viva!)
        self.nodes_evaluated = 0

        # UI Setup
        self.create_widgets()

    def create_widgets(self):
        # Header Label
        self.title_label = tk.Label(
            self.root,
            text="Tic-Tac-Toe AI",
            font=("Helvetica", 20, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        )
        self.title_label.pack(pady=(12, 2))

        # Scoreboard
        self.score_label = tk.Label(
            self.root,
            text="You (O): 0  |  AI (X): 0  |  Draws: 0",
            font=("Helvetica", 11, "bold"),
            bg="#1e1e2e",
            fg="#f9e2af"
        )
        self.score_label.pack(pady=(0, 4))

        # Status Label
        self.status_label = tk.Label(
            self.root,
            text="Your Turn (O) vs AI (X)",
            font=("Helvetica", 12),
            bg="#1e1e2e",
            fg="#a6adc8"
        )
        self.status_label.pack(pady=(0, 8))

        # 3x3 Grid Frame
        self.grid_frame = tk.Frame(self.root, bg="#313244", padx=10, pady=10)
        self.grid_frame.pack()

        self.buttons = []
        for i in range(9):
            btn = tk.Button(
                self.grid_frame,
                text="",
                font=("Helvetica", 24, "bold"),
                width=4,
                height=2,
                bg="#45475a",
                fg="#ffffff",
                activebackground="#585b70",
                relief="flat",
                command=lambda index=i: self.on_human_move(index)
            )
            row, col = divmod(i, 3)
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(btn)

        # AI Info Label (demonstrating Alpha-Beta efficiency)
        self.info_label = tk.Label(
            self.root,
            text="Algorithm: Minimax + Alpha-Beta Pruning",
            font=("Helvetica", 10, "italic"),
            bg="#1e1e2e",
            fg="#9399b2"
        )
        self.info_label.pack(pady=(10, 4))

        # Reset / Retry Button Frame
        self.btn_frame = tk.Frame(self.root, bg="#1e1e2e")
        self.btn_frame.pack(pady=10)

        self.reset_btn = tk.Button(
            self.btn_frame,
            text="🔄 Reset / Play Again",
            font=("Helvetica", 12, "bold"),
            bg="#89b4fa",
            fg="#11111b",
            activebackground="#b4befe",
            padx=18,
            pady=8,
            cursor="hand2",
            relief="flat",
            command=self.reset_game
        )
        self.reset_btn.pack(side="left", padx=5)

    # ---------------- Game Logic ----------------
    def check_winner(self, board):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for a, b, c in win_conditions:
            if board[a] != EMPTY and board[a] == board[b] == board[c]:
                return board[a]

        if EMPTY not in board:
            return "Tie"

        return None

    def on_human_move(self, index):
        if self.game_over or self.board[index] != EMPTY or self.current_player != HUMAN:
            return

        # Human makes move
        self.board[index] = HUMAN
        self.buttons[index].config(text=HUMAN, fg="#a6e3a1")

        winner = self.check_winner(self.board)
        if winner:
            self.handle_game_end(winner)
            return

        # AI Turn
        self.current_player = AI
        self.status_label.config(text="AI is thinking...")
        self.root.after(200, self.ai_move)

    def ai_move(self):
        if self.game_over:
            return

        self.nodes_evaluated = 0
        best_move = self.get_best_move()

        if best_move is not None:
            self.board[best_move] = AI
            self.buttons[best_move].config(text=AI, fg="#f38ba8")

        self.info_label.config(
            text=f"Nodes explored with Alpha-Beta: {self.nodes_evaluated}"
        )

        winner = self.check_winner(self.board)
        if winner:
            self.handle_game_end(winner)
        else:
            self.current_player = HUMAN
            self.status_label.config(text="Your Turn (O)")

    def handle_game_end(self, winner):
        self.game_over = True
        result_message = ""

        if winner == "Tie":
            self.draws += 1
            self.status_label.config(text="Game Tied!")
            result_message = "It's a Draw! Both sides played optimally."
        elif winner == AI:
            self.ai_score += 1
            self.status_label.config(text="AI (X) Wins!")
            result_message = "AI (X) Wins! Minimax chose the optimal path."
        else:
            self.human_score += 1
            self.status_label.config(text="You Win!")
            result_message = "Congratulations, you won!"

        # Update scoreboard
        self.score_label.config(
            text=f"You (O): {self.human_score}  |  AI (X): {self.ai_score}  |  Draws: {self.draws}"
        )

        # Ask to retry immediately
        retry = messagebox.askyesno("Game Over", f"{result_message}\n\nWould you like to retry and play again?")
        if retry:
            self.reset_game()

    # ---------------- Minimax with Alpha-Beta Pruning ----------------
    def minimax(self, board, depth, is_maximizing, alpha, beta):
        self.nodes_evaluated += 1

        result = self.check_winner(board)
        if result == AI:
            return 10 - depth  # Prefer faster wins
        if result == HUMAN:
            return depth - 10  # Prefer delayed losses
        if result == "Tie":
            return 0

        if is_maximizing:
            max_eval = -math.inf
            for i in range(9):
                if board[i] == EMPTY:
                    board[i] = AI
                    eval_score = self.minimax(board, depth + 1, False, alpha, beta)
                    board[i] = EMPTY

                    max_eval = max(max_eval, eval_score)
                    alpha = max(alpha, eval_score)
                    if beta <= alpha:
                        break  # Beta cut-off / prune
            return max_eval
        else:
            min_eval = math.inf
            for i in range(9):
                if board[i] == EMPTY:
                    board[i] = HUMAN
                    eval_score = self.minimax(board, depth + 1, True, alpha, beta)
                    board[i] = EMPTY

                    min_eval = min(min_eval, eval_score)
                    beta = min(beta, eval_score)
                    if beta <= alpha:
                        break  # Alpha cut-off / prune
            return min_eval

    def get_best_move(self):
        best_val = -math.inf
        best_move = None
        alpha = -math.inf
        beta = math.inf

        for i in range(9):
            if self.board[i] == EMPTY:
                self.board[i] = AI
                move_val = self.minimax(self.board, 0, False, alpha, beta)
                self.board[i] = EMPTY

                if move_val > best_val:
                    best_val = move_val
                    best_move = i

                alpha = max(alpha, best_val)

        return best_move

    def reset_game(self):
        self.board = [EMPTY] * 9
        self.current_player = HUMAN
        self.game_over = False
        self.status_label.config(text="Your Turn (O) vs AI (X)")
        self.info_label.config(text="Algorithm: Minimax + Alpha-Beta Pruning")
        for btn in self.buttons:
            btn.config(text="", fg="#ffffff")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeAI(root)
    root.mainloop()
