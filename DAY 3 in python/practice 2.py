#List Methods

list=[2,6,5,4,7]
list.append(8)          #The append() method adds an element to the end of the list. It will automatically add new value to the last
print(list)



#Shorting a list
list.sort()            #The sort() method sorts the list in ascending order by default. It modifies the original list and does not return a new sorted list.
print(list.sort())           #it will return NONE value because it will sort the list in place and does not return a new sorted list
print(list)          #it will print the sorted list because the sort() method has sorted the original list in place

print(list.sort(reverse=True))     #it will return NONE value because it will sort the list in place and does not return a new sorted list
print(list)          #it will print the sorted list in descending order because the sort() method


list2=["apple","banana","grape","orange"]
print(list2.sort())          #it will sort the list in alphabetical order because the sort() method sorts strings in alphabetical order by default
print(list2)          #it will print the sorted list in alphabetical order



list3=["Subhadeep","Shil","Kolkata","India"]
list3.reverse()         #it will reverse the list
print(list3)          #it will print the reversed list



list3=["Subhadeep","Shil","Kolkata","India"]
list3.insert(2,"New Element")         #it will insert an element at the specified index
print(list3)  


list3=["Subhadeep","Shil","Kolkata","India"]
list3.remove("Shil")         #it will remove the first occurrence of the specified element
print(list3)          #it will print the list after removing the specified element


list4=[1,2,3,4,5,]
list4.pop(2)         #it will remove the element at the specified index
print(list4) 