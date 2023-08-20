ch=int(input('''What conversion do you want?
1. C to F
2. F to C
Enter choice: '''))
t=int(input('Enter temperature: '))
if ch==1:
    print('Temp in F is', t*1.8+32)
elif ch==2:
    print('Temp in C is', ((t-32)*5)/9)
else:
    print('Enter a valid choice')
