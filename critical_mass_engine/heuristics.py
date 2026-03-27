"""Heuristic scoring and move ordering."""

from __future__ import annotations

from typing import List, Tuple

from .board import Board, get_critical_mass, valid_moves
from .constants import COLS, ROWS

Move = Tuple[int, int]


def position_weight(row: int, col: int) -> int:
    if (row in (0, ROWS - 1)) and (col in (0, COLS - 1)):
        return 5
    if row in (0, ROWS - 1) or col in (0, COLS - 1):
        return 3
    return 1


def is_dangerous(board: Board, row: int, col: int, opponent: int) -> bool:
    count, owner = board[row][col]
    return owner == opponent and count == get_critical_mass(row, col) - 1


def evaluate(board: Board, player: int) -> float:
    opponent = 3 - player
    score = 0.0

    my_cells = 0
    opp_cells = 0

    for row in range(ROWS):
        for col in range(COLS):
            count, owner = board[row][col]
            crit = get_critical_mass(row, col)
            weight = position_weight(row, col)

            if owner == player:
                my_cells += 1
            elif owner == opponent:
                opp_cells += 1

            if owner == player:
                score += count * weight

                if (row in (0, ROWS - 1)) and (col in (0, COLS - 1)):
                    score += 15

                if count == crit - 2:
                    score += 6

                if count == crit - 1:
                    score += 10

                if count < crit - 1:
                    score += 2

            elif owner == opponent:
                score -= count * weight * 0.8

                if count == crit - 1:
                    score -= 12

                if is_dangerous(board, row, col, opponent):
                    score -= 15

    if opp_cells > 0:
        opponent_moves = len(valid_moves(board, opponent))
        if opponent_moves <= 3:
            score += 12

    score += (my_cells - opp_cells) * 3

    return score


def order_moves(board: Board, moves: List[Move], player: int) -> List[Move]:
    del player
    scored = []
    for move in moves:
        row, col = move
        count = board[row][col][0]
        crit = get_critical_mass(row, col)

        score = position_weight(row, col) * 10

        if count == crit - 1:
            score += 100

        if count == crit - 2:
            score += 50

        scored.append((score, move))

    scored.sort(reverse=True)
    return [move for _, move in scored]
