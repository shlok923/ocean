n=int(input('Enter a no: '))
for i in range(2,n+1):
    prime=True
    for j in range(2,int(i**(0.5)+1):
        if i%j==0:
            prime=False
    if prime==True:
        print(i)

