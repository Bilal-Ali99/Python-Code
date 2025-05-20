# Create a new file and Write to it
# read file line by line
# File open Modes
# with statement

# creating a file
f = open("d:\\Notebook\\python\\writefile.txt","w")
f.write("This Text was written from a notebook")
f.close()
# for appending any text in the file we put "a" in the place of "w" and put \n so that it writes in the new line

# Simple way of reading a file
r = open("d:\\Notebook\\python\\readfile.txt","r")
# print(r.read()) -> this is also a way of reading out a file
for word in r:
    print(word)
r.close()

# now we are counting the number of words in a line
r = open("d:\\Notebook\\python\\readfile.txt","r")
r_out = open("d:\\Notebook\\python\\readfile_out.txt","w")
for word in r:
    tokens = word.split(" ") # tokens is the number of words in a line
   # print(str(tokens)) # this separates the words in " "
   # print(len(tokens)) # this will count the number of words in each line
    r_out.write("wordcount:"+str(len(tokens))+" "+word)
r.close()
r_out.close()



"""
We could have used 'with' statement here which allows us not to write the r.close() as it does it by itself
with open("d:\\Notebook\\python\\readfile.txt","r") as r:
print(r.read())
"""



