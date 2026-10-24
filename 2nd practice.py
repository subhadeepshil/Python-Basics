#in this practice we will learn about variables in python
name="Subhadeep Shil"   
age="24"                
height="5.10"
cost=30.99
print(name)
print(age)
print(height)
print(cost) 

### No.4 We can also assign value of one variable to another variable
age2=age
print(age2)     #This will print the value of age variable because we have assigned age variable value to age2 variable




 ### No.5 We can also check the data type of variable using type() function

   #Data Types in Python are five types:(str, int, float, bool, none)
   #int type is used for whole numbers like 1,2,3,4,5,30,-30,-5,0
   #float type is used for decimal numbers like 1.5, 2.5, 3.5
   #str type is used for text like "Hello", "Python", "Subhadeep Shil"
   #bool type is used for true or false value like True, False

print(type(name))           #This will print the data type of name variable which is string(str)
print(type(age))            #This will print the data type of age variable which is also string
print(type(height))         #This will print the data type of height variable which is also string
print(type(cost))           #This will print the data type of cost variable which is float because it has decimal value


print(type(age2))           #This will print the data type of age2 variable which is also string



## No.6 We can also change the value of variable
name1="Subhadeep Shil" 
name2='S.S'            #We can use single quotes for string but if we want to use single quote in string then we have to use double quotes for string
name3="""S.S"""        #We can also use triple quotes for string
name4='''Subhadeep Shil'''         #We can also use triple quotes for string


print(name1)          #This will print the value of name1 variable which is Subhadeep Shil
print(name2)          #This will print the value of name2 variable which is S.S
print(name4)          #This will print the value of name4 variable which is Subhadeep Shil