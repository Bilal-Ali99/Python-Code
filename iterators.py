a = ['hey','bro','how','are','you']
for i in a:
    print(i)

dir(a)

itr = iter(a)
itr

class RemoteControl():
    def __init__(self):
        self.channels = ['samaa','geo','ary','hum']
        self.index = -1
    def __iter__(self):
        return(self)
    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]

r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
