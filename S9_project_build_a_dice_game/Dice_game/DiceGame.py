from Player import Player
from Die import Die

class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("================================")
        print("🎲:-Welcome to the Dice Game!-:🎲")
        print("================================")

        while True:
            self.play_round()
            # TODO: Implement game over

    def play_round(self):
        # Welcome the user
        print("--- New Round ---")
        input("🎲:-Press any key to roll the dice.-:🎲")

        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        #Show the values
        print(f"Your die shows: {player_value}")
        print(f"Computer's die shows: {computer_value}")

        # Determine the winner and loser
        if player_value > computer_value:
            print("😁-You win this round!🥳-")
            self._player.decrement_counter()
            self._computer.increment_counter()
        elif player_value < computer_value:
            print("🙁-Computer wins this round!-🤖. Try again.")
            self._player.increment_counter()
            self._computer.decrement_counter()
        else:
            print("It's a tie!")

        # Show the counters
        print(f"Your counter: {self._player.counter}")
        print(f"Computer's counter: {self._computer.counter}")

player_die = Die()
computer_die = Die()
player = Player(player_die)
computer = Player(computer_die, is_computer=True)

game = DiceGame(player, computer)
game.play()