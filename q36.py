import random

n=int(input('Enter a no: '))    #taking input
l=[]                            #empty list
for i in range(n):              #adding n 'bins' to list, here rep by empty list
    l.append([])
for i in range(n):              #adding 'balls', here represented by 1
    a=random.randint(0,n-1)     #picking a random bin
    l[a].append(1)              #adding ball
count=0                         #count to count no of empty bin
for i in range(n):
    if l[i]==[]:                #checking empty bin
        count+=1                #adding to count 

def max_balls(l):               #to find max across any bin
    m=0                         #taking a variale
    for i in l:
        c=i.count(1)            #counting no of balls in bin
        if c>m:
            m=c                 #assigning amx to new max balls
        else:
            continue                     
    return m                    #return max 
prob=count/n                    #probability of bin being empty
print(f"Max no of balls in any bucket is {max_balls(l)}")        #output
print(prob)                   
