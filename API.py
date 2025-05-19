import json
import requests

get_data = requests.get('https://fake-json-api.mock.beeceptor.com/users')
headerValues = get_data.headers
print(headerValues)
print(type(headerValues))
for key, value in headerValues.items():
    print(key, value)
