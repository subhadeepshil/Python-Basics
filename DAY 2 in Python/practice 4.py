#NO 4 String Functions in python


#End with() function in python is used to check if a string ends with a specific suffix or not. It returns True if the string ends with the specified suffix, otherwise it returns False.
str="I love Python programming"
print(str.endswith("mming"))   #This will return True because the string str ends with "mming"


#Capitalize() function in python is used to convert the first character of a string to uppercase and the rest of the characters to lowercase.
str="i love Python programming"
print(str.capitalize())  #This will return "I love python programming" because the first character of the string str is converted to uppercase and the rest of the characters are converted to lowercase

#we cant't print the original string str because the capitalize() function does not change the original string, it returns a new string with the first character capitalized and the rest of the characters in lowercase. So if we want to see the original string str we can print it again after using the capitalize() function.
print(str)


str=str.capitalize()  #This will return "Python is a programming language 2" because the first character of the string str is converted to uppercase and the rest of the characters are converted to lowercase
print(str)  #This will print the new string str which is "Python is a programming language 2" because we have assigned the new string returned by the capitalize() function to the original string str. So now the original string str is changed to the new string returned by the capitalize() function.



#Replace function in python is used to replace a specific substring with another substring in a string. It returns a new string with the specified substring replaced by the new substring.
str="I love Python programming"
print(str.replace("Python","Bhai"))   #This will return "I love Bhai programming" because the substring "Python" is replaced by "Bhai" in the string str


#Find Function in python is used to find the index of the first occurrence of a specific substring in a string. It returns the index of the first occurrence of the specified substring, or -1 if the substring is not found.
str="I love Python programming"
print(str.find("ython"))   #This will return 2 because the substring "ython" is found at index 2 in the string str
print(str.find("S"))   #This will return -1 because the substring "S" is not found in the string str



#Count function in python is used to count the number of occurrences of a specific substring in a string. It returns the number of occurrences of the specified substring in the string.
str="I love Python programming"
print(str.count("o"))
print(str.count("g"))   #This will return 2 because the substring "o" is found 2 times in the string str