# ✅ Задача 9: Телеграм-бот "Echo"
# Функция echo_bot(). Пользователь вводит сообщение, бот повторяет, сохраняет в echo.json со временем.
# Цикл продолжается, пока не введено /exit.

# def echo_bot():
#     log = ""
#     count = 1
#
#     while True:
#         message = input("Enter your message: ")
#         if message == "/exit":
#             print("Bot: Bye!")
#             break
#         print(f"Bot: {message}")
#         log += f"{count}. {message}\n"
#         count += 1
#
#     with open("echo.txt", "w", encoding="utf-8") as file:
#         file.write(log)
#
# if __name__ == "__main__":
#     echo_bot()