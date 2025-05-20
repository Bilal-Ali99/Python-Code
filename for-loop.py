# calculating the expenses which in a list 

exp = [2130,2150,3100,512,2546]
# normal calculation is done this way
cal1= exp[0] + exp[1] + exp[2] + exp[3] + exp[4]
print("this is the total cal1:", cal1)

# using the for loop
cal2 = 0
for item in exp:
    cal2 = cal2 +item

print("this is the total cal2:", cal2)

# printing 1 to 10 using range() fn
for i in range(1,11): # in range fn for example if we have to put number till 10 then we will have to put 11 as the function works in n-1 
    print(i)

# for a square of number
for j in range(1,11):
    print(f"Square of Number {j}:",j*j)

# searching for a lost key and terminating the function when found

key_location = "under the bed"
locations = ["living room","behind the desk","inside the bag","under the bed","in the office"]
for location in locations:
    if location == key_location:
        print("key was found:",location)
        break
    else:
        print("key was not found at:",location)


# in this for loop the location was found in the 3rd index location hence the for loop is break and it did not iterated at 4th index

# printing square numbers except for even numbers

for i in range(1,25):
    if i%2 == 0:
        continue
    print(i)