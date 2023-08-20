v=['a','e','i','o','u']
c=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
w=input('Enter a word: ')
n=w.lower()
vowel=0
consonant=0
other=0
for i in n:
    if i in v:
        vowel+=1
    elif i in c:
        consonant+=1
    else:
        other+=1
print('There are ',vowel,' vowel(s), ',consonant,' consonant(s) and ',other,' others',sep='') 
