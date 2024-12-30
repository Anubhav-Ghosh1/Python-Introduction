# Set
# Set do not allow duplicates
# Set have no indexing/slicing
# Set do not allow mutable data type
# Set is itself mutable

set_1 = set()
set_1 = {8,1,2,4,4,6} # {1, 2, 4, 6, 8} is due to hashing
print(set_1)

# Add element
set_1.add(100)
print(set_1)

set_1.remove(100)
print(set_1)
set_1.pop()
print(set_1)
# set_1.clear()
print(set_1)

set_2 = set()
set_2 = {1,100}

print("Difference",set_1.difference(set_2)) # returns differenct of both the set
print(set_1.union(set_2)) # returns union of the set
print(set_1.intersection(set_2)) # returns common element of the set
print(set_1.isdisjoint(set_2)) # return true if there is no common value