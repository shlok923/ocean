import random

def is_empty(l):                      #func to check if any bin is empty
    empty=False                       #assuming no bins arre empty
    for i in l:                       
        if i==[]:                     #if empty bin found, set empty to be true and break loop
            empty=True
            break 
    return empty                      #return whether empty or not

l=[]                                  #empty list
n=int(input('Enter a no: '))          #input
for i in range(n):                    #adding input no of bins
    l.append([])
count=0                               #variable to count no of balls 
while is_empty(l):                    #looping till there's an empty bin
        a=random.randint(0,n-1)       
        l[a].append(1)                #adding ball to random bin
        count+=1                      #counting ball
print('No of balls required to fill each bin is',count)          #output
