# String creation
str = "Python"

str_1 = "'Python'" # Output 'Python'

str_2 = '"Python"' # Output "Python"

# str_3 = str("Python") # Output Python

# Accessing substring

str = "Python"
print(str[0])
# Positive Indexing left to right
# Negative Indexing right to left
print(str[-1])

# Slicing
print(str[0:4]) # This will return string from 0 to 3
print(str[2:]) # From 2 it will return rest of the string
print(str[:4]) # From 0 to 3
print(str[:]) # This will return the whole string

# str[start:till-1:step-1]

# Reverse a string
print(str[::-1])

# String are immutable
str = "Python"
del str

# Operations in string

# Concatination
print("String " + "Python")

# Loop
str = "Python"
for i in str:
    print(i)

# String function

# len
len(str) # returns length of the string

# max
max(str) # returns max character in string based on ascii

# min
min(str) # returns min character in string based on ascii

# sort
sorted(str) # returns list of elements in sorted order
sorted(str,reverse=True) # returns list of elements in decreasing order

# Capitalize
str.capitalize() # returns first character as capital and rest same

# Title
str.title() # It will make all the word first letter as capital

# Upper
str.upper() # returns string containing capital letters

# Lower
str.lower() # returns string containing lower characters

# Count
"Python".count("i") # returns frequency

# Find
"Python".find("P") # returns first occurance of the character else -1 is the character is not present

# Index
"Python".index("P") # returns the first occurance of the character else will throw error if character is not found

# Endswith
str.endswith("n") # returns true or false

# Startswith
str.startswith("P") # returns true or false

# Format
str = "Hello my name is {} and I am a {} developer".format("Python","Python")
str = "Hello my name is {1} and I am a {0} developer".format("Python","Python")
str = "Hello my name is {name} and I am a {technology} developer".format(name = "Python",technology = "Python")
print(str)

# isalnum
str.isalnum() # returns if string is alphanumeric
str.isalpha() # returns true if string contains alphabets
str.isdecimal() # return true if string contains numbers
str.isdigit() # return true if string contain digit
str.isidentifier() # returns true if string is a valid varaible name

# Split
"Hi I am Python".split() # returns list of elements output ['Hi','i','am','python']
str = "Hi I am Python".split("P") # returns list of elements containing ['Hi','I','ython']

# Join
str = ["Hi","I","am","Python"]
str = " ".join(str) # Output Hi I am Python
print(str)

# Replace
"Hi I am Python".replace("Python","Python1")

# Strip
"Hi I am Python ".strip() # removes leading and trailing spaces