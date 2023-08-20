n=int(input('Enter a no: '))
prime=True
for i in range(2,int(n**(1/2)+1)):
    if n%i==0:
        prime=False
        break
if prime==True:
    print("Entered no is a prime")
else:
    print("Entered no is not a prime")
