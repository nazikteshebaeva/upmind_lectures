# Theme: Lists
# List - it is editable collection of elements

# Example of list
# fruits = ["apple", "banana", "orange"]
# print(fruits[0]) #apple

#lists works with [] - this

#lists can have different types of data (integer, string, float, lists too)
# mixed_list = [42, "hello", 3.14, [1,2,3]]
# print(mixed_list[3][1]) #if I want an info from list which is in the list
# print(mixed_list[1], mixed_list[0], mixed_list[3][2]) #if I need each of them, or more than one data from the list

#negative indexes
# print(mixed_list[-1]) #info comes from the end of the list (-1, -2, -3, etc)

#editing index
# mixed_list[1] = "first lesson"
# mixed_list[2] = 33.11
# mixed_list[3] = 22
# print(mixed_list)

# print(len(mixed_list)) #len starts from 1, 2, etc

#concatenated list = summarise the peremennye

# concatenated_list = mixed_list + fruits
# print(concatenated_list)

#duplication of the index
# print(fruits * 2)
# ones = [1] * 10
# print(ones)

#construction of "in"
# print("orange" in fruits)
# print("banana" in fruits)
# print("banana" in mixed_list)

#!!! Methods od lists !!!
# append() (adding info in the end), insert() (adding the information before the index that I am going to write)- adding elements
# example:
# fruits.append("pineapple")
# fruits.insert(1, "grape")
# print(fruits)
#remove() (delete the info from anywhere, but be specific about info, if there are no right info it will be an error in consul), pop() (delete the info from the end) - deleting of elements
# fruits.pop()
# pineapple = fruits.pop()
# mixed_list.pop()
# mixed_list.remove(42)
# print(mixed_list)
#index - to find an index in the list, when in the list so mane info, we need index to find exact one, count (counting the amount of repeat of elements)-
# print(mixed_list.index(42))
# print(mixed_list)
# print(mixed_list.index(33.11))
# print(mixed_list.count(33.11))
# mixed_list.append(33.11)
# print(mixed_list.count(33.11))
# print(mixed_list)
#sor(sorting), reverse
# numbers = [2, 6, 1,9, 3, 4, 7]
# print(numbers)
# print(sorted(numbers)) #sorted but then the info will be returned
# print(numbers)
# numbers.sort() #sorted right away
# print(numbers)

#slices of indexes
# numbers.sort()
# print(numbers)
# print(numbers[2:5]) #2 - the start of the index and 5 - is the till index. See in consol

#EXERSISES
#1
# food = ["soup", "rice", "fries", "putin", "pizza"]
# print(food[2])

#2
# num = [10, 20, 30, 40, 50]
# num[2] = 99
# print(num)

#3
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# concatenated_list = list1 + list2
# print(concatenated_list)

#4
# list1 = [4, 2, 9, 1]
# list1.append(7)
# print(list1)
# list1.remove(2)
# print(list1)
# list1.sort()
# print(list1)

#5
# list2 = ["python", "java", "c++", "javascript", "php"]
# print(list2[0:3])
# list2.reverse()
# print(list2)

#6
# names = ["Anna", "Boris", "Vika"]
# names[0] = "Hello, Anna"
# names[1] = "Hello, Boris"
# names[2] = "Hello, Vika"
# print(names)

#7
# list3 = [[1,2], [3,4], [5,6]]
# print(list3[1][1])