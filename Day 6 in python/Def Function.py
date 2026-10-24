# a= 5 
# b= 10

# sum = a+b


# #more lines of code

# a= 6 
# b= 1

# sum = a+b

# #more lines of code

# a= 7
# b= 23

# sum = a+b


#it will repeat the same process for different values of a and b, calculating their sum each time.
#But we can use a function to avoid repeating the same code and make it more efficient.

def calculate_sum(a, b):          #calculate_sum is a name of the function, a and b are parameters
    sum = a + b
    return sum                    #return statement is used to return the value of sum, without this the function will return None

print (calculate_sum(5,10))      # Output: 15


#how will it help in my code
#we can call the function with different values of a and b, and it will return the sum of those values without repeating the same code.
calculate_sum(6,1)                 # Output: 7
print (calculate_sum(6,1))        # Output: 7


calculate_sum(7,23)                # Output: 30
print (calculate_sum(7,23))       # Output: 30



#we can use and make a cal calculator with this

def calculate_sum2(a, b):        #calculate_sum2 is a name of the function, a and b are parameters
    sum = a * b                  #for this function we are calculating the product of a and b instead of sum
    return sum



calculate_sum2(5,10)              # Output: 50
print (calculate_sum2(5,10))     # Output: 50


def calculate_sum3(a, b): 
    sum = a - b                  #for this function we are calculating the difference of a and b instead of sum
    return sum


def calculate_sum4(a, b): 
    sum = a / b                  #for this function we are calculating the quotient of a and b instead of sum
    return sum



calculate_sum3(10, 5)             # Output: 5
print (calculate_sum3(10, 5))    # Output: 5

calculate_sum4(10, 5)             # Output: 2.0
print (calculate_sum4(10, 5))    # Output: 2.0


#we can also print strings

def print_hello():                 #we can also create a function that prints a string, in this case "Hello, World!"
    print("Hello, World!")


print_hello()                       # Output: Hello, World!




#average of 3 numbers
def calculate_average(a, b, c):
    average = (a + b + c) / 3
    return average

print(calculate_average(5, 10, 15))  # Output: 10.0