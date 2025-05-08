
# 1. Функция, возвращающая разность двух чисел (например, 10 и 3).
# def subtract(a, b):
#     return a - b
# print(subtract(10, 3))

# 2. Функция, принимающая число (например, -7) и возвращающая его модуль.
# def num(x):
#     return abs(x)
# print(num(-7))

# 3. Функция, проверяющая, является ли число (например, -5) отрицательным.
# def num(x):
#     return x < 0
# print(num(-5))

# 4. Функция, возвращающая максимальное из двух чисел (например, 5 и 8).
# def num(a, b):
#     return max(a, b)
# print(num(5, 8))

# 5. Функция, возвращающая минимальное из трёх чисел (например, 3, 7, 2).
# def num(a, b, c):
#     return min(a, b, c)
# print(num(3, 7, 2))

# 6. Функция, возвращающая True, если строка (например, 'python is fun') содержит слово 'python'.
# def str1(w):
#     return "python" in w
#
# print(str1("python is fun"))
# print(str1("fun"))

# 7. Функция, проверяющая, пустая строка или нет (например, '').
# def str1(l):
#     return l == ""
#
# print(str1("Hello"))
# print(str1(""))

# 8. Функция, считающая количество символов в строке без пробелов (например, 'hello world').
# def str1(l): циклом
#     return len(l.replace(" ", ""))
# print(str1("hello world"))

# 9. Функция, возвращающая True, если в строке (например, 'abc123') есть хотя бы одна цифра.
# def check_number_integer(str1):
#     for char in str1:
#         if char.isnumeric():
#             return True
#     return False
# print(check_number_integer("abc123"))

# 10. Функция, возвращающая строку наоборот (например, 'python' -> 'nohtyp').
# def str1(l): циклом
#     return l[::-1]
# print(str1("python"))

# 11. Функция, проверяющая, является ли число (например, 17) простым.!!!
# 12. Функция, возвращающая все делители числа (например, 12 -> [1, 2, 3, 4, 6, 12]).!!!
# 13. Функция, возвращающая факториал числа (например, 5 -> 120). !!!
# 14. Функция, преобразующая список строк (например, ['cat', 'dog']) в список их длин.!!!
# def lst1(a, b):
#     return len([a, b])
# print(lst1["cat", "dog"])

# 15. Функция, проверяющая, все ли элементы списка (например, [2, 4, 6]) чётные.
# def num(a, b, c):
#     return a % 2 == 0 and b % 2 == 0 and c % 2 == 0
# print(num(2, 4, 6))

# 16. Функция, считающая количество чётных чисел в списке (например, [1, 2, 3, 4, 5]).
# def count_even_numbers(lst):
#      return len([x for x in lst if x % 2 == 0])
#
# print(count_even_numbers([1, 2, 3, 4, 5]))

# 17. Функция, возвращающая сумму квадратов всех чисел в списке (например, [1, 2, 3]).
# def sum_of_squares(lst):
#      return sum(x ** 2 for x in lst)
# print(sum_of_squares([1, 2, 3]))

# 18. Функция, возвращающая True, если два слова (например, 'listen', 'silent') являются анаграммами.
# def are_anagrams(word1, word2):
#     return sorted(word1) == sorted(word2)
# print(are_anagrams("listen", "silent"))

# 19. Функция, принимающая список (например, [1, 2, 2, 3]) и возвращающая только уникальные элементы.
# def unique_elements(lst):
#      return list(set(lst))
# print(unique_elements([1, 2, 2, 3]))

# 20. Функция, соединяющая два списка без повторений (например, [1, 2], [2, 3] -> [1, 2, 3]).
# def merge_unique(lst1, lst2):
#      return list(set(lst1 + lst2))
# print(merge_unique([1, 2], [2, 3]))

# 21. Функция, возвращающая среднее значение чисел из списка (например, [4, 8, 12]).
# def average(lst):
#      return sum(lst) / len(lst) if lst else 0
# print(average([4, 8, 12]))

# 22. Функция, проверяющая, входит ли элемент (например, 5) в список [1, 3, 5, 7].
# def contains_element(lst, element):
#      return element in lst
# print(contains_element([1, 2, 3, 7], 5))

# 23. Функция, принимающая строку (например, 'hello world') и возвращающая количество слов.
# def word_count(s):
#      return len(s.split())
# print(word_count("hello world"))

# 24. Функция, удаляющая все пробелы из строки (например, 'hello world' -> 'helloworld').
# def remove_spaces(s):
#      return s.replace(" ", "")
# print(remove_spaces("hello world"))

# 25. Функция, преобразующая строку (например, 'one two three') в список слов.
# def string_to_words(s):
#     return s.split()
# print(string_to_words("one two three"))

# 26. Функция, возвращающая True, если слово (например, 'madam') читается одинаково в обе стороны.
# def is_palindrome(word):
#     return word == word[::-1]
# print(is_palindrome("madam"))

# 27. Функция, удаляющая дубликаты из списка (например, [1, 2, 2, 3]).
# def remove_duplicates(lst):
#     return list(set(lst))
# print([1, 2, 2, 3])

# 28. Функция, заменяющая все гласные в строке (например, 'hello') на *.
# # 29. Функция, проверяющая, все ли символы в строке (например, 'abc') уникальны.
# def all_unique_chars(s):
#     return len(set(s)) == len(s)
# print(all_unique_chars("abc"))

# 30. Функция, принимающая два числа (например, 3 и 7) и возвращающая список чисел между ними.
# 31. Функция, преобразующая список чисел (например, [1, 2, 3]) в строку '1,2,3'.
# 32. Функция, находящая максимальное и минимальное число в списке (например, [4, 2, 9]).
# def min_max(lst):
#     return (min(lst), max(lst))
# print(min_max([4, 2, 9]))

# 33. Функция, возвращающая True, если список (например, [1, 2, 3, 4]) отсортирован по возрастанию.
# def is_sorted(lst):
#     return lst == sorted(lst)
# print(is_sorted([1, 2, 3, 4]))

# 34. Функция, возвращающая количество положительных чисел в списке (например, [-2, 3, 4]).
# def count_positive(lst):
#     return len([x for x in lst if x > 0])
# print(count_positive([-2, 3, 4]))

# 35. Функция, возвращающая произведение всех чисел в списке (например, [2, 3, 4]).
# 36. Функция, объединяющая значения словаря (например, {'a': 'hi', 'b': 'there'}) в одну строку 'hithere'.
# def merge_dict_values(d):
#     return ''.join(d.values())
# print(merge_dict_values({'a': 'hi', 'b': 'there'}))

# 37. Функция, сортирующая словарь (например, {'a': 3, 'b': 1}) по значениям.
# 38. Функция, принимающая строку (например, 'hello') и возвращающая словарь частот символов.
# 39. Функция, возвращающая словарь квадратов чисел от 1 до N (например, N = 5).
# 40. Функция, проверяющая, является ли введённый год (например, 2024) високосным.
# def is_leap_year(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)