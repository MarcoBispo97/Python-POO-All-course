from main import Move
from player import Player
class Board:

    EMPTY_CELL = 0

    def __init__(self):
        self.game_board = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
            ]
        
    def print_board(self):
        print('\n')
        self.print_board_with_positions()

    def print_board_with_positions(self):
        print("Positions:\n")
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n")

        print("Board:\n")
        for row in self.game_board:
            print("|", end="")
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |", end="")
                else:
                    print(f" {column} |", end="")
            print()

    def submit_move(self, player, move):
        row = move.get_row()
        col = move.get_column()
        value = self.game_board[row][col]

        if value == Board.EMPTY_CELL:
            self.game_board[row][col] = player.marker
        else:
            print("This position is already ttaken. Please enter another one")

        

board = Board()
player = Player()
move = Move(5)

print(move)

board.print_board()
board.submit_move(player, move)
board.print_board()