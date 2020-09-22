
'''
import time
import random
from threading import Thread

def piao(name):
    print("%s piaoing" % name)
    time.sleep(random.randint(0,5))
    print("%s" %name)

if __name__=='__main__':
    t1=Thread(target=piao,args=('vivian',))
    t1.start()
    print("main")
'''
import time
import random
from threading import Thread

class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print("%s piaoing" %self.name)
        time.sleep(random.randrange(1,5))
        print(self.name)

if __name__=='__main__':
    t1=MyThread("zey")
    t1.start()
    print("ok")