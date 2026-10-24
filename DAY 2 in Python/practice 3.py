#No 3 Slicing in string in python

str1="Hello.world"   #This is a string because it is in double quotes(")
print(str1[0:7])   #This will print the characters from index 0 to index 6 of str1 variable which is Hello.w because indexing starts from 0 in python and the last index is exclusive in slicing

print(str1[7:len(str1)])    #This will print the characters from index 7 to index 11 of str1 variable which is world because indexing starts from 0 in python and the last index is exclusive in slicing

print(str1[2:])    #This will print the characters from index 2 to index 4 of str1 variable which is llo because indexing starts from 0 in python and the last index is exclusive in slicing


#we can also use negative indexing in slicing
str3="Python is a programming language"   #This is a string because it is in double quotes(")
print(str3[-8:-3])    #This will print the characters from index -8 to index -3 of str3 variable which is program because indexing starts from 0 in python and the last index is exclusive in slicing and negative indexing starts from the end of the string