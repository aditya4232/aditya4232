"""Refresh the 'Recently updated' list in README.md from the GitHub API."""
import datetime as dt
import json
import os
import re
import urllib.request

USER = os.environ.get("GH_USER", "aditya4232")
SKIP = {USER.lower(), ".github"}
LIMIT = 6
README = os.path.join(os.path.dirname(__file__), "..", "README.md")


def fetch():
    req = urllib.request.Request(
        f"https://api.github.com/users/{USER}/repos?sort=pushed&per_page=40&type=owner",
        headers={"Accept": "application/vnd.github+json", "User-Agent": f"{USER}-readme"},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def short(text, n=72):
    text = re.split(r"\s{2,}|\n|##", (text or "").strip())[0].strip()
    text = text[:1].upper() + text[1:]
    if len(text) <= n:
        return text
    return text[:n].rsplit(" ", 1)[0].rstrip(",.;:-") + "..."


def main():
    repos = [r for r in fetch() if not r["fork"] and not r["archived"] and r["name"].lower() not in SKIP]
    lines = []
    for r in repos[:LIMIT]:
        when = dt.datetime.strptime(r["pushed_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%b %d, %Y").replace(" 0", " ")
        desc = short(r.get("description"))
        lines.append(f'[{r["name"]}]({r["html_url"]}) <sub>{when}</sub>' + (f"<br><sub>{desc}</sub>" if desc else ""))
    block = "\n\n".join(lines)
    with open(README, encoding="utf-8") as f:
        src = f.read()
    new = re.sub(r"(<!-- recent:start -->).*?(<!-- recent:end -->)", lambda m: f"{m[1]}\n{block}\n{m[2]}", src, flags=re.S)
    if new != src:
        with open(README, "w", encoding="utf-8", newline="\n") as f:
            f.write(new)
        print("README updated")
    else:
        print("no change")


if __name__ == "__main__":
    main()
