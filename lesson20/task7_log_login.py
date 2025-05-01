# ✅ Задача 7: История входов в аккаунт WhatsApp
# Функция log_login() записывает дату входа, имя пользователя, IP-адрес (запрос через input()).
# Сохраняется в login_history.json.

# def log_login():
#     username = ""
#     while not username.strip():
#         username = input("Enter your username: ")
#         if not username.strip():
#             print("Username can not be empty! Enter your username again: ")
#
#     ip_address = ""
#     while not ip_address.strip():
#         ip_address = input("Enter your IP-address: ")
#         if not ip_address.strip():
#             print("IP-address can not be empty! Enter your IP- address again: ")
#
#     login_time = ""
#     while not login_time.strip():
#         login_time = input("Enter a current date and time (example, 2025-04-29 11:10 AM): ")
#         if not login_time.strip():
#             print("Login time can not be empty! Enter your login time again: ")
#
#     entry = (
#         '{'
#         f'"username": "{username}", '
#         f'"ip": "{ip_address}", '
#         f'"login_time": "{login_time}"'
#         '}\n'
#     )
#
#     try:
#         with open("login_history.json", "a", encoding="utf-8") as file:
#             file.write(entry)
#             file.write(",\n")
#     except:
#         print("Error!")
#
# if __name__ == "__main__":
#     log_login()