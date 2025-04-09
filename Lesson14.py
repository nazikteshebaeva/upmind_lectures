# === Урок 15: Функции в Python ===

# --- Объяснение темы ---

# Функции — это блоки кода, которые можно переиспользовать.
# Они помогают структурировать программу, избегать повторений и повышать читаемость.

# Синтаксис определения функции:
# def имя_функции(аргументы):
#     блок_кода
#     return значение (необязательно)

# Пример:

# Функция без аргументов:
# def say_hello():
#     print("Привет, мир!")
#
#
# say_hello()  # Вызов функции без аргументов


# def greet(name):
#     print(f"Привет, {name}!")
#
#
# greet("Анна")  # Вызов функции


# Функция с возвратом значения:
# def square(x):
#     return x ** 2
#
#
# result = square(5)
# print(result)  # 25


# Функция с несколькими аргументами:
# def add(a, b):
#     return a + b
#
#
# print(add(2, 3))  # 5

# def subtract(a, b):
#     return a - b
#
# print(subtract(2, 3))

# Аргументы по умолчанию: #if there are no info like a name, we can use this argument so we can always have some answer.
# def greet_user(name="гость"):
#     print(f"Привет, {name}!")
#
# greet_user()
# greet_user("Nazik")

# --- Ознакомительные задачи (10) ---

# 1. Напиши функцию, которая выводит "Привет, мир!".
# def say_greeting():
#     print("Hello, World!")
#
# say_greeting()

# 2. Напиши функцию, которая принимает имя (например, 'Иван') и приветствует пользователя.
# def greet(name):
#     print(f"Hello, {name}!")
#
# greet("Ivan")

# 3. Напиши функцию, которая возвращает квадрат числа (например, 4).
# def square(x):
#     return x ** 2
#
# print(square(4))

# 4. Напиши функцию, которая возвращает сумму двух чисел (например, 5 и 7).
# def add(a, b):
#     return a + b
#
# print(add(5, 7))

# 5. Напиши функцию, которая проверяет, чётное число или нет (например, 10).
# def num(x):
#     return x % 2 == 0
# print(num(10))

# 6. Напиши функцию, которая возвращает длину строки (например, 'python').
# def get_length(x):
#     return len(x)
# print(get_length("python"))

# 7. Напиши функцию, которая принимает список (например, [1, 2, 3]) и возвращает его сумму.
# def list1(x):
#     return sum(x)
# print(list1([1, 2, 3]))

# 8. Напиши функцию, которая принимает строку (например, 'hello') и возвращает строку в верхнем регистре.
# def to_uppercase(x):
#     return x.upper()
# print(to_uppercase("hello"))

# 9. Напиши функцию, которая возвращает True, если число (например, 15) делится на 3 и 5.
# def num(x):
#     return x % 3 == 0 and x % 5 == 0
#
# print(num(15))

# 10. Напиши функцию, которая принимает имя и возраст ('Анна', 25), и возвращает строку вида
# "Меня зовут ... мне ... лет".
# def greet(name, age):
#     print(f"My name is {name}, I am {age} years old!")
# greet("Anna", 25)