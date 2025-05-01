# ✅ Задача: Фильтрация постов с несколькими условиями поиска

# 📋 Описание задачи:
# Напиши функцию filter_posts(), которая будет считывать посты из файла posts.json
# и позволять пользователю фильтровать их по разным критериям:
# - названию поста
# - описанию поста
# - тегам
# - дате публикации
# - музыке, использованной в посте

# 📥 Как работает фильтрация:
# - Пользователь может оставить любое поле пустым (тогда фильтр по этому полю не применяется).
# - Поиск по строкам (название, описание, музыка) происходит по частичному совпадению.
# - Сравнение тегов происходит без учёта регистра.
# - Даты должны быть в формате "ГГГГ-ММ-ДД".

# ⚙️ Условия работы:
# - Если пользователь оставляет все поля пустыми — выводится предупреждение.
# - Если пользователь вводит неправильный формат даты — нужно обработать исключение ValueError.
# - Если нет найденных постов по заданным условиям — вывести сообщение "Посты не найдены по заданным условиям."
# - Вывести все подходящие посты в удобочитаемом формате.

# 📂 Формат файла posts.json:
# [
#     {
#         "name": "Путешествие на Бали",
#         "description": "Незабываемая поездка с друзьями на остров Бали!",
#         "tags": ["#путешествия", "#весело", "#лето"],
#         "date_published": "2025-04-20",
#         "music": "Bali Beats"
#     },
#     ...
# ]

# 🔥 Особенности:
# - Работает с частичным совпадением строк.
# - Обрабатывает ввод даты.
# - Реализует гибкий фильтр по нескольким полям одновременно.
# - Обрабатывает все возможные ошибки.

# 🧹 Нужно обязательно обрабатывать:
# - Ошибки при конвертации даты (ValueError).
# - Ситуацию, если пользователь оставил все поля пустыми.
# - Ситуацию, если по заданным условиям ничего не найдено.

# 📈 Результат:
# Вывод всех постов, которые соответствуют заданным пользователем условиям.

# def filter_posts():
#     try:
#         with open("posts.json", "r", encoding="utf-8") as file:
#             content = file.read()
#             if not content.strip():
#                 print("File is empty!")
#                 return
#             posts = eval(content)
#     except:
#         print("Error! The file can not be opened! Try again: ")
#         return
#
#     name_filter = input("Name: ").strip().lower()
#     description_filter = input("Description: ").strip().lower()
#     tag_filter = input("Tag (through comma): ").strip().lower()
#     date_filter = input("Date of publication (YYYY-MM-DD): ").strip()
#     music_filter = input("Music: ").strip().lower()
#
#     if not (name_filter or description_filter or tag_filter or date_filter or music_filter):
#         print("Error! You did not enter any filters. Try again: ")
#         return
#
#     results = []
#     for post in posts:
#         if name_filter and name_filter not in post["name"].lower():
#             continue
#         if description_filter and description_filter not in post["description"].lower():
#             continue
#         if tag_filter:
#             tag_list = tag_filter.lower().split(",")
#             tag_list = [tag.strip() for tag in tag_list]
#             post_tags = [tag.lower() for tag in post["tags"]]
#             match_found = False
#             for tag in tag_list:
#                 if tag in post_tags:
#                     match_found = True
#                     break
#             if not match_found:
#                 continue
#         if date_filter and date_filter != post["date_published"]:
#             continue
#         if music_filter and music_filter not in post["music"].lower():
#             continue
#         results.append(post)
#
#     if results:
#         for p in results:
#             print(f"\n{p['name']}")
#             print(f"Description: {p['description']}")
#             print(f"Tags: {', '.join(p['tags'])}")
#             print(f"Date: {p['date_published']}")
#             print(f"Music: {p['music']}")
#     else:
#         print("Error! Posts can not be found!")
#
#
# if __name__ == "__main__":
#     filter_posts()