
import requests
import json
import jsonpath

# API URL
url = 'https://reqres.in/api/users?page=2'

# Send Get Request
response = requests.get(url)

# Parse response to Json Format
json_response = json.loads(response.text)
print(json_response)

# Fetch value using Json Path
pages = jsonpath.jsonpath(json_response, 'total_pages')
pages_number = 2
print(pages)

assert pages[0] == pages_number

if pages[0] == pages_number:
    print("Validacion Exitosa")
else:
    print("No paso la validacion")


