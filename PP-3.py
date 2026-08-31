def calculator():
    print("Thank for choosing Dauren's calculator!")
    while True:
        try:
            first_value = input("Enter your first value:")
            first_value_f = int(first_value)
            break
        except:
            print("Wrong value! Try again.")

    while True:
        try:
            second_value = input("Enter your second value:")
            second_value_f = int(second_value)
            break

        except:
            print("Wrong value! Try again.")

    while True:
            operator = input("Enter your math operator:")
            if operator == "+":
                break
            elif operator == "-":
                break
            elif operator == "*":
                break
            elif operator == "/":
                break
            else:
                print("Wrong math operator! Try again.")

    if operator == "+":
        result = first_value_f + second_value_f
    elif operator == "-":
        result = first_value_f - second_value_f
    elif operator == "*":
        result = first_value_f * second_value_f
    elif operator == "/":
        result = first_value_f / second_value_f

    return (f"The answer from value {first_value_f} and {second_value_f} with operator"
            f" {operator} is {result}")

print(calculator())


