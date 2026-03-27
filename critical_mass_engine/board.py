"""Board utilities and move application logic."""

from __future__ import annotations

import copy
from typing import List, Tuple

from .constants import COLS, DIRS, ROWS

Cell = List[int]
Board = List[List[Cell]]
Move = Tuple[int, int]


def get_critical_mass(row: int, col: int) -> int:
    return sum(1 for dr, dc in DIRS if 0 <= row + dr < ROWS and 0 <= col + dc < COLS)


def valid_moves(board: Board, player: int) -> List[Move]:
    return [
        (row, col)
        for row in range(ROWS)
        for col in range(COLS)
        if board[row][col][1] in (0, player)
    ]


def explode(board: Board) -> None:
    changed = True
    while changed:
        changed = False
        for row in range(ROWS):
            for col in range(COLS):
                count, owner = board[row][col]
                if owner != 0 and count >= get_critical_mass(row, col):
                    player = owner
                    board[row][col] = [0, 0]
                    for dr, dc in DIRS:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS:
                            board[nr][nc][0] += 1
                            board[nr][nc][1] = player
                    changed = True


def apply_move(board: Board, move: Move, player: int) -> Board:
    row, col = move
    new_board = copy.deepcopy(board)
    new_board[row][col][0] += 1
    new_board[row][col][1] = player
    explode(new_board)
    return new_board
