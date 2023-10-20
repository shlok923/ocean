import csv
f=open("C:/Users/hp/Desktop/sensex.csv")    #open csv file
d=csv.reader(f)                             #read file in d
v=[]                                        #list for values of closing
for i in d:                                 #putting values to list
    if i[0][0].isalpha()==False:            #using isalpha because 1st row has alphabets
        v.append(float(i[4]))

#for max profit, buy at local minima and sell at local maxima
bal=100000                        #starting balance
i=0                               #variable for loop
while i<(len(v)-1):               #looping till end of list v
    #finding local minima
    while i<(len(v)-1):
        if v[i+1]<=v[i]:
            i+=1
        else:
            break
    mini=v[i]                     #value of local minima
    #finding local maxima
    while i<(len(v)-1):
        if v[i+1]>=v[i]:
            i+=1
        else:
            break
    maxi=v[i]                     #value of local maxima
    bal*=maxi/mini                #update balance such that we bought stock at local min and sold at local max
print("Final balance after trading is",bal)
