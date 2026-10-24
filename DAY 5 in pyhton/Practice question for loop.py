#1 Print the elements of the following list using loop: {1,4,6,16,25,36,49,64,81,100}

num= [1,4,6,16,25,36,49,64,81,100]

for element in num:                    #it will print the elements in the list num one by one.
    print(element)








#2 Search for a number x in this tuple (1,4,6,16,25,36,49,64,81,100) using for loop.
num_tuple= (1,4,6,16,25,36,49,64,81,100)
x= int(input("Enter the number you want to search: "))
x=49
idx=0
for element in num_tuple:                    #it will print the elements in the tuple num_tuple one by one.
    if(element==x):
        print("The number is found at index: ",idx)
        break
    idx+=1