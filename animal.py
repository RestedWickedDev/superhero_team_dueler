class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(self.name + " is eating")

    def drink(self):
        print(self.name + " is drinking")

class Frog(Animal):
    def jump(self):
        print(self.name + " is jumping")

my_frog = Frog("Slippy")

my_frog.eat()
my_frog.drink()
my_frog.jump()