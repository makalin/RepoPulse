from flask import Flask, render_template, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# GitHub API Token (replace with your own)
GITHUB_TOKEN = "your_github_token_here"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

# List of repositories to monitor
REPOS = [
    {"owner": "owner1", "repo": "repo1"},
    {"owner": "owner2", "repo": "repo2"},
]

def fetch_repo_health(owner, repo):
    """Fetch repository health metrics from GitHub API."""
    base_url = f"https://api.github.com/repos/{owner}/{repo}"
    issues_url = f"{base_url}/issues?state=open"
    prs_url = f"{base_url}/pulls?state=open"
    commits_url = f"{base_url}/commits"

    # Fetch open issues
    issues = requests.get(issues_url, headers=HEADERS).json()
    open_issues = len([issue for issue in issues if "pull_request" not in issue])

    # Fetch open pull requests
    pull_requests = requests.get(prs_url, headers=HEADERS).json()
    open_prs = len(pull_requests)

    # Fetch latest commit activity
    commits = requests.get(commits_url, headers=HEADERS).json()
    last_commit = commits[0]["commit"]["author"]["date"] if commits else None
    last_commit_date = datetime.strptime(last_commit, "%Y-%m-%dT%H:%M:%SZ") if last_commit else None

    return {
        "open_issues": open_issues,
        "open_prs": open_prs,
        "last_commit": last_commit_date.strftime("%Y-%m-%d %H:%M:%S") if last_commit_date else "No commits",
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/repo-health")
def repo_health():
    health_data = {}
    for repo in REPOS:
        owner, repo_name = repo["owner"], repo["repo"]
        health_data[f"{owner}/{repo_name}"] = fetch_repo_health(owner, repo_name)
    return jsonify(health_data)

if __name__ == "__main__":
    app.run(debug=True)