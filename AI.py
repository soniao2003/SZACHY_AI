from Logic import Logic
from Pawn import Pawn
from King import King
from Queen import Queen
from Bishop import Bishop
from Rook import Rook
from Knight import Knight
import random

class AI:
    @staticmethod
    def get_ai_move(chessboard, invalid_moves, ai_color):
        best_moves = []
        best_score = float('inf')

        for move in chessboard.get_possible_moves(ai_color):
            if AI.is_invalid_move(move, invalid_moves):
                continue

            copy = Logic.clone(chessboard)
            copy.move_check_rules(move)

            score = AI.evaluate_board(copy, ai_color)

            if score < best_score:
                best_score = score
                best_moves = [move]
            elif score == best_score:
                best_moves.append(move)

        # szachmat
        if not best_moves:
            return None

        best_move = random.choice(best_moves)

        copy = Logic.clone(chessboard)
        copy.move_check_rules(best_move)

        if copy.is_king_in_check(ai_color):
            invalid_moves.append(best_move)
            return AI.get_ai_move(copy, invalid_moves, ai_color)

        return best_move

    @staticmethod
    def is_invalid_move(move, invalid_moves):
        return move in invalid_moves

    @staticmethod
    def evaluate_board(chessboard, ai_color):
        score = 0
        for piece in chessboard.get_all_pieces():
            if piece.get_color() == ai_color:
                score += AI.get_piece_value(piece)
        return score

    @staticmethod
    def get_piece_value(piece):
        if piece.get_piece_type() == Pawn.get_piece_type():
            return 1
        elif piece.get_piece_type() == Knight.get_piece_type():
            return 3
        elif piece.get_piece_type() == Bishop.get_piece_type():
            return 3
        elif piece.get_piece_type() == Rook.get_piece_type():
            return 5
        elif piece.get_piece_type() == Queen.get_piece_type():
            return 9
        elif piece.get_piece_type() == King.get_piece_type():
            return 100

        return 0
