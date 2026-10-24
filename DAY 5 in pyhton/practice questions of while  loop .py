#1 Print number 1 to 100 using while loop.
i=1
while i <= 100:                    #it will print the numbers from 1 to 100.
    print(i)
    i += 1




#2 Print number 100 to 1 using while loop.
i=100
while i >= 1:                    #it will print the numbers from 100 to 1 in reverse order.
    print(i)
    i -= 1


#3 Print multiple table of a number n using while loop.
n= int(input("Enter a number: "))
i=1
while i <= 10:                    #it will print the multiple table of the number n from 1 to 10.
    print(n*i)
    i += 1



#4 print number of the following list using loop. {1,4,6,16,25,36,49,64,81,100}
num= [1,4,6,16,25,36,49,64,81,100]
i=0
while i < len(num):                    #it will print the numbers in the list num.
    print(num[i])
    i += 1




#5 Search for number x in this tuple  (1,4,6,16,25,36,49,64,81,100) using while loop.

num= (1,4,6,16,25,36,49,64,81,100)
x= int(input("Enter a number to search: "))
i=0
while i < len(num):                    #it will search for the number x in the tuple num and print the index of the number if it is found, otherwise it will print "Number not found".
    if num[i] == x:
        print("Number found at index:", i)
        break                          # break is use for to end the loop when the number is found, so it will not continue to search for the number in the tuple.
    i += 1
 



