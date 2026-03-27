"""Monte Carlo rollout helpers."""

from __future__ import annotations

import copy
import random

from .board import Board, Move, apply_move, valid_moves
from .constants import ROLLOUT_DEPTH
from .heuristics import evaluate


def random_playout(board: Board, player: int) -> float:
    sim = copy.deepcopy(board)
    current = player

    for _ in range(ROLLOUT_DEPTH):
        moves = valid_moves(sim, current)
        if not moves:
            break

        move = random.choice(moves)
        sim = apply_move(sim, move, current)
        current = 3 - current

    return evaluate(sim, player)


def monte_carlo_score(board: Board, move: Move, player: int, sims: int) -> float:
    total = 0.0
    for _ in range(sims):
        new_board = apply_move(board, move, player)
        total += random_playout(new_board, player)
    return total / sims
