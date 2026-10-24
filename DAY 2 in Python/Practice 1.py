#No. 1 strings 
#(str stands for string which is a sequence of characters like "Hello", "Python", "Subhadeep Shil")

str1="It's a string"    #This is a string because it is in double quotes(") and \n is used for new line or next line in string   
str2='It\'s a 2nd string.'                 #This is also a string because we have used escape character(\) to use single quote in string
str3="""It's a 3rd string.\n Hello everyone"""              #This is also a string because it is in triple quotes(""") /n is used for new line or next line in string
str4='''It's a 4th string'''              #This is also a string because it is in triple quotes(''')


print(str1)          #This will print the value of str1 variable which is It's a string.Hello everyone

print(str3)          #This will print the value of str2 variable which is It's a 2nd string


#we can add two strings using + operator

print(str1 + str2)  #This will print the value of str1 and str2 variable which is It's a string It's a 2nd string
print(str1 + " " + str2)  #This will print the value of str3 and str4 variable which is It's a 3rd string. Hello everyone It's a 4th string because we have added space between str3 and str4 using " " in print statement

final_string=str1+str2 #This will add the value of str1 and str2 variable and store it in final_string variable
print(final_string)  #This will print the value of final_string variable which is It's a string It's a 2nd string