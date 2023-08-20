y=int(input('Enter an year:'))
leap=True
if y%4==0:
    if y%100==0:
        if y%400!=0:
            leap=False
else:
    leap=False
if leap==True:
    print('It is a leap year')
else:
    print('It is not a leap year')
