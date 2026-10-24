#No 12 Type Conversion in python
a=12
b =3.14
sum=a+b #This will print the sum of a and b which is 15.14 because when we add an integer and a float, the result is a float
print(sum) #This will print the value of sum which is 15.14 

#Type Casting in python
#If we want to add string to floating value then we need to convert the string to float using float() function

a= int("12")
b=3.14
print(type (a)) #This will print the data type of a variable which is int because we have converted the string "12" to integer using int() function
print(type (b)) #This will print the data type of b variable which is float because we have converted the string "3.14" to float using float() function
print(a+b) #This will print the sum of a and b which is 15.14 because we have converted the string "12" to integer using int() function and when we add an integer and a float, the result is a float


a= float("12.5")
b=3.14
print(type (a)) #This will print the data type of a variable which is float because we have converted the string "12.5" to float using float() function
print (a+b) #This will print the sum of a and b which is 15.64 because we have converted the string "12.5" to float using float() function and when we add two floats, the result is a float


a= 12
a= str(a) #This will convert the integer value of a to string using str() function
print(type (a)) #This will print the data type of a variable which is str because we have converted the integer "12" to string using str() function
