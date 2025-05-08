# Theme: Key value, dictionaries

#1 Creation of dictionaries:

#empty dictionary: my_dict = {}; my_dict = dict()
#full dictionary:
# student = {
#     "name": "Alex",
#     2: 33,
#     True: [1, 2, 3],
#     "status": True,
#     "age": 21,
#     "city": "Moscow"
# }

# "name" = key; "Alex" = value

#2 Getting the value by the key:
# print(student["name"]) #Alex
# print(student.get(333, "default value")) #333 - a key (it can be there in dict or not), "default value" - in case if
# there are not a key that exists. exp: ("city", "Moscow")
# print(student.get("status"))

#Methods of dictionaries

#   -.get(key, default) - safely retrieve a value
# print(student.get("status"))
#   -.keys() - returns all keys
# print(student.keys())
#   -.values() - returns all values
# print(student.values())
#   -.items() - returns keys and values together
# print(student.items())
#   -.update() - updates the dictionary. I CAN CHANGE THE MEANING INSIDE FOR EXAMPLE: "NAME": "ALEX" -> "NAME": "VLAD"
# print(student.update({"name": "vlad", "city": "Bishkek"}))
#   -.pop(key[, default]) - deletes the key and returns the value DELETE THE EXACT MEANING FROM DICT
# print(student.pop("name")) #there are going to be no meaning of name in consul
#   -.clear() - deletes the dictionary

#Adding and changing elements

# student["age"] = 22 #changes
# student["grade"] = "A" #adds
# print(student)

#Deleting elements:

# student.pop("city")
# del student["name"] #deletes the key "name" BUT WE HAVE TO BE SURE THAT THERE IS A KEY WITH A NAME "NAME". OTHERWISE
# IT WILL GIVE AN ERROR IN CONSOL.

#Checking the key

# if "name" in student:
#     print("The key 'name' is in the dictionary!")