#Listing in python (It can store elements of different data types in a single list (integers, strings, floats, etc.))
#List is a collection which is ordered and changeable. Allows duplicate members.

marks=[80.5,60.0,20.0,50.0,90.0]            #()[]{} are used to define a list
print(marks[3])                           #to access the elements of a list we use index number (index starts from 0)
print (type(marks))                          #to know the type of data structure we are using "type"



#we can add particular student marks to the list 

student1=["Subhadeep","80.5","Kolkata"]             #we can store different data types in a list  
print(student1)

student1[0]="Subhadeep Shil"                          #we can change the value of a list element by using index number
print(student1)



print(marks[3:5])   #to access a range of elements in a list we use slicing (start index : end index) (end index is not included)

print(marks[-3:-1])      #we can also use negative indexing to access elements from the end of the list (negative index starts from -1)         


