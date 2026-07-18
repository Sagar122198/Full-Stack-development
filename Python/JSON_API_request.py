import requests
req = requests.get("https://swapi.dev/api/people/1/")
starwars= req.json()
# print(starwars)
print(f"Name is : {starwars['name']}")
print(f"Height is : {starwars['height']}")

for film in starwars['films']:
    films=requests.get(film)
    fil = films.json()
    print(fil['title'])
