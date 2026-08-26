print("Enter your legal name:")
employee_name = input()
def basic_pay_enter():
    print("Enter your basic pay")
    try:
        basic_pay = int(input())
    except:
        print(f"That is not number! Try again")
        basic_pay_enter()

basic_pay_enter()

deductions = 200

total_pay = basic_pay - 200

print(f"{employee_name}'s total pay is {total_pay}$")