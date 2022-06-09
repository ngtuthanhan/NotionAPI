import requests

url = "https://api.notion.com/v1/databases?page_size=100"
integration = "secret_QC1jcz1Cd5eAcvYOX3kqqb1kXANG5wFjo0E2shJLAVJ"

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + integration,
    "Notion-Version": "2021-08-16"
}

response = requests.get(url, headers=headers)

print(response.text)