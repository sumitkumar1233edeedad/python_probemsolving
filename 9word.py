l = ['a', 'b', 'c']#this is use input in code
for i in range(len(l)):
    #actual i is start for zero than use i+1
    m = i+1
    #list per item add chang
    l[i] = f'{m}: {l[i]}'
    
print(l)#["1: a", "2: b", "3: c"] output