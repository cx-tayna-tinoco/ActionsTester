import requests

url = "https://mywebsite/api/mystuff?limit=1&offset=25"


mytoken = "token123FROMmainzzzz"

payload = {}
headers = {
  'Accept': 'application/json; version=1.0',
  'Authorization': f'Bearer {mytoken}'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
