from Piece import Piece

class Queen(Piece):

    PIECE_TYPE = "Q"

    def __init__(self, x, y, color):
        super(Queen, self).__init__(x, y, color, Queen.PIECE_TYPE)

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
        diagonal = self.get_possible_diagonal_moves(board)
        horizontal = self.get_possible_horizontal_moves(board)
        return horizontal + diagonal

    def return_piece(self):
        return Queen(self.get_x(), self.get_y(), self.get_color())

