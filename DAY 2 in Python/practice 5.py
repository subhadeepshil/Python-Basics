#conditional statements
#IFTTT Rule (IF THIS THEN THIS)
#If the temperature is above 30 degrees, then print "It's a hot day"

age= int(input("Enter your age: "))
if (age >=18):
    print("You are eligible to vote")

else:
    print("You are not eligible to vote or drive") #if all statements are false then the else block will be executed and it will print "You are not eligible to vote or drive" because the age entered by the user is less than 18






marks=float(input("Enter your marks: "))
if (marks >=90):
    print("You got A grade")

    marks=marks+5 #This will add 5 bonus marks to the original marks variable and store the new value in the same variable marks
    print("Your marks after adding 5 bonus marks is:", marks)

elif(marks >=80 and marks < 90): #This will check if the marks are greater than or equal to 80 and less than 90 and if it is true then it will print "You got B grade"
    print("You got B grade")


elif(marks>=70 and marks<80): #This will check if the marks are greater than or equal to 70 and less than 80 and if it is true then it will print "You got C grade"
    print("You got C grade")


else:
    print("Not Selected")  #This will be executed if the marks entered by the user are less than 0 or greater than 100 because the valid range of marks is from 0 to 100 and if the user enters a value outside this range then it will print "Invalid marks entered"









light=str(input("Enter the traffic light color: "))   #This will take input from the user and store it in the variable light as a string because it is in double quotes("")

if(light == "red"):             #if checks everytime the condition is true or not and if it is true then it will execute the block of code inside the if statement
        print("Stop")

elif(light == "yellow"):        #elif checks the condition only if the previous if condition is false and if it is true then it will execute the block of code inside the elif statement
        print("Get ready")

elif(light == "green"): 
        print("Go")

else:                          #else will be executed if all the previous conditions are false and it will execute the block of code inside the else statement
        print("Light is not working")









num=int(input("Enter a number: "))
if(num>5):
    print("Number is greater than 5") #This will check if the number entered by the user is greater than 5 and if it is true then it will print "Number is greater than 5"

elif(num>0):
    print("Number is positive")

else:
    print("Number is not positive")
