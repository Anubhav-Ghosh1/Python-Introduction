# Dictionary

# Dictionary has not indexing
# Dictionary is a mutable data type
# Keys should be immutable and value can be mutable
# Keys should be unique

dict_1 = {"Name":"Python","Age":21}
print(dict_1)

# Update
dict_1["Name"] = "Python_1" # {"Name":"Python_1","Age":21}

print(dict_1)

# Delete
del dict_1["Name"] # {"Age":21}

print(dict_1)

for i in dict_1:
    print(dict_1[i]) # returns value
    print(i) # returns key