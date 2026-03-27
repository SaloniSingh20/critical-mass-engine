"""Top-level move selection strategy."""

from __future__ import annotations

import random
import time

from .board import Board, Move, apply_move, valid_moves
from .constants import (
    MAX_ORDERED_MOVES,
    RANDOM_MOVE_PROBABILITY,
    ROLLOUTS_PER_MOVE,
    SEARCH_DEPTH,
    TOP_CANDIDATES,
)
from .heuristics import order_moves
from .search import minimax
from .simulation import monte_carlo_score


def choose_move(board: Board, player: int) -> Move:
    start_time = time.time()

    moves = valid_moves(board, player)
    if not moves:
        raise ValueError("No valid moves available for the current player.")

    moves = order_moves(board, moves, player)[:MAX_ORDERED_MOVES]

    scored = []
    for move in moves:
        score = monte_carlo_score(board, move, player, sims=ROLLOUTS_PER_MOVE)
        scored.append((score, move))

    scored.sort(reverse=True)
    top_moves = [move for _, move in scored[:TOP_CANDIDATES]]

    best_move = None
    best_score = float("-inf")

    for move in top_moves:
        new_board = apply_move(board, move, player)
        score, _ = minimax(
            new_board,
            SEARCH_DEPTH,
            float("-inf"),
            float("inf"),
            False,
            player,
            start_time,
        )

        if score > best_score:
            best_score = score
            best_move = move

    if random.random() < RANDOM_MOVE_PROBABILITY:
        return random.choice(moves)

    return best_move if best_move is not None else random.choice(moves)
