import function
print(function.is_even.__doc__) # returns documentation

def power(a=1,b=1): # default value
    return a**b

# positional argument
print(power(b=2,a=3))

# providing multiple input
def sum(*value): # *value will be tuple
    temp_sum = 0
    for i in value:
        temp_sum += i
    print("Sum ",temp_sum)

sum(2,4,6,8)