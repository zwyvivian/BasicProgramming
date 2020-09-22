from concurrent import futures
import time
import random


def returnNumber(number: int) -> int:
    print("start return number {}".format(number))
    time.sleep(random.randint(10, 20))  # 随机睡眠10-20秒
    print("end return number {}".format(number))
    return number  # 返回参数本身


if __name__ == '__main__':
    with futures.ThreadPoolExecutor(5) as executor:  # __exit__方法会调用executor.shutdown(wait=True)，在所有线程都执行完毕前阻塞当前线程
        res = executor.map(returnNumber,range(0, 10))  # 返回一个生成器，保存的是每个线程处理完返回的结果。其中range序列中0-4交给线程池并发调用，当其中一个线程完成后，将5交给线程池处理，以此类推。
        print(res)
    print("-----end-----")
    print(list(res))