class Animal: 
    fur_color = "Orange"

    def speak(self):
        print("parent")

    def eat(self):
        print("non-veg")

    def chase(self):
        print("dear")

class Tiger(Animal):
    def speak(self):
        super().speak()
        print("child")

tiger = Tiger()
tiger.speak()
