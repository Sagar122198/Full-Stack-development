import requests

req = requests.get("https://swapi.dev")
print(req.status_code)