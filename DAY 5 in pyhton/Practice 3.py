#for loops
# A for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable object.

nums=[1,2,3,4,5]
for val in nums:
    print(val)                    #it will print the values in the list nums one by one.

veg=["tomato","potato","onion","carrot"]
for val in veg:
    print(val)                    #it will print the values in the list veg one by one.

    
    tup=(1,2,3,4,9,5)
for val in tup:
    print(val)                    #it will print the values in the tuple tup one by one.


#optional else in for loop
for val in nums:
    print(val)
else:
    print("Loop is over")           #it will print the values in the list nums one by one and after the loop is over it will print "Loop is over".


str="Hello World"
for char in str:
    if (char == "o"):
        print("Found o")           #it will print the characters in the string str one by one and when it finds the character "o" it will print "Found o".
        print(char)
    else:
        print("Not Found o")    #it will print the characters in the string str one

print("ABCD")