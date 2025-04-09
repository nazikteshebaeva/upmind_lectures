# Контрольная работа по пройденным темам Python

# === Комментарии, int, str, bool, float ===


# --- Базовые ---

# 1. Создай переменную 10 и выведи её.
# num = 10
# print(num)

# 2. Создай строку 'Привет' и выведи её длину.
# str1 = "Hello"
# print(len(str1))

# 3. Дано число 42. Преобразуй его в строку, а затем обратно в число.
# num = 42
# num1 = str(42)
# print(num1)
# num2 = int(num1)
# print(num2)

# 4. Создай переменную x = 42. Проверь её тип с помощью type().
# x = 42
# print(type(x))

# 5. Создай переменную is_active = True и выведи её.
# is_active = True
# print(is_active)

# --- Средние ---

# 6. Дано число 18. Проверь, является ли оно чётным.
# num = 18
# print(num % 2 == 0)

# 7. Даны числа 10 и 3.14. Выведи результат их сложения.
# num = 10
# num1 = 3.14
# print(num + num1)

# 8. Даны числа 10, 20, 30. Найди их среднее арифметическое и выведи результат.
# num = 10
# num1 = 20
# num2 = 30
# sum1 = num + num1 + num2
# print(sum1)
# summ = sum1 // 3
# print(summ)

# 9. Дана строка "Привет, как дела?". Проверь, начинается ли она с заглавной буквы. !
# str1 = "hello, how are you?"
# print(str1.istitle())

# 10. Даны переменные 'Анна' и 25. Используй f-строку, чтобы вывести: 'Меня зовут Анна и мне 25 лет.'
# name = "Anna"
# age = 25
# print(f"My name is {name}, I am {25} years old")

# --- Сложные ---

# 11. Дано число 123.456. Выведи только его дробную часть.
# num = 123.456
# num1 = num - int(num)
# print(str(num1)[2:5])

# 12. Даны строки '123' и 'abc'. Проверь для каждой, состоит ли она только из цифр.
# str1 = "123"
# str2 = "abc"
# print(str1.isdigit())
# print(str2.isdigit())

# 13. Преобразуй строку '123.45' в число, прибавь 1 и выведи результат.
# num1 = float("123.45")
# print(num1 + 1)

# 14. Дана строка ''. Проверь, является ли она пустой.!!!
# str1 = ""

# 15. Дана строка 'Hello World'. Приведи её к нижнему регистру и проверь, есть ли подстрока 'world'.
# str1 = "Hello World"
# str2 = str1.lower()
# print(str2)
# print("world" in str2)

# === Методы int, str, bool, float ===


# --- Базовые ---

# 1. Дана строка 'hello world'. Выведи её в верхнем регистре с помощью метода .upper()
# sentence = "hello world"
# print(sentence.upper())

# 2. Дана строка '123abc'. Проверь, состоит ли она только из цифр, используя метод .isdigit()
# num = "123abc"
# print(num.isdigit())

# 3. Дано число 7.89. Округли его до ближайшего целого с помощью round()
# num = 7.89
# print(round(7.89))

# 4. Дана строка 'Python'. Определи, состоит ли она только из букв (без пробелов и цифр)
# word = "Python"
# print(word.isalpha())

# 5. Дана строка 'hello world'. Замени в ней все пробелы на подчёркивания с помощью .replace()
# sentence = "hello world"
# print(sentence.replace(" ", "-"))

# --- Средние ---

# 6. Дана строка 'banana' и символ 'a'. Выведи индекс первого вхождения символа в строку
# fruit = "banana"
# letter = "a"
# print(fruit.index(letter))

# 7. Дана строка 'Python is awesome'. Раздели её на список слов с помощью .split() и выведи результат
# sentence = "Python is awesome"
# print(sentence.split())

# 8. Даны строки 'Hello' и 'hello'. Проверь, равны ли они между собой без учёта регистра символов !!!
# word = "Hello"
# word1 = "hello"
# if word.lower() == word1.lower():
#     print("The same")
# else:
#     print("They are not the same")

# 9. Дано число 3.141592. Округли его до двух знаков после запятой
# num = 3.121592
# print(round(num, 2))

# 10. Дана строка 'python'. Проверь, состоит ли она только из строчных букв
# str1 = "python"
# print(str1.islower())

# --- Сложные ---

# 11. Дана строка 'level'. Проверь, является ли она палиндромом.
# word = "level"
# print(word == word[::-1])

# 12. Дана строка 'hello world'. Проверь, начинается ли она с 'hello' и заканчивается ли на 'world'.
# sentence = "hello world"
# print(sentence.startswith("hello"))
# print(sentence.endswith("world"))

# 13. Дана строка '456'. Проверь, можно ли её преобразовать в int без ошибки. !!!
# str1 = "456"
# print(int(str1))

# 14. Дана строка 'banana'. Посчитай, сколько раз в ней встречается буква 'a'.
# str1 = "banana"
# print(str1.count("a"))

# 15. Дана строка '10 20 30'. Преобразуй её в список чисел и выведи их сумму.!!!
# str1 = "10 20 30"
# split
# int
# num = list(str1)
# print(num)
# print(sum(num))

# === Условные конструкции (if, elif, else, логика) ===


# --- Базовые ---

# 1. Дано число -7. Напиши программу, которая проверяет, положительное ли оно.
# num = -7
# if num > 0:
#     print("Number is positive")
# else:
#     print("Number is not positive")

# 2. Даны числа 15 и 22. Выведи большее из них.
# num = 15
# num1 = 22
# if num > num1:
#     print("Error")
# else:
#     print("22 is bigger than 15")

# 3. Дано число 13. Проверь, чётное оно или нечётное.
# num = 13
# if num % 2 == 0:
#     print("Number is even")
# else:
#     print("Error")

# 4. Дано значение 17. Если возраст >= 18, выведи 'взрослый', иначе — 'ребёнок'.
# age = 17
# if age >= 18:
#     print("Adult")
# else:
#     print("Child")

# 5. Дана строка 'hello'. С помощью тернарного оператора выведи 'короткая' если длина < 10, иначе 'длинная'.
# word = "hello"
# print("short" if len(word) < 10 else "long")

# --- Средние ---

# 6. Дана строка 'abracadabra' и символ 'c'. Определи, входит ли символ в строку.
# word = "abracadabra"
# letter = "c"
# if letter in word:
#     print("letter 'c' in word 'abracadabra")
# else:
#     print("Error")

# 7. Дано имя 'иван'. Проверь, начинается ли оно с заглавной буквы.
# name = "ivan"
# print(name.istitle())

# 8. Дано число 30. Проверь, делится ли оно и на 3, и на 5. !!!
# num = 30
# if num // 3 and num // 5:
#     print("True")
# else:
#     print("False")

# 9. Дана переменная 4. Используй if/elif/else, чтобы вывести 'отлично', 'хорошо', 'удовлетворительно' или 'плохо'.
# num = int(input("Enter a score: "))
# if num == 5:
#     print("Excellent")
# elif num == 4:
#     print("Good")
# elif num == 3:
#     print("Satisfy")
# else:
#     print("Bad")
#
# 10. Даны числа 5, 5, 5. Проверь, равны ли они между собой.
# num = 5
# num1 = 5
# num2 = 5
# if num == num1 == num2:
#     print("Numbers are equal")
# else:
#     print("They are not equal")

# --- Сложные ---

# 11. Пользователь вводит два числа и оператор (+, -, *, /). С помощью if/elif/else выполни соответствующую операцию и выведи результат.
# num = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# action = input("enter an operator from (+, -, *, /)")
# if action == "+":
#     print(num + num2)
# elif action == "-":
#     print(num - num2)
# elif action == "*":
#     print(num * num2)
# elif action == "/":
#     print(num / num2)

# 12. Пользователь вводит год. Проверь, является ли он високосным.
# Год является високосным, если он делится на 4, но не делится на 100, или делится на 400.
# year = int(input("Enter a year: "))
# if year // 4 and year // 100 != 0 or year // 400:
#     print("Year is a Leap Year")
# else:
#     print("Year is not a Leap Year")

# 13. Напиши программу, которая определяет, в каком диапазоне находится число. (18 - 35)
# num = int(input("Enter a num from 18 to 35: "))
# if num < 18:
#     print("Number is less than 18")
# elif 18 <= num <= 35:
#     print("Number is between 18 and 35")
# else:
#     print("Number is more than 35")

# 14. Напиши тернарное выражение для вывода "да/нет" по логике.
# sentence = input("Enter a close ended question: ")
# print("Yes" if sentence else "No")

# 15. Пользователь вводит строку. Проверь, содержит ли она одновременно цифры, буквы и специальные символы
# (например: !@#).

# === Списки ===


# --- Базовые ---

# 1. Создай список из 5 чисел.
# list1 = [1, 2, 3, 4, 5]
# print(list1)

# 2. Получи третий элемент списка.
# print(list1[2])

# 3. Измени значение по индексу.
# list1[0] = 5
# print(list1)

# 4. Добавь новый элемент в список.
# list1[-1] = 45
# print(list1)

# 5. Удали последний элемент.
# list1.pop()
# print(list1)

# --- Средние ---

# 6. Пользователь вводит строку чисел через пробел. Преобразуй её в список и выведи длину списка.
# str1 = "Hello World"
# lst1 = list(str1)
# print(len(lst1))

# 7. Пользователь вводит строку чисел через пробел. Преобразуй её в список и выведи первые 3 элемента.
# str1 = "23 45 60"
# str2 = str1.split()
# lst1 = list(str2)
# print(lst1[0:3])

# 8. Пользователь дважды вводит строку чисел через пробел. Объедини их в один список и выведи.
# str1 = input("Enter a number: ")
# str2 = input("Enter the second number: ")
# print(list(str1 + str2))

# 9. Пользователь вводит строку чисел через пробел. Найди и выведи сумму всех чисел. !!! for i in
# str2 = str1.split()
# lst1 = list(str2)

# 10. Пользователь вводит строку чисел через пробел. Преобразуй в список и выведи отсортированный список по возрастанию.!!!
# num1 = input("Enter a number: ")
# num2 = input("Enter a number: ")
# num3 = input("Enter a number: ")
# lst1 = [list(num1), list(num2), list(num3)]
# print(sorted(lst1))

# --- Сложные ---

# 11. Пользователь вводит строку чисел через пробел. Выведи список квадратов этих чисел.
# nums = input("Enter 3 numbers: ")
# squares = [int(n)**2 for n in nums.split()]
# print(squares)

# 12. Проверь, есть ли дубликаты в списке.
# lst1 = [23, 3, 4, 56, 23]
# has_duplicates = len(lst1) != len(set(lst1))
# print(has_duplicates)

# 13. Удали все повторяющиеся элементы.
# lst1 = [23, 3, 4, 56, 23]
# lst1 = list(set(lst1))
# print(lst1)

# 14. Перевёрни список без reverse().
# lst1 = [23, 3, 4, 56]
# lst1 = lst1[::-1]
# print(lst1)

# 15. Заполни список вводом пользователя.
# lst = input("Enter a couple of numbers: ").split()
# print(lst)

# === Словари ===


# --- Базовые ---

# 1. Создай словарь person = {'name': 'Alice', 'age': 30}.
# person = {
#     'name': 'Alice',
#     'age': 30
# }
# print(person)

# 2. Используя словарь person, выведи значение по ключу 'name'.
# print(person.get("name"))

# 3. Добавь в словарь person ключ 'city' со значением 'London'.
# print(person)

# 4. Удали из словаря person ключ 'age'.
# 5. Проверь, есть ли ключ 'email' в словаре person.

# --- Средние ---

# 6. Перебери словарь и выведи ключи и значения.
# students = {
#     "name": "Nawal",
#     "age": 29
# }
# items = list(students.items())
# print(items[0][0], items[0][1])
# print(items[1][0], items[1][1])

# 7. Создай два словаря. Объедини два словаря. !!!
# university = {
#     "name": "Carleton",
#     "year": 2024
# }
# courses = {
#     "name": "upmind",
#     "year": 2025
# }
# summ1 = dict(list(university.items()) + list(courses.items()))
# print(summ1)

# 8. Создай словарь с квадратами чисел от 1 до 5.
# squares = dict(zip([1, 2, 3, 4, 5], [1**2, 2**2, 3**2, 4**2, 5**2]))
# print(squares)

# 9. Создай словарь из двух списков с помощью zip().
# keys = ["name", "age", "city"]
# values = ["Nawal", 29, "Ottawa"]
# result = dict(zip(keys, values))
# print(result)

# --- Сложные ---

# 11. Считай строку и выведи сколько раз встречается каждая буква.
# text = input("Enter a text: ")
# letters = list(text)
# unique = set(letters)
# result = {char: text.count(char) for char in unique}
# print(result)

# 12. Создай вложенный словарь.
# student = {
#     "name": "Nawal",
#     "info": {
#         "age": 29,
#         "city": "Ottawa",
#         "grades": {
#             "math": 90,
#             "english": 85
#         }
#     }
# }
#
# print(student)

# 13. Отсортируй словарь по значениям.
# university = {
#      "name": "Carleton",
#      "year": 2024
# }
# print(university.values())

# 14. Удали все пары, где значение меньше 5.
# numbers = {
#     "a": 6,
#     "b": 9,
#     "c": 3
# }
# if numbers["a"] < 5:
#     numbers.pop("a")
# if numbers["b"] < 5:
#     numbers.pop("b")
# if numbers["c"] < 5:
#     numbers.pop("c")
# print(numbers)

# 15. Считай пары ключ:значение от пользователя.
# key = input("Write a key: ")
# value = input("Write a value: ")
# my_dict = {key: value}
# print(my_dict)

# === Кортежи и множества ===


# --- Базовые ---

# 1. Создай кортеж (10, 20, 30).
# my_tuple = (10, 20, 30)
# print(my_tuple)

# 2. Выведи второй элемент кортежа (5, 15, 25).
# my_tuple = (5, 15, 25)
# print(my_tuple[1])

# 3. Проверь, содержится ли число 15 в кортеже (5, 10, 15, 20).
# my_tuple = (5, 10, 15, 20)
# if 15 in my_tuple:
#     print("Yes, there is 15 in tuple")
# else:
#     print("No, there are not 15 in tuple")

# 4. Преобразуй кортеж (1, 2, 3) в список.
# my_tuple = (1, 2, 3)
# print(list(my_tuple))

# 5. Дано: [1, 2, 2, 3, 3, 4]. Создай из него множество без дубликатов.
# lst1 = [1, 2, 2, 3, 3, 4]
# my_set = set(lst1)
# print(my_set)

# --- Средние ---

# 6. Найди пересечение множеств {1, 2, 3} и b = {2, 3, 4}.
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# print(set1.intersection(set2))

# 7. Объедини множества {1, 2} и b = {3, 4}.
# set1 = {1, 2}
# set2 = {3, 4}
# print(set1.union(set2))

# 8. Удали элемент 'apple' из множества {'apple', 'banana', 'cherry'}.
# fruits = {"apple", 'banana', 'cherry'}
# fruits.remove("apple")
# print(fruits)

# 9. В кортеже (1, 2, 2, 3), посчитай количество двоек и найди индекс первой двойки.
# num = (1, 2, 2, 3)
# print(num.count(2))
# print(num.index(2))

# 10. Преобразуй строку 'hello' в множество уникальных символов.
# str1 = "hello"
# print(tuple(str1))

# --- Сложные ---

# 11. Найди симметрическую разность двух множеств.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1.symmetric_difference(set2))

# 12. Проверь, является ли одно множество подмножеством другого.
# subset = {3, 4}
# superset = {1, 2, 3, 4}
# print(subset < superset)
# print(subset > superset)

# 13. Напиши функцию, возвращающую уникальные элементы списка.
# lst = [1, 2, 2, 3, 4, 4, 5]
# unique = list(set(lst))
# print(unique)

# 14. Создай кортеж из строк и найди самую длинную строку.
# my_tuple = ("Kyrgyzstan", "Canada", "Vietnam")
# longest = max(my_tuple, key=len)
# print(longest)

# === Циклы for и while ===


# --- Базовые ---

# 1. С помощью цикла for выведи числа от 1 до 10 включительно.
# for i in range(1, 11):
#     print(i)

# 2. Используя цикл while, выведи числа от 5 до 0.
# i = 5
# while i >= 0:
#     print(i)
#     i -= 1

# 3. Дана строка 'Python'. Выведи каждый символ строки на новой строке.
# text = "Python"
# i = 0
# while i < len(text):
#     print(text[i])
#     i += 1

# 4. Используя цикл, вычисли сумму чисел от 1 до 100.
# total = 0
# for i in range(1, 101):
#     total += i
# print(total)

# 5. С помощью цикла for выведи квадраты чисел от 1 до 5.
# for i in range(1, 6):
#     print(i ** 2)

# --- Средние ---

# 6. Посчитай количество чётных чисел от 1 до 20.
# count = 0
# for i in range(1, 21):
#     if i % 2 ==0:
#      count += 1
# print(count)

# 7. Запроси 5 чисел от пользователя и посчитай среднее.!!!


# 8. Выведи таблицу умножения на 3.
# for i in range(1, 11):
#     print(f"3 x {i} = {3 * i}")

# 9. Сгенерируй список квадратов через цикл.
# squares = []
# for i in range(1, 11):
#     squares.append(i ** 2)
# print(squares)

# 10. Создай обратный отсчёт с шагом 2.
# for i in range(10, 0, -2):
#     print(i)

# --- Сложные ---

# 11. Выведи числа Фибоначчи до 100.
# a, b = 0, 1
# while a <= 100:
#     print(a)
#     a, b = b, a + b

# 12. Найди факториал числа.
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(factorial)

# 13. Используй вложенный цикл для вывода таблицы умножения.
# 14. Угадай число с помощью while.
# 15. Запрашивай у пользователя числа и суммируй их, пока он не введёт 'стоп'.

# === Прерывание циклов (break, continue, else) ===


# --- Базовые ---

# 1. Запрашивай ввод пользователя в цикле и завершай цикл при вводе 'q'.
# while True:
#     user_input = input("Enter a word: ")
#     if user_input == 'q':
#         break
#     print(user_input)

# 2. С помощью цикла for выведи только нечётные числа от 1 до 10, используя continue.
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(i)

# 3. Напиши цикл for, который завершится без break, и используй конструкцию else.
# for i in range(5):
#     print(i)
# else:
#     print("Цикл ended without break.")

# 4. Создай бесконечный цикл, запрашивающий ввод чисел и завершающийся при вводе 0.
# while True:
#     num = int(input("Enter a number: "))
#     if num == 0:
#         break
#     print(num)

# 5. Запрашивай ввод строк и пропускай пустые строки, продолжая цикл.
# while True:
#     text = input("Enter a text: ")
#     if text == "q":
#         break
#     if text == "":
#         continue
#     print(text)

# --- Средние ---

# 6. Найди первое число, кратное 7, и выйди из цикла.
# for i in range(1, 100):
#     if i % 7 == 0:
#         print(i)
#         break

# 7. Пропусти ввод чисел меньше 0.
# while True:
#     num = int(input("Enter a number: "))
#     if num == 0:
#         break
#     if num < 0:
#         continue
#     print(num)

# 8. Проверь, содержит ли список хотя бы одно чётное (и выйди).
# numbers = [1, 3, 7, 10, 5]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)
#         break

# 9. Используй else, если число не найдено в списке.
# numbers = [1, 3, 5, 7, 9]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)
#         break
# else:
#     print("There are no even numbers")

# 10. Заверши цикл, если строка содержит 'x'.
# while True:
#     text = input("Enter a text: ")
#     if 'x' in text:
#         print("'x' was found")
#         break
#     if text == 'q':
#         break
#     print(text)

# --- Сложные ---

# 11. Выведи все делители числа, кроме 1 и самого числа.
# num = int(input("Enter a number: "))
# for i in range(2, num):
#     if num % i == 0:
#         print(i)

# 12. Запроси у пользователя числа. Прерви ввод с помощью break, как только пользователь введёт отрицательное число.
# while True:
#     num = int(input("Enter a number: "))
#     if num < 0:
#         break
#     print(num)

# 13. Прерви цикл, если сумма введённых чисел больше 100.
# total = 0
# while True:
#     num = int(input("Enter a number: "))
#     total += num
#     if total > 100:
#         print("The summ is over 100.")
#         break

# 14. Выведи числа от 1 до 30, пропуская те, которые делятся на 3 или 5 (с помощью continue).
# for i in range(1, 31):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     print(i)

# 15. Выведи только те числа от 1 до 50, которые не делятся на 2 и 3.
# for i in range(1, 51):
#     if i % 2 != 0:
#         print(i)

# === Генераторы списков, zip, enumerate, циклы в словарях ===


# --- Базовые ---

# 1. Используй генератор списка для создания списка квадратов чисел от 1 до 10.
# squares = [x ** 2 for x in range(1, 11)]
# print(squares)

# 2. Дано: {'a': 1, 'b': 2}. Перебери его и выведи все ключи.
# dict1 = {'a': 1, 'b': 2}
# for key in dict1:
#     print(key)

# 3. Дано: ['apple', 'banana', 'cherry']. Используй enumerate() для нумерации и вывода.
# fruits = ['apple', 'banana', 'cherry']
# for index, fruit in enumerate(fruits, start = 1):
#     print(f"{index}. {fruit}")

# 4. Даны списки names = ['Alice', 'Bob'] и ages = [30, 25]. Объедини их в пары с помощью zip().
# names = ['Alice', 'Bob']
# ages = [30, 25]
# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old.")

# 5. Дано: d = {'x': 10, 'y': 20}. Получи список всех значений с помощью .values().
# d = {'x': 10, 'y': 20}
# print(d.values())

# --- Средние ---

# 6. Создай словарь из двух списков с помощью zip().
# 7. Используй генератор для фильтрации чётных чисел.
# 8. Пронумеруй строки текста с помощью enumerate().
# 9. Создай список длины слов из строки.
# 10. Объедини три списка в список кортежей.

# --- Сложные ---

# 11. Дана строка 'hello world! hello python!'. Создай словарь, где ключ — буква, а значение — сколько раз она
# встречается в строке.
# 12. Используй zip() и генератор списков для сложения элементов.
# 13. Создай список кортежей (индекс, квадрат числа).
# 14. Преобразуй словарь в список строк “ключ: значение”.
# 15. Используй enumerate() в цикле while.
