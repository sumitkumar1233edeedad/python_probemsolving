""" 
Title: Counting Duplicates

📝 Description:
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that 
occur more than once in the input string.

The input string can be assumed to contain only alphabets (A-Z, a-z) and digits (0-9).

🧠 Goal:
You’re counting how many different characters (not how many times they repeat total) appear more than once, ignoring case.

📌 Function Signature:
python
Copy
Edit
def duplicate_count(text: str) -> int:
    pass
🧪 Examples:
python
Copy
Edit
duplicate_count("abcde")                # ➞ 0
# all characters appear only once

duplicate_count("aabbcde")              # ➞ 2
# 'a' and 'b' appear more than once

duplicate_count("aabBcde")              # ➞ 2
# 'a' and 'b' (case-insensitive) both appear twice

duplicate_count("indivisibility")       # ➞ 1
# 'i' appears 7 times, rest are unique

duplicate_count("Indivisibilities")     # ➞ 2
# 'i' and 's' appear multiple times

duplicate_count("aA11")                 # ➞ 2
# 'a' and '1' appear more than once

duplicate_count("ABBA")                 # ➞ 2
# 'a' and 'b' (case-insensitive)
"""

def counting(st):
    # Convert the string to lowercase to ensure case-insensitive comparison
    st = st.lower()
    # Create a list of all characters in the string
    word = [i for i in st]
    # Get a list of unique characters
    word1 = list(set(word))
    cout = 0
    # Count how many unique characters appear more than once
    for i in range(len(word1)):
        if word.count(word1[i]) >= 2:
            cout += 1
    return cout

if __name__ == "__main__":
    # Test cases to demonstrate the function
    print(counting("abcde"))                # Output: 0
    print(counting("aabbcde"))              # Output: 2
    print(counting("aabBcde"))              # Output: 2
    print(counting("indivisibility"))       # Output: 1
    print(counting("Indivisibilities"))     # Output: 2
    print(counting("aA11"))                 # Output: 2
    print(counting("ABBA"))                 # Output: 2

    # Additional test cases
    print(counting(""))                     # Output: 0 (empty string)
    print(counting("a"))                    # Output: 0 (single character)
    print(counting("1122334455"))           # Output: 5 (all digits repeated)
    print(counting("abcabcabc"))            # Output: 3 (a, b, c repeated)
    print(counting("xyzXYZ"))               # Output: 3 (x, y, z repeated, case-insensitive)
    print(counting("no duplicates"))        # Output: 2 (space and 'o' repeated)
    print(counting("111222333444555"))      # Output: 5 (all digits repeated)
    print(counting("AaBbCc"))               # Output: 3 (a, b, c repeated, case-insensitive)