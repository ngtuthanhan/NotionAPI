import requests

url = "https://api.notion.com/v1/databases/c4da7ce119494383b324a4236f9e0544/query"
integration  = "secret_QC1jcz1Cd5eAcvYOX3kqqb1kXANG5wFjo0E2shJLAVJ"

payload = {
    "filter": "string",
    "start_cursor": "string",
    "page_size": 100
}
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + integration,
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers)
# response = requests.post(url, json=payload, headers=headers)
# response = requests.request('POST', url, json=payload, headers=headers)

print(response.status_code)
print(response.text)