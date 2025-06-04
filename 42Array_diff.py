''' 
Title: Array.diff

📝 Description:
Your task is to implement a function that subtracts one list from another and returns the result.

It should remove all values from list a that are present in list b.
'''

def arr_detected(number, words):
    #compression use 
    m= [number[i] for i in range(len(number)) if number[i] not in words]
    
    #this method same but more line carry out
    # for i in range(len(number)):
    #     if number[i] in words:
    #         continue
    #     else:
    #         m.append(number[i])
            
    return m

if __name__ == "__main__":
    print(arr_detected([1, 2, 3, 4, 1,3, 4], [1, 3]))