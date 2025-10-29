import requests

url = "https://mywebsite/api/mystuff?limit=1&offset=25"


mytoken = "token123FROMdevzzzz"

payload = {}
headers = {
  'Accept': 'application/json; version=1.0',
  'Authorization': f'Bearer {mytoken}'
}

response = requests.request("GET", url, headers=headers, data=payload)
print(headers)
print(response.text)

#This commit only exists on the main branch