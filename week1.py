#-------------------------CONCEPT 1-------------------------

#QUESTION-1
def missing_no(l):
    l1=sorted(l)                          
    for i in range(len(l1)-1):          #check if each element is less than next element by 1, 
        if l1[i]==l1[i+1]-1:            #if not, there is an element missing
            pass
        else:
            return l1[i]+1
    return 'No no. was missing'
print(missing_no([0,1,2,3,4,6,7,8,9]))


#QUESTION-2
def rotate_list(l,k):
    for i in range(len(l)-k):
        pop=l.pop(0)                   #removing first element    
        l.append(pop)                  #adding it to end of list
    return l
print(rotate_list([0,1,2,3,4,5,6,7,8,9],5))


#QUESTION-3
def removing(l,r):
    l1=[]
    for i in l:
        if i!=r:
            l1.append(i)
    return l1
print(removing([0,1,2,3,4,5,6,7,8,9],6))

#-------------------------CONCEPT 2-------------------------

#QUESTION-1
def sumvalue(d):
    values=list(d.values())
    return sum(values)
print(sumvalue({'a':10,'b':20,'c':30}))


#QUESTION-2
def duplicate(s):
    sl=s.lower()
    d={}
    for i in sl:
        if i in d.keys():
            d[i]+=1
        else:
            d[i]=1
    return d
print(duplicate('trappraa'))


#QUESTION-3
def unique(d):
    val=list(d.values())
    keys=list(d.keys())
    most_unique_count=0
    most_unique_ind=0
    for i in val:
        l1=[]
        for j in i:
            if j not in l1:
                l1.append(j)
        if len(l1)>most_unique_count:
            most_unique_count=len(l1)
            most_unique_ind=val.index(i)
    return keys[most_unique_ind]
print(unique({"Python" : [5,7,9,0,0], "is":[6, 7, 4, 5, 3],"Best":[9,9,6,5,5]}))


#-------------------------CONCEPT 3-------------------------

#QUESTION-1
def max_min(t,k):
    l=sorted(list(t))
    out=[]
    for i in range(k):
        out.append(l[i])
        out.append(l[len(l)-i-1])
    return tuple(out)
print(max_min((3, 7, 1, 18, 9),2))


#QUESTON-2
def updating(l,n):
    for i in range(len(l)):
        a=[]
        for j in l[i]:
            a.append(j+n)
        l[i]=tuple(a)
    return l
print(updating([(1, 3, 4), (2, 4, 6), (3, 8, 1)],3))


#QUESTION-3
def remove_duplicate(t):
    l=[]
    for i in t:
        if i not in l:
            l.append(i)
    return tuple(l)
print(remove_duplicate((1, 3, 5, 2, 3, 5, 1, 1, 3)))

#-------------------------CONCEPT 4-------------------------

#QUESTION-1
def palindrome(s):
    pal=True
    for i in range(len(s)):
        if s[i]==s[len(s)-1-i]:
            pass
        else:
            pal=False
            break
    if pal==True:
        return 'A palindrome it is'
    else:
        return 'A palindrome it is not'
print(palindrome('noon'))


#QUESTION-2
def substring(s,ss):
    l=s.split(ss)
    return len(l)-1
print(substring('tCatBatSatFatOrt','t'))
