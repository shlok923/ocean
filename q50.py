def change(s,L):             #to change coordinates according to clockwise and anti-clockwise. 
	cs=''                    #for example, for clockwise D-L are exchanged 
	for i in s:              #if even index, add next element to new string. otherwise, add previous element   
		ind=L.index(i)       #check index of element 
		if ind%2==0:
			cs+=L[ind+1]
		else:
			cs+=L[ind-1]
	return cs                #return changed string

def anticlock(s):            #anticlock rotate function 
	L=['L','U','D','R']      # L-U and D-R interchange
	return change(s,L)

def clock(s):
	L=['R','U','D','L']      # R-U and D-L interchange
	return change(s,L)

def dir_pattern(n: int):         #main directional pattern function
	pattern='DRU'            #starting point
	i=1                      #variable for loop
	if n==1:                 #return starting pattern for n=1
		return pattern
	else:
		while i<n:           
		   i+=1
		   pattern=anticlock(pattern)+'D'+pattern+'R'+pattern+'U'+clock(pattern)     #else, algorithm is to rotate anticlock, connect to original, connect to original, connect to clock
	return pattern                                                                   #return resultant pattern

def sfc(n):                                #main function
    s=dir_pattern(n)
    L=[(1,1)]                              #starting point
    x=L[len(L)-1][0]                       #x-coord of last element of list
    y=L[len(L)-1][1]                       #y-coord of last element of list
    for i in s:                            #changing coords according to directions and appending to output list 
        if i=='D':
            L.append((x+1,y))
        elif i=='R':
            L.append((x,y+1))
        elif i=='U':
            L.append((x-1,y))
        elif i=='L':
            L.append((x,y-1))
        x=L[len(L)-1][0]                  #redefining x and y to be last elements again 
        y=L[len(L)-1][1]
    return L		                          #return list of tuples



n=int(input('Enter a number: '))          
print(sfc(n))

