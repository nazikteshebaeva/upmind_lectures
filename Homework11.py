# 1. Прервите цикл, если пользователь ввел отрицательное число.
# while True:
#     numbers = int(input("Enter  a number: "))
#     if numbers < 0:
#         print(numbers)
#         break

# 2. Используйте continue, чтобы пропустить все гласные буквы в введенной строке.
# while True:
#     letter = input("Enter a letter: ")
#     if letter.lower() in "aeiouy":
#         continue
#     print(letter)

# 3. Напишите программу, которая запрашивает у пользователя числа, суммируя их, пока не введено 0.
# num = 0
# while True:
#     numbers = int(input("Enter a number: "))
#     if numbers == 0:
#         print(numbers)
#         break
#     num += numbers
#     print(num)

# 4. Найдите первое число больше 50, которое делится на 9 без остатка.
# while True:
#     numbers = int(input("Enter a number: "))
#     if numbers > 50 and numbers % 9 == 0:
#         print(numbers)
#         break

# 5. Выведите все числа от 10 до 1, пропуская числа, делящиеся на 3.
# for num in range(1, 11):
#     if num % 3 == 0:
#         continue
#     print(num)

# 6. Проверьте, содержит ли список число 10, используя else в for.
# lst = [1, 2, 6, 7, 8]
# for i in lst:
#     if 10 in lst:
#         print("There is a number 10")
#         break
#     else:
#         print(i)

# 7. Выведите только четные числа из списка [1, 3, 4, 7, 8, 10].
# lst1 = [1, 3, 4, 7, 8, 10]
# for i in lst1:
#     if i % 2 == 0:
#         print(i)

# 8. Найдите первый символ "а" в строке и завершите поиск.
# str1 = "Hello Hannah"
# for i in str1:
#     print(i)
#     if i == "a":
#         print(i)
#         break

# 9. Прервите цикл, если число из списка [2, 4, 6, 8, 9] делится на 5.
# numbers = [2, 4, 6, 8, 9]
# for num in numbers:
#     if num % 5 == 0:
#         break
#     print(num)

# 10. Выведите первые 5 чисел Фибоначчи, но остановитесь, если встретите число больше 10.


# 11. Напишите программу, которая ищет первое четное число в списке и прекращает выполнение.
# lst1 = [13, 45, 2, 3]
# for num in lst1:
#     if num % 2 == 0:
#         break
#     print(num)

# 12. Используйте while, чтобы выводить числа от 100 до 1, пропуская числа, делящиеся на 5.!!!
# num = range(1, 101)
# while True:
#     if num[] % 5 == 0:
#         continue
#     print(num)


# 13. Используйте break в бесконечном цикле, если число больше 100.
# while True:
#     num = int(input("Enter a number: "))
#     if num > 100:
#         break
#     print(num)

# 14. Переберите список и пропустите все элементы, содержащие букву "e".
# lst1 = ["Emilie", "Emanuel", "Nawal"]
# for lst2 in lst1:
#     if "e" in lst2:
#         continue
#     print(lst2)

# 15. Используйте else в цикле while, который завершится без break.
# num = 0
# while num < 5:
#     print(num)
#     num += 1
# else:
#     print("While is not working")

# 16. Найдите первое число, большее 1000, которое делится на 37 без остатка.
# while True:
#     num = int(input("Enter a number: "))
#     if num > 1000 and num % 37 == 0:
#         print(num)
#         break

# 17. Запросите у пользователя пароль и прекратите цикл, если введен правильный пароль.
# password = "nazik99"
# while True:
#     enter_a_password = input("Enter a password: ")
#     if password == enter_a_password:
#         print("Welcome")
#         break

# 18. Используйте continue, чтобы пропускать числа, которые делятся на 4.
# while True:
#     num1 = int(input("Enter a number: "))
#     if num1 % 4 == 0:
#         continue
#     print(num1)

# 19. Прервите цикл, если сумма всех чисел превысила 200.
# num = 0
# while True:
#     num1 = int(input("Enter a number: "))
#     num += num1
#     if num > 200:
#         print(num)
#         break
#     print(num)

# 20. Выведите таблицу умножения на 9, но прекратите после 9 x 5.
# for i in range(1, 10):
#     for j in range(1, 6):
#         print(i * j, end="\t")
#     print()

# 21. Найдите первую букву в строке, которая не является заглавной.
# str1 = "naWAL"
# for i in str1:
#     if i.isupper():
#         print(i)
#         break

# 22. Переберите список имен и пропустите все, которые начинаются на "A".
# names = ["Nawal", "Emilie", "Aiman"]
# for i in names:
#     if i.startswith("A"):
#         continue
#     print(i)

# 23. Используйте break, чтобы прервать выполнение при нахождении простого числа.
# while True:
#     num = int(input("Enter a number: "))
#     if num % num == 0 and num % 1 == 0:
#         print(num)
#         break

# 24. Используйте else в цикле for, чтобы проверить, все ли числа четные.
# num = [12, 23, 34, 45]
# for i in num:
#     if i % 2 == 0:
#         print(i)
#     else:
#         print("Error")

# 25. Запросите у пользователя числа, и прекратите ввод, если сумма превысила 1000.
# num1 = 0
# while True:
#     num = int(input("Enter a number: "))
#     num1 += num
#     if num1 > 1000:
#         print(num1)
#         break

# 26. Переберите все цифры числа и остановитесь, если встретите 7.
# num = [2, 6, 4, 7, 9]
# for i in num:
#     print(i)
#     if i == 7:
#         break

# 27. Напишите программу, которая ищет первое четное число среди случайных чисел.
# num = [34, 22, 7]
# for i in num:
#     print(i)
#     if i % 2 == 0:
#         break

# 28. Используйте continue, чтобы пропустить числа, оканчивающиеся на 5.
# while True:
#     num = input("Enter a number: ")
#     if num.endswith("5"):
#         continue
#     print(num)

# 29. Выведите буквы слова "Programming", пропуская гласные.
# word = "Programming"
# for i in word:
#     if i.lower() in "aeiouy":
#         continue
#     print(i)

# 30. Напишите игру, где пользователь вводит числа, и проигрывает при вводе отрицательного числа.
# while True:
#     game = int(input("Enter a number: "))
#     if game < 0:
#         print("You lost the game")

# 31. Выведите все делители числа 100, но прекратите при нахождении первого простого делителя.!!!

# 32. Найдите сумму всех цифр числа, но прекратите, если цифра равна 0.
# num = input("Enter a number: ")
# for i in num:
#     if i == "0":
#         break
#     else:
#         print(i)

# 33. Переберите список дат и прекратите выполнение, если встретится 1 января.
# str1 = ["23.08", "01.01"]
# for i in str1:
#     if i == "01.01":
#         break
#     print(i)

# 34. Используйте while для проверки пароля, запрашивая ввод, пока он не будет правильным.
# passw = "nazik99"
# while True:
#     password = input("Enter a password: ")
#     if password == passw:
#         print("You have entered!")

# 35. Найдите первую букву в строке, которая является заглавной, и прекратите выполнение.
# str1 = "naWal"
# for i in str1:
#     if i.isupper():
#         print(i)
#         break

# 36. Прервите цикл, если встречается два подряд идущих одинаковых числа.
# num = [12, 23, 23, 45]
# for i in range(0, 5):
#     if num[i] == num[i + 1]:
#         print(num[i])
#         break

# 37. Используйте break для выхода из вложенного цикла, если сумма элементов превышает 50.!!!


# 38. Переберите числа от 1 до 100, останавливаясь на первом числе, делящемся на 17.
# for el in range(1, 101):
#     if el % 17 == 0:
#         print(el)
#         break

# 39. Используйте continue для пропуска всех слов, содержащих букву "z".
# words = ["year", "happy", "sza"]
# for el in words:
#     if "z" in el:
#         print(el)
#         break
#
# 40. Переберите список и прекратите выполнение, если элемент встречается второй раз.
# num = [12, 23, 23, 45]
# for i in range(0, 5):
#     if num[i] == num[i + 1]:
#         print(num[i])
#         break

# Дополнительные задачи с вложенными циклами
# 1. Нарисуйте треугольник из символов "*" с помощью вложенного цикла.
# 2. Создайте шахматную доску 8x8, используя символы "#" и ".".
# 3. Переберите числа от 1 до 100 и найдите первую пару чисел, сумма которых равна 50.
# 4. Переберите строку и найдите первую букву, которая встречается дважды.
# 5. Переберите список списков и найдите первый вложенный список, содержащий отрицательное число.
