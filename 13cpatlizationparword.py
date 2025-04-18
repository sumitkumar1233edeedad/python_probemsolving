n = "How can mirrors be real if our eyes aren't real"
'''
par word capitalize method use in word than this will be easy way to  solve
ex:->
Input = "How can mirrors be real if our eyes aren't real"
output = "How Can Mirrors Be Real If Our Eyes Aren't Real"
'''
#n convert to the list
n = n.split()
#empty list 
m = []
print(n)
#loop use for per word capitalize use  
for i in n:
    m.append(i.capitalize())
#convert to string and add on space (' ') this method use in space add
print(' '.join(m))