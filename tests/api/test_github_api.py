import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    print(r["total_count"])
    assert r["total_count"] == 57


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergii_butenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


# Тест, що кількість emoji з GitHub = 1935
@pytest.mark.api
def test_emoji_qnt(github_api):
    r = github_api.get_emoji()
    assert len(r) == 1935


# Тест, що комміт існує в репозиторії користувача, якщо відомий sha комміту
@pytest.mark.api_commit
def test_commit_exist(github_api):
    r = github_api.get_commit_list()
    # Присвоюємо змінній SHA комміту, який ми шукаємо
    target_sha = "4f8ffd8d01a675a0eb15fcb25b7cbe9f62405dab"

    # Циклом шукаємо комміт заданним sha
    for i in r:
        if i["sha"] == target_sha:
            global commit_sha
            commit_sha = i
    assert commit_sha["sha"] == target_sha


# Перевіряємо ім'я комміту
@pytest.mark.api_commit
def test_commit_name():
    assert commit_sha["commit"]["message"] == "Project Task 5 Compulsory Part Completed"


# Перевіряємо, автор і коммітер останнього комміту - одина людина
@pytest.mark.api_commit
def test_last_commit_author_equal_commiter(github_api):
    r = github_api.get_commit_list()
    last_commit = r[0]
    assert (
        last_commit["commit"]["author"]["name"]
        == last_commit["commit"]["committer"]["name"]
    )
    assert (
        last_commit["commit"]["author"]["email"]
        == last_commit["commit"]["committer"]["email"]
    )
    assert (
        last_commit["commit"]["author"]["date"]
        == last_commit["commit"]["committer"]["date"]
    )
