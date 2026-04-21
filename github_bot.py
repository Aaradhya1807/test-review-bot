import os
from github import Github, Auth
from dotenv import load_dotenv
from reviewer import review_code


load_dotenv()

def get_pr_diff(repo_name: str, pr_number: int) -> str:
    g = Github(auth=Auth.Token(os.getenv("GITHUB_TOKEN")))
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)

    diff_text = ""
    for file in pr.get_files():
        diff_text += f"\n\n### File: {file.filename}\n"
        diff_text += file.patch or "(binary or no changes)"

    return diff_text


def post_review(repo_name: str, pr_number: int, review: str):
    g = Github(auth=Auth.Token(os.getenv("GITHUB_TOKEN")))
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    pr.create_issue_comment(f"## 🤖 AI Code Review\n\n{review}")
    print("✅ Review posted to PR!")


if __name__ == "__main__":
    import sys
    REPO = os.getenv("GITHUB_REPOSITORY", "Aaradhya1807/test-review-bot")
    PR_NUMBER = int(os.getenv("PR_NUMBER", 1))

    print("📥 Fetching PR diff...")
    diff = get_pr_diff(REPO, PR_NUMBER)

    print("🤖 Reviewing code...")
    review = review_code(diff)

    print("📤 Posting review to GitHub...")
    post_review(REPO, PR_NUMBER, review)