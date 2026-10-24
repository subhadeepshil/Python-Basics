#No.9 Relational and logical operators in python
a=10
b=20


print(a==b)       #This will print False because a is not equal to b
print(a!=b)       #This will print True because a is not equal to b
print(a<b)        #This will print True because a is less than b
print(a>b)        #This will print False because a is not greater than b
print(a<=b)       #This will print True because a is less than or equal to b
print(a>=b)       #This will print False because a is not greater than or equal to b




#N0 .10 Assignment operators in python
a=10
a+=5     #10+5 is equivalent to a=a+5 which will add 5 to a and assign the result to a which is 15
print(a)     #This will print the value of a which is 15

num=20
num-=5     #20-5 is equivalent to num=num-5 which will subtract 5 from num and assign the result to num which is 15
print("num=", num)   #This will print the value of num which is 15





#No.11 Logical operators in python

a=50
b=30
print(not True)    #This will print False because not operator will negate the value of True which is False
print(not False)   #This will print True because not operator will negate the value of False which is True

print(not False)   #This will print True because not operator will negate the value of False which is True
print(not (a-b))  #This will print False because a-b is 20 which is not equal to 0 and not operator will negate the value of False which is True
print((a>b) and (b>10))   #This will print True because a is greater than b and b is greater than 10
print((a>b) or (b>10))    #This will print True because a is greater than b and b is greater than 10




val1=True
val2=False
print("and operator:", val1 and val2)   #This will print False because val1 is True and val2 is False and and operator will return True only if both operands are True otherwise it will return False
print("and operator:",(a==b) and (a>b)) # This will print False because a is not equal to b and a is not greater than b and and operator will return True only if both operands are True otherwise it will return False

val1=True
val2=True
print("and operator:", val1 and val2) # This will print True because val1 is True and val2 is True and and operator will return True only if both operands are True otherwise it will return False



val1=True
val2=False
print("or operator:", val1 or val2)   #This will print True because val1 is True and val2 is False and or operator will return True if at least one operand is True
print("or operator:",(a==b) or (a>b))# This will print True because a is not equal to b but b is greater than 10 and or operator will return True if at least one operand is True



val1=True
val2=True
print("or operator:", val1 or val2) # This will print True because val1 is True and val2 is True and or operator will return True if at least one operand is True