# coding: utf-8

import asyncio
import time


# 异步方法
async def getData(data):
    print('正在下载', data)
    time.sleep(2)
    print(data, ':下载成功')
    return data


list = ['123', '456', '789', 'aaa', 'nnn']

if __name__ == '__main__':
    # 创建循环对象
    # loop = asyncio.get_event_loop()
    # 注册和启动函数
    # loop.run_until_complete(getData("123"))

    # task的使用
    loop = asyncio.get_event_loop()
    # loop.create_task(getData("123"))

    # future的使用
    future = asyncio.ensure_future(getData("123"))

    result = loop.run_until_complete(future)
    print("返回值:", result)


    # 回掉方法
    def call_back(future):
        print("线程执行完成后的回掉方法  值为:", future.result())


    future = asyncio.ensure_future(getData("回掉值"))
    # call_back默认参数为  future
    future.add_done_callback(call_back)
    callback = loop.run_until_complete(future)
