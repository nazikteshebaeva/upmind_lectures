
# Урок 27: Введение в ООП (Объектно-Ориентированное Программирование)

# 1. Что такое ООП (Объектно-Ориентированное Программирование)?
# ООП — это методология программирования, основанная на концепции объектов и классов.
# Классы представляют собой шаблоны для создания объектов.
# Объекты — это экземпляры классов, которые содержат данные (атрибуты) и методы для работы с этими данными.

# Пример:

# class Person: #the name of the class comes with a capital letter
#     """ Class, talking about a person in general """
#     def __init__(self, name, age):
#         #construction: initiating atributs
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."
#
# p = Person("John", 30)
# print(p.greet())  # Output: Hello, my name is John, and I am 30 years old.


# 2. Основные элементы ООП:
# Классы и объекты:
# Класс — это как шаблон для объектов. #overall like Person
# Объект — это экземпляр класса. #Anna (specific example of the Person)

# Пример:

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return f"{self.name} makes a sound."
#
# animal1 = Animal("Dog")
# print(animal1.speak())  # Output: Dog makes a sound.


# Конструктор __init__():
# Метод __init__ используется для инициализации объекта с атрибутами, которые он будет содержать.

# Пример:

# class Car:
#     def __init__(self, make, model, wheels=4):
#         self.wheels = wheels
#         self.make = make
#         self.model = model
#
# my_car = Car("Toyota", "Corolla", 3)
# print(my_car.make, my_car.model, my_car.wheels)  # Output: Toyota Corolla


# 3. Методы и атрибуты:
# Атрибуты — это переменные, которые хранят информацию о объекте.
# Методы — это функции, которые выполняют операции с атрибутами объекта.

# Пример:

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#
#     def bark(self):
#         return f"{self.name} barks!"
#
# dog1 = Dog("Buddy", "Golden Retriever")
# print(dog1.bark())  # Output: Buddy barks!


# 4. Подведение итогов:
# ООП является мощной концепцией, которая позволяет создавать гибкие и масштабируемые программы.
# В ООП важны классы и объекты как основные элементы.
# В следующем уроке мы подробно рассмотрим инкапсуляцию, полиморфизм, наследование и абстракцию в ООП.

# Домашнее задание (Задачи для практики):
# 1. Создайте класс Car, который имеет атрибуты make (марка автомобиля), model (модель) и year (год выпуска).
# Добавьте метод get_car_info(), который выводит информацию о машине.

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_car_info(self):
#         return f"Car Info: {self.year} {self.make} {self.model}"
#
# car = Car("Toyota", "Camry", 2022)
# print(car.get_car_info())  # Output: Car Info: 2022 Toyota Camry


# 2. Создайте класс Circle, который имеет атрибут radius (радиус).
# Добавьте методы для вычисления площади и периметра круга.

import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * (self.radius ** 2)
#
#     def perimeter(self):
#         return 2 * math.pi * self.radius
#
# circle = Circle(5)
# print(circle.area())  # Output: 78.53981633974483
# print(circle.perimeter())  # Output: 31.41592653589793


# 3. Создайте класс Rectangle, который имеет атрибуты width (ширина) и height (высота).
# Добавьте метод для вычисления площади прямоугольника.

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# rectangle = Rectangle(10, 5)
# print(rectangle.area())  # Output: 50


# 4. Реализуйте полиморфизм, создав классы Bird и Fish, которые переопределяют метод move(),
# в котором будет описан способ передвижения (полет и плавание соответственно).

# class Bird:
#     def move(self):
#         return "I fly in the sky!"
#
# class Fish:
#     def move(self):
#         return "I swim in the water!"
#
# bird = Bird()
# fish = Fish()
# print(bird.move())  # Output: I fly in the sky!
# print(fish.move())  # Output: I swim in the water!


# 5. Создайте класс Person с атрибутами name и age. Реализуйте метод greet(), который будет возвращать приветствие.
# Используя наследование, создайте класс Student, который будет добавлять атрибут student_id и переопределит метод greet().

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."
#
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id
#
#     def greet(self):
#         return f"Hello, my name is {self.name}, I am {self.age} years old, and my student ID is {self.student_id}."
#
# student = Student("Alice", 20, "S1234")
# print(student.greet())  # Output: Hello, my name is Alice, I am 20 years old, and my student ID is S1234.

# ДЗ

# 1. **Класс «Круг»**
#    Создайте класс `Circle` с публичным атрибутом `radius` (радиус). Добавьте метод `area()`, возвращающий площадь
#    круга (`π * radius**2`), и метод `circumference()`, возвращающий длину окружности (`2 * π * radius`).

import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
#     def circumference(self):
#         return 2 * math.pi * self.radius
#
# c = Circle(15)
# print(c.area())
# print(c.circumference())

# 2. **Класс «Студент»**
#    Определите класс `Student` с атрибутами `name` (имя) и `grades` (список оценок). Реализуйте методы:
#
#    * `add_grade(grade)` — добавить оценку в список;
#    * `average()` — вычислить и вернуть среднее арифметическое всех оценок.

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#
#     def average(self):
#         if self.grades:
#             return sum(self.grades) / len(self.grades)
#         else:
#             return "Error!"
#
# s = Student("Nawal")
# s.add_grade(100)
# s.add_grade(98)
# s.add_grade(88)
#
# print(f"{s.name}'s average grade is: {s.average()}")

# 3. **Класс «Вектор 2D»**
#    Напишите класс `Vector2D` с атрибутами `x` и `y`. Реализуйте «магические» методы:
#
#    * `__add__(other)` для сложения двух векторов;
#    * `__sub__(other)` для вычитания;
#    * `__repr__()` для удобного строкового представления.

# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self):
#         return self.x + self.y
#
#     def __sub__(self):
#         return self.x - self.y
#
#     def __repr__(self):
#         return "Hello, World!"
#
# v = Vector2D(2, 6)
# print(v.__add__(), v.__repr__(), v.__sub__())

# 4. **Класс «Книга»**
#    Создайте класс `Book` с атрибутами `title`, `author` и `pages` (кол-во страниц). Добавьте метод `description()`, возвращающий строку:
#
#    ```
#    "<title> — автор <author>, <pages> стр."
#    ```
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def description(self):
#             return f"'{self.title}' - author {self.author}, {self.pages} pages."
#
# b = Book("Maybe in another life", "TJR", 2014)
# print(b.description())

# 5. **Класс «Точка»**
#    Определите класс `Point` с координатами `x` и `y`. Добавьте метод `distance_to_origin()`,
#    возвращающий расстояние от точки до начала координат, и метод `distance_to(other)`,
#    возвращающий расстояние до другой точки.

# import math
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def distance_to_origin(self):
#         return math.sqrt(self.x ** 2 + self.y ** 2)
#
#     def distance_to(self, other):
#         return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
# p1 = Point (3, 4)
#
# print(p1.distance_to_origin())

# 6. **Класс «Конвертер температур»**
#    Напишите класс `TemperatureConverter` с двумя статическими методами (без использования `@classmethod`):
#
#    * `c_to_f(celsius)` — перевод из °C в °F;
#    * `f_to_c(fahrenheit)` — перевод из °F в °C.

# class TemperatureConverter:
#     @staticmethod
#     def c_to_f(celsius):
#         return celsius * 9 / 5 + 32
#
#     @staticmethod
#     def f_to_c(fahrenheit):
#         return (fahrenheit - 32) * 5 / 9
#
# print(TemperatureConverter.c_to_f(0))
# print(TemperatureConverter.f_to_c(99))


# 7. **Класс «Матрица 2×2»**
#    Создайте класс `Matrix2x2`, хранящий четыре числа `a, b, c, d`. Реализуйте методы:
#
#    * `determinant()` — вычисление определителя;
#    * `__mul__(other)` — умножение двух матриц 2×2.

# class Matrix2x2:
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
#     def determinant(self):
#         return self.a * self.b * self.c * self.d
#
#     def __mul__(self, other):
#         a = self.a * other.a + self.b * other.c
#         b = self.a * other.b + self.b * other.d
#         c = self.c * other.a + self.d * other.c
#         d = self.c * other.b + self.d * other.d
#
#         return Matrix2x2(a, b, c, d)
#
# m = Matrix2x2(1, 6, 3, 8)
# m1 = Matrix2x2(2, 7, 4, 9)
# m2 = m * m1
#
# print(m2.a, m2.b, m2.c, m2.d)

# 8. **Класс «Список покупок»** !!!
#    Определите класс `ShoppingList` с атрибутом `items` (список строк). Реализуйте методы:
#
#    * `add(item)` — добавить товар;
#    * `remove(item)` — удалить товар по имени (если есть);
#    * `show()` — вывести все товары в виде нумерованного списка.
#
# class ShoppingList:
#     def __init__(self, items):
#         self.items = []
#
#     def __add__(self, item):
#         self.items.append(item)
#
#     def remove(self, item):
#         if item in self.items:
#             self.items.remove(item)
#         else:
#             print("The product can not be found on the list!")
#
#     def show(self):
#         if not self.items:
#             print("Error!")
#         else:
#             for i, item in enumerate(self.items, start=1):
#                 print(f"{i}. {item}")
#
# sl = ShoppingList()
# sl.add("Bread")
# sl.add("Milk")
# sl.add("Eggs")
# sl.show()
#
# sl.remove("Milk")
# sl.show()
#
# sl.remove("Cheese")


# 9. **Класс «Комплексное число»** !!!
#    Напишите класс `ComplexNumber` с атрибутами `real` и `imag`. Реализуйте методы:
#
#    * `__add__(other)` и `__mul__(other)` для сложения и умножения комплексных чисел;
#    * `__repr__()` для отображения в формате `"a + bi"` или `"a - bi"`.
#
# class ComplexNumber:
#     def __init__(self, real, imag):
#         self.real = real
#         self.image = imag
#
#     def __add__(self, other):
#         return ComplexNumber(self.real + other.real, self.imag + other.imag)
#
#     def __mul__(self, other):
#         real_part = self.real * other.real - self.imag * other.imag
#         imag_part = self.real * other.imag + self.imag * other.real
#         return ComplexNumber(real_part, imag_part)



# 10. **Класс «Счётчик»**
#     Создайте класс `Counter` с атрибутом `value`, инициализируемым в конструкторе. Добавьте методы:
#
#     * `increment()` — увеличить на 1;
#     * `decrement()` — уменьшить на 1;
#     * `reset()` — обнулить;
#     * `__repr__()` — вернуть текущее значение в виде строки.

# class Counter:
#     def __init__(self, value):
#         self.value = value
#
#     def increment(self):
#         self.value += 1
#
#     def decrement(self):
#         self.value -= 1
#
#     def reset(self):
#         self.value = 0
#
#     def __repr__(self):
#         return f"{self.value}"
#
# c = Counter()
# print(c)
# c.increment()
# c.increment()
# print(c)
# c.decrement()
# print(c)
# c.reset()
# print(c)