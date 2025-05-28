""" 

Title: Sum of Digits / Digital Root

📝 Description:
Given a non-negative integer, repeatedly sum all its digits until the result has only one digit.

Return that single-digit result.

📌 Function Signature:
python
Copy
Edit
def digital_root(n: int) -> int:
    pass
🧪 Examples:
python
Copy
Edit
digital_root(16)       # ➞ 7    (1 + 6 = 7)
digital_root(942)      # ➞ 6    (9 + 4 + 2 = 15 -> 1 + 5 = 6)
digital_root(132189)   # ➞ 6    (1 + 3 + 2 + 1 + 8 + 9 = 24 -> 2 + 4 = 6)
digital_root(493193)   # ➞ 2    (4 + 9 + 3 + 1 + 9 + 3 = 29 -> 2 + 9 = 11 -> 1 + 1 = 2)
💡 Notes:
Use loops or recursion.

Continue summing digits until only one digit remains.



"""

def digital_root(n: int) -> int:
    n = str(n)
    while len(n) > 1:
        m = [int(n[i]) for i in range(len(n))]
        n = str(sum(m))
    return n

if __name__ == "__main__":
    print(digital_root(16))  # Output: 7
    print(digital_root(1245)) # Output: 3
    print(digital_root(16))    # ➞ 7    
    print(digital_root(942))      # ➞ 6     
    print(digital_root(132189))   # ➞ 6     
    print(digital_root(493193))   # ➞ 2 
    print(digital_root(0))        # ➞ 0
    print(digital_root(999999999)) # ➞ 9
    print(digital_root(123456789)) # ➞ 9
    print(digital_root(1000000001)) # ➞ 2
    print(digital_root(9876543210)) # ➞ 9