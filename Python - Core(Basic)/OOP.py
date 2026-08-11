#1. Class & Object

class Person:
    def __init__(self, name, age):
        self.name = name   # Attribute
        self.age = age

    def greet(self):       # Method
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create object
p1 = Person("Alice", 25)
p1.greet()

# 2. Inheritance

class Animal:
    def speak(self):
        print("I am an animal.")

class Dog(Animal):
    def bark(self):
        print("Woof!")

d = Dog()
d.speak()  # Inherited method
d.bark()

# 3. Polymorphism

class Bird:
    def sound(self):
        print("Birds sing")

class Parrot(Bird):
    def sound(self):
        print("Parrot talks")

def make_sound(bird: Bird):
    bird.sound()

b1 = Bird()
b2 = Parrot()

make_sound(b1)
make_sound(b2)  # Same method name, different behavior

#4  Encapsulation

class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account(1000)
acc.deposit(500)
print(acc.get_balance())  # 1500

#5 Abstraction (via Abstract Base Class)

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

c = Car()
c.start_engine()
