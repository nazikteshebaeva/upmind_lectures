#1
# login1 = input("Enter your login: ")
# password1 = input("Enter your password: ")
#
# if login1 == "admin" and password1 == "1234":
#     print("Access was successful")
# else:
#     print("Access denied, please try again. Two tries left.")
#     login1 = input("Enter your login: ")
#     password1 = input("Enter your password: ")
#     if login1 == "admin" and password1 == "1234":
#         print("Access denied")
#     else:
#         print("Access denied, please try again. One try left.")
#         login1 = input("Enter your login: ")
#         password1 = input("Enter your password: ")
#         if login1 == "admin" and password1 == "1234":
#             print("Access granted")
#         else:
#             print("Wrong Password")


#2
# visa = input("Do you have visa? ")
# citizenship = input("Do you have a citizenship? ")
# passport = input("Is your passport valid? ")
# if (visa == "yes" or citizenship == "yes") and passport == "yes":
#     print("Access granted")
# else:
#     print("Access denied")


#3
# year = int(input("Which year is it? "))
# if year % 4 == 0 and year != 100 or year % 400 == 0:
#     print("Leap Year")
# else:
#     print("Usual Year")

#4
# password = input("What is the password")
# if password >= "8 symbols and has number":
#     print("Strong password")
# else:
#     print("Weak password")

# password = input("What is the password? ")
# if password.isalnum() and len(password) >= 8:
#     print("Strong Password")
# else:
#     print("Weak Password")

#5
# temperature = int(input("Enter the temperature of the water: "))
# if temperature <= 0:
#     print("Ice")
# elif 1 <= temperature <= 99:
#     print("Liquid")
# elif temperature >= 100:
#     print("Steam")

#6
# income = int(input("Enter your income: "))
# if income <= 10000:
#     print(income * 0.05)
# elif 10001 <= income <= 50000:
#     print(income * 0.1)
# elif income >= 50000:
#     print(income * 0.2)

#7
# game = "rock, scissors, paper"
# comp = input("Enter computer's version")
# user = input("Enter user's version")
# if comp == user:
#     print("draw")
# elif comp == "paper" and user == "scissors":
#     print("User Won!")
# elif comp == "scissors" and user == "rock":
#     print("User Won!")
# elif comp == "rock" and user == "scissors":
#     print("User Failed!")

#8!
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = (num1 + num2)
# if num3 % 2 == 0:
#     print("Sum is even")
# else:
#     print("Sum is odd")

#9
# car = input("Enter the type of the car: ")
# if car == "Electro":
#     print("Free parking")
# else:
#     print("Fine 100 rubles")

#10!
# num1 = int(input("Enter a number a: "))
# num2 = int(input("Enter a number b: "))
# if num1 % num2 == 0:
#     print("a = b")
# else:
#     print("a != b")

#11!
# ticket = int(input("Enter a 6 digits number: "))
# if len(ticket) == 6 and ticket.isdigit():
#     first_half = sum(int(digit) for digit in ticket[:3])
#     second_half = sum(int(digit) for digit in ticket[3:])
#     if first_half == second_half:
#         print("You won!")


#12
# num = int(input("Enter a number of the month: "))
# print("winter" if num == 12 or num == 1 or num == 2 else "spring" if num == 3 or num == 4 or num == 5 else "summer" if num == 6 or num == 7 or num == 8 else "autumn")

#13
# num = int(input("Enter a number: "))
# print("+" if num > 0 else "-" if num < 0 else "0")

# sign = (works when the condition is True) if the condition is else (works when condition is False)

# #14
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
#
# print(num1 if num1 < num2 and num1 < num3 else "Wrong answer")

# #15
# score = int(input("Enter your average score: "))
# print("Perfect" if score >= 85 else "Good" if 70 <= score <= 84 else "Not bad" if 50 <= score <= 69 else "Bad")

#16
# row = int(input("Enter a number of the row: "))
# seat = int(input("Enter a number of the seat: "))
# if row <= 3:
#     print("VIP-zone")
# elif 4 <= row <= 10:
#     print("Middle row")
# else:
#     print("Budget row")

#17
# date = int(input("Enter a number from 1 to 7: "))
# if date 1:
#     print("Monday")
# elif date 2:
#     print("Tuesday")
# elif date 3:
#     print("Wednesday")
# elif date 4:
#     print("Thursday")
# elif date 5:
#     print("Friday")
# elif date 6:
#     print("Saturday")
# elif date 7:
#     print("Sunday")

#18


#19
# num1 = 45
# num2 = 56
# num3 = 1
# print(min to max (num1, num2, num3))

#20
# age = 40
# if age <= 18:
#     print("Access available")
# else:
#     print("Access declined")