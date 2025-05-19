""" 
Title: Find the Odd Int

Description:

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Function Signature:

def find_it(seq: list[int]) -> int:
    pass

🧪 Examples:

find_it([20, 1, 1, 2, 2, 3, 3, 5, 5])        # ➞ 20
find_it([4, 4, 5, 5, 5])                    # ➞ 5
find_it([10])                               # ➞ 10
find_it([1, 1, 2])                           # ➞ 2
find_it([0, 0, 0, 1, 1])                     # ➞ 0


"""

def find_it(number):
    m = set(number)
    m = list(sorted(m))
    count = [ number.count(m[i]) for i in range(len(m))]
    for i in count:
        if i%2 != 0:
            return m[count.index(i)]
             
  

if __name__ == "__main__":
    print(find_it([20, 1, 1, 2, 2, 3, 3, 5, 5]))        # ➞ 20
    print(find_it([4, 4, 5, 5, 5]))                    # ➞ 5
    print(find_it([10]))                               # ➞ 10
    print(find_it([1, 1, 2]))                           # ➞ 2
    print(find_it([0, 0, 0, 1, 1]))                     # ➞ 0

    # Additional test cases
    print(find_it([7, 7, 7, 7, 7]))                     # ➞ 7 (all odd count)
    print(find_it([2, 2, 3, 3, 4, 4, 4]))               # ➞ 4
    print(find_it([9, 8, 8, 9, 9]))                     # ➞ 9
    print(find_it([100, 200, 100, 200, 100]))           # ➞ 100
    print(find_it([-1, -1, -2, -2, -2]))                # ➞ -2
    print(find_it([0, 1, 0, 1, 0]))                     # ➞ 0
    print(find_it([42]))                                # ➞ 42
    print(find_it([5, 5, 5, 5, 5, 5, 5]))               # ➞ 5