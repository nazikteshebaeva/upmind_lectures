# ✅ Задача 3: Модерация сообщений в Telegram
# Реализуй функцию moderate_messages(). Считай сообщения из файла messages.json (список словарей).
# Удали сообщения, содержащие запрещённые слова (например, 'плохой', 'spam').
# Перезапиши файл без нарушений.
from xml.etree.ElementTree import indent
# import json
#
# def moderate_messages():
#     bad_words = input("Enter bad words (separated by space): ").split()
#     tmp = None
#     with open("message.json", "r", encoding="utf-8") as file:
#         tmp = json.load(file)
#
#     for item in tmp:
#         if item.get("message"):
#             words = item.get("message").lower().split()
#             for word in words:
#                 if word in bad_words:
#                     item["message"] = item["message"].replace(word, "***")
#
#     with open("messages.json", 'w', encoding="utf-8") as file:
#         json.dump(tmp, file, indent=4)
#
#     print("Bad words has been removed. File has been saved.")
#
# if __name__ == "__main__":
#     moderate_messages()
