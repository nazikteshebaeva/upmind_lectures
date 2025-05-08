# === Урок 18: Обработка исключений ===

# 🔹 Что такое исключения:
# Исключения — это ошибки, возникающие во время выполнения программы.
# Обработка исключений позволяет избежать аварийного завершения программы.

# 🔹 Основной синтаксис try/except:

# try:
#     number = int("abc")
# except ValueError:
#     print("Ошибка: это не число!")
#     number = int(input("Enter a number of the card again, the number should be only numeric: "))
#
# # 🔹 Несколько типов исключений:
#
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Ошибка деления на ноль!")
# except ValueError:
#     print("Ошибка значения!")

# 🔹 Блок finally — выполняется всегда:

# try:
#     file = open("somefile.txt")
# except FileNotFoundError:
#     print("Файл не найден")
# finally:
#     print("Завершение работы")

# 🔹 Блок else — срабатывает, если ошибок не возникло:

# try:
#     a = int(input("Введите число: "))
# except ValueError:
#     print("Ошибка ввода")
# else:
#     print("Число принято")
#
# # 🔹 Генерация собственных исключений:
#
# age = -1
# if age < 0:
#     raise ValueError("Возраст не может быть отрицательным")
#
# # 🔹 Использование функций с try/except:
#
# def safe_divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Ошибка: деление на ноль"
#
# print(safe_divide(5, 0))

# --- Практические задачи (40 задач) ---

# 1. Создай функцию divide_by_zero(), которая делит число 100 на 0. Обработай исключение ZeroDivisionError и выведи сообщение об ошибке.
# def divide_by_zero():
#     try:
#         print(100 / 0)
#     except ZeroDivisionError:
#         print("You can not divide into 0")
#
# def divide_by_zero():
#     try:
#         print(100 / 0)
#     except Exception as e:
#         print(e)

# 2. Создай функцию get_number() принимающую строку "123abc", "223", "23f23". Преобразуй строку в число и верни число, если возможно. Обработай исключение, если строка не преобразовывается в число.
# def get_number(n):
#     try:
#         number = int(n)
#         return number
#     except ValueError:
#         print("Error! You must write numbers only!")
# print(get_number("123abc"))
# print(get_number("223"))
# print(get_number("23f23"))

# 3. Создай функцию open_or_create_file(). Открой файл "input.txt". Если файла нет — создай его и запиши туда строку "Файл создан".
# def open_or_create_file():
#     try:
#         file = open("input.txt")
#         print("File was successfully open!")
#     except FileNotFoundError:
#         print("File was not found!")
#         file = open("input.txt", "w")
#         file.write("File was opened")
#         print("File was successfully open")


# 4. Создай функцию parse_numbers() принимающую строку "1 2 три 4". Преобразуй строку в список чисел и обработай ValueError для элементов, которые нельзя преобразовать.
# def func():
#     nums = ["1", "2", "three", "4"]
#     new_nums = []
#     for el in nums:
#         try:
#             new_nums.append(int(el))
#             print(new_nums)
#         except ValueError:
#             print("Here are some problems")
# func()


