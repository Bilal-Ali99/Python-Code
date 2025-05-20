# JSON = Java script object notation 
# JSON is similar to XML
# JSON is like a dictionary and is light weight
"""We will write two programs first we will create an address book and secondly we will read the address book"""

book = {}
book['tom'] = {
    'name' : 'tom',
    'address' : 'street 3 house 214',
    'phone' : 123456789
}

book['bob'] = {
    'name' : 'bob',
    'address' : 'street 2 house 109',
    'phone' : 987654321
}

import json
s = json.dumps(book)
print(s)
import sys
with open("d://Notebook//python//json.txt","w") as f:
    f.write(s)


# reading the data from the json file
read = open("d://Notebook//python//json.txt","r")
a = read.read()
a
book_1 = json.loads(a)
book_1
type(book)
book_1['bob']
# printing all the values in the book_1
for person in book_1:
    print(book_1[person])