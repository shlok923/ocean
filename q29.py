#for binary, check divide by 2 and add remainder in front
#for example, divide 100 continously by 2 and note down the remainders right to left, that is binary equivalent

a=int(input('Enter a no: '))
q=a                           #assigning a quotient which will be divided repeatedly
r=0
binary=''                     #making empty string for binary to concatenate remainders into 
while q>=1:                   #divide till quotient less than or equal to 1
    r=q%2                  
    binary+=str(r)            #concatenate to binary
    q=q//2
print('Binary equivalent of the no is: ',binary[::-1])   #print binary in reverse 
