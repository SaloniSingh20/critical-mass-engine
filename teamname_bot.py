"""Compatibility entrypoint for the competition bot."""

from __future__ import annotations

from critical_mass_engine.bot import choose_move as engine_choose_move
from critical_mass_engine.io_utils import load_board_from_text_file


def choose_move(board, player):
    """Competition-facing function expected by the game runner."""
    return engine_choose_move(board, player)


if __name__ == "__main__":
    board = load_board_from_text_file("test_cases/sample_board.txt")
    move = choose_move(board, player=1)
    print(f"Suggested move for player 1: {move}")
