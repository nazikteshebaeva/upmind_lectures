# Задача 10: Сбор статистики по постам в Instagram
# Функция analyze_posts(). Считывает posts.json, где у каждого поста есть "likes", "comments".
# Вычисли среднее количество лайков и комментариев. Выведи в формате:
# Среднее лайков: X, комментариев: Y
# import json
#
# def analyze_posts():
#     with open("posts.json", "r", encoding="utf-8") as file:
#         posts = json.load(file)
#
#     total_likes = sum(post["likes"] for post in posts)
#     total_comments = sum(post["comments"] for post in posts)
#     count = len(posts)
#
#     print("Average of likes:", round(total_likes / count, 1))
#     print("Average of comments:", round(total_comments / count, 1))
#
# if __name__ == "__main__":
#     analyze_posts()