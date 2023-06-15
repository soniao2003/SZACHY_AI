from Piece import Piece

class Pawn(Piece):

    PIECE_TYPE = "P"

    def __init__(self, x, y, color):
        super(Pawn, self).__init__(x, y, color, Pawn.PIECE_TYPE)

    @classmethod
    def get_piece_type(cls):
        return cls.PIECE_TYPE

    def is_starting_position(self):
        if (self.get_color() == Piece.BLACK):
            return self.y == 1
        else:
            return self.y == 8 - 2

    def get_possible_moves(self, board):
        moves = []
        if self.get_color() == Piece.WHITE:
            direction = -1
        if self.get_color() == Piece.BLACK:
            direction = 1

        # 1 ruch do przodu
        target_y = self.get_y() + direction
        if board.get_piece(self.get_x(), target_y) == 0:
            move = self.get_move(board, self.get_x(), target_y)
            moves.append(move)

        # pionek, ktory nie wykonał ruchu może isc 2 pola do przodu
        if self.is_starting_position():
            target_y = self.get_y() + direction * 2
            if board.get_piece(self.get_x(), target_y) == 0:
                move = self.get_move(board, self.get_x(), target_y)
                moves.append(move)

        # pionek moze zbijac na ukos
        target_x = self.get_x() + 1
        target_y = self.get_y() + direction
        piece = board.get_piece(target_x, target_y)
        if piece != 0:
            move = self.get_move(board, target_x, target_y)
            moves.append(move)
        target_x = self.get_x() - 1
        piece = board.get_piece(target_x, target_y)
        if piece != 0:
            move = self.get_move(board, target_x, target_y)
            moves.append(move)
        return self.remove_0_from_list(moves)

    def return_piece(self):
        return Pawn(self.get_x(), self.get_y(), self.get_color())
