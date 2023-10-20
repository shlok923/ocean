#----------QUESTION1----------
import random
import time
from matplotlib import pyplot as plt

def linearSearch(l :list, n :int):
    for i in l:
        if i==n:
            return n
    return 'Not found'

def binarySearch(l :list,n :int):
    start=0
    end=len(l)-1
    mid=0
    while start<=end:
        mid = (end+start)//2
        if l[mid]<n:
            start=mid+1
        elif l[mid]>n:
            end=mid-1
        else:
            return mid
    return 'Element not found'
linearTime=[]
binaryTime=[]

#l=[8, 16, 26, 31, 33, 33, 33, 34, 37, 46, 48, 50, 62, 67, 79, 82, 92, 94, 96, 98]
#print(binarySearch(l,31))
'''
for i in range(2,7):
    l=[]
    length = 10**i
    for j in range(length-1):
        l.append(random.randint(1,length))
    n=random.randint(1,length)
    l.insert(random.randint(1,length),n)
    #print(l,n)
    t1=time.time()
    linearSearch(l,n)
    t2=time.time()
    binarySearch(l,n)
    t3=time.time()
    linearTime.append(t2-t1)
    binaryTime.append(t3-t2)
print(linearTime, binaryTime)
plt.plot([100,1000,10000,100000,1000000],linearTime)
plt.plot([100,1000,10000,100000,1000000],binaryTime)
plt.show()
'''

#----------QUESTION2----------

def fiboIterate(n):
    a=0
    b=1
    for i in range(n):        #running loop for n terms
        a,b=b,a+b             #exchanging variables after adding
    return b              #printing element

def fiboRecursion(n):
    if n<=1:
        return n
    return fiboRecursion(n-1) + fiboRecursion(n-2)
 
'''
recTime=[]
itTime=[]
for i in range(1,5):
    l=[]
    n = 10*i
    t1=time.time()
    fiboIterate(n)
    t2=time.time()
    fiboRecursion(n)
    t3=time.time()
    itTime.append(t2-t1)
    recTime.append(t3-t2)
print(itTime, recTime)
plt.plot([10,20,30,40],itTime,label='iteration')
plt.plot([10,20,30,40],recTime,label='recursion')
plt.legend()
plt.show()
'''

#----------QUESTION3----------

def bubble_sort(list1):
    """
    Perform bubble sort on a list and return the sorted list.

    Args:
        list1 (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(list1)
    for i in range(n):
        for j in range(0, n-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1

def quick_sort(list1):
    """
    Perform quicksort on a list and return the sorted list.

    Args:
        list1 (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    if len(list1) <= 1:
        return list1

    pivot = list1[len(list1) // 2]
    left = [x for x in list1 if x < pivot]
    middle = [x for x in list1 if x == pivot]
    right = [x for x in list1 if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

bubbleTime=[]
quickTime=[]
'''
for i in range(1,4):
    l=[]
    length = 100*i
    for j in range(length-1):
        l.append(random.randint(1,length))
    n=random.randint(1,length)
    l.insert(random.randint(1,length),n)
    t1=time.time()
    bubble_sort(l)
    t2=time.time()
    quick_sort(l)
    t3=time.time()
    bubbleTime.append(t2-t1)
    quickTime.append(t3-t2)
print(bubbleTime, quickTime)
plt.plot([100,200,300],bubbleTime)
plt.plot([100,200,300],quickTime)
plt.show()
'''

#----------QUEESTION4----------

def q4(l:list):
    lis = [l[0]]
    max = l[0]
    for i in l:
        if i>max:
            lis.append(i)
            max = i
    return lis

print(q4([10,22,9,33,21,50,41,60,80]))


























