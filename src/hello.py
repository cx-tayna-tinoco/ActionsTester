import requests
#This comment only exissts on my dev branch


url = "https://mywebsite/api/mystuff?limit=1&offset=25"


mytoken = "token123FROMdevzzzz"
phone = "990000000"
payload = {"phone": phone}
headers = {
  'Accept': 'application/json; version=1.0',
  'Authorization': f'Bearer {mytoken}'
}

response = requests.request("GET", url, headers=headers, data=payload)
print(phone)
print(headers)
print(response.text)
