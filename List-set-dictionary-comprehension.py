"""list comprehension provides a way to transform one list into another and same for Set and Dictionary
"""
# example of list comprehension

numbers = [1,2,3,4,5,6,7]
even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)

even
# in the above code we wrote about 3 lines of code
# list comprehension provides us a way to write code in a single line

even = [i for i in numbers if i % 2 == 0 ]
even
sqr_numbers = [i*i for i in numbers]
sqr_numbers

# example of sets comprehension
# set are in-ordered collection of numbers
s = set([1,2,3,3,4,5,1,6,7])
s

# it will clear the repeative number
# for finding even number in sets 
s_even = [i for i in s if i % 2 ==0]
s_even

# Dictionary comprehension
# we have two list country and city

cities = ['Karachi','Newyork','Manchester','Tokyo']
countries = ['Pakistan','America','England','Japan']

# for creating a dictionary where cities is key and country is value
# we use zip function
# what zip funtion does is it combines two list into tuples

z = zip(cities,countries)
z # an object is created now we need to iterate through this object to print the tuple

for i in z:
    print(i)
# this printed form will be in tuple 
# now to make it in dictionary form we need to do comprehension in it
d = {city:country for city, country in zip(cities,countries)}
d
