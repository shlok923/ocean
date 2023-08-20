n=int(input('Enter a no: '))
start=int(input('Start table from? '))
end=int(input('End table at? '))
for i in range(start,end+1):
    print(n,'X',i,'=',n*i,sep='')
