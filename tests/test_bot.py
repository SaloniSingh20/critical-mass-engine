import unittest

from critical_mass_engine.constants import COLS, ROWS
from teamname_bot import choose_move


def make_empty_board():
    return [[[0, 0] for _ in range(COLS)] for _ in range(ROWS)]


class TestBotInterface(unittest.TestCase):
    def test_choose_move_returns_valid_coordinate(self):
        board = make_empty_board()
        move = choose_move(board, player=1)

        self.assertIsInstance(move, tuple)
        self.assertEqual(len(move), 2)
        row, col = move
        self.assertTrue(0 <= row < ROWS)
        self.assertTrue(0 <= col < COLS)


if __name__ == "__main__":
    unittest.main()
