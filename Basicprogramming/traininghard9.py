'''
from multiprocessing import Process
def task(name):
    print("%s is runing" %name)
    time.sleep(3)
    print("%s is done" %name)

if __name__=="__main__":
    p=Process(target=task,arg=('sub1',))
    p.start() #signalling the OS
'''
from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self,name):
        print("%s is running" %name)
        time.sleep(3)
        print("%s is done" % name)

if __name__=="__main__":
    p=MyProcess("zwy")
    p.sart()
