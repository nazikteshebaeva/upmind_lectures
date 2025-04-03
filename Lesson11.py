"""
Урок 12: Прерывание циклов (break, continue, else)
"""

# 1. break - досрочное завершение цикла
"""
Оператор break прерывает выполнение цикла и выходит из него.
"""
# for i in range(1, 11):
#     if i == 5:
#         print("Остановлено на", i)
#         break  # Выход из цикла при i == 5
#     print(i)  # Выведет 1, 2, 3, 4

# 2. continue - пропуск итерации
"""
Оператор continue пропускает текущую итерацию цикла и переходит к следующей.
"""
# for i in range(1, 6):
#     if i == 3:
#         continue  # Пропускаем число 3
#     print(i)  # Выведет 1, 2, 4, 5

# 3. else в циклах
"""
Блок else выполняется, если цикл завершился без использования break.
"""
# for i in range(1, 6):
#     print(i)
# else:
#     print("Цикл завершился без прерываний")  # Этот код выполнится
#
# for i in range(1, 6):
#     if i == 3:
#         break  # Прерываем цикл
#     print(i)
# else:
#     print("Этот код не выполнится, так как цикл прерван")

# ОЗНАКОМИТЕЛЬНЫЕ ЗАДАЧИ (10 штук)

# 1. Используя break, прервите цикл при достижении числа 7.
# for i in range(1, 11):
#     if i == 7:
#         break
#     print(i)

# 2. Используя continue, пропустите число 4 в цикле от 1 до 10.
# for i in range(1, 11):
#     if i == 4:
#         continue
#     print(i)

# 3. Выведите все числа от 1 до 10, но остановитесь при первом четном числе.
# for i in range(1, 11):
#     if i % 2 ==0:
#         break
#     print(i)

# 4. Найдите первое число, делящееся на 7 в диапазоне 10-100.
# for i in range(10, 101):
#     if i % 7 == 0:
#         break
#     print(i)

# 5. Используйте else в цикле, чтобы определить, было ли найдено число 5 в списке [1, 2, 3, 6, 7].
# list1 = [1, 2, 3, 6, 7]
# for i in list1:
#     if i == 5:
#         print(i)
# else:
#     print("5 was not found")

# 6. Выведите все буквы слова "Python", кроме "o".
# for character in "Python":
#     if character == "o":
#         break
#     print(character)

# 7. Используйте continue, чтобы вывести все нечетные числа от 1 до 20.
# for i in range(1, 21):
#     if i % 2 == 0:
#         continue
#     print(i)

# 8. Используйте break, чтобы найти первое число, кратное 13 в диапазоне 1-100.
# for i in range(1, 101):
#     if i % 13 == 0:
#         print(i)
#         break

# 9. Используйте else в while-цикле, чтобы определить, был ли завершен поиск числа.
# lst = list(range(1, 21))
# i = 0
#in while we have to create i
# while i < len(lst):
#     if lst[i] == 10:
#         print("10 was found")
#         break
#     print(lst[i])
#     i += 1
# else:
#     print("No 10 was found")

# lst =[1, 2, 3, 4, 5, 6, 7, 8, 9]
# i = 0
# while i < len(lst):
#     if lst[i] == 10:
#         print("10 was found")
#         break
#     print(lst[i])
#     i += 1
# else:
#     print("No 10 was found")

# 10. Напишите программу, которая завершает ввод пользователя после слова "стоп".
# got_response = False
# while not got_response:
#     response = input("Input a sentence: ")
#     print(response)
#     if response == "stop":
#         got_response = True
#         print("Process has been done!")
#         break
#The second version of number 10
# while True:
#     s = input()
#     if s == "stop":
#         break




#More examples to understand more:
# numbers =[5, 124, 12, 53, 5]
# students = {"nazik": 25, "beks": 28, "begaiym": 22}
# for i in numbers:
#     print(i)
# else:
#     print("that is it")
#
# for i in students.values():
#     print(i + 1)
#
# el = 0
# while el < len(numbers):
#     print(numbers[el] + 1)
#     el += 1
#
# for el in numbers:
#     print(el)
#     print(el + 1)
#
# print(numbers[0] + 1)
# print(numbers[1] + 1)
# print(numbers[2] + 1)
# print(numbers[3] + 1)
# print(numbers[4] + 1)