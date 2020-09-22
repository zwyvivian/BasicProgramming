#import threading
from tqdm import tqdm
from concurrent import futures
import logging
import time
import os
# 定义输出的格式
#FORMAT = "%(asctime)-15s\t[%(processName)s:%(threadName)s , %(process)d:%(thread)8d] %(message)s"
logging.basicConfig(level=logging.DEBUG)

def worker(n):
    logging.info("begin to work{},the pid is {}".format(n,os.getpid()))
    time.sleep(n*2)
    logging.info("finished{}".format(n))
    return "worker{}".format(n)


if __name__=='__main__':
    l=[1,2,3,4,5,6]
    with futures.ThreadPoolExecutor() as executor:
        result=list(tqdm(executor.map(worker,l,chunksize=6),total=6))
#        executor.shutdown(wait=True)

    for item in result:
        print(item)