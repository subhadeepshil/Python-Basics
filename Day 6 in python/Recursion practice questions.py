#Write a recursive function to calculate the sum of first n natural number
def calculate_sum(n):
    if n ==0:
        return 0
    else:
        return n + calculate_sum(n-1)
    
print(calculate_sum(5))  # Output: 15 (1 + 2 + 3 + 4 + 5 = 15)    







#Write a recursive function to print all elements in a list. HINT:Use list & Index as parameter in function.

def print_elements(lst, index=0):
    if index>=len(lst):
        return
    print(lst[index])
    print_elements(lst, index+1)

Country = ["India", "USA", "UK", "Australia"]
print_elements(Country)  # Output: India, USA, UK, Australia (each on a new line)