import requests, json

url = "https://api.notion.com/v1/pages"

data = {
    "parent": {"database_id": "c4fd58a5157a47e79e1e534fb12bca2b" },
    "properties": {
        "Name": {
            "title": [
                {
                    "text": {
                        "content": "Review"
                    }
                }
            ]
        },
        "Tags": {
            "multi_select": [
                {
                    "name": "🥦Vegetab",
                    "color": "green"
                }
            ]
        }
    }
}

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer secret_QC1jcz1Cd5eAcvYOX3kqqb1kXANG5wFjo0E2shJLAVJ",
    "Notion-Version":  "2022-02-22",
    "Content-Type": "application/json"
}
data = json.dumps(data)

response = requests.post(url, headers=headers, data = data)
print(response.text)