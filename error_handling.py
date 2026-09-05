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
    
def multiply(num1, num2):
    try:
        1/num1
        1/num2
        return num1 * num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'Please use Numbers as arguments: {err}')
    finally:
        print('Done')
multiply(0, 5)