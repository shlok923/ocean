def find_max(l):               #defining func
    max=l[0]                   #assuming first element is max
    for i in l:                #checking if any other element larger than max    
        if i>max:              #assigning new max if so
            max=i              
        else:
            pass               
    return max                 #return max
l=[]                                                 #empty list
n=int(input('Enter no of elements of list: '))       #asking for no of elements
for i in range(n):                                   #taking n elements as input
    n=int(input('Enter element: '))
    l.append(n)                                      #adding to list
print('Max element of list is',find_max(l))          #output
