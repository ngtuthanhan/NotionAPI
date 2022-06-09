import requests, json

url = "https://api.notion.com/v1/databases/c4fd58a5157a47e79e1e534fb12bca2b/"
integration = "secret_QC1jcz1Cd5eAcvYOX3kqqb1kXANG5wFjo0E2shJLAVJ"

data = {
    "properties": {
        "Name": {
            "title": {}
        }
    }       
}

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + integration,
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json"
}
data = json.dumps(data)
response = requests.patch(url, headers=headers,data= data)

print(response.text)

