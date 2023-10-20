import string

def textstrip(filename):
    '''This takes the file and converts it to a string with all the spaces and other
    special characters removed. What remains is only the lower case letters,
    retain only the lowercase letters!
    '''
    f=open(filename,'r')                    #open file in f
    s=f.read()                              #read in s
    ns=''                                   #variable to store stripped string
    for i in s:                           
        if i in string.ascii_lowercase:     #if element of s lowercase, add to ns 
            ns+=i                                    
    return ns                               #return stripped string

def letter_distribution(s):
    '''Consider the string s which comprises of only lowercase letters. Count
    the number of occurrences of each letter and return a dictionary'''
    d={}                    #dictionary to append result into
    for i in s:             #for every element in string
        if i in d.keys():   #if element already in dict, add to its value
            d[i]+=1
        else:
            d[i]=1          #if not, make its key-value pair
    return d                #return dict

def substitution_encrypt(s,d):
    '''encrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    ns=''          #result variable
    for i in s:    #for every element in s
        ns+=d[i]   #add i's dictionary equivalent to ns
    return ns      #return encrypted string

def substitution_decrypt(s,d):
    '''decrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    ns=''                  #result variable
    k=list(d.keys())       #list of dictionary keys
    v=list(d.keys())       #list of dictionary values
    for i in s:            #for element in s,
        ns+=k[v.index(i)]  #check its index in v, and add its corresponding key to ns
    return ns              #return decrypted string

def cryptanalyse_substitution(s):
    '''Given that the string s is given to us and it is known that it was
    encrypted using some substitution cipher, predict the d''' 
    letters=letter_distribution(s) #make dict of letter distribution of s            
    d={}                           #result variable 
    #letter frequency in english
    repeating_order=['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']
    #key, value and sorted value lists of letter distribution dictionary
    k, v, sortv=list(letters.keys()), list(letters.values()), sorted(list(letters.values()))[::-1]
    
    j=0                              #to iterate through repeating order
    for i in sortv:                  #for element in sorted values
        ind=v.index(i)               
        d[k[ind]]=repeating_order[j] #add corresponding key-value pair to d
        j+=1                         #go to next frequent letter
    return d                         #return resultant dictionary

def vigenere_encrypt(s,password):
    '''Encrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    
    #to make pass length same as string
    p=list(password)                 #make list of elements of pass
    pas=''                           #string to store repeated pass in
    i=0                              #for case where i exceed length of key, we use this.                                                      
    while len(pas)<len(s):           #loop till lengths same
        if i==len(p):                #if length of p and i become equal, set i to 0
            i=0
        else:
            pas+=p[i]                #else, keep adding elements to pas
            i+=1                     #go to next element
            
    letters=list(string.ascii_lowercase)  #letters list
    out=''                                #result variable
    #method of vigenere encryption
    for i in range(len(s)):               
        pi=letters.index(pas[i])
        si=letters.index(s[i])
        out+=letters[(pi+si)%26]
    return out                     #return encrypted string

def vigenere_decrypt(s,password):
    '''Decrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    
    #again making pass length same as string
    p=list(password)                
    pas=''                            
    i=0
    out=''
    while len(pas)<len(s):
        if i==len(p):
            i=0
        else:
            pas+=p[i]
            i+=1
    letters=list(string.ascii_lowercase)
    
    #method of vigenere decryption
    for i in range(len(s)):
        pi=letters.index(pas[i])
        ei=letters.index(s[i])
        out+=letters[(ei-pi)%26]
    return out                       #return decrypted string

def rotate_compare(s,r):
    '''This rotates the string s by r places and compares s(0) with s(r) and
    returns the proportion of collisions'''
    rotateds=(" "*r)+s       #rotated string
    t=0                      #collision count
    for i in range(len(s)):  
        if s[i]==rotateds[i]:#check for collision, add to count if found
            t+=1
    return t/len(s)          #return no of collision divided by total string length, i.e., proportion


def cryptanalyse_vigenere_afterlength(s,k):
    '''Given the string s which is known to be vigenere encrypted with a
    password of length k, find out what is the password'''
    l=[]                      #to make list of s elements
    pasw=''                   #password variable
    for i in s:               #converting string to list
        l.append(i)
    for u in range(k):        #loop k times for k boxes.
        box=[]                #box for every nth letter. 
        for i in range(len(l)):        #to add nth element to list
            if ((k*i)+u)>=len(l):      #stopping loop if it exceeds the given loop 
                    break
            box.append(l[(k*i)+u])     #appending values with interval of password length
        boxs=''                    #empty string
        for i in range(len(box)):    #converting list to string
            boxs+=box[i]
        #print(boxs)
        ld=letter_distribution(boxs)   #checking the distribution of letters in the string and taking the result in a dictionary
        print(ld)
        maxi=sorted(list(ld.values()))[-1]        #max occurence values
        val=list(ld.values())           #list of dict values
        keys=list(ld.keys())            #list of dict keys
        #find index of maximum occurence in val, ang give corresponding val element. This will be max occuring letter
        e=keys[val.index(maxi)]
        letters=string.ascii_lowercase  #a to z list
        ind=(letters.index(e)-letters.index('e'))%26  #reverse vigen formula key to find password letter 
        pasw+=letters[ind]
    return pasw
def cryptanalyse_vigenere_findlength(s):
    '''Given just the string s, find out the length of the password using which
    some text has resulted in the string s. We just need to return the number
    k'''
    assume_key_len=1                           #assume length of key to be 1
    #we use prob in this. if at a certain rotation shift, probability of collision comes out to be more than 0.06, that will be key length
    prob=0                                     #prob check variable
    passlen=0                                  #reuslt variable
    while prob<0.06:                           #run till prob >0.06
        prob=rotate_compare(s,assume_key_len)  #chec prob at shift
        if prob>0.06:
            passlen=assume_key_len             #if prob>0.06, it is key length
            break 
        else:
            assume_key_len+=1                  #else, add shift by 1
    return passlen                             #return output

def cryptanalyse_vigenere(s):
    '''Given the string s cryptanalyse vigenere, output the password as well as
    the plaintext'''
    k=cryptanalyse_vigenere_findlength(s)               #finding the length of password
    password=cryptanalyse_vigenere_afterlength(s,k)     #finding the password used for encryption
    decrypt=vigenere_decrypt(s,password)                #putting the decrypted string in decrypt variable
    return (password,decrypt[:1000])

#Code Check
#d={}
#for i in range(len(string.ascii_lowercase)):
#    d[string.ascii_lowercase[i]]=string.ascii_uppercase[i]
#a=open('english_random','r')
#red=a.read()
#enc=vigenere_encrypt(red,'hue')
#print(cryptanalyse_vigenere(enc))

