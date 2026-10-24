#WAP to ask the user to enter names of their 3 favorite movies & store them in a list


movies=[]
mov1=input("Enter Your 1st movie")     #we can store different data types in a list
mov2=input("Enter Your 2nd movie")
mov3=input("Enter Your 3rd movie")
movies.append(input("Enter Your 4th movie"))   #we can also directly append the input to the list without storing it in a variable

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)




#WAP TO CHECK IF A LIST CONTAINS PALINDROME OF ELEMENT.(HINT:USE COPY()METHOD)


list1=[1,2,3,2,1]
copy_list1=list1.copy()          #to create a copy of the list
copy_list1.reverse()              #to reverse the copy of the list
if(copy_list1==list1):          #to check if the reversed copy of the list is equal to the original list
    print("Palindrome")          #if the condition is true, it will print "Palindrome"
else:
    print("Not a Palindrome")

list2=[1,"abc","abc",5]
copy_list2=list2.copy()
copy_list2.reverse()
if(copy_list2==list2):
    print("Palindrome")
else:
    print("Not a Palindrome")





#WAP TO COUNT THE NUMBER OF STUDENT WITH THE "A GRADE IN THE FOLLOWING TUPLE"
#["C","A","B","A","C","B","A"]
#STORE THE ABOVE VALUE IN A LIST &sort THEM FROM "A" TO "D"

grade = ["C","A","B","A","C","B","A"]
grade.sort()  
print(grade)        #to sort the list in alphabetical order
print(grade.count("A"))          #to count the number of occurrences of "A" in the list, we use the count() methodt


