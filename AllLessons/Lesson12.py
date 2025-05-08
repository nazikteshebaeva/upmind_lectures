"""
Урок 13: Углубленное изучение списков: генераторы списков.
Циклы в словарях, zip(), enumerate()
"""

# Генераторы списков
"""
Генераторы списков позволяют создавать списки в одну строку кода, что делает их удобными и читаемыми.

Синтаксис:
[выражение for переменная in последовательность if условие]

Пример:
"""
# Создадим список квадратов чисел от 1 до 10
squares = [x ** 2 for x in range(1, 11)]
print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Оставим только чётные квадраты
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]

# Циклы в словарях
"""
Когда работаем со словарями, часто нужно итерироваться по ключам, значениям или сразу по парам (ключ, значение).
"""
example_dict = {'apple': 3, 'banana': 5, 'cherry': 2}

# Перебор ключей
for key in example_dict:
    print(key)

# Перебор значений
for value in example_dict.values():
    print(value)

# Перебор ключей и значений
for key, value in example_dict.items():
    print(f"{key}: {value}")

# Функция zip()
"""
Функция zip() используется для объединения нескольких последовательностей в кортежи.
"""
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name} набрал {score} баллов")

# Функция enumerate()
"""
enumerate() добавляет индекс к элементам последовательности.
"""
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1): #numbers like a list of items, if we just delete start=1,
    # and write only fruits, it will give us an index of items in consol.
    print(f"{index}. {fruit}")

