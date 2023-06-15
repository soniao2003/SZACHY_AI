class Board:
    WIDTH = 8
    HEIGHT = 8

    def __init__(self, chesspieces):
        self.chesspieces = chesspieces

    def get_chesspieces(self):
        return self.chesspieces

    @classmethod
    def clone(cls, chessboard):
        pieces = [[0] * Board.WIDTH for i in range(Board.HEIGHT)]
        for x in range(Board.WIDTH):
            for y in range(Board.HEIGHT):
                piece = chessboard.get_chesspieces()[x][y]
                if piece != 0:
                    pieces[x][y] = piece.return_piece()
        return cls(pieces)

    def get_piece(self, x, y):
        if not self.on_board(x, y):
            return 0
        return self.get_chesspieces()[x][y]

    def on_board(self, x, y):
        return x >= 0 and y >= 0 and x < Board.WIDTH and y < Board.HEIGHT
