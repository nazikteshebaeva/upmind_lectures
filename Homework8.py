#Домашнее задание (40 задач):
# 1. Создай кортеж из трёх случайных строк и проверь, содержится ли в нём строка "Python".
# strings = ("Lemon", "Apple", "Python")
# print("Python" in strings)

# 2. Преобразуй строку "hello world" в кортеж символов.
# str1= "hello world"
# print(tuple("hello world"))

# 3. Даны два кортежа: (1, 2, 3) и (4, 5, 6). Объедини их в один.
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# tuple1 += tuple2
# print(tuple1)

# 4. Создай кортеж чисел и посчитай количество вхождений числа 5.
# numbers = (5, 5, 5, 5, 5, 6)
# print(numbers.count(5))

# 5. Даны два кортежа. Проверь, совпадает ли первый элемент первого кортежа с последним элементом второго.
# tuple1 = (1, 2, 3)
# tuple2 = (3, 2, 2)
# if tuple1[0] == tuple2[-1]:
#     print("Pass")
# else:
#     print("Error")

# 6. Напиши программу, которая меняет местами первый и последний элемент кортежа.!!!
# tuple1 = (1, 2, 3, 4, 5)


# 7. Создай пустое множество и добавь в него три уникальных числа.
# my_set = set()
# my_set.add(12)
# my_set.add(13)
# my_set.add(14)
# print(my_set)

# 8. Удали произвольный элемент из множества {10, 20, 30, 40}.
# set1 = {10, 20, 30, 40}
# set1.pop()
# print(set1)

# 9. Создай множество из строки "abracadabra" и выведи уникальные символы.
# set1 = set("abracadabra")
# print(set1)

# 10. Объедини множества {1, 2, 3} и {3, 4, 5}.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1.union(set2))

# 11. Проверь, являются ли множества {1, 2, 3} и {3, 2, 1} равными.
# set1 = {1, 2, 3}
# set2 = {3, 2, 1}
# if set1 == set2:
#     print("Sets are equal")
# else:
#     print('Sets are not equal')

# 12. Создай множество с числами от 1 до 10 и удали все чётные числа. !!!
# set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#set1 % 2 != 0 I did not understand how to write this

# 13. Напиши программу, которая проверяет, есть ли пересечение у множеств {1, 2, 3} и {4, 5, 6}.
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# print(set1.intersection(set2))

# 14. Дан кортеж чисел. Выведи все элементы, кроме первого и последнего.
# num1 = (1, 2, 3, 4, 5)
# num2 = num1[1:-1]
# print(num2)

# 15. Проверь, может ли кортеж (1, 2, 3) быть ключом словаря. !!!
# tuple1 = (1, 2, 3)

# 16. Создай кортеж и преобразуй его в строку через запятую.
# tuple2 = tuple("apple",)
# string1 = ",".join(tuple2)
# print(string1)

# 17. Найди количество уникальных символов в строке "datascience" с использованием множества.
# str_text = "datasciene"
# text = set(str_text)
# print(len(text))

# 18. Создай множество из списка чисел [1, 2, 2, 3, 4, 4, 5] и выведи его длину.
# numbers1 = [1, 2, 2, 3, 4, 4, 5]
# num2 = set(numbers1)
# print(len(num2))

# 19. Напиши программу, которая возвращает разность множеств {1, 2, 3} и {2, 3, 4}.
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# print(set1.difference(set2))
# print(set2.difference(set1))

# 20. Дан кортеж чисел. Найди сумму всех элементов, не используя встроенную функцию sum(). !!!
# tuple1 = (23, 34, 45, 56)


# 21. Создай множество из чисел от 1 до 5 и проверь, является ли число 3 элементом множества.
# set1 = {1 ,2 , 3, 4, 5}
# print(3 in set1)

# 22. Найди длину кортежа (10, 20, 30, 40).
# tuple1 = (10, 20, 30, 40)
# print(len(tuple1))

# 23. Создай кортеж, содержащий 5 одинаковых элементов.
# tuple1 = (1, 1, 2, 3, 3, 4, 4, 5, 5, 5)

# 24. Дан кортеж с числами. Найди индекс первого отрицательного числа.
# tuple1 = (23, 34, 45, -1, -34)
# print(tuple1.index(-1))

# 25. Напиши программу, которая проверяет, можно ли преобразовать множество {1, 2, 3} в неизменяемое множество (frozenset).
# set1 = {1, 2 , 3}
# print(frozenset(set1))

# 26. Проверь, является ли множество {1, 2} подмножеством {1, 2, 3, 4}.
# subset = {1, 2}
# superset = {1, 2, 3, 4}
# print(subset < superset)
# print(subset > superset)

# 27. Напиши программу, которая возвращает симметрическую разность множеств {1, 2, 3} и {3, 4, 5}.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1.symmetric_difference(set2))

# 28. Создай кортеж и найди индекс первого вхождения числа 7.
# tuple1 = (1, 2, 3, 4, 5, 6, 7)
# print(tuple1.index(7))

# 29. Напиши программу, которая создаёт множество из всех символов строки "python" и удаляет из него символ 'h'.
# word = "python"
# set1 = set(word)
# set1.discard("h")
# print(set1)

# 30. Проверь, является ли множество {1, 2, 3} надмножеством {2, 3}.
# superset = {1, 2, 3}
# subset = {2, 3}
# print(superset < subset)
# print(superset > subset)

# 31. Создай кортеж и попытайся изменить его элемент (ожидай ошибку).
# tuple1 = (1, 2, 3, 4, 5)
# print(tuple1.add(6))
# print(tuple1)

# 32. Напиши программу, которая находит общие элементы в кортежах (1, 2, 3) и (2, 3, 4).
# tuple1 = (1, 2, 3)
# tuple2 = (2, 3, 4)
# set1 = set(tuple1)
# print(set1)
# set2 = set(tuple2)
# print(set2)
# print(set1.intersection(set2))

# 33. Создай множество из чисел и удали из него минимальное значение.
# set1 = {11, 22, 44, 1}
# set2 = min(set1)
# print(set2)
# set1.remove(set2)
# print(set1)

# 34. Преобразуй кортеж (1, 2, 3) в список и добавь к нему число 4.
# tuple1 = (1, 2, 3)
# list1 = list(tuple1)
# print(list1)
# list1.append(4)
# print(list1)

# 35. Создай кортеж из случайных чисел и отсортируй его (без изменения оригинала).
# tuple1 = (4, 8, 9 ,2, 1)
# sorted_t = tuple(sorted(tuple1))
# print(sorted_t)

# 36. Напиши программу, которая проверяет, есть ли пересечение у множеств {1, 2, 3} и {4, 5, 6}.
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# print(set1.intersection(set2))

# 37. Создай кортеж из строк и найди самую длинную строку. !!!
# tuple1 = ("apple", "grapes", "cucumber")
# long_string = max(tuple1)
#len?

# 38. Преобразуй кортеж в множество и найди его длину.
# tuple1 = (1, 2, 3, 4, 5)
# set1 = set(tuple1)
# print(set1)
# print(len(set1))

# 39. Найди минимальный элемент множества {10, 20, 5, 30}.
# set1 = {10, 20, 5, 30}
# print(min(set1))

# 40. Создай множество и добавь в него все буквы строки "data" и "science" без повторений.
# set1 = set("data")
# set2 = set("science")
# print(set1.union(set2))