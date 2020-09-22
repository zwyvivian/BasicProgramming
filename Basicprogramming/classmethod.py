class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def walk(self):
        print("walk")

p= Person("Alex",22)
if hasattr(p,"name"):
    print(".....")

a=getattr(p,'age')
print(a)

user_command = input(">>:").strip()
if hasattr(p,user_command):
    func = getattr(p,user_command)
    func()

