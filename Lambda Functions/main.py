# lambda functions
# lambda input:expression
value = lambda a: a**2
print(value(2))

# Difference
# Lambda has no return value
# Type of lambda is function
# Lambda function is of one line
# There is no name associated with lambda function

# Why lambda function
# It is used along higher order functions
# Higher order function is a function that require another function or a function that returns a function

b = lambda a:a[0] == 'a'

b = lambda a: "True" if a%2 == 0 else "False"

def sum_func(func,List):
    result = 0

    for i in List:
        if func(i):
            result += i
    return result

a = lambda x:x%2 == 0
b = lambda x:x%2!=0
c = lambda x:x%3 == 0

List = [1,2,4,5,6]
print(a,List)
print(b,List)
print(c,List)

# Map
list_2 = list(map(lambda x:x*2,List))
print(list_2)

# Filter
list_3 = list(filter(lambda a:(a>4),List))

# Reduce
import functools
value = functools.reduce(lambda a,b:a+b,List);
print(value)