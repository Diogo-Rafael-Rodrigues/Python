import requests
from datetime import datetime

# HTTPS REQUESTS - GET, POST, PUT AND DELETE #

USERNAME = "diogo"
TOKEN = "JAJIAHA4A45SD3"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=graph_params)
# print(response.text)

graphs_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Programing Graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graphs_endpoint, json=graph_params, headers=headers)


dot_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now()

point_params = {
    "date": today.strftime("%Y%m%d"),  # <---- turns datetime module result to a string
    "quantity": input(" How many hours did you study today?"),

}

response = requests.post(url=dot_endpoint, json=point_params, headers=headers)
print(response.text)


# PUT
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

# DELETE
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=update_endpoint, headers=headers)
