"""
why do we need lock in real life?

it is because when something is aquired by one person then the
other does not acquire it.

For Example a bathroom when one person uses it the others cannot

Similarly in programming

when 2 threads try to access the shared memory it can cause conflict
and issues for execution therefore we use a LOCK



"""




import time
import multiprocessing
'''
def deposit(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value + 1


def withdraw(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value - 1

# right now we have not used the lock for critical section where the shared memory will not be shared
# so the output of the code can vary everytime


the code below does not use the lock 

if __name__ == '__main__':
    balance = multiprocessing.Value('i', 200)

    d = multiprocessing.Process(target=deposit, args = (balance,))
    w = multiprocessing.Process(target=withdraw, args = (balance,))

    d.start()
    w.start()

    d.join()
    w.join()

    print(balance.value)
    

'''

# the code below uses the lock for critical section


def deposit(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire() # this is the part where the critical section is involved so that any other thread does not use the shared memory
        balance.value = balance.value + 1
        lock.release()


def withdraw(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire() # this is the part where the critical section is involved so that any other thread does not use the shared memory
        balance.value = balance.value - 1
        lock.release()



if __name__ == '__main__':
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit, args = (balance,lock))
    w = multiprocessing.Process(target=withdraw, args = (balance,lock))

    d.start()
    w.start()

    d.join()
    w.join()

    print(balance.value)
