# 1. Функция, принимающая любое количество чисел и возвращающая максимум.
# def find_maximum(*args):
#     if not args:
#         return None
#     return max(args)
# print(find_maximum(3, 7, 1, 9, 4))
# print(find_maximum(-5, -1, -12))
# print(find_maximum())

# 2. Функция, принимающая **kwargs и выводящая пары ключ: значение.
# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_kwargs(name="Oliver", age=37, city="Toronto")

# 3. Функция, возвращающая список квадратов чисел из *args.
# def get_squares(*args):
#     return [x**2 for x in args]
# print(get_squares(1, 2, 3, 4))

# 4. Функция, возвращающая True, если в *args есть хотя бы одно чётное число.
# def has_even(*args):
#     return any(x % 2 == 0 for x in args)
# print(has_even(1, 3, 5))
# print(has_even(1, 4, 7))
# print(has_even())

# 5. Функция, принимающая строку и символ, возвращающая количество вхождений символа.
# def count_char_occurrences(text, char):
#     return text.count(char)
# print(count_char_occurrences("hello world", "l"))
# print(count_char_occurrences("banana", "a"))
# print(count_char_occurrences("test", "z"))

# 6. Функция, возвращающая словарь: символ — количество его вхождений в строке.!
# def char_frequency(text):
#     freq = {}
#     for char in text:
#         freq[char] = freq.get(char, 0) + 1
#     return freq
# print(char_frequency("hello world"))

# 7. Функция, принимающая список и возвращающая только уникальные значения.
# def get_unique_elements(lst):
#     return list(set(lst))
# print(get_unique_elements([1, 2, 2, 3, 4, 4, 5]))

# 8. Функция, которая принимает список строк и возвращает их объединение.
# def join_strings(strings):
#     return ''.join(strings)
# print(join_strings(["Hello", " ", "world", "!"]))

# 9. Функция, возвращающая True, если слово палиндром.
# def is_palindrome(word):
#     return word == word[::-1]
# print(is_palindrome("madam"))
# print(is_palindrome("python"))

# 10. Функция, проверяющая, все ли слова в списке начинаются с заглавной буквы.!!!
# def all_start_with_upper(words):
#     for word in words:
#         if not word or not word[0].isupper():
#             return False
#     return True
# print(all_start_with_upper(["Hello", "World"]))
# print(all_start_with_upper(["Hello", "world"]))
# print(all_start_with_upper(["hello", "World"]))

# 11. Функция, возвращающая список имён из **kwargs, где ключи — 'name1', 'name2', и т.д.
# def get_names(**kwargs):
#     names = []
#     for key, value in kwargs.items():
#         if key.startswith('name'):
#             names.append(value)
#     return names
# print(get_names(name1="Nawal", name2="Oliver", age=30, name3="Emilie"))

# 12. Лямбда-функция для получения остатка от деления числа на 3.
# remainder = lambda x: x % 3
# print(remainder(10))
# print(remainder(15))
# print(remainder(7))

# 13. Функция, которая принимает функцию и список, применяет функцию ко всем элементам и возвращает новый список.!!!


# 14. Функция, возвращающая другую функцию, добавляющую префикс к строке.!!!


# 15. Функция, которая подсчитывает общее количество символов в строках списка.
# def total_characters(strings):
#     return sum(len(s) for s in strings)
# strings = ["Hello", "world", "Python"]
# print(total_characters(strings))

# 16. Функция, возвращающая сумму всех значений словаря.
# def sum_values(dictionary):
#     return sum(dictionary.values())
# data = {"a": 5, "b": 10, "c": 15}
# print(sum_values(data))

# 17. Функция, которая преобразует все значения словаря в строки.
# def values_to_strings(dictionary):
#     return {key: str(value) for key, value in dictionary.items()}
# data = {'a': 5, 'b': 10.5, 'c': True}
# print(values_to_strings(data))

# 18. Функция, сортирующая словарь по длине ключей.
# def sort_dict_by_key_length(dictionary):
#     return dict(sorted(dictionary.items(), key=lambda item: len(item[0])))
# data = {'apple': 1, 'banana': 2, 'kiwi': 3, 'grape': 4}
# sorted_data = sort_dict_by_key_length(data)
# print(sorted_data)

# 19. Функция, принимающая список чисел и возвращающая их в виде строки через точку с запятой.!!!


# 20. Функция, считающая количество чисел больше 10 в *args.
# def count_greater_than_10(*args):
#     return sum(1 for x in args if x > 10)
# print(count_greater_than_10(5, 12, 8, 15, 3, 20))

# 21. Функция, возвращающая True, если длина всех строк в списке больше 3.!!!


# 22. Функция, объединяющая списки, переданные через *args.!
# def combine_lists(*args):
#     return [item for sublist in args for item in sublist]
# list1 = [1, 2, 3]
# list2 = [4, 5]
# list3 = [6, 7, 8]
# combined = combine_lists(list1, list2, list3)
# print(combined)

# 23. Функция, возвращающая минимальное значение в **kwargs.
# def min_in_kwargs(**kwargs):
#     return min(kwargs.values())
# data = {"a": 10, "b": 5, "c": 20}
# print(min_in_kwargs(**data))

# 24. Функция, проверяющая, есть ли в списке строки, содержащие подстроку 'test'.
# def contains_test(strings):
#     for s in strings:
#         if 'test' in s:
#             return True
#     return False
# print(contains_test(["hello", "this is a test", "world"]))
# print(contains_test(["hello", "world"]))

# 25. Функция, применяющая функцию к каждому значению словаря.!!!


# 26. Функция, возвращающая количество параметров в **kwargs.
# def count_kwargs(**kwargs):
#     return len(kwargs)
# data = {"a": 1, "b": 2, "c": 3}
# print(count_kwargs(**data))

# 27. Функция, принимающая список чисел и возвращающая их факториалы.
# def factorials(numbers):
#     def factorial(n):
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result
#
#     return [factorial(x) for x in numbers]
# numbers = [1, 2, 3, 4, 5]
# print(factorials(numbers))

# 28. Функция, которая возвращает True, если хотя бы одно значение в словаре больше 100.
# def has_value_greater_than_100(dictionary):
#     for value in dictionary.values():
#         if value > 100:
#             return True
#     return False
# data = {"a": 50, "b": 150, "c": 75}
# print(has_value_greater_than_100(data))

# 29. Функция, объединяющая строки из *args через пробел.
# def join_strings(*args):
#     return ' '.join(args)
# print(join_strings("Hello", "world", "this", "is", "Nazik"))

# 30. Функция, возвращающая True, если в **kwargs есть ключ 'email'.
# def has_email_key(**kwargs):
#     return "email" in kwargs
# data = {"name": "Nazik", "email": "teshebaevanazik99@gmail.com"}
# print(has_email_key(**data))

# 31. Функция, возвращающая количество цифр в строке.
# def count_digits(string):
#     return sum(1 for char in string if char.isdigit())
# print(count_digits("Hello123"))

# 32. Функция, проверяющая, входит ли строка в список (игнорируя регистр).!!!


# 33. Функция, возвращающая True, если все значения в словаре уникальны.
# def all_values_unique(dictionary):
#     return len(dictionary.values()) == len(set(dictionary.values()))
# data1 = {"a": 1, "b": 2, "c": 3}
# print(all_values_unique(data1))

# 34. Функция, принимающая список кортежей и возвращающая сумму второго элементов.
# def sum_second_elements(tuples):
#     return sum(t[1] for t in tuples)
# tuples = [(1, 2), (3, 4), (5, 6)]
# print(sum_second_elements(tuples))

# 35. Функция, выводящая имя и возраст в формате: "Имя: ..., Возраст: ..." с помощью f-строки.
# def display_name_and_age(name, age):
#     print(f"name: {name}, age: {age}")
# display_name_and_age("Emilie", 23)

# 36. Функция, создающая и возвращающая словарь из списка ключей и списка значений.
# def create_dict(keys, values):
#     return dict(zip(keys, values))
# keys = ["name", "age", "city"]
# values = ["Nawal", 28, "Ottawa"]
# result = create_dict(keys, values)
# print(result)

# 37. Функция, принимающая список слов и возвращающая количество слов длиной больше 5.
# def count_words_longer_than_5(words):
#     return sum(1 for word in words if len(word) > 5)
# words = ["apple", "banana", "cherry", "kiwi", "orange"]
# print(count_words_longer_than_5(words))

# 38. Функция, проверяющая, начинается ли каждая строка в списке с заглавной.
# def all_start_with_capital(strings):
#     for s in strings:
#         if not s[0].isupper():
#             return False
#     return True
# words = ["Hello", "World", "Python"]
# print(all_start_with_capital(words))

# 39. Функция, возвращающая True, если сумма всех чисел *args кратна 10.
# def sum_is_multiple_of_10(*args):
#     return sum(args) % 10 == 0
# print(sum_is_multiple_of_10(10, 20, 30))

# 40. Функция, принимающая строку и возвращающая словарь с частотой каждого слова.
# def word_frequency(text):
#     words = text.split()
#     frequency = {}
#     for word in words:
#         frequency[word] = frequency.get(word, 0) + 1
#     return frequency
# text = "hello world hello python world hello"
# print(word_frequency(text))