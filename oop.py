class PlayerCharacters:
    membership = True

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self, speed):
        print(f"{self._name} runs at {speed} km/h")

    def print_self(self):
        print(self.__dict__)

    @classmethod
    def adding_nums(cls, num1, num2):
        print(num1 + num2)

    def greet_class():
        print("hello")

    @staticmethod
    def greet():
        print("hello")


player1 = PlayerCharacters('Praga', 21)
player1.run(100)
print(player1.membership)
player1.print_self()
player1.adding_nums(9, 2)
PlayerCharacters.adding_nums(9, 2)
player1.greet_class()


class OfflinePlayers(PlayerCharacters):
    membership = False


off_player = OfflinePlayers("offline1", 12)

off_player.run(10)
