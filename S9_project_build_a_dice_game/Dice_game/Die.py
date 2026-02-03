import random
class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value

# Testing the Die class
if __name__ == "__main__":
    die = Die()
    print("Rolling the die...")
    for _ in range(5):
        print(die.roll())
        print(die.value)
        rolled_value = die.roll()
        print(f"Rolled: {rolled_value}, Die value: {die.value}")