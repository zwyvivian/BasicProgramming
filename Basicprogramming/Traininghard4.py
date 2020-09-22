l=['a','b','c']
m=['q','w','e']
dic={}.fromkeys(l,)
print(dic)

from collections import defaultdict
dic=defaultdict(lambda:'ok')
print(dic['key2'])

name='memememe'

def change_name():
    global name
    name='Alex'
    print('after change',name)

change_name()

print("really change",name)