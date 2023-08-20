#Euclid gcd
#taking numbers
n1=int(input('Enter 1st no: '))
n2=int(input('Enter 2nd no: '))
#using euclid's algorithm, i.e., divide numbers and then further divide remainder and smaller number till 0 shows up. there, the number other than zero is divisor  
while n2>0:
    n1,n2=n2,n1%n2
print(n1,'is GCD of given numbers')
