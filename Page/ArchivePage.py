# Notworking
import requests, json

url = "https://api.notion.com/v1/pages/f6e4acf7bff1403e9a091f9084242fe6"

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer secret_QC1jcz1Cd5eAcvYOX3kqqb1kXANG5wFjo0E2shJLAVJ",
    "Notion-Version":  "2022-02-22",
}

data = {
    "archived": True
}
data = json.dumps(data)
response = requests.patch(url, headers=headers, data = data)

print(response.text)
print(response.status_code)