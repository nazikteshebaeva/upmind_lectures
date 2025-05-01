# ✅ Задача 6: Отправка сообщений в Facebook Messenger
# Функция send_message() запрашивает получателя и текст. Имя не пустое, сообщение не пустое.
# Добавь к каждому сообщению timestamp (datetime.now). Сохрани в messages.json

# def send_message():
#     receiver = ""
#     while not receiver.strip():
#         receiver = input("Enter a name of receiver: ")
#         if not receiver.strip():
#             print("Error! Name can not be empty! Try again: ")
#
#     text = ""
#     while not text.strip():
#         text = input("Enter your message: ")
#         if not text.strip():
#             print("Error! Message can not be empty! Try again: ")
#
#     timestamp = input("Enter date and time (For example: 2025-05-01 12:56): ")
#
#     message = (
#         '{'
#         f'"receiver": "{receiver}", '
#         f'"text": "{text}", '
#         f'"timestamp": "{timestamp}"'
#         '}\n'
#     )
#
#     try:
#         with open("messages.json", "a", encoding="utf-8") as file:
#             file.write(message)
#             file.write(",\n")
#     except:
#         print("Error!")
#
# if __name__ == "__main__":
#     send_message()