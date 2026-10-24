#Range 
print (range(6))             #0,1,2,3,4,5


#Range with start and stop
seq=range(2,7)               #2,3,4,5,6
print (seq[0])               #2
print (seq[4])               #6
print (seq[-1])              #6
print (seq[1:4])             #3,4,5


for i in range(2,7):        #it will print from 2 to 6 (start to stop-1)
    print (i)                #2,3,4,5,6




for i in range(2,7,2):        #it will print from 2 to 6 (start to stop-1) with step of 2
    print (i)   





#it's also called linier search because it will search for the number in a linear way
for i in range(0,100):       #it will print from 0 to 99 (start to stop-1)
    print (i)                  #0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,


#we can also even numbers wit step of 2
for i in range(0,100,2):       #it will print from 0 to 99 (start to stop-1) with step of 2
    print (i)                  #0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,



#if we want odd numbers with step of 2
for i in range(1,100,2):       #it will print from 1 to 99 (start to stop-1) with step of 2
    print (i)                  #1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,