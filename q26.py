#divisibility check
a=int(input('Enter a no: '))
b=int(input('Enter another: '))
check=int(input('Enter no to check diisibility of: '))

#checking
if check%a==0 and check%b==0:                              
    print(check,'is divisible by',a,'and',b)
else:
    print(check,'is not divisible by given numbers')
    
