#Tuples in pyhton

tup=(1,2,3,4,5)
print(tup)          #to print the tuple
print(type(tup))    #to know the type of data structure we are using "type


tup=()              #to create an empty tuple
print(tup)          #to print the tuple
print(type(tup))



tup=(2,)              #to create a tuple with a single element
print(tup)          #to print the tuple
print(type(tup))


tup=(2)            #if we remove , it will be considered as an integer, not a tuple
print(tup)          #to print the tuple
print(type(tup))


tup=(1,2,3,4,5)
print(tup[0:3])          #to print the first element of the tuple
print(type(tup)) 


print(tup.index(3))          #to find the index of a specific element in the tuple  0,1,2,3,4


print(tup.count(2))          #to count the number of occurrences of a specific element in the tuple