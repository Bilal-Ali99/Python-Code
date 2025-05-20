"""
What is Multithreading?

Taking an example of mother who is a house wife she handles multiple things at the same time
for e.g
handling a new born child 
cooking food
washing cloths
cleaning the house etc 


all task done at same time is called multithreading
"""
# the code below is not multithreading code it is simple code

import time

def cal_sqr(numbers):
    print("Calculating Square numbers\n")
    for i in numbers:
        time.sleep(0.2)
        print("Square of Numbers are: ",i*i)

def cal_cube(numbers):
    print("\nCalculating Cube of numbers\n")
    for i in numbers:
        time.sleep(0.2)
        print("Cube of Numbers are: ",i*i*i)


array = [2,3,7,8,3,11]
t = time.time()
sqr =  cal_sqr(array)
cube = cal_cube(array)

print("time taken", time.time() - t )
print("done now")

# now we will do same coding with threading included in it 


import time
import threading


def cal_sqr(numbers):
    print("Calculating Square numbers\n")
    for i in numbers:
        time.sleep(0.2)
        print("Square of Numbers are: ",i*i)

def cal_cube(numbers):
    print("\nCalculating Cube of numbers\n")
    for i in numbers:
        time.sleep(0.2)
        print("Cube of Numbers are: ",i*i*i)


array = [2,3,7,8,3,11]
t = time.time()


# the target is the worker function the task we want to execute like mom handling all the task
t1 = threading.Thread(target = cal_sqr, args = (array,) )
t2 = threading.Thread(target = cal_cube, args = (array,) )

# for starting the thread we do
t1.start()
t2.start()

# what the join function does is it will wait until one thread is done and after first is done it will execute
t1.join()
t2.join()

print("time taken", time.time() - t )


"""
The Time Taken for this code to execute is almost half time

In this code when the function of time.time(0.2) was getting executed in cal_sqr the cal_cube function 
was getting executed

Therefore the square and cube of 1 number was given in the output from the array

Multithreading is typically using when CPU is in idle mode it can do different work
When calling a web service it might take sometime to response during that time if we want to optimize the 
performances of program we can use the CPU for other task that is multithreading

"""
