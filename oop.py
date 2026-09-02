from functools import reduce


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


off_player = OfflinePlayers("Praga", 20, "praga@gmail.com", '15:30')
off_player.run(10)

online_player1 = OnlinePlayers("jonas", 33, "jonas@gmail.com")
online_player1.run(90)

# ======================= #


def multiplyby_2(item):
    return item * 2


new_list = list(map(multiplyby_2, [1, 2, 3]))
print(new_list)

my_list = [1, 2, 3, 4]
your_list = [13, 52, 23]
print(list(zip(my_list, your_list)))


reduce_func = reduce(lambda acc, curr: acc + curr, my_list, 0)
print(reduce_func)


def accumulator(acc, item):
    return acc + item


reduce_func = reduce(accumulator, my_list, 0)

print(reduce_func)

a = [(1, 2), (93, 5), (6, -7)]
a.sort(key=lambda x: x[0])
print(a)

b = [('a', 'b'), ('o', 'p'), ('e', 'q')]
b.sort(key=lambda letter: letter[0])
print(b)


# list comprehensions
my_list1 = [char for char in "Pragatheshwaran"]
my_list2 = [num for num in range(0,100) if num % 2 == 0]
print(my_list1)
print(my_list2)

my_list = ['a', 'b', 'b', 'd', 'e', 'r', 'e']
duplicate = list(set(letter for letter in my_list if my_list.count(letter) > 1))
print(duplicate)