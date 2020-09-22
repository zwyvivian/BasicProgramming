class Animal:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex = sex


    def eat(self):
        print("%s is eating..."  % self.name)

class Person(Animal):
    def talk(self):
        print("I AM TALKING")

    def eat(self):
        Animal.eat()
        super().eat()
        print("I am eating.")

class Dog(Animal):
    def chase_rabbit(self):
        print("dog is chasing rabbit")

p=Person('Alex',22,'M')
p.eat()
p.talk()






