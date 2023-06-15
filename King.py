from Piece import Piece

class King(Piece):
    PIECE_TYPE = "K"

    def __init__(self, x, y, color):
        super(King, self).__init__(x, y, color, King.PIECE_TYPE)

    @classmethod
    def get_piece_type(cls):
        return cls.PIECE_TYPE

    def get_possible_moves(self, board):
        moves = []
        moves.append(self.get_move(board, self.get_x(), self.get_y() + 1))
        moves.append(self.get_move(board, self.get_x() + 1, self.get_y() + 1))
        moves.append(self.get_move(board, self.get_x() + 1, self.get_y()))
        moves.append(self.get_move(board, self.get_x() + 1, self.get_y() - 1))
        moves.append(self.get_move(board, self.get_x(), self.get_y() - 1))
        moves.append(self.get_move(board, self.get_x() - 1, self.get_y() - 1))
        moves.append(self.get_move(board, self.get_x() - 1, self.get_y()))
        moves.append(self.get_move(board, self.get_x() - 1, self.get_y() + 1))
        return self.remove_0_from_list(moves)

    def return_piece(self):
        return King(self.get_x(), self.get_y(), self.get_color())


