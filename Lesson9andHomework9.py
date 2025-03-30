# Переменные, типы данных и базовые операции ###
#
# # Легкие:
# 1. Создайте переменную `age` и присвойте ей ваш возраст. Выведите ее.
# age = 25
# print(age)

# 2. Перемножьте два числа `5` и `7`, результат сохраните в переменную `result`.
# num1 = 5
# num2 = 7
# result = num1 * num2
# print(result)

# 3. Преобразуйте число `10` в строку и выведите его тип.
# num3 = 10
# print(str(num3))
# num4 = str(num3)
# print(type(num4))

# 4. Сложите строки `"Hello"` и `"World"` с пробелом между ними.
# words = "Hello", "World"
# print(" ".join(words))

# str1 = "Hello"
# str2 = "World"
# print(str("Hello"), str("World"))

# 5. Проверьте, является ли `100` больше `99` (выведите `True` или `False`).
# num4 = 100
# num5 = 90
# print(num4 > num5)

# # Средние:
# 6. Даны две переменные: `a = 10`, `b = 3`. Найдите результат деления `a` на `b` с остатком.
# a = 10
# b = 3
# print(a / b)

# 7. Пользователь вводит два числа. Выведите их сумму.
# numbers = input("Enter the first number: ")
# numbers1 = input("Enter the second number: ")
# print(numbers + numbers1)

# 8. Преобразуйте строку `"123"` в число и умножьте на `2`.
# string1 = "123"
# string2 = int(string1)
# print(string2 * 2)

# 9. Сравните строки `"apple"` и `"Apple"` (равны ли они?).
# string1 = "apple"
# string2 = "Apple"
# print(string1 == string2)

# 10. Дано число `15.8`. Округлите его до целого.
# number = 15.8
# print(round(15.8))
#
# # Сложные:
# 11. Напишите код, который меняет значения двух переменных местами.
# a = 5
# b = 2
# a, b = b, a
# print(a)
# print(b)

# 12. Вычислите среднее арифметическое трех чисел.
# num1 = 34
# num2 = 45
# num3 = 56
# numbers = (num1 + num2 + num3)
# print(numbers)
# print(numbers // 3)

# 13. Проверьте, является ли строка `"12345"` числом (используйте методы строк).
# print("12345".isdigit())

# 14. Дано число `1001`. Проверьте, является ли оно палиндромом (читается одинаково слева направо).
# number1 = str(1001)
# print(number1[0],number1[-1],number1[1],number1[-2])
# print(number1[0] == number1[-1] and number1[1] == number1[-2])

# ### Ввод и вывод данных ###
#
# # Легкие:
# 16. Пользователь вводит имя. Выведите `"Привет, [имя]!"`.
# name = input("Enter your name: ")
# print(name)
# print("Hello", name)

# 17. Запросите у пользователя возраст и выведите его через 5 лет.
# age = int(input("Enter your age: "))
# print(age + 5)

# 18. Напишите программу, которая спрашивает любимый цвет и выводит его в верхнем регистре.
# color = input("Enter your favourite color: ")
# print(color.upper())

# 19. Запросите два числа и выведите их произведение.
# num1 = 23
# num2 = 45
# print(num1 * num2)
#
# # Средние:
# 21. Пользователь вводит строку. Выведите ее длину.
# str1 = input("Enter your favourite book: ")
# print(len(str1))

# 22. Запросите число и проверьте, четное ли оно.
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("Correct")
# else:
#     print("Error")

# 23. Напишите программу-калькулятор для двух чисел (+, -, *, /).
# num1 = input("Enter the first number: ")
# num2 = input("Enter + or - or * or /")
# num3 = input("Enter the secod number: ")
# if num2 == "+":
#     print(num1 + num3)
# elif num2 == "-":
#     print(num1 - num3)
# elif num2 == "*":
#     print(num1 * num3)
# else:
#     print(num1 / num3)

# 24. Пользователь вводит предложение. Разбейте его на слова (список).
# suggestions = input("Enter a sentence: ")
# print(suggestions.split(" "))

# 25. Преобразуйте введенную строку в обратном регистре (большие → маленькие и наоборот).
# string1  = input("Enter a word: ")
# print(string1.swapcase())

# # Сложные:
# 26. Запросите пароль. Если длина меньше 8 символов, выведите ошибку.
# password = input("Enter your password: ")
# if len(password) < 8:
#     print("Error")
# else:
#     print("Correct")

# 27. Напишите программу, которая проверяет, является ли введенная строка палиндромом.
# 28. Конвертируйте введенное количество градусов Цельсия в Фаренгейты.  *1.8 + 32
# 29. Запросите число и выведите его квадрат, куб и квадратный корень.
# num1 = int(input("Enter a number: "))
# print(num1 ** 2)
# print(num1 ** 3)
# print(num1 ** 0.5)
#
# ### Списки ###
#
# # Легкие:
# 31. Создайте список чисел от `1` до `5` и выведите его.
# numbers = [1, 2, 3, 4, 5]
# print(numbers)

# 32. Добавьте число `6` в конец списка.
# numbers.append(6)
# print(numbers)

# 33. Выведите второй элемент списка `["яблоко", "банан", "вишня"]`.
# fruits = ["apple", "banana", "cherry"]
# print(fruits)

# 34. Удалите первый элемент списка `[10, 20, 30, 40]`.
# num1 = [10, 20, 30, 40]
# num1.remove(10)
# print(num1)

# 35. Проверьте, есть ли `"кофе"` в списке `["чай", "вода", "сок"]`.
# drinks = ["tea", "water", "juice"]
# print("coffee" in drinks)
#
# # Средние:
# 36. Дан список `[3, 1, 4, 2]`. Отсортируйте его.
# num1 = [3, 1, 4, 2]
# num1.sort()
# print(num1)

# 37. Объедините два списка `[1, 2]` и `[3, 4]` в один.
# num1 = [1, 2]
# num2 = [3, 4]
# concatenated_list = num1 + num2
# print(concatenated_list)

# 38. Найдите сумму элементов списка `[5, 10, 15, 20]`.
# list1 = [5, 10, 15, 20]
# print(sum(list1))

# 39. Удалите дубликаты из списка `[1, 2, 2, 3, 4, 4]`.
# list1 = [1, 2, 2, 3, 4, 4]
# print(set(list1))

# 40. Разверните список `[1, 2, 3, 4]` в обратном порядке.
# list1 = [1, 2, 3, 4]
# list1.reverse()
# print(list1)
#
# # Сложные:
# 41. Найдите наибольший и наименьший элементы в списке.
# list1 = [23, 45, 11, 46]
# print(max(list1))
# print(min(list1))

# 42. Отфильтруйте только четные числа из списка `[1, 2, 3, 4, 5, 6]`.
# list1 = [1, 2, 3, 4, 5, 6]
# print(list1[1::2])

# 43. Создайте список квадратов чисел от `1` до `10`.
# num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num2 = [num1 [0] ** 2, num1 [1] ** 2, num1 [2] ** 2, num1 [3] ** 2, num1 [4] ** 2, num1 [5] ** 2, num1 [6] ** 2, num1 [7] ** 2, num1 [8] ** 2, num1 [9] ** 2]
# print(num2)

# 44. Дан список чисел. Замените все отрицательные числа на `0`.
# numbers = [-23, -45, 56, -1, 66]
# numbers[0] = 0
# numbers[1] = 0
# numbers[3] = 0
# print(numbers)

# 45. Посчитайте количество вхождений элемента `5` в списке `[1, 5, 3, 5, 5, 2]`.
# list1 = [1, 5, 3, 5, 5, 2]
# print(list1.count(5))

#
# ### Словари ###
#
# # Легкие:
# 46. Создайте словарь `{"имя": "Анна", "возраст": 25}` и выведите имя.
# names = {
#     "name": "Anna",
#     "age": 25
# }
# print(names["name"])

# 47. Добавьте в словарь ключ `"город"` со значением `"Москва"`.
# names["city"] = "Moscow"
# print(names)

# 48. Удалите ключ `"возраст"` из словаря.
# names.pop("age")
# print(names)

# 49. Проверьте, есть ли ключ `"зарплата"` в словаре.
# if "wage" in names:
#     print("The key 'wage' is in the dictionary")
# else:
#     print("Error")

# 50. Выведите все ключи словаря `{"a": 1, "b": 2, "c": 3}`.
# num1 = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }
# print(num1.keys())
#
# # Средние:
# 51. Объедините два словаря `{"a": 1}` и `{"b": 2}`.
# dic1 = {
#     "a": 1
# }
# dic2 = {
#     "b": 2
# }
# dic1.update(dic2)
# print(dic1)

# 52. Инвертируйте словарь (`{1: "a", 2: "b"}` → `{"a": 1, "b": 2}`). !!!
# dic1 = {
#     1: "a",
#     2: "b"
# }
# print(dic1.clear())

# 53. Посчитайте сумму всех значений в словаре `{"яблоко": 50, "банан": 30}`.
# fruits = {
#     "apple": 50,
#     "banana": 30
# }
# print(fruits.values())
# print(sum(fruits.values()))

# 54. Отсортируйте словарь по ключам.
# print(fruits.keys())

# 55. Создайте словарь из списков `["a", "b"]` и `[1, 2]` (ключи — первый список).
# list1 = ["a", "b"]
# list2 = [1, 2]
# print({list1 [0] : list2 [0], list1 [1] : list2 [1]})
#
# # Сложные:
# 56. Найдите ключ с максимальным значением в словаре.
# num1 = {
#     1: 23,
#     2: 45,
#     3: 11
# }
# print(num1.values())
# num2 = num1.values()
# print(max(num2))

# 57. Удалите все элементы с пустыми значениями из словаря.
# my_dic = {
#     "apple": 2,
#     "grapes": 0,
#     "cherry": 3
# }
# my_dic.pop("grapes")
# print(my_dic)

# 58. Сгенерируйте словарь, где ключи — числа от `1` до `5`, а значения — их квадраты.
# numbers = {
#     1: 1 ** 2,
#     2: 2 ** 2,
#     3: 3 ** 2,
#     4: 4 ** 2,
#     5: 5 ** 2
# }
# print(numbers)

# 59. Дан список слов. Создайте словарь `{слово: длина_слова}`.
# list1 = ["apple", "grapes"]
# dict1 = {
#     list1[0]: len(list1[0]),
#     list1[1]: len(list1[1])
# }
# print(dict1)

# 60. Сравните два словаря на идентичность.
# print(my_dic == numbers)

# ### Кортежи и множества ###
#
# # Легкие:
# 61. Создайте кортеж `(1, 2, 3)` и выведите его длину.
# tuple1 = (1, 2, 3)
# print(len(tuple1))

# 62. Преобразуйте список `[4, 5, 6]` в кортеж.
# list1 = [4,  5, 6]
# print(tuple(list1))

# 63. Создайте множество `{1, 2, 3}` и добавьте `4`.
# set1 = {1, 2, 3}
# set1.add(4)
# print(set1)

# 64. Проверьте, есть ли `5` в множестве `{2, 3, 4}`.
# set1 = {2, 3, 4}
# print(5 in set1)

# 65. Найдите общие элементы множеств `{1, 2, 3}` и `{3, 4, 5}`.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1.intersection(set2))

#
# # Средние:
# 66. Объедините два множества `{1, 2}` и `{2, 3}`.
# set1 = {1, 2}
# set2 = {2, 3}
# print(set1.union(set2))

# 67. Удалите элемент `3` из множества `{1, 2, 3, 4}`.
# set0 = {1, 2, 3, 4}
# set0.remove(3)
# print(set0)

# 68. Проверьте, является ли множество `{1, 2}` подмножеством `{1, 2, 3}`.
# subset = {1, 2}
# superset = {1, 2, 3}
# print(subset < superset)
# print(subset > superset)

# 69. Создайте неизменяемое множество (frozenset).
# set1 = (frozenset[1, 2, 3, 4, 5])
# print(set1)

# 70. Посчитайте количество уникальных слов в списке `["яблоко", "банан", "яблоко"]`.
# list1 = ["apple", "banana", "apple"]
# print(len(set(list1)))
#
# # Сложные:
# 71. Удалите дубликаты из списка, используя множества.
# list1 = [1, 1, 2, 2, 4, 5]
# print(set(list1))

# 72. Найдите элементы, которые есть только в одном из двух множеств.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1.difference(set2))

# 73. Сгенерируйте все возможные подмножества множества `{1, 2}`.
# superset = {1, 2}
# subset = {1}
# subset1 = {2}
# subset2 = {2, 1}

# 74. Проверьте, являются ли два множества непересекающимися.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(True if set1.intersection(set2) else False)

# 75. Дан кортеж чисел. Найдите минимальный и максимальный элементы.
# tuple1 = (34, 78, 12, 99)
# print(max(tuple1))
# print(min(tuple1))

#
# ### Комбинированные задачи (сложные) ###
#
# 76. Создайте список словарей (каждый словарь — информация о человеке).
# info = [{"name": "Nawal", "age": 29, "job": "sales associate"}, {"name": "Emilie", "age": 23, "job": "key holder"}]
# print(info)

# 77. Отсортируйте список словарей по ключу `"возраст"`. !!!
# ages = {"Nawal": 29, "Emilie": 23, "Oliver": 37}
# print(ages)

# 78. Из списка чисел создайте словарь `{число: его_квадрат}`.
# list1 = [12, 2, 3, 5]
# list2 = {list1[0]: list1[0] ** 2, list1[1]: list1[1] ** 2, list1[2]: list1[2] ** 2, list1[3]: list1[3] ** 2}
# print(list2)

# 79. Объедините два списка в словарь (`keys = ["a", "b"]`, `values = [1, 2]`).
# keys = ["a", "b"]
# values = [1, 2]
# list1 = {keys[0]: values[0], keys[1]: values[1]}
# print(list1)

# 80. Найдите самое часто встречающееся слово в тексте (строка → список слов → счетчик).
# str1 = "Hello World Love Peace"
# list1 = str1.split()
# counts = [list1.count("Hello"), list1.count("World"), list1.count("Love"), list1.count("Peace")]
# print(list1)
# print(counts)

# 81. Создайте вложенный словарь (например, данные о студентах с предметами и оценками).
# students = {
#     "Nawal": {"History": 100, "Music": 98},
#     "Emilie": {"History": 90, "Music": 99},
#     "Oliver": {"History": 89, "Music": 100}
# }
# print(students)

# 82. Преобразуйте список кортежей `[("a", 1), ("b", 2)]` в словарь.
# list1 = [("a", 1), ("b", 2)]
# dict1 = dict(list1)
# print(dict1)

# 83. Отфильтруйте словарь, оставив только элементы со значениями больше `10`.
# numbers = {
#     "a": 4,
#     "b": 5,
#     "c": 9
# }
# if numbers.get("a") > 10:
#     print(numbers.get("a"))
# if numbers.get("b") > 10:
#     print(numbers.get("b"))
# if numbers.get("c") > 10:
#     print(numbers.get("c"))
# else:
#     print("All values are less then 10")

# 84. Сгенерируйте словарь, где ключи — буквы алфавита, а значения — их ASCII-коды. !!!


# 85. Напишите функцию, которая объединяет два списка в словарь (проверяя длину).
# list1 = ["Nawal", "Emilie", "Oliver"]
# list2 = [29, 23, 37]
# if len(list1) == len(list2):
#     print({list1[0]: list2[0], list1[1]: list2[1], list1[2]: list2[2]})
# else:
#     print("Error")

# 86. Дан список чисел. Создайте словарь `{число: количество_вхождений}`.
# numbers1 = [12, 23, 34, 12]
# num1 = {numbers1[0]: numbers1.count(numbers1[0]), numbers1[1]: numbers1.count(numbers1[1]), numbers1[2]: numbers1.count(numbers1[2])}
# print(num1)

# 87. Найдите пересечение ключей двух словарей.
# dict1 = {
#     "Nawal": 29,
#     "Emilie": 23,
#     "Oliver": 37
# }
# dict2 = {
#     "Nawal": 29,
#     "Vesna": 56,
#     "Natalya": 46
# }
# d1 = set(dict1.values()).intersection(set(dict2.values()))
# print(d1)

# 88. Отсортируйте словарь по значениям в порядке убывания.
# sorted_dict1 = dict(sorted(dict1.items(), reverse= True))
# print(sorted_dict1)

# 89. Создайте словарь из строки, где ключи — символы, а значения — их количество в строке.
# name = "Nawal"
# dict2 = {name[0]: name.count(name[0]), name[1]: name.count(name[1]), name[2]: name.count(name[2]),
#          name[3]: name.count(name[3]), name[4]: name.count(name[4])}
# print(dict2)

# 90. Реализуйте поиск по значению в словаре (выведите ключ по заданному значению).!!!
# search = int(input("Enter a value: "))
# dic1 = {
#     "Nawal": 29,
#     "Emilie": 23,
#     "Oliver": 39
# }


# 91. Создайте кортеж из списка, удалив повторяющиеся элементы.
# list1 = [1, 2, 3, 4, 4, 4, 5, 5]
# print(tuple(set(list1)))

# 92. Объедините несколько словарей в один (используйте `update` или `**`).
# dic1 = {
#     "Nawal": 29,
# }
# dic2 = {
#     "Emilie": 23,
#     "Oliver": 37
# }
# dic1.update(dic2)
# print(dic1)

# 93. Проверьте, все ли значения в словаре уникальны.
# dic1 = {
#     "apple": 2,
#     "cherry": 6,
#     "pineapple": 3
# }
# if dic1.get("apple") == dic1.get("cherry") and dic1.get("apple") == dic1.get("pineapple") and dic1.get("cherry") == dic1.get("pineapple"):
#     print("All values are the same")
# else:
#     print("All values are unique")

# 94. Разделите словарь на два: в одном ключи с четными значениями, в другом — с нечетными.
# dic1 = {
#     "apple": 2,
#     "cherry": 6,
#     "pineapple": 3,
# }
# dic2 = {}
# dic3 = {}
# if dic1.get("apple") % 2 == 0 and dic1.get("cherry") % 2 == 0:
#     print("Yes")
#     dic2.setdefault(dic1.get("apple"))
#     dic2.setdefault(dic1.get("cherry"))
# if dic1.get("pineapple") % 2 != 0:
#     print("No")
#     dic3.setdefault(dic1.get("pineapple"))
#
# print(dic2)
# print(dic3)

# 95. Преобразуйте словарь в список кортежей `(ключ, значение)`.
# tuple1 = (tuple[(dic1.items())])
# print(tuple1)

# 96. Напишите функцию, которая инвертирует вложенный словарь (меняет местами ключи и значения).!!!


# 97. Создайте множество из списка, но с условием (например, только четные числа).
# list1 = [1, 2, 3]
# set1 = set()
# if list1[0] % 2 == 0:
#     set1.add(list1[0])
# if list1[1] % 2 == 0:
#     set1.add(list1[1])
# if list1[2] % 2 == 0:
#     set1.add(list1[2])
# print(set1)

# 98. Найдите симметричную разность трех множеств.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set3 = {5, 6, 7}
# print(set1.symmetric_difference(set2))
# print(set1.symmetric_difference(set3))
# print(set2.symmetric_difference(set3))

# 99. Реализуйте проверку на анаграмму (используйте множества и словари).
# set1 = {1001}
# set2 = set(sorted(set1, reverse= True))
# print(set1)
# print(set2)
# if set1 == set2:
#     print("True")
# else:
#     print("False")

# 100. Создайте генератор словарей для хранения таблицы умножения (ключи — пары чисел).
