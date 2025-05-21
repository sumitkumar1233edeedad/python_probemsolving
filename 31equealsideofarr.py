""" 
Equal Sides Of An Array
📝 Description:

You are given an array of integers. Your task is to find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N.

If there is no such index, return -1.

If there are multiple such indexes, return the lowest one.
📌 Function Signature:

def find_even_index(arr: list[int]) -> int:
    pass

🧪 Examples:

find_even_index([1,2,3,4,3,2,1])       # ➞ 3
# left: [1,2,3] → sum = 6
# right: [3,2,1] → sum = 6

find_even_index([1,100,50,-51,1,1])   # ➞ 1
# left: [1] → sum = 1
# right: [50, -51, 1, 1] → sum = 1

find_even_index([1,2,3,4,5,6])         # ➞ -1
# no index has equal left/right sum

find_even_index([20,10,30,10,10,15,35]) # ➞ 3

find_even_index([0,0,0,0,0])           # ➞ 0
# all are zero, any index works, return first (0)

find_even_index([10,-80,10,10,15,35,20]) # ➞ 6n

"""

def find_even_index(s):
    """
    Finds the index N where the sum of the integers to the left of N 
    is equal to the sum of the integers to the right of N.
    Returns the lowest such index, or -1 if no such index exists.
    """
    mid = int(len(s)/2)
    # Special case: all elements are zero
    if len(set(s)) == 1 and s[0] == 0:
        return 0 
    # Odd length array
    elif len(s)%2 != 0:
        left_s = [s[i] for i in range(mid)]
        right_s = [s[i] for i in range(mid+1,len(s))]
        right_s = right_s[::-1]
        if sum(left_s) == sum(right_s):
            return len(left_s)
        # Special case for length 3
        elif len(s) == 3:
            left_s = [s[i] for i in range(mid+1)]
            right_s = [s[i] for i in range(mid+1,len(s))]
            if sum(left_s) == sum(right_s):
                return len(left_s)
        else:
            t = 0
            for i in range(len(left_s)): 
                if left_s[i]  == right_s[i]:
                    t += 1
                else:
                    if t == 0:
                        t = -1
            return t
    # Even length array
    else:
        left_s = [s[i] for i in range(mid)]
        right_s = [s[i] for i in range(mid,len(s))]
        right_s = right_s[::-1]
        if sum(left_s) == sum(right_s):
            return len(left_s)
        else:
            t = 0
            for i in range(len(left_s)): 
                if left_s[i]  == right_s[i]:
                    t += 1
                else:
                    if t == 0:
                        t = -1
            return t 

if __name__ == "__main__":
    # Test cases
    print(find_even_index([1,2,3,4,3,2,1]))         # ➞ 3
    print(find_even_index([1,100,50,-51,1,1]))      # ➞ 1
    print(find_even_index([1,2,3,4,5,6]))           # ➞ -1
    print(find_even_index([20,10,30,10,10,15,35]))  # ➞ 3
     
    print(find_even_index([0,0,0,0,0]))             # ➞ 0
    print(find_even_index([1,-1,0]))                # ➞ 2
    print(find_even_index([2,4,2]))                 # ➞ 1
    print(find_even_index([1,2,1,2,1,2,1]))         # ➞ 3
    print(find_even_index([1]))                     # ➞ 0