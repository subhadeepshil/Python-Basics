
#Using Break and Continue in While Loop

num= (1,4,6,16,25,36,49,64,81,100)
x= int(input("Enter a number to search: "))
i=0
while i < len(num):                    #it will search for the number x in the tuple num and print the index of the number if it is found, otherwise it will print "Number not found".
    if num[i] == x:
        print("Number found at index:", i)
        break                          # break is use for to end the loop when the number is found, so it will not continue to search for the number in the tuple.
    i += 1
print("End Of loop")    




# we can also use continue statement in while loop, it is used to skip the current iteration of the loop and move to the next iteration.

i=0
while i < 10:
    i += 1
    if i % 2 == 0:                    # it will print only the odd numbers from 1 to 10, because when i is even, it will skip the current iteration and move to the next iteration.
        continue
    print(i)
