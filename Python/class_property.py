class fridge : 
    items = {
        "fruit" : "Apple",
        "vegitable": "tomatos"
    }

    lst =  [1,3,"five", "six"]
    _anything = "this is a private property"
store = fridge()
print(store.items)
print(store.lst)
print(store._anything)
print(fridge._anything)
