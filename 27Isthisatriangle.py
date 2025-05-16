""" 
Title: Is this a triangle?

Description:

Implement a function that accepts three integers a, b, c as arguments and returns True if they form a valid triangle. Otherwise, return False.

Function Signature:

def is_triangle(a: int, b: int, c: int) -> bool:
    pass

A triangle is valid if:

    The sum of any two sides must be greater than the third side.

Examples:

is_triangle(1, 2, 2)     # ➞ True
is_triangle(7, 2, 2)     # ➞ False
is_triangle(3, 4, 5)     # ➞ True
is_triangle(1, 10, 12)   # ➞ False

Constraints:

    All inputs are positive integers.

    The function must return a boolean (True or False).
"""

def is_triangle(a: int, b: int, c: int) -> bool:
    
    m =  (True if a+b > c and c+a > b and b+c > a else False)
    return m

if __name__ == "__main__":
    print(is_triangle(1, 2, 2))     # ➞ True
    print(is_triangle(7, 2, 2))     # ➞ False
    print(is_triangle(3, 4, 5))     # ➞ True
    print(is_triangle(1, 10, 12))   # ➞ False