# 1  Выведите таблицу умножения на 5
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i * j, end="\t")
#     print()

# 2. Выведите все числа кратные 3 от 1 до 100
# for i in range(1, 101, 3):
#     print(i)

# 3. Запросите у пользователя число и выведите его таблицу умножения
# num1 = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num1} * {i} = {num1 * i}")
#     print()

# 4. Найдите сумму всех чисел от 1 до N (N вводит пользователь)
# N = int(input("Enter a N number: "))
# for i in range(1, N):
#     print(i)

# 5. Выведите числа Фибоначчи до 100: I had to google this.
# a = 0
# b = 1
# while a <= 100:
#     print(a, end=" ")
#     a, b = b, a + b

# 6. Проверьте, является ли введённое число простым!!!
# num1 = int(input("Enter a number: "))
# if num1 % 2 == 0:

# 7. Переверните строку, введённую пользователем
# string1 = input("Enter a sentence: ")
# reversed_string = string1[::-1]
# print(reversed_string)

# 8. Посчитайте количество гласных букв в строке
# string1 = input("Enter a sentence: ")
# vowels = "aeiouAEIOU"
# count = sum(1 for character in string1 if character in vowels)
# print(count)

# 9. Посчитайте сумму цифр числа
# numbers = input("Enter a number: ")
# print(sum(int(d) for d in numbers if d.isdigit()))

# 10. Запросите у пользователя строку и выведите её без гласных
# string1 = input("Enter a sentence: ")
# vowels = "aeiouAEIOU"
# string2 = ''.join(character for character in string1 if character not in vowels)
# print(string2)

# # 11. Сгенерируйте список из 10 случайных чисел и выведите их среднее значение
# list1 = [2, 3, 6, 8, 5, 8, 2, 5, 8, 9]
# average = sum(list1) / len(list1)
# print(average)

# 12. Определите, является ли введённая строка палиндромом
# string1 = input("Enter a word: ")
# if string1 == string1[::-1]:
#     print("This is a palindrome")
# else:
#     print("This is not a palindrome")

# 13. Используйте while для создания обратного отсчёта от 10 до 1
# num1 = 10
# while num1 > 0:
#     print(num1)
#     num1 -=1

# 14. Выведите квадраты всех чётных чисел от 1 до 50
# for num in range(1, 51):
#     if num % 2 == 0:
#         print(num ** 2)

# 15. Найдите максимальное число в списке
# list1 = [23, 56, 34, 57]
# print(max(list1))

# 16. Выведите все пары чисел от 1 до 10, сумма которых равна 10
# for i in range(1, 11):
#     for j in range(1, 11):
#         if i + j == 10:
#             print(i, j)

# 17. Запросите у пользователя 5 чисел и выведите их среднее
# numbers = input("Enter 5 numbers: ")
# if len(numbers) == 5:
#     numbers = [int(num) for num in numbers]
#     average = sum(numbers) / 5
#     print(average)
# else:
#     print("Please, enter 5 numbers")

# 18. Используйте цикл while, чтобы угадать число, загаданное программой!!!
# number = input("Enter a number: ")
# while number > 0:
#     print(number)
#     number += 1

# 19. Сгенерируйте таблицу квадратов чисел от 1 до 10
# for num in range(1, 11):
#     print(num ** 2)

# 20. Найдите количество чётных и нечётных чисел в списке
# numbers = [int(input("Enter numbers: "))]
# even_num = 0
# odd_num = 0
# for num in numbers:
#     if num % 2 == 0:
#         even_num += 1
#     else:
#         odd_num += 1
# print(even_num)
# print(odd_num)

# 21. Определите наибольший общий делитель (НОД) двух чисел I dont know how to do this!!!

# 22. Найдите все простые числа в диапазоне от 1 до 100 had to look at google
# for num in range(1, 101):
#     is_prime = True
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#         if is_prime:
#             print(num, end=" ")

# 23. Создайте список из первых 10 чисел Фибоначчи !!!
# fib = [0, 1]
# for i in range(1, 11):

# 24. Подсчитайте, сколько раз встречается определённая буква в строке
# word = input("Enter a word: ")
# letter = input("Enter a letter to count: ")
# count = 0
# for char in word:
#     if char == letter:
#         count += 1
# print(count)

# 25. Найдите сумму элементов списка, которые больше 10
# numbers = [5, 12, 7, 15, 3, 20]
# total = 0
# for num in numbers:
#     if num > 10:
#         total += num
#     print(total)

# 26. Проверьте, являются ли два введённых слова анаграммами
# word1 = input("Enter the first word: ")
# word2 = input("Enter the second word: ")
# if sorted(word1) == sorted(word2):
#     print("Words are anagrams")
# else:
#     print("Words are not anagrams")

# 27. Создайте программу, которая заменяет все пробелы в строке на подчеркивания
# str1 = input("Enter a word: ")
# str1 = str1.replace(" ", "_")
# print(str1)

# 28. Определите, сколько раз в строке встречается определённое слово!!!
# str1 = input("Enter a sentence: ")
# word = input("Enter the word to count: ")
# count = str1.split().count(word)
# print(count)

# 29. Напишите программу, которая считает, сколько раз в строке встречаются цифры
# password = input("Enter your password: ")
# digit_count = sum(1 for character in password if character.isdigit())
# print(digit_count)

# 30. Используйте цикл while, чтобы находить сумму вводимых пользователем чисел, пока он не введёт "стоп"!!!
# user_input = input("Enter a number or 'stop' to finish")
# while True:
