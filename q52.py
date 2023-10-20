def mergesort(l):               #make main mergesort function
    if len(l)<=1:               #if single or no element in list, return the same
        return l
    
    mid=len(l)//2               #middle of list
    left=mergesort(l[:mid])     #recursively sort left portion
    right=mergesort(l[mid:])    #recursively sort right portion
    
    return merge(left,right)    #return merged left and right; here every partition gets sorted 

def merge(a,b):                       #function to merge
    i=j=0                             #we'll use i to check elements of a and j for b
    merged_list=[]                    #list to put result into

    while i<len(a) and j<len(b):      #checking both lists
        if a[i]<=b[j]:                #if element of b greater than a, append element of a to result list
            merged_list.append(a[i])
            i+=1                      #move on to next element of a
        else:
            merged_list.append(b[j])  #same for b
            j+=1
    
    merged_list+=a[i:]                #appending any leftover elements to result
    merged_list+=b[j:]
    return merged_list                #returning merged list

l=[12,22,3,1,3,4323,0,56]
print(mergesort(l))

