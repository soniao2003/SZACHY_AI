from Piece import Piece
from Pawn import Pawn
from King import King
from Queen import Queen
from Bishop import Bishop
from Rook import Rook
from Knight import Knight
from Board import Board

class Logic(Board):
    def __init__(self, chesspieces):
        super().__init__(chesspieces)

    @classmethod
    def new_board(cls):
        pieces_on_board = [[0] * Board.WIDTH for _ in range(Board.HEIGHT)]

        for x in range(Board.WIDTH):
            pieces_on_board[x][1] = Pawn(x, 1, Pawn.BLACK)
            pieces_on_board[x][Board.HEIGHT - 2] = Pawn(x, Board.HEIGHT - 2, Pawn.WHITE)

        pieces_on_board[1][0] = Knight(1, 0, Knight.BLACK)
        pieces_on_board[6][0] = Knight(6, 0, Knight.BLACK)
        pieces_on_board[1][Board.HEIGHT - 1] = Knight(1, Board.HEIGHT - 1, Knight.WHITE)
        pieces_on_board[6][Board.HEIGHT - 1] = Knight(6, Board.HEIGHT - 1, Knight.WHITE)

        pieces_on_board[2][0] = Bishop(2, 0, Bishop.BLACK)
        pieces_on_board[5][0] = Bishop(5, 0, Bishop.BLACK)
        pieces_on_board[2][Board.HEIGHT - 1] = Bishop(2, Board.HEIGHT - 1, Bishop.WHITE)
        pieces_on_board[5][Board.HEIGHT - 1] = Bishop(5, Board.HEIGHT - 1, Bishop.WHITE)

        pieces_on_board[0][0] = Rook(0, 0, Rook.BLACK)
        pieces_on_board[7][0] = Rook(7, 0, Rook.BLACK)
        pieces_on_board[0][Board.HEIGHT - 1] = Rook(0, Board.HEIGHT - 1, Rook.WHITE)
        pieces_on_board[7][Board.HEIGHT - 1] = Rook(7, Board.HEIGHT - 1, Rook.WHITE)

        pieces_on_board[3][0] = Queen(3, 0, Queen.BLACK)
        pieces_on_board[3][Board.HEIGHT - 1] = Queen(3, Board.HEIGHT - 1, Queen.WHITE)

        pieces_on_board[4][0] = King(4, 0, King.BLACK)
        pieces_on_board[4][Board.HEIGHT - 1] = King(4, Board.HEIGHT - 1, King.WHITE)

        return cls(pieces_on_board)

    def print_board(self):
        top = "    A  B  C  D  E  F  G  H"
        line = "    -----------------------"
        print(top)
        print(line)
        for y in range(Logic.HEIGHT):
            row = str(8 - y) + " | "
            for x in range(Logic.WIDTH):
                piece = self.get_chesspieces()[x][y]
                if piece != 0:
                    row += piece.to_string()
                else:
                    row += "__ "
            print(row)
        print("")

    def get_all_pieces(self):
        all_pieces = []
        for x in range(Logic.WIDTH):
            for y in range(Logic.HEIGHT):
                piece = self.get_chesspieces()[x][y]
                if piece != 0:
                    all_pieces.append(piece)
        return all_pieces

    #metoda iteruje po szachownicy, dla kazdego pionka wywołuje metode get_possible_moves
    def get_possible_moves(self, color):
        moves = []
        for x in range(Board.WIDTH):
            for y in range(Board.HEIGHT):
                piece = self.get_chesspieces()[x][y]
                if piece != 0:
                    if piece.get_color() == color:
                        moves += piece.get_possible_moves(self)

        return moves

    #metoda zmienia aktualną pozycje pionka na 0, co oznacza, że miejsce jest puste
    #następnie zmienione są koordynaty na xto i yto
    def move_piece_onboard(self, piece, xto, yto):
        self.get_chesspieces()[piece.x][piece.y] = 0
        piece.set_x(xto)
        piece.set_y(yto)

        #na polu xto, yto ustawiamy pionek
        chess_pieces = self.get_chesspieces()
        chess_pieces[xto][yto] = piece

    def move_check_rules(self, move):
        #bierzemy pionek, który stoi na wskazanej pozycji i uzywamy metody move_piece_onboard
        piece = self.chesspieces[move.xfrom][move.yfrom]
        self.move_piece_onboard(piece, move.xto, move.yto)

        #Jeśli pionek dotrze do końca zamienia się w królową
        if piece.piece_type == Pawn.PIECE_TYPE:
            if piece.y == 0 or piece.y == Logic.HEIGHT - 1:
                self.chesspieces[piece.x][piece.y] = Queen(piece.x, piece.y, piece.color)

    def is_king_in_check(self, color):
        king_piece = None
        for x in range(Board.WIDTH):
            for y in range(Board.HEIGHT):
                piece = self.get_chesspieces()[x][y]
                if piece != 0 and piece.get_color() == color and piece.get_piece_type() == King.PIECE_TYPE:
                    king_piece = piece
                    break
            if king_piece:
                break
        if not king_piece:
            return False
        if color == Piece.WHITE:
            other_color = Piece.BLACK
        else:
            other_color = Piece.WHITE
        for x in range(Board.WIDTH):
            for y in range(Board.HEIGHT):
                piece = self.get_chesspieces()[x][y]
                if piece != 0 and piece.get_color() == other_color:
                    if isinstance(piece, King):
                        # król nie może szachować króla
                        moves = piece.get_possible_moves(self)
                        for move in moves:
                            if move.getx_to() == king_piece.x and move.gety_to() == king_piece.y:
                                return True
                    else:
                        # sprawdzenie czy pionek może szachować króla
                        moves = piece.get_possible_moves(self)
                        for move in moves:
                            if move.getx_to() == king_piece.x and move.gety_to() == king_piece.y:
                                return True
        return False

    def is_checkmate(self, color):
        if not self.is_king_in_check(color):
            return False

        possible_moves = self.get_possible_moves(color)

        for move in possible_moves:
            clone_board = Board.clone(self)
            clone_rules = Logic(clone_board.get_chesspieces())
            clone_rules.move_check_rules(move)
            if not clone_rules.is_king_in_check(color):
                return False
        return True

    def is_stalemate(self, color):
        if self.is_king_in_check(color):
            return False

        possible_moves = self.get_possible_moves(color)

        for move in possible_moves:
            clone_board = Board.clone(self)
            clone_rules = Logic(clone_board.get_chesspieces())
            clone_rules.move_check_rules(move)
            if not clone_rules.is_king_in_check(color):
                return False
        return True




