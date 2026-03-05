#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:00:24 2026

@author: geo
"""

class Animal:
    def __init__(self, name, species, age = 0):
        self.name = name
        self.species = species
        self.age = age
    def greet(self):
        print(f"I am a {self.species} named {self.name}")
    def how_old(self):
        print(f"I am {self.age} years old")
class Dog(Animal):
    def __init__(self, name, breed, age = 0):
        super().__init__(name, "Dog", age)
        self.breed = breed
    def greet(self): # dogs bark
        print(f"Woof! I am a {self.breed} breed.")
class Cat(Animal):
    def __init__(self, name, breed, age = 4):
        super().__init__(name, breed, age)
    def greet(self): # cats meow,
        print(f"Meow! I am a {self.species} cat.")
        
dog = Dog("Buddy", "Golden Retriever", 4)
cat = Cat("Whiskers", "Siami", 2) 
for animal in [dog, cat]:
    animal.greet()
    animal.how_old()