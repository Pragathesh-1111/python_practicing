# name = input('What is your name?\n')
# print(f"Helloooo {name}")

# FUNDAMENTAL Data Types #
int
float
bool
str
list
tuple
set
dict
complex

# Classes -> custom types

# Specialized Data types

None

# -------------------------- #
# print(type(2 + 2))
# print(type(2 - 5))
# print(type(2 * 3))
# print(type(2 / 4))

# print(2**4)
# print(7//3)
# print(41 % 3)

# round()
print(round(3.1))
print(round(3.5))

# abs()
print(abs(-20))

# -------------------------- #
print((20 - 3) + 2 ** 2)

# ()
# **
# *
# /
# +
# -

print(bin(19))
print(int('0b10011', 2))

# -------------------------- #
first_name = 'Pragathesh'
last_name = first_name
print(last_name)

print(type(True))
print(type(10 > 9))
print(10 == '10')
print(10 == 10)

# ---------------------------------------------- #
# print('------------------------------')
# is_old = True
# is_licenced = True

# # if is_old:
# #     print('You are old enough to drive!✅')
# # elif is_licenced:
# #     print('You have a license')
# # else:
# #     print('You are not old enough to drive!❌')
# # print('Default')

# if is_old and is_licenced:
#     print('You are old enough to drive!✅')
#     print('You have a license')
# else:
#     print('You are not allowed to drive!❌')

# adult = 18
# person1 = {
#     'name':'Praga',
#     'age': 11
# }

# print('ADULT') if person1['age'] >= adult else print('NOT ADULT')

# print('----------------')

# is_magician = False
# is_expert = True

# if is_magician and is_expert:
#     print('you are a master magician')

# elif is_magician and not is_expert:
#     print('atleast you are getting there')
# else:
#     print('you need some magic')


def calculate_age(born_year):
    calculation = 2026 - born_year
    print(calculation)


calculate_age(2006)
# =================================
tree_image = [
    (0, 0, 0, 1, 0, 0, 0),
    (0, 0, 1, 1, 1, 0, 0),
    (0, 1, 1, 1, 1, 1, 0),
    (1, 1, 1, 1, 1, 1, 1),
    (0, 0, 0, 1, 0, 0, 0),
    (0, 0, 0, 1, 0, 0, 0)
]


def draw_tree_from_pixels(data):
    for row in data:
        for pixel in row:
            if (pixel):
                print('*', end="")
            else:
                print(' ', end="")
        print('')


draw_tree_from_pixels(tree_image)
draw_tree_from_pixels(tree_image)

# =================================


def test(a):
    '''
        This function tests and prints the param 'a'
    '''
    if (a):
        print(a)


test('!!!!')
print(test.__doc__)


def is_even(num):
    return True if num % 2 == 0 else False


def is_even_clean_func(num):
    return num % 2 == 0
# =================================


print(is_even(93))
print(is_even(60))
print(is_even_clean_func(93))
print(is_even_clean_func(60))


def super_func(*args, **kwargs):
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))

# -- params, *args, default parameters, **kwargs --#
# =================================


def highest_even(li):
    evens = [item for item in li if item % 2 == 0]
    return max(evens) if evens else None


print(highest_even([]))
print(highest_even([2, 3, 2, 1, 4, 5, 6, 3, 3, 6, 9, 10]))
print(highest_even([-2, 2]))
print(highest_even([-2, -24]))

# =================================

grades = [55, 72, 80, 45]
results = ["Pass" if g >= 60 else "fail" for g in grades]
print(results)


# =================================

a = 'helloooooooooooo'
if ((n := len(a)) > 10):
    print(f"Too long {n} elements")

b = 'hellooooooooo'
while ((n := len(b)) > 1):
    print(n)
    b = b[:-1]

# =================================

class BigObject:
    pass

obj1 = BigObject()
print(type(obj1))