class PlayerCharacters:
    membership = True

    def __init__(self, name, age, email):
        self._name = name
        self._age = age
        self.email = email

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


# player1 = PlayerCharacters('Praga', 21)
# player1.run(100)
# print(player1.membership)
# player1.print_self()
# player1.adding_nums(9, 2)
# PlayerCharacters.adding_nums(9, 2)
# player1.greet_class()


class OfflinePlayers(PlayerCharacters):
    membership = False
    
    def __init__(self, name, age, email, offline_timing):
        super().__init__(name, age, email)
        self.offline_timing = offline_timing

class OnlinePlayers(PlayerCharacters):
    membership = True
    
    def __init__(self, name, age, email):
        super().__init__(name, age, email)

off_player = OfflinePlayers("Praga", 20,"praga@gmail.com", '15:30')
off_player.run(10)

online_player1 = OnlinePlayers("jonas", 33, "jonas@gmail.com")
online_player1.run(90)