import numpy as np

class Board:
    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.board = np.zeros((n_rows, n_cols), dtype='int')

    def drop_at(self, col_idx, piece):
        if col_idx < 0 or col_idx >= self.n_cols:
            raise Exception("Invalid coloumn index, try again")
        row_idx = 0
        for idx in range(self.n_rows):
            if self.board[idx, col_idx] == 0:
                row_idx = idx
        if self.board[row_idx][col_idx] != 0:
            raise Exception("Entire column is busy, try other column indexes")
        self.board[row_idx][col_idx] = piece

    def check_win(self, piece):
        h = self._check_horizontal(piece)
        v = self._check_vertical(piece)
        d = self._check_diagonal(piece)
        cd = self._check_counterdiagonal(piece)
        return h or v or d or cd

    def check_tie(self):
        for row_idx in range(0, self.n_rows):
            for col_idx in range(0, self.n_cols):
                if self.board[row_idx][col_idx] == 0:
                    return False
        return True


    def _check_horizontal(self, piece):
        for row_idx in range(self.n_rows):
            for col_idx in range(self.n_cols - 3):
                if self.board[row_idx][col_idx] == piece and \
                   self.board[row_idx][col_idx + 1] == piece and \
                   self.board[row_idx][col_idx + 2] == piece and \
                   self.board[row_idx][col_idx + 3] == piece:
                        return True
        return False

    def _check_vertical(self, piece):
        for row_idx in range(self.n_rows - 3):
            for col_idx in range(self.n_cols):
                if self.board[row_idx][col_idx] == piece and \
                   self.board[row_idx + 1][col_idx] == piece and \
                   self.board[row_idx + 2][col_idx] == piece and \
                   self.board[row_idx + 3][col_idx] == piece:
                        return True
        return False

    def _check_diagonal(self, piece):
        for row_idx in range(self.n_rows - 3):
            for col_idx in range(self.n_cols - 3):
                if self.board[row_idx][col_idx] == piece and \
                   self.board[row_idx + 1][col_idx + 1] == piece and \
                   self.board[row_idx + 2][col_idx + 2] == piece and \
                   self.board[row_idx + 3][col_idx + 3] == piece:
                        return True
        return False

    def _check_counterdiagonal(self, piece):
        for row_idx in range(3, self.n_rows):
            for col_idx in range(self.n_cols - 3):
                if self.board[row_idx][col_idx] == piece and \
                   self.board[row_idx - 1][col_idx + 1] == piece and \
                   self.board[row_idx - 2][col_idx + 2] == piece and \
                   self.board[row_idx - 3][col_idx + 3] == piece:
                        return True
        return False

    def __str__(self):
        col_row = '##'
        for col_idx in range(self.n_cols):
            col_row += str(col_idx)+'#'
        col_row += '#\n'
        return 'GameBoard\n' +\
        col_row + str(np.matrix(self.board))
