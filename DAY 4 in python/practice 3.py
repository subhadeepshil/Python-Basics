#Sets in python
#A set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Sets are written with curly brackets.

set1={1,2,3,4,5}          #we can store different data types in a set {}   
set2={"Subhadeep","Shil",25,80.5}          #we can store different data types in a set {}
print(type(set1))          #to print the set
print(len(set1))           #to print the length of the set

print(type(set2))          #to print the set
print(len(set2))           #to print the length of the set


#we can also create empty set and add elements to it later
null_set=set()          #to create an empty set

#adding elements to the set
null_set.add(1)         #to add elements to the set we use the add() method
print(null_set)         #to print the set


#removing elements from the set
null_set.remove(1)      #to remove elements from the set we use the remove() method
print(null_set)         #to print the set



#Clear the set
set.clear        #to clear the set we use the clear() method
print(set)        #to print the set



#pop() method is used to remove a random element from the set
set1.pop()        #to remove a random element from the set we use the pop()
print(set1)        #to print the set after removing a random element

