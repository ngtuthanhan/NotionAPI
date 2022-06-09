import requests

url = "https://api.notion.com/v1/pages/43ddad39f7264b7ba17d142a1453ece4"

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer secret_QC1jcz1Cd5eAcvYOX3kqqb1kXANG5wFjo0E2shJLAVJ",
    "Notion-Version":  "2022-02-22",
}

response = requests.get(url, headers=headers)

print(response.text)