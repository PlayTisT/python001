# Operators

# =======================================
# Arithmetic Operators in Python
# =======================================
a = 7
b = 2

# addition
print ('Sum: ', a + b)  

# subtraction
print ('Subtraction: ', a - b)   

# multiplication
print ('Multiplication: ', a * b)  

# division
print ('Division: ', a / b) 

# floor division
print ('Floor Division: ', a // b)

# modulo
print ('Modulo: ', a % b)  

# a to the power b
print ('Power: ', a ** b)   

Sum: 9
Subtraction: 5
Multiplication: 14
Division: 3.5
Floor Division: 3
Modulo: 1
Power: 49


# =======================================
# Python Assignment Operators
# =======================================

# assign 10 to a
a = 10

# assign 5 to b
b = 5 

# assign the sum of a and b to a
a += b      # a = a + b

print(a)

# Output: 15


# =======================================
# Python Comparison Operators
# =======================================

a = 5
b = 2

# equal to operator
print('a == b =', a == b)

# not equal to operator
print('a != b =', a != b)

# greater than operator
print('a > b =', a > b)

# less than operator
print('a < b =', a < b)

# greater than or equal to operator
print('a >= b =', a >= b)

# less than or equal to operator
print('a <= b =', a <= b)

a == b = False
a != b = True
a > b = True
a < b = False
a >= b = True
a <= b = False

# =======================================
#Python Logical Operators
# =======================================
a = 5
b = 6
print((a > 2) and (b >= 6))    # True

# logical AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical NOT
print(not True)          # False

# =======================================
# Python Bitwise operators
# =======================================
# example, 2 is 10 in binary, and 7 is 111.
# In the table below: Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)
#----------------------------------------------
# Operator	/  Meaning	/  Example
#----------------------------------------------
&	    /       Bitwise AND	x & y = 0 (0000 0000)
|     /     	Bitwise OR	x | y = 14 (0000 1110)
~	    /       Bitwise NOT	~x = -11 (1111 0101)
^	    /       Bitwise XOR	x ^ y = 14 (0000 1110)
>>	  /       Bitwise right shift	x >> 2 = 2 (0000 0010)
<<	  /       Bitwise left shift	x 0010 1000)

# =======================================
# Python Special operators
# =======================================
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # prints False
print(x2 is y2)  # prints True
print(x3 is y3)  # prints False

# =======================================
# Membership operators
# =======================================
message = 'Hello world'
dict1 = {1:'a', 2:'b'}

# check if 'H' is present in message string
print('H' in message)  # prints True

# check if 'hello' is present in message string
print('hello' not in message)  # prints True

# check if '1' key is present in dict1
print(1 in dict1)  # prints True

# check if 'a' key is present in dict1
print('a' in dict1)  # prints False

# oUTPUT 
True
True
True
False

#==========================================


