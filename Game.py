from Logic import Logic
from AI import AI
from Piece import Piece
from King import King
from Move import Move
import re

class Game:
    def __init__(self):
        pass

    def get_valid_user_move(self, board, user_color):
        while True:
            move = self.get_user_move()
            if any(move.equals(possible_move) for possible_move in board.get_possible_moves(user_color)):
                break
            else:
                print("Wrong move")
        return move

    def letter_to_x(self, letter):
        letter = letter.lower()
        return ord(letter) - ord('a')

    def choose_player_color(self):
        player_color = input("Choose your color (white or black): ").lower()
        if player_color == "white" or player_color == "black":
            return player_color
        else:
            print("Invalid color choice. Please choose 'white' or 'black'.")

    def get_user_move(self):
        print("Type your move for example: d2->d3")
        move_str = input("Your Move: ")

        if len(move_str) != 6 or not re.match(r'^[a-h][1-8]->[a-h][1-8]$', move_str):
            print("Invalid move format. Please enter a move in the format 'a2->a4'.")
            return self.get_user_move()

        xfrom = self.letter_to_x(move_str[0])
        yfrom = 8 - int(move_str[1])
        xto = self.letter_to_x(move_str[4])
        yto = 8 - int(move_str[5])
        return Move(xfrom, yfrom, xto, yto)

    def play(self):
        board = Logic.new_board()
        board.print_board()
        player_color = self.choose_player_color()

        while True:
            if player_color == "white":
                move = self.get_valid_user_move(board, Piece.WHITE)
                board.move_check_rules(move)

                if board.is_king_in_check(King.BLACK):
                    print("Check")
                if board.is_checkmate(King.BLACK):
                    print("Checkmate!")
                    break
                if board.is_stalemate(King.BLACK):
                    print("Stalemate!")
                    break

                board.print_board()

                ai_move = AI.get_ai_move(board, [], Piece.BLACK)

                board.move_check_rules(ai_move)

                if board.is_king_in_check(King.WHITE):
                    print("Check")
                if board.is_checkmate(King.WHITE):
                    print("Checkmate!")
                    break
                if board.is_stalemate(King.WHITE):
                    print("Stalemate!")
                    break

                board.print_board()
                print("AI move: " + ai_move.to_string())

            else:
                move = self.get_valid_user_move(board, Piece.BLACK)

                board.move_check_rules(move)

                if board.is_king_in_check(King.WHITE):
                    print("Check")
                if board.is_checkmate(King.WHITE):
                    print("Checkmate!")
                    break
                if board.is_stalemate(King.WHITE):
                    print("Stalemate!")
                    break

                board.print_board()

                ai_move = AI.get_ai_move(board, [], Piece.WHITE)

                board.move_check_rules(ai_move)

                if board.is_king_in_check(King.BLACK):
                    print("Check")
                if board.is_checkmate(King.BLACK):
                    print("Checkmate!")
                    break
                if board.is_stalemate(King.BLACK):
                    print("Stalemate!")
                    break

                board.print_board()
                print("AI move: " + ai_move.to_string())





