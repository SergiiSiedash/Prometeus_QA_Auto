import requests


class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = r.json()

        return body

    # Метод для збереження всіх доступних emoji GitHub у JSON файл
    def get_emoji(self):
        r = requests.get("https://api.github.com/emojis")
        body = r.json()

        return body

    # Метод для отримання списку коммітів
    def get_commit_list(self):
        r = requests.get("https://api.github.com/repos/SergiiSiedash/Prometeus_QA_Auto/commits")
        body = r.json()

        return body

