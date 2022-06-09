import requests, json

url = "https://api.notion.com/v1/databases"
integration = "secret_QC1jcz1Cd5eAcvYOX3kqqb1kXANG5wFjo0E2shJLAVJ"

payload = {
    "parent": "string",
    "properties": "string"
}

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + integration,
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json"
}
data = {
    "parent": {
        "type": "page_id",
        "page_id": "4f23954f2fa644f582d2680c43f6993e"
    },
    "icon": {
    	"type": "emoji",
			"emoji": "🎉"
  	},
  	"cover": {
  		"type": "external",
    	"external": {
    		"url": "https://website.domain/images/image.png"
    	}
  	},
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": None
            }
        }
    ],
    "properties": {
        "Name": {
            "title": {}
        },
        "Description": {
            "rich_text": {}
        },
        "In stock": {
            "checkbox": {}
        },
        "Food group": {
            "select": {
                "options": [
                    {
                        "name": "🥦Vegetable",
                        "color": "green"
                    },
                    {
                        "name": "🍎Fruit",
                        "color": "red"
                    },
                    {
                        "name": "💪Protein",
                        "color": "yellow"
                    }
                ]
            }
        },
        "Price": {
            "number": {
                "format": "dollar"
            }
        },
        "Last ordered": {
            "date": {}
        },
        "Meals": {
          "relation": {
            "database_id": "c4fd58a5-157a-47e7-9e1e-534fb12bca2b"
          }
    	},
        "Number of meals": {
          "rollup": {
            "rollup_property_name": "Name",
            "relation_property_name": "Meals",
            "function": "count"
          }
        },
        "Store availability": {
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "name": "Duc Loi Market",
                        "color": "blue"
                    },
                    {
                        "name": "Rainbow Grocery",
                        "color": "gray"
                    },
                    {
                        "name": "Nijiya Market",
                        "color": "purple"
                    },
                    {
                        "name": "Gus'\''s Community Market",
                        "color": "yellow"
                    }
                ]
            }
        },
        "+1": {
            "people": {}
        },
        "Photo": {
            "files": {}
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
response = requests.post(url, headers=headers, data = data)

print(response.text)