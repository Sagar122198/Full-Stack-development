class Animal: 
    fur_color = "Orange"

    def speak(self):
        print("Raawwwwrr")

    def eat(self):
        print("non-veg")

    def chase(self):
        print("dear")

class Tiger(Animal):
    def speak(self):
        print("hawwwwww")

class Cat(Animal):
    def eat(self):
        print("both")

class Cow(Animal):
    def chase(self):
        print("no one")

tiger = Tiger()
tiger.speak()

cat = Cat()
cat.eat()

cow = Cow()
cow.chase()