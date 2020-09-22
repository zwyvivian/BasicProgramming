class Dog:
    role='dog'

    def __init__(self,name,age,breed,master):
        self.name=name
        self.age=age
        self.breed=breed
        self.master=master

    def sayhi(self):
        print('Hi, I am %s, master %s' % (self.name,self.master.dream))


class Person:
    dream='writer'
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def walk_dog(self,dog_obj):
        print("master %s go walking %s" % (self.name,dog_obj.name))


p1=Person("vivian",24,'F')
d1=Dog("vi",4,"F",p1)
d1.sayhi()
p1.walk_dog(d1)