class Animal:
    def eat(self):
        print("Animal is eating:")
class Dog(Animal):
    def eat(self):
        print("Dog is eating")
class Cat(Animal):
    def eat(self):
        print("Cat is eating")
a=Animal()
d=Dog()
c=Cat()
a.eat()
d.eat()
c.eat()