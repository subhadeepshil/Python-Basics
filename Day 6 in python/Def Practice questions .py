#WAF to print the length of list.(List is the parameter of the function)
list1=["kolkata","Mumbai","Pune","Delhi"]
list2=["4","2","5","1","8"]
def calculate_length(list1):
    length = len(list1)
    return length

print(calculate_length(list1))  # Output: 4
print(calculate_length(list2))  # Output: 5





#WAF to print the elements of a list in a single line.(List is the parameter of the function)

print(list1[0], end=" ")  # Output: kolkata
print(list2[1], end=" ")  # Output: 2
print(list1[2], end=" ")  # Output: Pune
print(list2[3], end=" ")  # Output: 1

#we can also start loop
def print_list_elements(list):
    for item in list:
        print(item, end=" ")
print_list_elements(list1)  # Output: kolkata Mumbai Pune Delhi
print_list_elements(list2)  # Output: 4 2 5 1 8




#WAF to find the factorial of n.(n is the parameter of the function)

n=5
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

print(calculate_factorial(n))  # Output: 120




#WAF to convert USD to INR.

int_usd = float(input("Enter the amount in USD: "))
def convert_usd_to_inr(usd):
    rate= 96  # 1 USD = 96 INR (example exchange rate)
    inr= usd*rate
    return inr

print(convert_usd_to_inr(int_usd))  # Output: 9600.0