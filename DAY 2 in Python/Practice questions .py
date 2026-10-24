#1 WAP to input user's first name & print it's length
name=input("Enter your first name: ")   #This will take input from the user and store it in the variable first_name
print("the length of your first name is:", len(name))   #This will print the length of the string stored in the variable first_name using the len() function which returns the number of characters in a string including spaces



#2 WAP to find the occurrence of "S" in a string
str="I love Python programming"   #This is a string because it is in double quotes(")
print(str.count("S"))   #This will return 0 because the substring "S" is not found in the string str




#3 WAP to check a number entered by the user is even or odd
num=int(input("Enter a number: "))   #This will take input from the user and store it in the variable num as an integer because it is in int() function
if(num%2==0):   #This will check if the number entered by the user is divisible by 2 or not and if it is true then it will print "Even number"
    print("Even ")
else:
    print("Odd ")


#4 Wap to find the greatest of 3 numbers entered by user. 
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

if(num1>num2 and num1>num3):
    print("num1 is greatest")

elif(num2>num1 and num2>num3):
    print("num2 is greatest")

else:
    print("num3 is greatest")




#5 WAp to check if number is multiple of 7 or not.
num=int(input("Enter a number: "))
if(num%7==0):
    print("Number is multiple of 7")
else:
    print("Number is not multiple of 7")