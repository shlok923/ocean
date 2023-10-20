def is_even(n):              #defining func    
    if n%2==0:               #checking if even
        return True          #return true if even
    else:                
        return False         #return false otherwise
n=int(input('Enter no: '))   #input

if is_even(n)==True:         #print even no if true returned
    print('Even no.')
else:
    print('Odd no.')         #print odd otherwise
