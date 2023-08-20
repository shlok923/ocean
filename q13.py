str1=input('Enter a word: ')
str2=input('Enter another word: ')
out=''
if len(str1)==len(str2):
    for i in range(len(str1)):
        out+=str1[i]+str2[i]
    print(out)
else:
    print('Enter words of same length')
