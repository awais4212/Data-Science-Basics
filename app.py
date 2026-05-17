# -*- coding: utf-8 -*-
"""
8-Puzzle Problem Solver using BFS
Course: CSC-471 Artificial Intelligence
Submitted by: Muhammad Awais Hashmi, Habiba Arif, Momina Aamir
"""

import tkinter as tk
from tkinter import messagebox
from collections import deque
import time
import random

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def get_neighbors(state):
    neighbors = []
    blank = state.index(0)
    row, col = divmod(blank, 3)
    if row > 0: neighbors.append((blank - 3, 'Up'))
    if row < 2: neighbors.append((blank + 3, 'Down'))
    if col > 0: neighbors.append((blank - 1, 'Left'))
    if col < 2: neighbors.append((blank + 1, 'Right'))
    result = []
    for pos, direction in neighbors:
        ns = list(state)
        ns[blank], ns[pos] = ns[pos], ns[blank]
        result.append((tuple(ns), direction))
    return result

def bfs(start):
    if start == GOAL:
        return [start], [], 0
    queue = deque([(start, [start], [])])
    visited = {start}
    explored = 0
    while queue:
        state, path, dirs = queue.popleft()
        explored += 1
        for ns, d in get_neighbors(state):
            if ns not in visited:
                np2 = path + [ns]
                nd2 = dirs + [d]
                if ns == GOAL:
                    return np2, nd2, explored
                visited.add(ns)
                queue.append((ns, np2, nd2))
    return None, None, explored

def is_solvable(state):
    tiles = [t for t in state if t != 0]
    inv = sum(1 for i in range(len(tiles))
              for j in range(i+1, len(tiles)) if tiles[i] > tiles[j])
    return inv % 2 == 0

def random_solvable():
    while True:
        s = list(range(9))
        random.shuffle(s)
        t = tuple(s)
        if is_solvable(t) and t != GOAL:
            return t

C_BG       = "#f0f0f0"
C_WHITE    = "#ffffff"
C_BORDER   = "#cccccc"
C_PURPLE   = "#5b4fcf"
C_PURPLE_L = "#ede9ff"
C_GREEN    = "#166534"
C_GREEN_L  = "#dcfce7"
C_AMBER    = "#92400e"
C_AMBER_L  = "#fef3c7"
C_RED      = "#991b1b"
C_RED_L    = "#fee2e2"
C_GRAY     = "#6b7280"
C_DARK     = "#111827"

PRESETS = {
    "Easy":   (1, 2, 3, 4, 0, 5, 7, 8, 6),
    "Medium": (1, 2, 3, 0, 4, 6, 7, 5, 8),
    "Hard":   (8, 6, 7, 2, 5, 4, 3, 0, 1),
}

class PuzzleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("8-Puzzle Solver  |  BFS  |  CSC-471 AI")
        self.configure(bg=C_BG)
        self.resizable(False, False)
        self.solution_path = []
        self.solution_dirs = []
        self.step_index    = 0
        self.playing       = False
        self._after_id     = None
        self._build_ui()
        self._load_preset(PRESETS["Easy"])

    def _build_ui(self):
        title_frame = tk.Frame(self, bg=C_PURPLE, pady=10)
        title_frame.pack(fill="x")
        tk.Label(title_frame, text="8-Puzzle Problem Solver",
                 font=("Segoe UI", 16, "bold"),
                 bg=C_PURPLE, fg="white").pack(side="left", padx=16)
        tk.Label(title_frame, text="BFS Algorithm  |  CSC-471 AI  |  Spring 2026",
                 font=("Segoe UI", 9),
                 bg=C_PURPLE, fg="#c4b5fd").pack(side="right", padx=16)

        main = tk.Frame(self, bg=C_BG, padx=16, pady=12)
        main.pack(fill="both")

        left = tk.Frame(main, bg=C_BG)
        left.grid(row=0, column=0, sticky="n", padx=(0, 12))

        right = tk.Frame(main, bg=C_BG)
        right.grid(row=0, column=1, sticky="nsew")

        self._build_left(left)
        self._build_right(right)

        self.status_var = tk.StringVar(value="Load a preset or enter a state, then press SOLVE.")
        sf = tk.Frame(self, bg=C_BORDER, pady=1)
        sf.pack(fill="x", side="bottom")
        self.status_lbl = tk.Label(sf, textvariable=self.status_var,
                                   font=("Segoe UI", 9), bg=C_WHITE,
                                   fg=C_GRAY, anchor="w", padx=12, pady=6)
        self.status_lbl.pack(fill="x")

    def _build_left(self, parent):
        tk.Label(parent, text="INITIAL STATE", font=("Segoe UI", 8, "bold"),
                 bg=C_BG, fg=C_PURPLE).pack(anchor="w", pady=(0, 4))

        ic = self._card(parent)
        ic.pack(fill="x", pady=(0, 10))

        self.input_vars = []
        igrid = tk.Frame(ic, bg=C_WHITE)
        igrid.pack(pady=4)
        for i in range(9):
            v = tk.StringVar()
            e = tk.Entry(igrid, textvariable=v, width=3, justify="center",
                         font=("Segoe UI", 20, "bold"),
                         bg=C_PURPLE_L, fg=C_PURPLE,
                         relief="solid", bd=1,
                         highlightthickness=0)
            e.grid(row=i//3, column=i%3, padx=3, pady=3, ipady=4)
            self.input_vars.append(v)

        pb = tk.Frame(ic, bg=C_WHITE)
        pb.pack(pady=(6, 2))
        for label, state in PRESETS.items():
            tk.Button(pb, text=label,
                      command=lambda s=state: self._load_preset(s),
                      font=("Segoe UI", 9), bg=C_BG, fg=C_DARK,
                      relief="solid", bd=1, padx=8, pady=3,
                      cursor="hand2").pack(side="left", padx=2)

        tk.Button(ic, text="Random Shuffle",
                  command=self._random_puzzle,
                  font=("Segoe UI", 9), bg=C_BG, fg=C_PURPLE,
                  relief="solid", bd=1, padx=8, pady=3,
                  cursor="hand2").pack(pady=(4, 6))

        tk.Label(parent, text="GOAL STATE", font=("Segoe UI", 8, "bold"),
                 bg=C_BG, fg=C_PURPLE).pack(anchor="w", pady=(0, 4))

        gc = self._card(parent)
        gc.pack(fill="x", pady=(0, 10))

        ggrid = tk.Frame(gc, bg=C_WHITE)
        ggrid.pack(pady=4)
        for i, v in enumerate(GOAL):
            lbl = tk.Label(ggrid, width=3,
                           text=str(v) if v != 0 else "",
                           font=("Segoe UI", 14, "bold"),
                           bg=C_GREEN_L if v != 0 else C_BG,
                           fg=C_GREEN if v != 0 else C_BG,
                           relief="solid", bd=1)
            lbl.grid(row=i//3, column=i%3, padx=3, pady=3, ipady=4)

        tk.Label(parent, text="BFS STATISTICS", font=("Segoe UI", 8, "bold"),
                 bg=C_BG, fg=C_PURPLE).pack(anchor="w", pady=(0, 4))

        sc = self._card(parent)
        sc.pack(fill="x")

        sf = tk.Frame(sc, bg=C_WHITE)
        sf.pack(fill="x", pady=4)
        self.stat_moves    = self._stat(sf, "Moves")
        self.stat_explored = self._stat(sf, "Explored")
        self.stat_ms       = self._stat(sf, "ms")

    def _build_right(self, parent):
        tk.Label(parent, text="CURRENT BOARD", font=("Segoe UI", 8, "bold"),
                 bg=C_BG, fg=C_PURPLE).pack(anchor="w", pady=(0, 4))

        bc = self._card(parent)
        bc.pack(fill="x", pady=(0, 10))

        self.board_labels = []
        bgrid = tk.Frame(bc, bg=C_WHITE)
        bgrid.pack(pady=6)
        for i in range(9):
            lbl = tk.Label(bgrid, width=3, text="",
                           font=("Segoe UI", 24, "bold"),
                           bg=C_PURPLE_L, fg=C_PURPLE,
                           relief="solid", bd=1)
            lbl.grid(row=i//3, column=i%3, padx=4, pady=4, ipady=10)
            self.board_labels.append(lbl)

        ctrl = tk.Frame(bc, bg=C_WHITE)
        ctrl.pack(pady=(2, 4))

        self.btn_solve = tk.Button(ctrl, text="SOLVE (BFS)",
                                   command=self._solve,
                                   font=("Segoe UI", 10, "bold"),
                                   bg=C_PURPLE, fg="white",
                                   relief="flat", padx=14, pady=6,
                                   cursor="hand2")
        self.btn_solve.grid(row=0, column=0, padx=4, pady=2)

        self.btn_reset = tk.Button(ctrl, text="Reset",
                                   command=self._reset,
                                   font=("Segoe UI", 10),
                                   bg=C_BG, fg=C_GRAY,
                                   relief="solid", bd=1, padx=10, pady=5,
                                   cursor="hand2", state="disabled")
        self.btn_reset.grid(row=0, column=1, padx=4, pady=2)

        nav = tk.Frame(bc, bg=C_WHITE)
        nav.pack(pady=(0, 4))

        self.btn_prev = tk.Button(nav, text="<< Prev",
                                  command=self._prev_step,
                                  font=("Segoe UI", 9), bg=C_BG, fg=C_GRAY,
                                  relief="solid", bd=1, padx=8, pady=4,
                                  cursor="hand2", state="disabled")
        self.btn_prev.pack(side="left", padx=3)

        self.btn_play = tk.Button(nav, text=">> Play",
                                  command=self._toggle_play,
                                  font=("Segoe UI", 9, "bold"),
                                  bg=C_GREEN_L, fg=C_GREEN,
                                  relief="solid", bd=1, padx=10, pady=4,
                                  cursor="hand2", state="disabled")
        self.btn_play.pack(side="left", padx=3)

        self.btn_next = tk.Button(nav, text="Next >>",
                                  command=self._next_step,
                                  font=("Segoe UI", 9), bg=C_BG, fg=C_GRAY,
                                  relief="solid", bd=1, padx=8, pady=4,
                                  cursor="hand2", state="disabled")
        self.btn_next.pack(side="left", padx=3)

        spd = tk.Frame(bc, bg=C_WHITE)
        spd.pack(pady=(0, 4))
        tk.Label(spd, text="Speed:", font=("Segoe UI", 9),
                 bg=C_WHITE, fg=C_GRAY).pack(side="left", padx=(0, 4))
        self.speed_var = tk.IntVar(value=600)
        tk.Scale(spd, from_=100, to=1200, orient="horizontal",
                 variable=self.speed_var, length=130,
                 bg=C_BG, fg=C_GRAY, troughcolor=C_BORDER,
                 highlightthickness=0, showvalue=False).pack(side="left")
        tk.Label(spd, text="Slow <-> Fast", font=("Segoe UI", 8),
                 bg=C_WHITE, fg=C_GRAY).pack(side="left", padx=4)

        self.step_var = tk.StringVar(value="Step -- / --")
        tk.Label(bc, textvariable=self.step_var,
                 font=("Segoe UI", 9), bg=C_WHITE, fg=C_GRAY).pack(pady=(0, 4))

        tk.Label(parent, text="SOLUTION PATH LOG", font=("Segoe UI", 8, "bold"),
                 bg=C_BG, fg=C_PURPLE).pack(anchor="w", pady=(0, 4))

        lc = self._card(parent)
        lc.pack(fill="both", expand=True)

        lf = tk.Frame(lc, bg=C_WHITE)
        lf.pack(fill="both", expand=True, pady=4)

        sb = tk.Scrollbar(lf)
        sb.pack(side="right", fill="y")

        self.log_box = tk.Text(lf, height=13, width=42,
                               font=("Courier New", 9),
                               bg=C_BG, fg=C_DARK,
                               relief="flat", bd=0, state="disabled",
                               yscrollcommand=sb.set,
                               wrap="none")
        self.log_box.pack(fill="both", expand=True)
        sb.config(command=self.log_box.yview)

        self.log_box.tag_config("header",  foreground=C_PURPLE, font=("Courier New", 9, "bold"))
        self.log_box.tag_config("current", foreground=C_AMBER,  background=C_AMBER_L)
        self.log_box.tag_config("done",    foreground=C_GREEN)
        self.log_box.tag_config("future",  foreground=C_GRAY)

    def _card(self, parent):
        outer = tk.Frame(parent, bg=C_BORDER, bd=0)
        inner = tk.Frame(outer, bg=C_WHITE, padx=10, pady=6)
        inner.pack(padx=1, pady=1, fill="both", expand=True)
        return inner

    def _stat(self, parent, label):
        box = tk.Frame(parent, bg=C_BG, padx=8, pady=6, relief="solid", bd=1)
        box.pack(side="left", expand=True, fill="x", padx=4)
        tk.Label(box, text=label, font=("Segoe UI", 8),
                 bg=C_BG, fg=C_GRAY).pack()
        var = tk.StringVar(value="--")
        tk.Label(box, textvariable=var, font=("Segoe UI", 18, "bold"),
                 bg=C_BG, fg=C_DARK).pack()
        return var

    def _set_status(self, msg, color=C_GRAY):
        self.status_var.set(msg)
        self.status_lbl.config(fg=color)

    def _render_board(self, state, prev):
        for i, v in enumerate(state):
            lbl = self.board_labels[i]
            if v == 0:
                lbl.config(text="", bg=C_BG, fg=C_BG, relief="flat")
            else:
                moved   = prev is not None and prev[i] != state[i]
                correct = GOAL[i] == v
                if moved:
                    lbl.config(text=str(v), bg=C_PURPLE,   fg="white",   relief="solid")
                elif correct:
                    lbl.config(text=str(v), bg=C_GREEN_L,  fg=C_GREEN,   relief="solid")
                else:
                    lbl.config(text=str(v), bg=C_PURPLE_L, fg=C_PURPLE,  relief="solid")

    def _update_step(self):
        if not self.solution_path:
            self.step_var.set("Step -- / --")
        else:
            self.step_var.set(f"Step {self.step_index} / {len(self.solution_path)-1}")

    def _rebuild_log(self):
        lb = self.log_box
        lb.config(state="normal")
        lb.delete("1.0", "end")
        lb.insert("end", f"{'#':>3}  {'Dir':>5}  Board\n", "header")
        lb.insert("end", "-" * 40 + "\n", "header")
        for i, state in enumerate(self.solution_path):
            d = self.solution_dirs[i-1] if i > 0 else "Start"
            row = "  ".join(str(v) if v != 0 else "_" for v in state)
            line = f"{i:>3}  {d:>5}  {row}\n"
            tag = "current" if i == self.step_index else ("done" if i < self.step_index else "future")
            lb.insert("end", line, tag)
        lb.config(state="disabled")
        if self.solution_path:
            lb.yview_moveto(self.step_index / len(self.solution_path))

    def _load_preset(self, state):
        self._stop_play()
        self.solution_path = []
        for i, v in enumerate(state):
            self.input_vars[i].set(str(v))
        self._render_board(list(state), None)
        self._clear_stats()
        self._set_status("Preset loaded. Press SOLVE to run BFS.")

    def _random_puzzle(self):
        self._stop_play()
        state = random_solvable()
        self.solution_path = []
        for i, v in enumerate(state):
            self.input_vars[i].set(str(v))
        self._render_board(list(state), None)
        self._clear_stats()
        self._set_status("Random puzzle loaded. Press SOLVE.")

    def _clear_stats(self):
        self.stat_moves.set("--")
        self.stat_explored.set("--")
        self.stat_ms.set("--")
        self.step_var.set("Step -- / --")
        self.log_box.config(state="normal")
        self.log_box.delete("1.0", "end")
        self.log_box.config(state="disabled")
        for b in [self.btn_prev, self.btn_next, self.btn_play, self.btn_reset]:
            b.config(state="disabled")

    def _get_state(self):
        try:
            vals = [int(self.input_vars[i].get()) for i in range(9)]
        except ValueError:
            return None
        if sorted(vals) != list(range(9)):
            return None
        return tuple(vals)

    def _solve(self):
        self._stop_play()
        state = self._get_state()
        if state is None:
            messagebox.showerror("Invalid Input", "Enter digits 0-8 exactly once.\n0 = blank tile.")
            return
        if not is_solvable(state):
            messagebox.showwarning("Not Solvable", "This puzzle cannot be solved.\nOdd number of inversions.")
            self._set_status("This configuration is unsolvable.", C_RED)
            return
        if state == GOAL:
            messagebox.showinfo("Done", "Already at goal state!")
            return

        self._set_status("Running BFS...", C_AMBER)
        self.update()

        t0 = time.perf_counter()
        path, dirs, explored = bfs(state)
        ms = (time.perf_counter() - t0) * 1000

        if not path:
            self._set_status("No solution found.", C_RED)
            return

        self.solution_path = path
        self.solution_dirs = dirs
        self.step_index    = 0

        self.stat_moves.set(str(len(path) - 1))
        self.stat_explored.set(str(explored))
        self.stat_ms.set(f"{ms:.1f}")

        self._render_board(list(path[0]), None)
        self._update_step()
        self._rebuild_log()

        self.btn_prev.config(state="disabled")
        self.btn_next.config(state="normal")
        self.btn_play.config(state="normal")
        self.btn_reset.config(state="normal")
        self._set_status(
            f"Solved! {len(path)-1} moves | {explored} states explored | {ms:.1f} ms",
            C_GREEN)

    def _go_to(self, i):
        if not self.solution_path: return
        i = max(0, min(i, len(self.solution_path) - 1))
        prev = list(self.solution_path[self.step_index])
        self.step_index = i
        self._render_board(list(self.solution_path[i]), prev)
        self._update_step()
        self._rebuild_log()
        self.btn_prev.config(state="disabled" if i == 0 else "normal")
        self.btn_next.config(state="disabled" if i == len(self.solution_path)-1 else "normal")

    def _prev_step(self): self._go_to(self.step_index - 1)
    def _next_step(self): self._go_to(self.step_index + 1)

    def _toggle_play(self):
        if self.playing:
            self._stop_play()
        else:
            if self.step_index == len(self.solution_path) - 1:
                self._go_to(0)
            self.playing = True
            self.btn_play.config(text="[STOP]", bg=C_RED_L, fg=C_RED)
            self._tick()

    def _tick(self):
        if not self.playing: return
        if self.step_index >= len(self.solution_path) - 1:
            self._stop_play()
            self._set_status("Playback complete.", C_GREEN)
            return
        self._next_step()
        delay = max(80, 1300 - self.speed_var.get())
        self._after_id = self.after(delay, self._tick)

    def _stop_play(self):
        self.playing = False
        if self._after_id:
            self.after_cancel(self._after_id)
            self._after_id = None
        self.btn_play.config(text=">> Play", bg=C_GREEN_L, fg=C_GREEN)

    def _reset(self):
        self._stop_play()
        self._go_to(0)
        self._set_status("Reset to initial state.")


if __name__ == "__main__":
    app = PuzzleApp()
    app.mainloop()