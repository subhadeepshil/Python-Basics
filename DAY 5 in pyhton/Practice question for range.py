#1 Print the element of the following list using loop: [1,4,9,16,25,36,49,64,81,100]
for i in range(1,101):
    print (i)






#2 Search for a x in this tuple using loop: (1,4,9,16,25,36,49,64,81,100)
input=int(input("Enter the number you want to search: "))
for i in range(1,101):
    if i==input:
        print("Found")
        break




# #3 Print the multiplication table of a number using loop:
# input=int(input("Enter the number you want to search: "))
# for i in range(1,11):
#     print(input*i)