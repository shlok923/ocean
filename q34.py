def fact(n):
    if n==0:
        return 1       #point of termination
    else:
        p=n*fact(n-1)  #calling function inside function, recursion
        return p       #returning result
n=int(input('Enter a no: '))         #input
print(fact(n))                       #output
