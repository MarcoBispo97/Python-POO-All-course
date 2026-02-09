class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 4

    @property
    def die(self):
        return self._die
    
    @property
    def counter(self):
        return self._counter
    
    @property
    def is_computer(self):
        return self._is_computer

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.roll()
    
# # Testing the Player class
# if __name__ == "__main__":
#     from Die import Die

#     my_die = Die()

#     my_player = Player(my_die)

#     print("Player:", my_player)
#     print("Die associated with player:", my_player.die)
#     print("Initial counter value:", my_player.counter)
#     print("Value Die: ",my_player.roll_die())

#     die = Die()
#     player = Player(die)

#     print("Player rolling the die...")
#     for _ in range(5):
#         rolled_value = player.roll_die()
#         print(f"Rolled: {rolled_value}, Die value: {player.die.value}")
#         print(f"Player counter before increment: {player.counter}")
#         player.increment_counter()
#         print(f"Player counter after increment: {player.counter}")
#         player.decrement_counter()
#         print(f"Player counter after decrement: {player.counter}")

