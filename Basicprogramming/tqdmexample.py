'''
from tqdm import tqdm
from time import sleep
pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    sleep(0.25)
    pbar.set_description("Processing %s" % char)
'''

import concurrent.futures
import time
from itertools import count

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def evaluate_item(x):
    for i in count(x):  # count 是无限迭代器，会一直递增。
        print(f"{x} - {i}")
        time.sleep(0.01)


if __name__ == "__main__":
        # 进程池
        start_time_2 = time.time()

        # 使用 with 在离开此代码块时，自动调用 executor.shutdown(wait=true) 释放 executor 资源
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                # 将 10 个任务提交给 executor，并收集 futures
                futures = [executor.submit(evaluate_item, item) for item in number_list]

                # as_completed 方法等待 futures 中的 future 完成
                # 一旦某个 future 完成，as_completed 就立即返回该 future
                # 这个方法，使每次返回的 future，总是最先完成的 future
                # 而不是先等待任务 1，再等待任务 2...
                for future in concurrent.futures.as_completed(futures):
                        print(future.result())
        print ("Thread pool execution in " + str(time.time() - start_time_2), "seconds")