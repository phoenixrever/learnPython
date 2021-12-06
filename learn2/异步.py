# coding: utf-8
import multiprocessing
import time
import requests
from multiprocessing.dummy import Pool


def getData(data):
    print('正在下载', data)
    time.sleep(2)
    print(data, ':下载成功')
    return data


list = ['123', '456', '789', 'aaa', 'nnn']
if __name__ == '__main__':
    # 10大小的线程池 ==
    pool = Pool(10)  # type: multiprocessing.pool.ThreadPool
    starttime = time.time()
    # 将list 的每个元素作为参数传给方法 返回值为函数的返回值的列表
    # map会阻塞等待 每个线程完成
    result = pool.map(getData, list)
    print(result)
    pool.close()
    # 主线程等待pool结束
    pool.join()
    endTime = time.time()
    print("耗时:%d 秒" % (endTime - starttime))
