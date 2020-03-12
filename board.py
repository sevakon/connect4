import numpy as np


class Board:
    """ Class for Game Board interface and logic """
    def __init__(self, n_rows, n_cols, n_pieces):
        """
        Board init
        :param n_rows: number of board rows
        :param n_cols: number of board columns
        :param n_pieces: number of pieces to win
        """
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n_pieces = n_pieces
        self.board = np.zeros((n_rows, n_cols), dtype='int')

    def drop_at(self, col_idx, piece):
        """
        Interface for piece drop
        :param col_idx: column index at which to drop index
        :param piece: Player ID
        """
        if col_idx < 0 or col_idx >= self.n_cols:
            raise Exception("Invalid coloumn index, try again")
        final_idx = 0
        for row_idx in range(self.n_rows):
            if self.board[row_idx, col_idx] == 0:
                final_idx = row_idx
        if self.board[final_idx][col_idx] != 0:
            raise Exception("Entire column is busy, try other column indexes")
        self.board[final_idx][col_idx] = piece

    def check_win(self, piece):
        """
        Interface to check if player has winning sequence
        :param piece: Player ID
        :return: true if player has winning sequence, otherwise false
        """
        h = self._check_horizontal(piece)
        v = self._check_vertical(piece)
        d = self._check_diagonals(piece)
        return h or v or d

    def check_tie(self):
        """
        check if no blank cells left on the board
        :return: true if it is a tie, otherwise false
        """
        for row_idx in range(0, self.n_rows):
            for col_idx in range(0, self.n_cols):
                if self.board[row_idx][col_idx] == 0:
                    return False
        return True

    def _check_horizontal(self, piece):
        """
        Check for horizontal winning sequences
        :param piece: Player ID
        :return: true if player has winning sequence, otherwise false
        """
        for row_idx in range(self.n_rows):
            for col_idx in range(self.n_cols - self.n_pieces + 1):
                if np.sum(self.board[row_idx,col_idx:col_idx+self.n_pieces] == piece) == self.n_pieces:
                    return True
        return False

    def _check_vertical(self, piece):
        """
        Check for vertical winning sequences
        :param piece: Player ID
        :return: true if player has winning sequence, otherwise false
        """
        for row_idx in range(self.n_rows - self.n_pieces + 1):
            for col_idx in range(self.n_cols):
                if np.sum(self.board[row_idx:row_idx+self.n_pieces,col_idx] == piece) == self.n_pieces:
                    return True
        return False

    def _check_diagonals(self, piece):
        """
        Check for horizontal winning sequences
        :param piece: Player ID
        :return: true if player has winning sequence, otherwise false
        """
        for row_idx in range(self.n_rows - self.n_pieces + 1):
            for col_idx in range(self.n_cols - self.n_pieces + 1):
                if np.sum(self.board[row_idx:row_idx+self.n_pieces,\
                    col_idx:col_idx+self.n_pieces].diagonal() == piece) == self.n_pieces:
                    return True
                if np.sum(self.board[row_idx:row_idx+self.n_pieces,\
                    col_idx:col_idx+self.n_pieces:-1].diagonal() == piece) == self.n_pieces:
                    return True
        return False

    def load_board_from_file(self, filename):
        """
        Loads game status from file
        :param filename: file from where to load
        :return: None
        """
        f = open(filename, "r")
        for idx, line in enumerate(f):
            if idx == 1 or idx == 0:
                continue

            col_idx = 0
            for char in line:
                if char.isdigit():
                    self.board[idx - 2, col_idx] = int(char)
                    col_idx += 1
    
        f.close()

    def __str__(self):
        """
        String representation
        :return: string for Console UI
        """
        col_row = '##'
        for col_idx in range(self.n_cols):
            col_row += str(col_idx)+'#'
        col_row += '#\n'
        return 'GameBoard\n' +\
        col_row + str(np.matrix(self.board))
