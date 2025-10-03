class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
class Dog(Animal):
    def move(self):
        print("Running 🐕")
class Bird(Animal):
    def move(self):
        print("Flying 🐦")
class Fish(Animal):
    def move(self):
        print("Swimming 🐟")
# List of animal objects
animals = [Dog(), Bird(), Fish()]
# Demonstrate polymorphism
for animal in animals:
    animal.move()
