class Animal: 
    fur_color = "Orange"

    def speak(self):
        raise NotImplementedError

    def eat(self):
        print("non-veg")

    def chase(self):
        print("dear")

class Tiger(Animal):
    def speak(self):
        print("hawwwwww")

tiger = Tiger()
tiger.speak()
