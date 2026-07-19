import requests
import json
name = input("Enter pokemon name : ")
url = f"https://pokeapi.co/api/v2/pokemon/{name}"

req = requests.get(url)
data = req.json()

# changed_data = json.loads(data)
# print(type(changed_data))

while True:
    ask = input("Want to access the data 'y' or 'n' :  ")

    if ask == 'y':
        user = input("Search for data : ")
        print(data[user])
        if user == "abilities":
            data = req.json()
            for i in data['abilities']:
                print(i['ability'] ['name'] )
    
    elif ask == 'n':
        break

    else:
        print("Enter 'y' or 'n' you DUMB ")