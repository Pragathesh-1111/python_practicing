while True:
    try:
        age = int(input("What's your age:  "))
        10/age
        print(age)
    except ValueError:
        print("Please enter a number!!!!")
        print("-------------------------")
    except ZeroDivisionError:
        print("Please enter a age higher then 0")
        print("-------------------------")
    else:
        print('Thank you!')
        break