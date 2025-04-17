#input = 'success' output = ")())())"
#use any string input than this one convert this condition according give the answer
n = 'success'
#co use  for the count the par element
co = 0
# re use for the "(" ")" add on the string in condition according
re = []
#for loop use in n
for i in range(len(n)):
    #par element n count
    co = n.count(n[i])
    #if no duplicate than this condition use and space 
    if co == 1 or co == " ":
        re.append("(")
    #duplicate element than this one use
    else:
        re.append(")")
#than last is your result
print(''.join(re))