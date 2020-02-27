import unittest
from board import Board


class TestBoardMethods(unittest.TestCase):
    def test_drop_at(self):
        board = Board(6, 7, 4)
        board.drop_at(0, 1)
        self.assertEqual(board.board[5, 0], 1)
        board.drop_at(0, 2)
        self.assertEqual(board.board[4, 0], 2)
        board.drop_at(0, 3)
        self.assertEqual(board.board[3, 0], 3)

    def test_check_win(self):
        board = Board(6, 7, 4)
        board.drop_at(0, 1)
        board.drop_at(1, 1)
        board.drop_at(2, 1)
        board.drop_at(3, 1)
        self.assertTrue(board.check_win(1))

    if __name__ == '__main__':
        unittest.main()