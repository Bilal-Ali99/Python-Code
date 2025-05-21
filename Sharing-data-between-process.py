import multiprocessing


def cal_sqr(numbers,result,v):
    v.value = 2.9
    for idx, i in enumerate(numbers): # enumerate gives us the index and value both
        result[idx] = i*i
    

if __name__ == "__main__":
    array = [2,4,6,8]
    result = multiprocessing.Array('i',4) # we created a shared memory variable which is different from the normal variable
    v = multiprocessing.Value('d',0.0) # it is similar to array but gives only one value
    p = multiprocessing.Process(target = cal_sqr, args = (array,result,v))

    p.start()
    p.join()


    print(result[:]) # this is the way print all the element in a list
    print(v.value)
'''
the output of this code will show two outputs where the inside process
will show the square of numbers and the output of outside process
will show empty list.


to solve this problem for which we create a shared memory to solve the problem


'''