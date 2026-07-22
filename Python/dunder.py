class Animal:
    def __init__(self,color):
        print("The color is :" , color)

class Pet(Animal):
    def __init__(self,color):
        super().__init__(color)
        print("something more", color)
z = Pet("yellow")
# z.__init__()
        