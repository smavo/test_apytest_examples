
import requests
import json
import jsonpath

# API URL
url = 'https://reqres.in/api/users?page=2'

# Send Get Request
response = requests.get(url)

# Parse response to Json Format
json_response = json.loads(response.text)

# Fetch value using Json Path
for i in range(0, 6):
    id = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].id')
    email = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].email')
    data_1 = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    data_2 = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].last_name')
    avatar = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].avatar')
    print(id, data_1, data_2, email, avatar)
    # print((data_1[0]))

