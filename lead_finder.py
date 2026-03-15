import requests
import csv

KEYWORDS = [
    "airdrop checker",
    "wallet analyzer",
    "web3 dashboard",
    "sybil detection",
    "crypto portfolio tracker",
    "on-chain analytics"
]

results = []

for keyword in KEYWORDS:
    url = f"https://api.github.com/search/repositories?q={keyword}&sort=updated&order=desc&per_page=20"
    
    response = requests.get(url)
    data = response.json()

    if "items" not in data:
        continue

    for repo in data["items"]:
        results.append([
            keyword,
            repo["name"],
            repo["owner"]["login"],
            repo["html_url"],
            repo["description"],
            repo["stargazers_count"]
        ])

with open("leads.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["keyword", "repo_name", "owner", "repo_url", "description", "stars"])
    writer.writerows(results)

print("Leads saved to leads.csv")