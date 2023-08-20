sum=0                                   #variable for sum of marks 
for i in range(5):
    m=int(input('Enter your marks: '))  #taking marks
    sum+=m                              #adding marks
avg=sum/5                               #taking avg
grade=''                                #making variable for grade  
#checking
if avg>=90: 
    grade='A'
elif 80<=avg<90:
    grade='B'
elif 70<=avg<80:
    grade='C'
elif 60<=avg<70:
    grade='D'
else: 
    grade='F'
print('Your grade is',grade)            #printing grade            

