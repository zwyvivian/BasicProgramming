from multiprocessing import Process
import time,os

def task(name):
    print("%s is running" %os.getpid(),'%s parent is running'%os.getppid())
    time.sleep(3)
    print(name)
    print("%s is running" %os.getpid(),'%s parent is running'%os.getppid())

if __name__=="__main__":
    p=Process(target=task,args=['sub1'])
    p.start()
    print(os.getpid())