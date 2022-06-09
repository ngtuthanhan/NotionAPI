import requests

url = "https://api.notion.com/v1/databases/c4da7ce119494383b324a4236f9e0544"
integration = "secret_QC1jcz1Cd5eAcvYOX3kqqb1kXANG5wFjo0E2shJLAVJ"


headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + integration,
    "Notion-Version": "2022-02-22"
}

response = requests.get(url, headers=headers)

print(response.text)