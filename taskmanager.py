#python taskmanager.py
#-*- coding:utf-8 -*-
import random,time,Queue
from multiprocessing.managers import BaseManager


task_queue = Queue.Queue()
result_queue = Queue.Queue()

class QueueManager(BaseManager):
    pass
def gettaskqueue():
    global task_queue
    return task_queue
def getresultqueue():
    global result_queue
    return result_queue    
if __name__ == '__main__':
    #QueueManager.register('get_task_queue',callable=lambda: task_queue)
    #QueueManager.register('get_result_queue',callable=lambda: result_queue)
    QueueManager.register('get_task_queue',callable=gettaskqueue)
    QueueManager.register('get_result_queue',callable=getresultqueue)

    manager = QueueManager(address=('localhost',5000),authkey = 'abc')
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0,10000)
        print ('Put task %d...'%n)
        task.put(n)
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print ('Result:%s'%r)
    manager.shutdown()