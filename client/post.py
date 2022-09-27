import requests

# Define the API endpoint
endpoint = 'http://127.0.0.1:8000/api/post/'

# POST
# NIM and Nama could be redefined using input()
data = {
	'nim': 18220009,
	'nama': 'Fatih Darielma Gaizta'
}

get_response = requests.post(endpoint, json=data)

# Print raw text of what is returned by the server, the returned value could be an HTML or JSON
# If it returns JSON, means that we are sending request to REST API
print(get_response.text)
print('STATUS:', get_response.status_code)