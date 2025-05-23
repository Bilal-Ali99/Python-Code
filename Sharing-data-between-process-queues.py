

import multiprocessing
import multiprocessing.queues

result = []


def cal_sqr(numbers,q):
    for i in numbers:
        q.put(i*i) # method put is taken from the concept of data structure where we use the queue for First In First Out
    

if __name__ == "__main__":
    array = [2,4,6,8]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=cal_sqr, args=(array,q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get()) # this will iterate the queue and get the elements from the start of the queue
    