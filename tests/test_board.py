import unittest

from critical_mass_engine.board import apply_move, explode, get_critical_mass, valid_moves
from critical_mass_engine.constants import COLS, ROWS


def make_empty_board():
    return [[[0, 0] for _ in range(COLS)] for _ in range(ROWS)]


class TestBoardLogic(unittest.TestCase):
    def test_valid_moves_allow_empty_and_own_cells_only(self):
        board = make_empty_board()
        board[0][0] = [1, 1]
        board[0][1] = [2, 2]

        moves = set(valid_moves(board, player=1))

        self.assertIn((0, 0), moves)
        self.assertNotIn((0, 1), moves)
        self.assertEqual(len(moves), ROWS * COLS - 1)

    def test_apply_move_does_not_mutate_input_board(self):
        board = make_empty_board()
        _ = apply_move(board, (0, 0), player=1)

        self.assertEqual(board[0][0], [0, 0])

    def test_corner_explosion_transfers_to_neighbors(self):
        board = make_empty_board()
        # Corner critical mass is 2. This move should explode (0, 0).
        board[0][0] = [1, 1]

        new_board = apply_move(board, (0, 0), player=1)

        self.assertEqual(get_critical_mass(0, 0), 2)
        self.assertEqual(new_board[0][0], [0, 0])
        self.assertEqual(new_board[1][0], [1, 1])
        self.assertEqual(new_board[0][1], [1, 1])

    def test_chain_reaction_captures_neighbor(self):
        board = make_empty_board()
        # First explosion at (0, 0) adds to (0, 1), causing second explosion there.
        board[0][0] = [1, 1]
        board[0][1] = [2, 2]

        new_board = apply_move(board, (0, 0), player=1)

        # (0, 1) should have exploded and ownership propagated from player 1.
        self.assertEqual(new_board[0][1], [0, 0])
        self.assertEqual(new_board[0][2], [1, 1])
        self.assertEqual(new_board[1][1], [1, 1])


if __name__ == "__main__":
    unittest.main()
