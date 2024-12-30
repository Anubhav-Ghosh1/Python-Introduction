# List
# List can be hetrogenous
# Value might not be stored in contagious memory location

list_1 = [100,"Python"]
list_2 = [100,list_1]

# Access element in list
print(list_1[0])

# Access 4 from list_3
list_3 = [1,2,[4,5]]
print(list_3[2][0]) # list_3[2] = [4,5]

list_4 = [[[1,2],[4,5]],[[6,7],[8,10]]]
print(list_4[1][1][1])

# Updating value
list_1[0] = 1000
print(list_1)

# Add value
# Append add one value to the list
# extend adds multiple value in the list
# insert adds element in position list_1.insert(index,value)

# Remove value
# del value_1
# del list_1[0]
# list_1.remove(value)
# list_1.pop() removes right most element
# list_1.clear() removes all the values

# Operations
# list_1 + list_2 new list containing all the value of list_1 and list_2

# Implement title function
str = "hi i am a python developer"
str_1 = str.split(" ")
str_4 = list()
print(str_1)
for i in str_1:
    value = i[0].upper()
    i = value + i[1:]
    str_4.append(i)
str_2 = " ".join(str_4)
print(str_2)

str = "iamanubhav11@gmail.com" # output should be iamanubhav
index = str.find("@")
print(str[0:index])