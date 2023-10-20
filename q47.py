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


def matrix_multiply(a,b):
    try:
        c=[]                           #empty list to put product into
        for i in range(len(a)): 
            c.append([])               #adding as many 0's as there are elements in a and b  
            for j in range(len(a)):
                c[i].append(0)
        for i in range(len(a)):        #multiplication of matrices
            for j in range(len(a)):    
                for k in range(len(a)):
                    c[i][j]+=a[i][k]*b[k][j]      #multiply 'i'th row with 'j'th column and, that is term Cij of product matrix 
        return c
    except IndexError:                            #if there is IndexError, i.e., matrices are not of equal length, return said message
        return 'Matrices are not of same length'
print(matrix_multiply(mat1,mat2))                       #function call 

