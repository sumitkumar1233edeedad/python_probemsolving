""" 

Title: Persistent Bugger

Description:

Write a function, persistence, that takes in a positive integer
and returns its multiplicative persistence, which is the number 
of times you must multiply the digits in the number until you reach
a single digit.

Function Signature:

python
Copy code
def persistence(n: int) -> int:
    pass
What is multiplicative persistence?

It’s the number of times you must repeatedly multiply the digits 
of a number until you’re left with a single-digit number.

Examples:

python
Copy code
persistence(39)    # ➞ 3  → 3*9 = 27 → 2*7 = 14 → 1*4 = 4
persistence(4)     # ➞ 0  → already a single digit
persistence(25)    # ➞ 2  → 2*5 = 10 → 1*0 = 0
persistence(999)   # ➞ 4

"""

def persistence(n):
    n = str(n)
    if len(n) == 1:
        return 0
    else:
        count = 0
        while int(n) >= 10:
            d = [int(i) for i in str(n)]
            pro = 1
            for m in d:
                pro *= m
            n = pro
            count += 1                
            
        return count
    
if __name__ == "__main__":
    print(persistence(999))    # Output: 4
    print(persistence(39))     # Output: 3
    print(persistence(4))      # Output: 0
    print(persistence(25))     # Output: 2
    print(persistence(77))     # Output: 4
    print(persistence(123))    # Output: 1
    print(persistence(1))      # Output: 0
    print(persistence(10))     # Output: 1
    print(persistence(444))    # Output: 3
    print(persistence(222))    # Output: 3
    print(persistence(0))      # Output: 0
    print(persistence(11))     # Output: 1
    print(persistence(9999))   # Output: 4
    print(persistence(6788))   # Output: 6