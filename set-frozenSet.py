"""sets are unordered collection of unique elements
"""

basket = {"orange","apple","mango","pineapple","orange","apple"}
type(basket)

# there is another way of initializing sets
a = set()
a.add(1)
a.add(2)
a
type(a)
a = {}
type(a)

# we also cannot access any element in the set by using the index number for example
basket[1]
# it will show error as TypeError

# sets are used multiple times for multiple purposes specifically for eleminating the repetitive numbers
# for example
numbers = [1,2,3,4,5,1,2,3,4]
uni_numbers = set(numbers)
uni_numbers # here the repititive numbers will be eleminated
# for adding any new number we use add() function
uni_numbers.add(6)
uni_numbers

# if we want to a set where the values cannot be changed then we use frozen set

fset = ["orange","apple","banana","mango","mango","pineapple"]
fs = frozenset(fset)
fs
# it will not allow to add or remove any value in it
fs.add(1)

x = {"a","b","c","d"}
"a" in x

#we can also Iterate in frozen set
for i in fs:
    print(i)

# using the OR AND NOT for sets
a = {"a","b","c","d","e"}
b = {"c","d","e","f","g","h","j"}

print(a|b)
print(a&b)
print(a-b)
print(a<b)
print(b<a)