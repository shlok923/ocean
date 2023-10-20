import string
a=open('sherlock','r')
f=a.read()
new=''
for i in f:
    if i in string.ascii_letters:
        new+=i

print(new)
