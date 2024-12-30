# while loop
a = 1
while a < 10:
    print(a)
    a+=1

# for loop
# range
list(range(1,11)) # 1 till 10
# range(5) by default start is 0
# if single number is passed it is assumed to be last element
# range(start,till,step)
# step is i++ or i += 2

for i in range(1,11):
    print(i)
for i in [1,2,4,5,6]:
    print(i)

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()