import pytest


# Compulsory part tests
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
    assert r["total_count"] == 58


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("sergii_butenko_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


# Additional part of the Task 4 begins


# Test that Github emojies quantity is 1935
@pytest.mark.api_emojis_qnt
def test_emoji_qnt(github_api):
    r = github_api.get_all_emojis()
    assert len(r) == 1935


# Test that particular commit exist in repo
@pytest.mark.api_commit
def test_commit_exist(github_api):
    global owner
    global repo
    owner = "SergiiSiedash"
    repo = "Prometeus_QA_Auto"
    r = github_api.get_commit_list(owner, repo)

    target_sha = "4f8ffd8d01a675a0eb15fcb25b7cbe9f62405dab"

    # Loop to find particular commit index by sha
    for i in r:
        if i["sha"] == target_sha:
            global commit_sha
            commit_sha = i
    assert commit_sha["sha"] == target_sha


# Commit name check
@pytest.mark.api_commit
def check_commit_name():
    assert commit_sha["commit"]["message"] == "Project Task 5 Compulsory Part Completed"


# Test that recent commit author's name, email and date equal to commiter ones
@pytest.mark.api_commit
def test_recent_commit_author_equal_commiter(github_api):
    r = github_api.get_commit_list(owner, repo)
    recent_commit = r[0]
    assert (
        recent_commit["commit"]["author"]["name"]
        == recent_commit["commit"]["committer"]["name"]
    )
    assert (
        recent_commit["commit"]["author"]["email"]
        == recent_commit["commit"]["committer"]["email"]
    )
    assert (
        recent_commit["commit"]["author"]["date"]
        == recent_commit["commit"]["committer"]["date"]
    )
