import threading
from concurrent import futures
import logging
import time
import os
# 定义输出的格式
FORMAT = "%(asctime)-15s\t[%(processName)s:%(threadName)s , %(process)d:%(thread)8d] %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)

def worker(n):
    logging.info("begin to work{},the pid is {}".format(n,os.getpid()))
    time.sleep(5)
    logging.info("finished{}".format(n))

# 创建线程池, 容量为3
if __name__=='__main__':
    executer = futures.ProcessPoolExecutor(max_workers=3)
    fs = []

    for i in range(3):
        future = executer.submit(worker, i)
        fs.append(future)

    # for i in range(3, 6):
    #     future = executer.submit(worker, i)
    #     fs.append(future)

    while True:
        time.sleep(2)
        logging.info(threading.enumerate())  ##输出正在运行的线程

        flag = True
        count=0
        for f in fs: #判断是否还有未完成的任务
            count+=1
            print(f'This is the number {count},and it is {f.done()}')
            flag = flag and f.done()   #有一个未完成flag都会变成False
            if not flag:##出现一次就说明未完成, 提前结束
                break

        print("-" * 30)

        if flag:
            executer.shutdown()
            logging.info(threading.enumerate())
            break