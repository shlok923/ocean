def fibonacci(n):
    a=0                    #starting values
    b=1
    for i in range(n-1):   
        a,b=b,a+b          #fibonacci sequence
    return b               #returning nth term

n=int(input('Enter a no: '))  #input
print(fibonacci(n))           #output
