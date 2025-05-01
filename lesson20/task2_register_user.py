# ✅ Задача 2: Регистрация пользователя в WhatsApp
# Напиши функцию register_user(), которая запрашивает имя, возраст и номер телефона.
# Проверь, что возраст — целое число > 13, а номер телефона состоит только из цифр и длиной 10.
# Сохрани пользователей в список словарей и запиши в файл whatsapp_users.json.

# def register_user():
#     users = []
#
#     name = input("Enter your name: ").strip()
#
#     age = ""
#     while True:
#         age = input("Enter your age: ").strip()
#         if age.isdigit() and int(age) > 13:
#             age = int(age)
#             break
#         else:
#             print("Error! Age must be more than 13! Try again: ")
#
#     phone = ""
#     while True:
#         phone = input("Enter your phone number (10 digits): ").strip()
#         if phone.isdigit() and len(phone) == 10:
#             break
#         else:
#             print("Error! Number must have 10 digits only! Try again: ")
#
#     user = {
#         "name": name,
#         "age": age,
#         "phone": phone
#     }
#
#     users.append(user)
#
#     try:
#         with open("whatsapp_users.json", "a", encoding="utf-8") as file:
#             file.write(str(users) + "\n")
#     except:
#         print("Error!")
#
# if __name__ == "__main__":
#     register_user()