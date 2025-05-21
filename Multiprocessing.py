"""both are ways of achieving of multitasking
a process has it on virtual memory or address space 
in the virtual memory multiple threads are created

difference of process and thread

the threads share the same address space although they have their own stack memory, instruction pointer

Processes have their own address space and if they want to communicate with each they use intercommunication technique like a shared memory, file or a message pipe  

Threads are light weight
process are heavy weight

the benefit of multiprocessing is that the error or memomy leak in one process won't hurt hurt execution of another process meaning if one process is problematic it wont effect other process but if one thread is problematic it create hinderance for other threads too"""


import time
import multiprocessing

# square_result= []

def cal_sqr(numbers):
    for i in numbers:
        time.sleep(3)
        print("square is " + str(i*i))


def cal_cube(numbers):
    for i in numbers:
        time.sleep(3)
        print("cube is " +  str(i*i*i))


if __name__ == "__main__":
    array = [2,3,7,8,3,11]
    p1 = multiprocessing.Process(target=cal_sqr, args=(array,))
    p2 = multiprocessing.Process(target=cal_cube, args=(array,))
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    print("Done")


"""
taking the example of printing the results of anyone process for example p1

then we will need to print it in the function where we are calculating the square of the numbers
taking the example

def cal_sqr(numbers):
    global square_result
    for i in numbers:
        print("square is " + str(i*i))
        square_result.append(i*i)
    print('result of calculation within the process' + str(square_result))


    

"""