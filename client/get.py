import requests

# Define the API endpoint
endpoint = 'http://127.0.0.1:8000/api/'

# GET
# No data (normally) should be sent while using GET method
get_response = requests.get(endpoint)

# Print raw text of what is returned by the server, the returned value could be an HTML or JSON
# If it returns JSON, means that we are sending request to REST API
print(get_response.text)
print('STATUS:', get_response.status_code)