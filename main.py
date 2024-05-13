import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    'token': "tahalearnspixela17041996",
    'username': "tahalearnspixela",
    'agreeTermsOfService': "yes",
    'notMinor': 'yes'
}

r = requests.post(url=pixela_endpoint, json=user_params)
r.raise_for_status()
print(r.text)