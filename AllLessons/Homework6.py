#1
# numbers = [1, 2, 3, 4, 5]
# print(numbers[0] + numbers[-1])

#2
# num = int(input("Enter a number: "))
# if num / 3 == 0 and num / 5 == 0:
#     print("Yes")
# else:
#     print("No")

#3
# numbers = [5, 10, 15, 20, 25]
# if 20 in numbers:
#     print("Yes")
# else:
#     print("No")

#4
# string1 = "python"
# if string1 == "Python":
#     print("The word does start with capital letter")
# else:
#     print("The word does not start with capital letter")
#     print(string1.capitalize())

#5
# string = input("Enter a words: ")
# print(string[::-1])

#6
# numbers = [5, 10, 15, 20]
# print(numbers[0] + numbers[1] + numbers[2] + numbers[3])
# print(numbers[0] * numbers[1] * numbers[2] * numbers[3])

#7
# num1 = 58
# num2 = 67
# num3 = 90
# if num1 >= num2 >= num3:
#     print("The max is num1")
# elif num1 <= num2 >= num3:
#     print("The max is num2")
# else:
#     print("The max is num3")

#8
# string = input("Enter a number: ")
# if string.isdigit() and int(string) >= 0:
#     print("The number is digital and positive number")
# else:
#     print("The number is string and negative number")

#9
# names = ["Anna", "Boris", "Aleksey", "Vika"]
# if "Aleksey" in names:
#     print("Aleksey was found")

#10
# string = input("Enter a word: ")
# if " " in string:
#     print("Yes")
# else:
#     print("No")

#11
# strings = [True, False, True, False, True]
# print(strings.count(True))

#12
# string = input("Enter the sentence: ")
# print(string.replace(" ", "-"))

#13
# numbers = [1, 2, 3, 4, 5]
# print(numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4])
# num1 = (numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4])
# num2 = len(numbers)
# print(num1 / num2)

#14
# string = input("Enter a word: ")
# if len(string) >= 10:
#     print(string[0:10], "...")

#15
# string = input("Enter a word: ")
# print(string.isalnum())

#16
# numbers = [1, -2, 3, -4, 5]
# print(abs(numbers[1]), abs(numbers[3]))

#17
# string = ["a", "b", "c", "d", "e"]
# print(string[0], string[1], string[2], string[3], string[4])

#18
# num1 = int(input("Enter a number: "))
# if num1 % 2 == 0:
#     print("Yes")
# else:
#     print("No")

#19
# email = "teshebaevanazik99@gmail.com"
# if "@" in email:
#     print("Yes")
# else:
#     print("No")

#20
# string = "hello world"
# if string.isupper():
#     print("Uppercase")
# else:
#     print("Lowercase")

#21
# string = input("Enter a string: ")
# print(string.swapcase())

#22 - try to use another method to make it easier.
# numbers = [5, -3, 7, -1, 0]
# if numbers[0] >= numbers[1]:
#     print("Index 0 is max")
# elif numbers[1] >= numbers[2]:
#     print("Index 1 is max")
# elif numbers[2] >= numbers[3]:
#     print("Index 2 is max")
# else:
#     print("Index 4 is max")
  #too many numbers to work on lol

#23
# num1 = 34
# num2 = 45
# print(num1 if num1 >= num2 else num2)

#24
# string = " Python Programming "
# print(string.lstrip())
# print(string.rstrip())

#25
# string = input("Enter a word: ")
# if len(string) == 0:
#     print("String is empty")
# else:
#     print("String has a word")

#26
# string = ["tea", "juice", ""]
# if "" in string:
#     print("Yes")
# else:
#     print("No")

#27
# a = 45
# b = 67
# print(a + b)
# summ1 = (a + b)
# if summ1 >= 100:
#     print("The summ is more than 100")
# else:
#     print("The summ is less or equal to 100")

#28
# string = input("Enter a sentence: ")
# print(string.replace("a", "*"))
# print(string.replace("e", "*"))
# print(string.replace("i", "*"))
# print(string.replace("o", "*"))
# print(string.replace("u", "*"))
# print(string.replace("y", "*"))

#29
# numbers = [1, 2, 3, 4, 5]
# print(sum(numbers))
# num1 = sum(numbers)
# if num1 >= 50:
#     print("A big number")
# else:
#     print("Not a big number")

#30
# x = 34
# y = 23
# print(x * y)
# num1 = (x * y)
# if num1 >= 100:
#     print(num1)
# else:
#     print(x + y)

#31
# string = input("Enter a sentence: ")
# print(string.replace(".", ""))
# print(string.replace(",", ""))
# print(string.replace("?", ""))
# print(string.replace("!", ""))

#32
# words = "apple"
# words1 = "grapes"
# words2 = ""
# if words == "" or words1 == "" or words2 == "":
#     print("There is an empty string")

#33
# numbers = int(input("Enter a number: "))
# if numbers >= 0:
#     print("The number is positive")
# elif numbers <= 0:
#     print("The number is negative")
# else:
#     print("The number is equal to 0")

#34
# string = input("Enter a word: ")
# if string.startswith("A"):
#     print("The string starts with an A")

#35
# num1 = 34
# num2 = 56
# num3 = 78
# print(num1 * num2 * num3)
# num4 = (num1 * num2 * num3)
# if num4 >= 1000:
#     print(num1 * num2 * num3)
# else:
#     print(num1 + num2 + num3)

#36
# string = input("Enter a string: ")
# print(string.isdigit())

#37
# str1 = "Nazar"
# str2 = "apple"
# str3 = ""
# if str1.istitle() or str2.istitle() or str3.istitle():
#     print("There is a titled string")

#38
# string = "restaurant"
# print(string.upper())

#39
# string = input("Enter a string: ")
# if string == string[::-1]:
#     print("Yes")
# else:
#     print("No")

#40
# string = input("Enter a word: ")
# print(len(string))
# if len(string) % 2 == 0:
#     print("string[len(string) // 2")
# else:
#     print("string[len(string) // 2 - 1 ")