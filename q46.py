#a=[[1,2,3],[2,3,4],[3,4,5]]                    #matrices to add
#b=[[3,4,5],[2,3,4],[1,2,3]]
dim=int(input('Enter dimension of your matrices: '))
mat1=[]
mat2=[]
for i in range(dim):
    mat1.append([])
    mat2.append([])
for i in range(2):
    for j in range(dim):
        for k in range(dim):
            ask='Enter values for matrix '+str(i+1)+' rowwise: '
            n=int(input(ask))
            if i==0:
                mat1[j].append(n)    
            else:
                mat2[j].append(n)


def matrix_sum(a,b):
    try:                                       #try this code
        dim=len(a)
        c=[]                                   #making matrix with as many rows as a and b to put sum into
        for i in range(dim):           
            c.append([])
        for i in range(dim):                   #sum of matrices
            for j in range(dim):
                c[i].append(a[i][j]+b[i][j])   #i is fix for a j loop, so 'i'th row is being appended. With another i iteration, another row will be filled  
        return c
    except IndexError:                         #if there is IndexError, i.e., matrices are not of equal length, return said message 
        return 'Matrices not equal length' 

ans=matrix_sum(mat1,mat2)                      #function call
print('\n Sum of entered matrices is:')
for i in ans:
    print(i)
