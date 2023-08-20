age=int(input('Enter your age: '))     #taking age
#checking conditions
if age<18:
    print('You are a minor')
elif 18<=age and age<65:
    print('You are an adult')
else:
    print('You are a senior citizen')
