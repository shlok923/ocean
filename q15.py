w=input('Enter a word: ')
pal=True
for i in range(len(w)):
    if w[i]==w[len(w)-1-i]:
        pass
    else:
        pal=False
        break
if pal==True:
    print('A palindrome it is')
else:
    print('A palindrome it is not')
