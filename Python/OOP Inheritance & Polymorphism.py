# Exercise 1: Simple Inheritance

class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Demonstrate polymorphism
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.speak())

# Exercise 2: Multi-level Inheritance

class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving"

class SportsCar(Car):
    def move(self):
        return "SportsCar is racing"

# Demonstrate polymorphism
vehicles = [Vehicle(), Car(), SportsCar()]
for v in vehicles:
    print(v.move())