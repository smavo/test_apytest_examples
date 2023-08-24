
import requests
import json
import jsonpath

# API URL
url = 'https://reqres.in/api/user/13'

response = requests.delete(url)

# Send Get Request
print(response.status_code)

assert response.status_code == 204

