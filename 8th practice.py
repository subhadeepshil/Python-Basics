#No. 13 User Input in Python

name = input("Enter your name: ")  # This will take input from user and store it in name variable
age = input("Enter your age: ")    # This will take input from user and store it in age variable

print("Welcome", name)  # This will print the value of name variable which is entered by user
print("You are", age, "years old.")  # This will print the value of age variable which is entered by user

#we can add values with val()ue of variable
val=input("Enter a number: ")  # This will take input from user and store it in val variable
print (type(val), val)  # This will print the data type of val variable which is string because input() function always returns a string value


#we can limit the value of input using int() function
int("5")  # This will convert the string "5" to an integer
val2=float(input("Enter a number: "))  # This will take input from user and store it in val2 variable and convert it to float using float() function
print (type(val2), val2)  # This will print the data type of val2 variable which is float because we have converted the string input to float using float() function



#we can also check marks of student using input() function
name = input("Enter your name: ")  # This will take input from user and store it in name variable
age = int(input("Enter your age: "))    # This will take input from user and store it in age variable
marks= float (input("Enter your marks: "))  # This will take input from user and store it in marks variable

print("Welcome", name)  # This will print the value of name variable which is entered by user
print("You are", age, "years old.")  # This will print the value of age variable which is entered by user
print("Your marks are", marks)  # This will print the value of marks variable which is entered by user