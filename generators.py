"""a simple way of creating the iterators

yield and return are same to some extent

return function returns and destroys everything after completing 
yield function preserves the state of last execution
yield is usefull when we have a long list of values and we dont want to return them in one shot as returning all values in one shot requires a lot of memory secondly in return the compiler has to process the values in the code block 
where as yield we can produce the result and get the return immideatley 
"""
def remote_control_next():
    yield "cnn"
    yield "espn"

itr = remote_control_next()
itr

print(next(itr))
print(next(itr))

# creating a fibonacci series

def fib():
    a , b = 0 , 1
    while True:
        yield a
        a,b = b , a+b

for f in fib():
    if f > 100:
        break
    print(f)


"""Benefit of generator over class based iterator is that

1) you don't need to define iter() and next() methods
2) you don't need to raise StopIteration exceptions

"""