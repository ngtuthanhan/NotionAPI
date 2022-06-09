import requests

url = "https://api.notion.com/v1/pages/f6e4acf7bff1403e9a091f9084242fe6/properties/ZM%5CV"

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer secret_QC1jcz1Cd5eAcvYOX3kqqb1kXANG5wFjo0E2shJLAVJ",
    "Notion-Version":  "2022-02-22",
}

response = requests.get(url, headers=headers)

print(response.text)