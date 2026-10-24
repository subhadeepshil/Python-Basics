#Recursion function meaning calling a function inside itself. It is used to solve problems that can be broken down into smaller subproblems of the same type.   


    
    #how we use recoursion to find factorial of a number

   
   #we can stop it with return statement
def show(n):
    if (n == 0):      # ":" It's a base case which is used to stop the recursion when n reaches 0. It prevents infinite recursion and allows the function to return a value or terminate gracefully.
        return
    print(n)
   
    show(n-1)              #  Output: 5   we can also get it from 4 = n-1, 3 =n-2, 2 = n-3, 1 = n-4, 0 = n-5
    print("END")

show(3)





#Recursion to factorial of a number
def factorial(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!

print(factorial(3))  # Output: 6