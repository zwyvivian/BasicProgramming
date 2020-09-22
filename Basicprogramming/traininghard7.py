class Dog(object):
    name='mj'
    def __init__(self,name):
        self.name=name

    @classmethod
    def eat(self,bread):
        print("-->",self)
        print("dog %s is %s" %(self.name,bread))

    @classmethod
    def run(cls):
        print(cls)
d=Dog("mk")
d.eat('bread')
d.run()

