#snake.py
n=int(input('No of lines: '))
c=float(input('Enter curvature: '))
for i in range(n):
    print(int(((n-i)**2)*c)*' ','*')
for i in range(1,n+1):
    print(int((i**2)*c)*' ','*')
