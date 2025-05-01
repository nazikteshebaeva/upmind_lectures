# ✅ Задача 8: Поиск друзей в Facebook
# Функция find_friends() запрашивает имя, ищет частичное совпадение по users.json (список словарей с ключами: name, city).
# Если нет совпадений — вывести "Ничего не найдено".

# def find_friends():
#     try:
#         with open("users.json", "r", encoding="utf-8") as file:
#             users = eval(file.read())
#             file.close()
#     except:
#         print("Error!")
#         return
#
#     name = input("Enter a name to search: ").strip().lower()
#     if not name:
#         print("Error! Name section can not be empty! Try again: ")
#         return
#
#     found = False
#     for user in users:
#         if name in user["name"].lower():
#             print(f"{user['name']}, {user['city']}")
#             found = True
#
#     if not found:
#         print("None information!")
#
# if __name__ == "__main__":
#     find_friends()