import requests
import json

url = "https://api.notion.com/v1/databases/c4da7ce119494383b324a4236f9e0544/query"
integration = "secret_QC1jcz1Cd5eAcvYOX3kqqb1kXANG5wFjo0E2shJLAVJ"

payload = {
    "page_size": 100,
    "sorts": [
        {
            "property": "Name",
            "direction": "ascending"
        }
    ],
    "filter": {
        "property": "Name",
        "rich_text": {
            "contains": "Bruh"
        }
    }
    
}


headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + integration,
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers)
data = response.json()
with open('ReadDatabase.json', 'w', encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False)
