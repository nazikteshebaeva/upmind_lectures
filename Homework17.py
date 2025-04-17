#5. Создай функцию write_numbers_to_file(). Запиши список [1, 2, 3, 4] в файл "numbers.txt". Обработай IOError при записи.!!!
# def write_numbers_to_file():
#         numbers = [1, 2, 3, 4]
#         try:
#             file = open("numbers.txt", "x", encoding="utf-8")
#             print("File was found")
#         except IOError:
#             print("Error was found!")

# 6. Создай функцию read_users(). Прочитай файл "users.txt". Если файл не найден — обработай FileNotFoundError и выведи сообщение.!!!
# def read_users():
#     try:
#         file = open("users.txt", "r")
#         print("File was found!")
#     except FileNotFoundError:
#         print("Error! File was not found!")
# read_users()

# 7. Создай функцию check_divisibility(). Проверь, делится ли число 17 на 3 и на 5. Если нет — выброси исключение ValueError с пояснением.
# def check_divisibility():
#     num = input("Enter a number: ")
#     try:
#         print(int(num) // 17)
#         print(int(num) // 3)
#         print(int(num) // 5)
#     except ValueError:
#         print("Error")
# check_divisibility()

# 8. Создай функцию save_user(). Запиши строку "Иван, 25" в файл users.csv. Обработай ошибки записи файла.
# def save_user():
#     str1 = "Ivan, 25"
#     try:
#         with open("users.csv", "w", encoding="utf-8") as file:
#             file.write(str1)
#     except FileNotFoundError:
#         print("Error")
# save_user()

# 9. Создай функцию is_digit_string(). Проверь, можно ли строку "456a" преобразовать в число. Обработай исключение, если преобразование невозможно.
# def is_digit_string():
#     str1 = "456a"
#     try:
#         print(int(str1))
#     except ValueError:
#         print("Error")
# is_digit_string()

# 10. Создай функцию write_text(). Запиши строку "Пример строки" в файл "example.txt". Обработай IOError.
# def write_text():
#     str1 = "Example of the string"
#     try:
#         with open("example.txt", "w", encoding="utf-8") as file:
#             file.write(str1)
#     except IOError:
#         print("Error")
# write_text()

# 11. Создай функцию get_age_from_dict(). Получи значение ключа 'age' из словаря {'name': 'Anna'}. Обработай исключение KeyError, если ключ отсутствует.
# def get_age_from_dict():
#     dict1 = {"name": "Anna"}
#     try:
#         print(dict1.get("age"))
#     except KeyError:
#         print("Error")
# get_age_from_dict()

# 12. Создай функцию validate_not_empty() принимающую строку. Если строка пустая — выброси исключение ValueError с пояснением.?
# def validate_not_empty():
#     str1 = input("Enter a sentence: ")
#     try:
#         if str1 != "":
#             print("Sentence has been written")
#     except ValueError:
#         print("Error!")
# validate_not_empty()

# 13. Создай функцию open_log_file(). Открой файл "log.txt" и обязательно выведи "Готово" в блоке finally.
# def open_log_file():
#     try:
#         with open("log.txt", "r", encoding="utf-8") as file:
#             file.read()
#     except FileNotFoundError:
#         print("Error")
#     finally:
#         print("Ready")
# open_log_file()

# 14. Создай функцию count_lines(). Прочитай файл "lines.txt" и выведи количество строк. Обработай FileNotFoundError, если файл не найден.
# def count_lines():
#     try:
#         with open("Lines.txt", "r", encoding="utf-8") as file:
#             line_count = sum(1 for i in file)
#             print(line_count)
#     except FileNotFoundError:
#         print("Error")
# count_lines()

# 15. Создай функцию check_char_in_number(). Проверь, входит ли символ 'x' в число 123. Обработай исключение TypeError при попытке перебора числа как строки.
# def check_char_in_number():
#     try:
#         if "x" in 123:
#             print("True")
#     except TypeError:
#         print("Error")
# check_char_in_number()

# 16. Создай функцию split_string(). Преобразуй строку "hello world" в список слов. Обработай TypeError, если строка имеет значение None.
# def split_string():
#     str1 = "hello world"
#     try:
#         print(str1.split())
#     except TypeError:
#         print("Error")
# split_string()

# 17. Создай функцию sum_input_values(). Обрабатывай ввод пользователя: "5", "abc", "стоп". Суммируй только корректные числа до команды "стоп".
# def sum_input_values():
#     summ = 0
#     while True:
#         num = input("Enter a number: ")
#         if num == "stop":
#             break
#         else:
#             summ += int(num)
#             print(summ)
# sum_input_values()

# 18. Создай функцию get_length(). Внутри неё вызови len() от строки "строка". Обработай исключение, если на вход подаётся не строка.
# def get_length():
#     str1 = "string"
#     try:
#         print(len(str1))
#     except TypeError:
#         print("Error")
# get_length()

# 19. Создай функцию read_users_json(). Используй JSON-файл users.json (50 записей). Считай пользователей и обработай исключения при чтении.
# 20. Создай функцию filter_adults(). Прочитай файл users.json и выведи всех пользователей, чей возраст больше 18 лет (год рождения < 2006).

# 21. Создай функцию save_list_to_json(). Запиши список [5, 10, 15] в файл data.json. Обработай исключения записи.
# 22. Создай функцию convert_to_numbers(). Преобразуй элементы ["1", "2", "a"] в числа. Обработай ошибки преобразования.
# 23. Создай функцию total_orders_sum(). Прочитай файл orders.json с [{'sum': 100}, {'sum': 200}]. Выведи общую сумму заказов.
# 24. Создай функцию compare_types(). Попробуй сравнить "10" и 5. Обработай исключение TypeError.
# 25. Создай функцию read_lines_loop(). Прочитай строки из файла "input.txt" в цикле. Обработай IOError при чтении.
# 26. Создай функцию assert_positive(). Проверь с помощью assert, что число -3 положительное. Обработай AssertionError.
# 27. Создай функцию ensure_file_exists(). Проверь, существует ли файл "testfile.txt". Если нет — создай файл и запиши в него любую строку.
# 28. Создай функцию delete_file(). Удали файл "trash.txt". Обработай исключение FileNotFoundError, если файл не существует.
# 29. Создай функцию analyze_string_content(). В строке "abc123" проверь, содержит ли она буквы и цифры. Обработай любые ошибки анализа строки.
# 30. Создай функцию convert_list_items(). Преобразуй ["1", "2", "три"] в числа. Обработай ValueError при невозможности преобразования.

# 31. Создай функцию simple_calculator(). Реализуй калькулятор, выполняющий деление, сложение и умножение. Обработай все возможные ошибки при вводе и вычислениях.
# 32. Создай функцию read_with_all_blocks(). Прочитай файл "example.txt", используй конструкции try/except/else/finally и обработай все ошибки.
# 33. Создай функцию average_from_dict(). Используй словарь {"Маша": 5, "Саша": 4} и выведи среднюю оценку. Обработай ошибки доступа к данным.
# 34. Создай функцию write_to_output(). Запиши строку "данные" в файл output.txt. Если файл уже существует — перезапиши его, обработай ошибки записи.
# 35. Создай функцию safe_enumerate(). Перебери список ["a", "b", 3] с помощью enumerate(). Обработай TypeError, если возникнет.
# 36. Создай функцию parse_date(). Преобразуй строку "2023-13-01" в дату с использованием datetime. Обработай ValueError при неверном формате.
# 37. Создай функцию save_dict_to_json(). Запиши словарь {"a": 1} в JSON-файл safe.json. Обработай ошибки записи и сериализации.
# 38. Создай функцию find_users_named_anna(). Прочитай файл users.json и выведи всех пользователей, у которых имя "Анна".
# 39. Создай функцию read_first_lines(). Прочитай первые 5 строк из файла "text.txt". Обработай IOError при чтении.
# 40. Напиши функцию run_with_handler(func), которая вызывает переданную функцию и ловит любые возникающие ошибки. Выведи сообщение при ошибке.

# 📂 Пример JSON-файла users.json (содержит 50 записей):
# [
#   {"name": "Иван", "surname": "Сидоров", "birth_year": 2002},
#   {"name": "Мария", "surname": "Петрова", "birth_year": 1998},
#   ...
#   {"name": "Анна", "surname": "Кузнецова", "birth_year": 2005}
# ]