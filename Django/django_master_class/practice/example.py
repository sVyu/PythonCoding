class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def greet(self):
        print(f"Hi! My name is {self.name} and I am a {self.species}")

class Cat(Animal):
    def __init__(self, name, species = 'Cat'):
        Animal.__init__(self, name, species)

    def sound(self):
        print("Meow")

class Dog(Animal):
    def __init__(self, name, species = 'Dog'):
        Animal.__init__(self, name, species)

    def sound(self):
        print("Ruff")

cat1 = Cat("haha")
cat1.sound()