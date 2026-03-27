"""Input parsing utilities for board files."""

from __future__ import annotations

import ast

from .board import Board
from .constants import COLS, ROWS


def load_board_from_text_file(path: str) -> Board:
    rows = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            stripped = line.strip()
            if not stripped:
                continue
            row = ast.literal_eval(stripped)
            rows.append(row)

    if len(rows) != ROWS:
        raise ValueError(f"Expected {ROWS} rows, got {len(rows)}")

    for idx, row in enumerate(rows):
        if len(row) != COLS:
            raise ValueError(f"Row {idx} expected {COLS} columns, got {len(row)}")

    return rows
