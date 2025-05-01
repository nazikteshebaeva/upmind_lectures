# ✅ Задача 4: Управление подписчиками в Instagram
# Реализуй функцию manage_followers(). Позволь пользователю добавлять/удалять/просматривать подписчиков.
# Все действия через цикл while, ввод с консоли, команды: add, remove, show, stop
# Сохрани данные в followers.json.
#
# def manage_followers():
#     followers = []
#
#     while True:
#         command = input("Enter command (add, remove, show, stop): ").strip().lower()
#
#         if command == "add":
#             name = input("Enter a name to add: ").strip()
#             if name:
#                 if name not in followers:
#                     followers.append(name)
#                     print(f"{name} has been added to followers.")
#                 else:
#                     print(f"{name} is already your follower.")
#             else:
#                 print("Error! Name section can not be empty! Try again: ")
#
#         elif command == "remove":
#             name = input("Enter a name to remove: ").strip()
#             if name in followers:
#                 followers.remove(name)
#                 print(f"{name} has been removed from followers.")
#             else:
#                 print(f"{name} can not be found on the list.")
#
#         elif command == "show":
#             if followers:
#                 print("Followers: ")
#                 for follower in followers:
#                     print("-", follower)
#             else:
#                 print("A list of followers is empty.")
#
#         elif command == "stop":
#             break
#
#         else:
#             print("Error! Unknown command! Enter add, remove, show or stop.")
#
#     try:
#         with open("followers.json", "w", encoding="utf-8") as file:
#             file.write(str(followers))
#     except:
#         print("Error!")
#
# if __name__ == "__main__":
#     manage_followers()