# given a list and n simply delete the n range above elemnt same in list than delete 
# ex:- l = [1, 2, 3, 4,1 , 3, 4]
# n = 1
# output :- [1, 2, 3, 4] acutal n above element remove in dublication delelte

words = [1, 2, 3, 1, 2, 1, 2,1, 3]
n = 2
lo = []
#duplication delete
for i in words:
    if i not in lo:
        lo.append(i)
print(lo)
# no_ = set(words)
# no_ = list(no_)
element_counter = []
#use for counter per element 
for i in range(len(lo)):
    element_counter.append(words.count(lo[i]))
print(element_counter)
#this one element delete for lo list location according delete how time remove this minimize list  and detele is  rev_words list
minimize = [i-n for i in element_counter]
print(minimize)
rev_words = words[::-1]
#how to remove element if counter above for the n number for all counter check any up than remove this
# #remove element if counter above n
for j in range( len(minimize)):
    #this how many time remove this element
    for k in range(minimize[j]):
        rev_words.remove(lo[j])
print(rev_words[::-1])
         
            
            
    

 