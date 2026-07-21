class fridge : 
    items = {
        "fruit" : "Apple",
        "vegitable": "tomatos"
    }

    lst =  [1,3,"five", "six"]
    _anything = "this is a private property"

    def get_property(self):
        return self.items
    
    def remove(self, item):
        self.lst.remove(item)
        return self.lst
    
    @property
    def get_lst(self):
        return self.lst
     
store = fridge()
print(store.get_property())
print(store.get_lst)
print(store.remove("five"))

