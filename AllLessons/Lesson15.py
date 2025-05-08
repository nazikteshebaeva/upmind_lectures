# === Урок 16: Расширенные возможности функций в Python ===

#   Аргументы функций:
# - позиционные аргументы: def f(x, y)
# - аргументы по умолчанию: def f(x=10)
# - переменное число позиционных аргументов: *args
# - переменное число именованных аргументов: **kwargs


#   Примеры аргументов по умолчанию:
# def greet(name="Гость"):
#     print(f"Привет, {name}!")


# greet("Анна")  # Привет, Анна
# greet()         # Привет, Гость


#   Пример *args: любое количество позиционных аргументов, it comes as a tuple
# def multiply_all(*args):
#     result = 1
#     for number in args:
#         result *= number
#     return result
#
#
# print(multiply_all(2, 3, 4))  # 24


#   Пример **kwargs: любое количество именованных аргументов kw - key value pairs, they gonna come as a dictionary
# def show_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# show_info(name="Иван", age=30, city="Москва")

#   Функции как объекты (их можно передавать в другие функции)

#   Вложенные функции (одна функция внутри другой)

#   Лямбда-функции — короткий способ записать функцию: # in one string can be written, and the result will be saved in peremennaya
# Пример:
# double = lambda x: x * 2
# print(double(5))  # 10

#   Функции высшего порядка — принимают функции как аргументы или возвращают функции

#   Область видимости переменных: глобальные и локальные, ключевые слова global и nonlocal

# Пример глобальной переменной:
# x = 5
#
#
# def change_global():
#     global x
#     x = 10
#     print("x in function", x)
#
# # change_global()
# print("x before function", x)
# change_global()
# print("x after function", x)  # 10


# Пример nonlocal:
# def outer():
#     y = 3
#
#     def inner():
#         nonlocal y #one level up will add an information, so that is why outer and inner is 5.
#         y += 2
#         print("Внутри inner:", y)
#     inner()
#     print("Внутри outer:", y)
#
#
# outer()



# def len2(lst):
#     length = 0
#     for i in lst:
#         length += 1
#     return length
#
# num = [1, 2, 3, 4, 5, 6, 7]
# print(len2(num))

# #   Декораторы:
# # Декораторы — это функции, которые принимают другую функцию и возвращают новую функцию с дополнительным поведением.
# # Обычно используются для логирования, проверки прав доступа, измерения времени выполнения и др.
#
#
# # Пример простого декоратора:
# def my_decorator(func):
#     def wrapper():
#         print("До выполнения функции")
#         func() #my decorator which is Hi. So that is why it comes print1, hi, and then print2
#         print("После выполнения функции")
#     return wrapper
#
#
# @my_decorator
# def say_hi():
#     print("Привет!")
#
#
# say_hi()
# Вывод:
# До выполнения функции
# Привет!
# После выполнения функции
#

# # Декоратор с аргументами:
# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Вызов функции {func.__name__} с аргументами: {args}, {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @logger
# def add(a, b):
#     return a + b
#
#
# print(add(2, 3))

# --- Ознакомительные задачи (10) ---

#1. Напиши функцию, которая принимает любое количество чисел и возвращает их произведение.
# def num(*args):
#     result = 0
#     for number in args:
#         result *= number
#     return result
# print(num(23, 45, 67))

# 2. Напиши функцию с именованными аргументами name и age, которая выводит: "Имя: ..., Возраст: ...".
# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# greet(name="Nawal", age = 29)

# 3. Напиши функцию, которая принимает список и возвращает сумму только положительных чисел.
# def num(*args):
#     result = 0
#     for number in args:
#         if number > 0:
#             result += number
#     return result
# print(num([1, 2, 3, 4]))

# 4. Напиши лямбда-функцию, которая принимает число и возвращает его куб.
# triple = lambda x: x ** 3
# print(triple(3))

# 5. Напиши функцию, которая возвращает другую функцию, которая возводит число в квадрат.
# def outer():
#     x = 5
#     def inner():
#         nonlocal x
#         x **= 2
#         print(x)
#     inner()
#     print(x)
# outer()

# 6. Напиши функцию, которая использует global для изменения глобальной переменной.
# x = 25
# def change_global():
#     global x
#     x = 40
#     print(x)
# change_global()
# print(x)

# 7. Напиши функцию, которая принимает **kwargs и возвращает их ключи в списке.
#
# def get_list(**kwargs):
#     l = []
#     for key in kwargs.keys():
#         l.append(key)
#     return l
#
# print(get_list(apple = "Chinese", grapes = "Kyrgyz"))


# 8. Напиши функцию, которая считает сумму всех чисел в списке с помощью вложенной функции.
# def sum_of_numbers(numbers):
#     def calculate_sum(nums):
#         total = 0
#         for num in nums:
#             total += num
#         return total
#
#     return calculate_sum(numbers)
# numbers = [1, 2, 3, 4, 5]
# print(sum_of_numbers(numbers))

# 9. Напиши функцию, принимающую другую функцию и число, и возвращающую результат.
# def apply_function(func, num):
#     return func(num)
# def square(x):
#     return x ** 2
# result = apply_function(square, 5)
# print(result)

# 10. Напиши функцию, использующую nonlocal для изменения переменной во вложенной функции.
# def outer_function():
#     count = 0
#     def inner_function():
#         nonlocal count
#         count += 1
#         print(f"Count inside inner function: {count}")
#
#     inner_function()
#     return count
# result = outer_function()
# print(f"Count after calling outer function: {result}")






# --- Дополнительные задачи по декораторам (10) ---

# 41. Напиши декоратор, который выводит 'Начало выполнения' и 'Конец выполнения' перед и после вызова функции.
# Пример: задекорируй функцию print_name(), которая печатает 'Алексей'.

# 42. Напиши декоратор, который логирует аргументы и результат функции.
# Пример: задекорируй функцию multiply(a=3, b=4), которая возвращает произведение.

# 43. Напиши декоратор, который запрещает вызов функции без аргументов.
# Пример: функция divide(a, b). Если не переданы аргументы — выводится сообщение об ошибке.

# 44. Напиши декоратор, который считает и выводит количество вызовов функции.
# Пример: задекорируй функцию hello(), вызывай её 3 раза.

# 45. Напиши декоратор, который ограничивает выполнение функции максимум 2 раза.
# Пример: задекорируй функцию greet(), которая просто печатает приветствие.

# 46. Напиши декоратор, который проверяет тип аргументов функции и вызывает её только если все аргументы — числа.
# Пример: функция add(a, b), вызов add(2, 'a') должен выводить сообщение об ошибке.

# 47. Напиши декоратор, который измеряет и выводит время выполнения функции.
# Пример: задекорируй функцию wait(), которая вызывает time.sleep(1).

# 48. Напиши декоратор, который преобразует результат функции в строку.
# Пример: функция get_number() возвращает число 42, декоратор делает return '42'.

# 49. Напиши декоратор, который к каждому выводу из функции добавляет '✔'.
# Пример: функция print_msg() выводит 'Успешно'. С декоратором — 'Успешно✔'.

# 50. Напиши универсальный декоратор, который можно применить к любой функции и он будет выводить
# её имя и время запуска.
# Пример: задекорируй любую функцию, например def say_hello().

