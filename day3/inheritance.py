class Animal:
    def __init__(self,name):
        self.name=name
    
    def eat(self):
        print(f"{self.name} is eating")

    def speak(self):
        print("some sound")

class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed

    def speak(self):
        print(f"{self.name} says:bow")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says:meow")

# dog=Dog("brownie","lab")
# cat=Cat('kitty')

dog.eat()
dog.speak()
cat.speak()