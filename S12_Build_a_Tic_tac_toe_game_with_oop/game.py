from player import Player
from board import Board
from player import Player


class TicTacToeGame:
    def start(self):
        print("================================")
        print("🎮 Welcome to Tic Tac Toe! 🎮 ")
        print("================================")

        board = Board()
        player = Player()
        computer = Player(False)

        board.print_board()
        # ask tje user if he/she would like to play another round
        while True:
            # Get move, check tie, check game over
            while True:
                player_move = player.get_move()
                board.submit_move(player, player_move)
                board.print_board()

                if board.check_is_game_over(player, player_move):
                    print("Congratulations! You won! 🎉")
                    break

                if board.check_is_tie():
                    print("It's a tie! 👍 Try again.")
                    break

                computer_move = computer.get_move()
                board.submit_move(computer, computer_move)
                board.print_board()

                if board.check_is_game_over(computer, computer_move):
                    print("Computer wins! 🤖 Try again.")
                    break

                if board.check_is_tie():
                    print("It's a tie! 👍 Try again.")
                    break
            print("================================")
            play_again = input("Would you like to play again? (y/n): ").upper()
            if play_again != "Y":
                print("Thanks for playing! Goodbye! 👋")
                break
            elif play_again == "Y":
                self.start_new_round(board)
            else:
                print("Invalid input! Please enter 'y' or 'n'.")

    def start_new_round(self, board):
        print("================================")
        print("🎮 Starting a new round! 🎮 ")
        print("================================")
        board.reset_board()
        board.print_board()


game = TicTacToeGame()
game.start()
