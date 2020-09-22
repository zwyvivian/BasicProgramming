class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __len__(self):
        return 2
p=Person("Alex",22)
if hasattr(p,"name"):
    print("l........")

