'''
name = 'A'

def changename():
    global name
    name='b'
    print("after",name)

changename()


print("outer",name)

'''
'''
def america():
    return 2

def login(f):
    def inner():
        c=f()
        return c+1
    return inner

america=login(america)
print(america)
'''
import time


def timingcal(func):
    def inner(*arg):
        start=time.time()
        time.sleep(5)
        func(*arg)
        interval=time.time()-start
        return interval
    return inner


@timingcal
def func():
    sum=0
    for i in range(10):
        sum+=i
    print(sum)

@timingcal
def func1():
    sum=0
    for i in range(20):
        sum+=i
    print(sum)


print(func())


