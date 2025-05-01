# ✅ Задача 1: Добавление постов в Instagram
# Создай функцию add_post(), которая через цикл позволяет пользователю добавить несколько постов.
# Каждый пост должен содержать заголовок, описание и список хэштегов (через пробел), дата публикации, музыка.
# Проверь: описание не должно быть пустым, каждый хэштег должен начинаться с '#'.
# Все посты сохраняются в файл posts.json. При ошибках записи в файл или неверном формате — обработай исключения.
import json
#
# def add_posts():
#     posts = []
#
#     while True:
#         title = input("Enter a title of the post: ")
#         if title == "":
#             print("Title can not be empty! Please, try again!")
#             break
#         else:
#             while True:
#                 description = input("Enter a description of the post: ").strip()
#                 if description == "":
#                     print("Description can not be empty! Please, enter again!")
#                     break
#                 else:
#                     while True:
#                         hashtags_input = input("Enter hashtags '#' using a space: ")
#                         hashtags = hashtags_input.split()
#                         correct = True
#                         for tag in hashtags:
#                             if not tag.startswith("#"):
#                                 correct = False
#                                 print(f"Error: hashtag '{tag}' is not starts with '#'. Try again!")
#                                 break
#                         if correct:
#                             break
#
#         date = input("Enter the date of publication (YYYY-MM-DD): ")
#         music = input("Enter a name of music: ")
#
#         post = {
#             "Title": title,
#             "Description": description,
#             "Hashtags": hashtags,
#             "Date of publication": date,
#             "Music": music
#         }
#
#         posts.append(post)
#         more = input("Would you like to add more posts? (Yes or No): ").strip().lower()
#         if more != "yes":
#             break
#     return posts
#
# def save_posts_to_file(posts, filename="posts.json"):
#     try:
#         with open(filename, "w", encoding="utf-8") as file:
#             print(f"Posts has been successfully saved in {filename}!")
#     except FileNotFoundError:
#         print(f"Error!")
#
# if __name__ == "__main__":
#     add_posts()
#




# образец файла posts.json
#     {
#         "name": "Утренняя зарядка",
#         "description": "Лучшие упражнения для бодрого утра!",
#         "tags": [
#             "#фитнес",
#             "#здоровье",
#             "#утро"
#         ],
#         "date_published": "2025-04-10",
#         "music": "Workout Power",
#         "likes": 16,
#         "comments": [
#             "Hi",
#             "Hi there",
#             "How many are you"
#         ]
#     },

