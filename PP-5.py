
# for i in range(1, 11):
#     result = 3 * i
#     print(f"3 * {i} = {result}")

def mult_chart():
    print("Welcome! Thank you for using Dauren's multiplication chart")
    while True:
        try:
            first_value = input("Enter the value you want to have mult chart for: ")
            first_value_f = int(first_value)
            break
        except:
            print("You entered wrong value. Try Again!")

    while True:
        try:
            second_value = input("Enter the value you want your chart to go for: ")
            second_value_f = int(second_value)
            break
        except:
            print("You entered wrong value. Try Again!")

    for i in range(1, second_value_f+1):
        result = first_value_f * i
        print(f"{first_value_f} * {i} = {result}")

print("Thank for using Dauren's calculator!")
def calucaltor():
    print(""
          " Addition - 1."
          " Substruction - 2."
          " Multiply - 3."
          " Divide - 4."
          " Exit - 0."
          "")
    while True:
        try:
            answer = input("Enter what you want to do(0-4): ")
            answer_f = int(answer)
            break
        except:
            print("Wrong value. Try again!")

    if answer_f == 1:
        print("You chose Addition!")
        while True:
            try:
                first_value = input("Enter your first value: ")
                first_value_f = int(first_value)
                break
            except:
                print("Wrong value. Try again!")

        while True:
            try:
                second_value = input("Enter your second value: ")
                second_value_f = int(second_value)
                break
            except:
                print("Wrong value. Try again!")

        result = first_value_f + second_value_f
        print(f"The result of {first_value_f} + {second_value_f} = {result}")
        calucaltor()

    if answer_f == 2:
        print("You chose Sub!")
        while True:
            try:
                first_value = input("Enter your first value: ")
                first_value_f = int(first_value)
                break
            except:
                print("Wrong value. Try again!")

        while True:
            try:
                second_value = input("Enter your second value: ")
                second_value_f = int(second_value)
                break
            except:
                print("Wrong value. Try again!")

        result = first_value_f - second_value_f
        print(f"The result of {first_value_f} - {second_value_f} = {result}")
        calucaltor()

    if answer_f == 3:
        print("You chose Multiplication!")
        while True:
            try:
                first_value = input("Enter your first value: ")
                first_value_f = int(first_value)
                break
            except:
                print("Wrong value. Try again!")

        while True:
            try:
                second_value = input("Enter your second value: ")
                second_value_f = int(second_value)
                break
            except:
                print("Wrong value. Try again!")

        result = first_value_f * second_value_f
        print(f"The result of {first_value_f} * {second_value_f} = {result}")
        calucaltor()

    if answer_f == 4:
        print("You chose Division!")
        while True:
            try:
                first_value = input("Enter your first value: ")
                first_value_f = int(first_value)
                break
            except:
                print("Wrong value. Try again!")

        while True:
            try:
                second_value = input("Enter your second value: ")
                second_value_f = int(second_value)
                break
            except:
                print("Wrong value. Try again!")

        result = first_value_f / second_value_f
        print(f"The result of {first_value_f} : {second_value_f} = {result}")
        calucaltor()

    if answer_f == 0:
        print("You chose Exit!")
        print("Thanks you for choosing Dauren's calculator. See you soon!")
        exit()

calucaltor()




