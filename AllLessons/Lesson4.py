#conditions (if elif else)
"""
If (it is rainy in outside)
    bring an umbrella
else
    Go without an umbrella
"""
# is_rainy = True
# if is_rainy:
#     print("Is rainy")
# else:
#     print("Is not rainy")

# login = "nazikteshebaeva"
# password = "NT1234"
# if login == "admin" and password == "1234":
#     print("Login successful")
# else:
#     print("Login failed")

# is_cold = True
# if is_cold:
#     print("Take a hot tea")
#
#     is_cold = False
#     print("you are in if")
#
# else:
#   print("you are not in if")

# Theme: Syntaksis of conditions in python, condition if
# age = 18
# if age >= 18:
#     print("You are an adult")
# #The result will be True or False. Code after if will work if the condition is True. IF - ELSE

# age = 16
# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are not an adult")
# #esle works only when the condition if is False. IF - ELIF - ELSE

# score = 85
# if score >= 90:
#     print("Perfect")
# elif score >= 70:
#     print("Good")
# else:
#     print("Try better")
# elif adds additional conditions. The code goes up to down. If is the most important and can go by itself. We can not
# go elif by itself. It goes only after if. There are can be multiple ifs and elifs. Else is conclusion.

# age = 20
# has_license = True
# if age >= 18:
#     if has_license:
#         print("You can drive a car")
#     else:
#         print("Get a drivers license")
# else:
#     print("You are too young to drive")
#if under another if helps to double check the info. Better not to use such kind of double ifs.

#and, or, not
# age = 25
# income = 40000
# if age > 18 and income > 30000:
#     print("You can take a credit")
#and - both conditions have to be True
#or - at lease one condition should be True
#not - inversion of condition

#6 Ternary condition

# age = 20
# message = "Adult" if age >= 18 else "Child"
# print(message)