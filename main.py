import requests

USERNAME = "tahaleatnspixela"
TOKEN = "tahalearnspixela17041996"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': "yes",
    'notMinor': 'yes'
}

# r = requests.post(url=pixela_endpoint, json=user_params)
# r.raise_for_status()
# print(r.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
