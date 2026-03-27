"""Minimax search with alpha-beta pruning."""

from __future__ import annotations

import time
from typing import Optional, Tuple

from .board import Board, Move, apply_move, valid_moves
from .constants import MAX_ORDERED_MOVES, TIME_LIMIT
from .heuristics import evaluate, order_moves


def minimax(
    board: Board,
    depth: int,
    alpha: float,
    beta: float,
    maximizing: bool,
    player: int,
    start_time: float,
) -> Tuple[float, Optional[Move]]:
    if time.time() - start_time > TIME_LIMIT:
        return evaluate(board, player), None

    if depth == 0:
        return evaluate(board, player), None

    opponent = 3 - player
    current = player if maximizing else opponent

    moves = valid_moves(board, current)
    moves = order_moves(board, moves, player)[:MAX_ORDERED_MOVES]

    if not moves:
        return evaluate(board, player), None

    best_move: Optional[Move] = None

    if maximizing:
        best_score = float("-inf")
        for move in moves:
            new_board = apply_move(board, move, current)
            score, _ = minimax(new_board, depth - 1, alpha, beta, False, player, start_time)

            if score > best_score:
                best_score = score
                best_move = move

            alpha = max(alpha, score)
            if beta <= alpha:
                break

        return best_score, best_move

    best_score = float("inf")
    for move in moves:
        new_board = apply_move(board, move, current)
        score, _ = minimax(new_board, depth - 1, alpha, beta, True, player, start_time)

        if score < best_score:
            best_score = score
            best_move = move

        beta = min(beta, score)
        if beta <= alpha:
            break

    return best_score, best_move
