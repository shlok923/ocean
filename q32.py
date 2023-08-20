import random
l=[]
n=int(input('How many elements should the list have? '))     #input for no of elements
for i in range(n):
    l.append(random.randint(1,1000))                         #adding random numbers to list
print(l)
