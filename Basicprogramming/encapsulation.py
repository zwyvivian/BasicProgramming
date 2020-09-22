class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__life_val=100

    def get_life_val(self):
        return self.__life_val

    def got_attack(self):
        self.__life_val-=20
        return self.__life_val

    def __breath(self):
        print("breaking")


a = Person("Alex",22)
#print(a.__life_val)
print(a.get_life_val())
a._Person__breath()

