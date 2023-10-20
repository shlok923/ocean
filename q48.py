f=open('/home/cslab/shlok/files/Q48.txt','w')  #opening file in f

n=int(input('Enter a no: '))                   #taking input for n

for i in range(1,n+1):                        
    f.write(str(i)+'\n')                       #writing numbers 1 to n in file with a newline character 
f.close()                                      #closing file
