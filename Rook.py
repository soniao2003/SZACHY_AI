from Piece import Piece

class Rook(Piece):

    PIECE_TYPE = "R"

    def __init__(self, x, y, color):
        super(Rook, self).__init__(x, y, color, Rook.PIECE_TYPE)

    @classmethod
    def get_piece_type(cls):
        return cls.PIECE_TYPE

    def get_possible_horizontal_moves(self, board):
        moves = []

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for direction in directions:
            (dx, dy) = direction
            (x, y) = (self.get_x(), self.get_y())

            while True:
                x += dx
                y += dy

                if not board.on_board(x, y):
                    break

                piece = board.get_piece(x, y)
                moves.append(self.get_move(board, x, y))

                if piece != 0:
                    break

        return self.remove_0_from_list(moves)

    def get_possible_moves(self, board):
        return self.get_possible_horizontal_moves(board)

    def return_piece(self):
        return Rook(self.get_x(), self.get_y(), self.get_color())
