from Piece import Piece

class Bishop(Piece):

    PIECE_TYPE = "B"

    def __init__(self, x, y, color):
        super(Bishop, self).__init__(x, y, color, Bishop.PIECE_TYPE)

    @classmethod
    def get_piece_type(cls):
        return cls.PIECE_TYPE

    def get_possible_diagonal_moves(self, board):
        moves = []

        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        for direction in directions:
            (x, y) = (self.x, self.y)
            (dx, dy) = direction

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
        return self.get_possible_diagonal_moves(board)

    def return_piece(self):
        return Bishop(self.get_x(), self.get_y(), self.get_color())