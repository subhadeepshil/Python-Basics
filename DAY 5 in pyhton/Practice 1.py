# Loops 
# There are two types of loops in Python: for loops and while loops.
# For loops are used to iterate over a sequence (such as a list, tuple, or string) or other iterable object.

count = 1
while count <=5:           #if we only write 
    print(count)           #while true: it will run forever, so we need to add a condition to stop the loop.
    count += 1


count = 2
while count <=5:           # it will print the even numbers from 2 to 5 because we are starting from 2 and adding 1 to it in each iteration, so it will print 2, 4 and then stop when it reaches 6 which is greater than 5.
    print("Hello")          
    count += 1

    i=1
    while i <= 100:                    #it will print my name 100 times and also print the i value which is the number of times it has printed my name.
        print("Subhadeep",i)
        i += 1


    i=5
    while i >= 1:                    #it will print the numbers from 5 to 1 in reverse order.
        print(i)
        i -= 1

print("End Loop")

  



#  i=5
#  while i <= 6:                    #it is make a infinite loop because the condition is always true, so it will keep printing the value of i which is 5.  
#  print(i)
#  i -= 