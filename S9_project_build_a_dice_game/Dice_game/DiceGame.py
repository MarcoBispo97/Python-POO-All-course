from Player import Player
from Die import Die

class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("================================")
        print("🎲 Welcome to the Dice Game! 🎲 ")
        print("================================")

        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break

    def play_round(self):
        # Welcome the user
        self.print_round_welcome()

        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        #Show the values
        self.show_dice(player_value, computer_value)

        # Determine the winner and loser
        if player_value > computer_value:
            print("😁 You win this round!🥳 ")
            self.update_counters(winner = self._player, loser=self._computer)
        elif player_value < computer_value:
            print("🙁 Computer wins this round! 🤖. Try again.")
            self.update_counters(winner = self._computer, loser=self._player)
        else:
            print("It's a tie!")

        self.show_counters()

    def print_round_welcome(self):
        print("\n--- New Round ---")
        input("🎲 Press any key to roll the dice. 🎲  ")

    def show_dice(self, player_value, computer_value):
        print(f"Your die shows: {player_value}")
        print(f"Computer's die shows: {computer_value}")

    def update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def show_counters(self):
        print(f"Your counter: {self._player.counter}")
        print(f"Computer's counter: {self._computer.counter}")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over_message(winner=self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over_message(winner=self._computer)
            return True
        else:
            return False
    
    def show_game_over_message(self, winner):
        if winner.is_computer:
            print("\n===============================")
            print(" G A M E  O V E R 🌟")
            print("=================================")
            print("🤖 Computer wins the game! Better luck next time. Sorry... ☠️")
            print("=================================")
        else:
            print("\n===============================")
            print(" G A M E  O V E R 🌟")
            print("=================================")
            print("🎉 Congratulations! You won the game! 🎈")
            print("=================================")


player_die = Die()
computer_die = Die()
player = Player(player_die, is_computer=False)
computer = Player(computer_die, is_computer=True)

game = DiceGame(player, computer)
game.play()