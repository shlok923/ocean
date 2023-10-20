
import csv                                                      #importing to read csv file
import matplotlib.pyplot as plt                                 #importing to plot graph
e=open("/home/shlok/Downloads/SOCR-HeightWeight.csv",'r')       #opening file in e
d=csv.reader(e)                                                 #read in d

h=[]                                   #height list                        
w=[]                                   #weight list
bmi=[]                                 #bmi list
for i in d:                            #adding data to height and weight list
    if i[1][0].isalpha()==False:       #using isalpha bacause first dataset has strings and give error otherwise
        h.append(float(i[1]))           
        w.append(float(i[2]))
for i in range(len(h)):                #adding to bmi list 
    bmi.append((w[i]/(h[i]**2))*703)   #bmi formula


plt.scatter(w,bmi,marker="*",s=0.01)   #plotting bmi v/s weight graph. it gives an almost linear correlation
plt.xlabel('Weight(In pounds)')        #labelling axes
plt.ylabel('BMI')
plt.show()                             #show graph
