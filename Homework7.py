#1
# book = {
#     "name": "Malibu Rising",
#     "author": "Taylor Jenkins Reid",
#     "year": 2021
# }
# print(book["author"])
# print(book.get("author"))

#2
# dictionary = dict()
# dictionary["name"] = "Nazik"
# dictionary["age"] = 25
# dictionary["city"] = "Ottawa"
# print(dictionary)

#3
# dictionary = {
#     "name": "Nazik",
#     "age": 25,
#     "city": "Ottawa"
# }
# dictionary.pop("city")
# print(dictionary)

#4
# if "phone" in book:
#     print("No, there is no phone")

#5
# dictionary["age"] = 30
# print(dictionary)

#6
# friends = {
#     "Nawal": "black",
#     "Emmanuel": "yellow",
#     "Vesna": "blue"
# }
# print(friends["Emmanuel"])

#7
# students = {
#     "Nawal": 100,
#     "Emmanuel": 98,
#     "Vesna": 88
# }
# print(students.items())

#8
# dictionary = dict()
# dictionary.get(0, "default")
# print(dictionary)

#9
# grocery = {
#     "bread": 14,
#     "milk": 9,
#     "eggs": 11
# }
# grocery["juice"] = 18
# print(grocery)

#10
# dictionary = {
#     "book": "Carrie Soto is back",
#     "date": 2024,
#     "author": "TJR"
# }
# dictionary.len()

#11
cars = {
    "GGG693": "Darling",
    "GLH781": "Adam",
    "055CDR": "Cooper"
}
print(cars["GLH781"])
print(cars.get("GLH781"))

#12
# cars["SZN944"] = "Brian"
# print(cars)

#13
# cars.pop("GGG693")
# print(cars)

#14
# print(cars.items())

#15
# print(cars.values())

#16
countries = {
    "Canada": "Ottawa",
    "USA": "Washington",
    "Kyrgyzstan": "Bishkek"
}
print(countries.get("USA"))

#17
# countries["Kyrgyzstan"] = "Frunze"
# print(countries)

#18
# if "Canada" in countries:
#     print("There is a Canada")
# else:
#     print("Error")

#19
# cars.update(countries)
# print(cars)

#20
# login = {
#     "nazikteshebaeva": 12345,
#     "upmindcamp": 678910,
#     "carleton": "bright"
# }
# if login["nazikteshebaeva"] == 12345:
#     print("Login is successful")
# else:
#     print("Login has been failed")

#21
# days_of_the_week = {
#     "Monday": 1,
#     "Tuesday": 2,
#     "Wednesday": 3,
#     "Thursday": 4,
#     "Friday": 5,
#     "Saturday": 6,
#     "Sunday": 7
# }
# print(days_of_the_week.get("Wednesday"))
#
# #22
# if "Sunday" in days_of_the_week:
#     print("There is a Sunday in the days of the week")
# else:
#     print("Error")

#23
# money = {
#     "1USD": 856093,
#     "1EUR": 933783,
#     "1CNY": 118285
# }
# print(money.get("1USD"))

#24
# money["1RUB"] = 10428
# print(money)

#25
# films = {
#     "Nawal": "How I met your mother",
#     "Oliver": "Friends",
#     "Emilie": "The Office"
# }
# print(films.get("Nawal"))

#26
# films["Oliver"] = "The Big Bang Theory"
# print(films)

#27
# goods = {
#     "pen": 20,
#     "paper": 33,
#     "book": 45,
#     "map": 3
# }
# goods["paper"] = 30
# print(goods)

#28
# goods.clear()

#29
# prof = {
#     "Nawal": "Sales Associate",
#     "Oliver": "Makeup Artist",
#     "Emilie": "A key holder"
# }
# print(prof.get("Emilie"))

#30
# prof.pop("Nawal")
# print(prof)

#31
# classes = {
#     "Chemistry": 100,
#     "Physics": 98,
#     "History": 66
# }
# print(classes.values())
# print(sum(classes.values()))

#32
# animals = {
#     "cat": "mrmr",
#     "dog": "gav",
#     "caw": "moo"
# }
# print(animals.get("dog"))

#33
# animals["cat"] = "miyaw"
# print(animals)

#34

#35
# students = {
#     "Nawal": 28,
#     "Oliver": 30,
#     "Emilie": 22
# }
# print(students.get("Emilie"))

#36
# if "Nawal" in students:
#     print("Nawal is here")
# else:
#     print("Error")

#37
# towns = {
#     "Ottawa": "1072 million",
#     "Montreal": "1792 million",
#     "Calgary": "1414 million"
# }
# towns["Ottawa"] = "2000 million"
# print(towns)

#38
# towns.pop("Calgary")
# print(towns)

#39
# games = {
#     "Elden Ring": 96,
#     "The Last of Us": 97,
#     "Got of War: Ragnarok": 94
# }
# if games["Elden Rings"] >= games["The Last of Us"] >= games["Got of War: Ragnarok"]:
#     print("Elden Rings has the highest rating")
# elif games["Elden Rings"] <= games["Last of Us"] >= games["Got of War: Ragnarok"]:
#     print("The Last of Us has the highest rating")
# else:
#     print("Error")

#40
# contacts = {
#     "Nawal": 6137626988,
#     "Oliver": 6137626455,
#     "Emilie": 3145676788
# }
# print(contacts.get("Oliver"))