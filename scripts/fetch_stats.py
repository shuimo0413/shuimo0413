#!/usr/bin/env python3
"""Fetch public profile stats for shuimo0413 and write data/profile-stats.json."""

import collections
import datetime
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

USER = "shuimo0413"
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "profile-stats.json"


def get_json(url):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "shuimo-profile-stats",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as response:
        return json.load(response)


def fetch_repos():
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner&page={page}"
        chunk = get_json(url)
        repos.extend(chunk)
        if len(chunk) < 100:
            return repos
        page += 1


def month_range(start, end):
    current = datetime.date(int(start[:4]), int(start[5:7]), 1)
    last = datetime.date(int(end[:4]), int(end[5:7]), 1)
    months = []
    while current <= last:
        months.append(current.strftime("%Y-%m"))
        if current.month == 12:
            current = datetime.date(current.year + 1, 1, 1)
        else:
            current = datetime.date(current.year, current.month + 1, 1)
    return months


def main():
    user = get_json(f"https://api.github.com/users/{USER}")
    repos = [repo for repo in fetch_repos() if not repo["fork"]]
    created = user["created_at"]
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    languages = collections.Counter(repo["language"] or "Unlabeled" for repo in repos)
    monthly = collections.Counter()
    active_days = set()
    seen_shas = set()
    per_repo = {}

    for repo in repos:
        if repo["size"] == 0:
            per_repo[repo["name"]] = {"commits": 0, "reported": 0}
            continue
        query = urllib.parse.urlencode({
            "sha": repo["default_branch"],
            "author": USER,
            "per_page": 100,
            "since": created,
            "until": now,
        })
        url = f"https://api.github.com/repos/{USER}/{repo['name']}/commits?{query}"
        commits = get_json(url)
        count = 0
        for commit in commits:
            sha = commit["sha"]
            if sha in seen_shas:
                continue
            seen_shas.add(sha)
            count += 1
            date = commit["commit"]["committer"]["date"]
            monthly[date[:7]] += 1
            active_days.add(date[:10])
        per_repo[repo["name"]] = {"commits": count, "reported": len(commits)}

    first_month = min(monthly) if monthly else now[:7]
    continuous_months = month_range(first_month, now[:7])
    result = {
        "generated_at": now,
        "account_created_at": created,
        "repo_count": len(repos),
        "languages": dict(languages.most_common()),
        "commit_total": sum(monthly.values()),
        "active_days": len(active_days),
        "monthly_commits": {month: monthly.get(month, 0) for month in continuous_months},
        "per_repo": per_repo,
        "scope": "owned public non-fork repos, default branch, authored by user, deduplicated by SHA, committer date in UTC",
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"saved {OUT}")
    print("repos:", result["repo_count"])
    print("languages:", result["languages"])
    print("commits:", result["commit_total"], "active days:", result["active_days"])


if __name__ == "__main__":
    main()
