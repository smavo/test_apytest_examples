
import requests

# API URL
url = 'https://reqres.in/api/users?page=2'

# Send Get Request
response = requests.get(url)
print(response.content)

# Validate Status Code
assert response.status_code == 200
print(response.status_code)

if response.status_code == 200:
    print("Peticion Exitosa")
else:
    print("Peticion Errorea")

# Fetch Response Header
print(response.headers.get('Date'))
print(response.headers.get('Server'))


# Fetch Cookies
print(response.cookies)

# Fetch Encoding
print(response.encoding)

print(response.elapsed)
