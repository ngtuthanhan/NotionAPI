import requests, json

url = "https://api.notion.com/v1/databases/9e9e8210b3c34a96815c12af4d592567/"
integration = "secret_QC1jcz1Cd5eAcvYOX3kqqb1kXANG5wFjo0E2shJLAVJ"

data = {
    "title": [
        {
            "text": {
                "content": "Today'\''s grocery list"
            }
        }
    ],
    "properties": {
        "Photo": {
            "url": {},
            "name": "renamePhoto"
        },
        "Store availability": {
            "multi_select": {
                "options": [
                    {
                        "name": "Duc Loi Market"
                    },
                    {
                        "name": "Rainbow Grocery"
                    },
                    {
                        "name": "Gus'\''s Community Market"
                    },
                    {
                        "name": "The Good Life Grocery",
                        "color": "orange"
                    }
                ]
            }
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

