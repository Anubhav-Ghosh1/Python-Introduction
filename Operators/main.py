# Operators

# Arithmetic operators
x = 5
y = 2
print(x+y,x-y,x*y,x/y,x%y,x**y,x//2)

# // is interger division

# Comparision operator
# x < y x > y x <= y x >= y x == y x != y


# Logical operator
# and or not

# Bitwise
x = 2
y = 3
print(x & y) # x = 010 y = 011 = 0 1 0 = 2
print(x | y) # x = 010 y = 011 = 011 = 3
print(x >> 2) # right shift which is equivalent to dividing a with 2^b
print(x << 2) # left shift with 2^b (2 raised to power b)
print(~x)

# Identity operator used to check whether two variable are pointing to the same memory location
a = 3
b = 3
print(a is b) # True as they are pointing to the same memory location
print(a is not b) # False as they are pointing to the same memory location

# Membership operator
x = "Python"
a = [1,2,4,5,6]
print("P" in x)
print(1 in a)
print("P" not in x)