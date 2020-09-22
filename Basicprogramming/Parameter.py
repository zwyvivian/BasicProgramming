
def register(name,age,major,country='cn'):
    pass


name='vivian'
def change():
    name='alex'
    age=22
    print(name)
    print(locals())
 #   print(globals())


change()

def change():
    global name
