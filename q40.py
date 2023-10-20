def spiral():
    i=1                                       #variable to inc letters                  
    st=''                                     #string to concatenate to
    while len(st)<100000:                     #we have to do till 100000 letters. although this loop wont give us exavtly that, it stops close enough and we can string slice later
        st+=i*'R'+i*'U'+(i+1)*'L'+(i+1)*'D'   #the pattern
        i+=2                                  #inc variable by 2, to inc no o f letters by 2 in next iteration
    return st[0:100000]                       #return till 100000 letters
print(spiral())                               #call function
print(len(spiral()))                          #checking its length
