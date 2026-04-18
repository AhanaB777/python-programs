""" Hierarchical Inheritance """
class Animal:
    def __init__(self,name):
        self.name=name
        
    def display(self):
        print(f"Animal name: {self.name}")

class Dog(Animal):
    def sound(self):
        print(self.name,"barks")

class Cat(Animal):
    def sound(self):
        print(self.name,"meows")

d1=Dog("Buddy")
d1.display()
d1.sound()
c1=Cat("Lily")
c1.display()
c1.sound()