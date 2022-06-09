import requests

url = "https://notion.com/v1/databases"

headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers)

print(response.text)