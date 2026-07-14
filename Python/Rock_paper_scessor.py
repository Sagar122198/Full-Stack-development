import random
while True:
    ran = random.choice(["Rock","Paper", "Scessor"])
    user = input('Chosse : "Rock","Paper", "Scessor" : or type "quit" to exit ')
    if ran == user :
        print("You won")
        break
    elif user == "quit":
        print("Get outta here than")
        break
    else:
        print("Chose again : ")
        continue