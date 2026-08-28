# print("Welcome! You are using 'Number Greater'")
#
# while True:
#     try:
#         n1 = input("Enter your first value:")
#         n1_c = int(n1)
#         break
#     except:
#         print("That is wrong value. Try again!")
#
# while True:
#     try:
#         n2 = input("Enter your second value:")
#         n2_c = int(n2)
#         break
#     except:
#         print("That is wrong value. Try again!")
#
#
# if n1_c > n2_c:
#     print("n1 is the biggest")
# elif n1_c == n2_c:
#     print("they are equal")
# elif n1_c < n2_c:
#     print("n2 is the biggest")
# else:
#     print("Invalid numbers")


n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))

if n1 > n2 and n1 > n3:
    print(f"Number 1: {n1} is the biggest")

elif n2 > n1 and n2 > n3:
    print(f"Number 2: {n2} is the biggest")

else:
    print(f"Number 3 {n3} is the biggest")

