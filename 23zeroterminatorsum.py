"""
Mary's Puzzle Books: Zero Terminated Sum

Mary has another puzzle book, and it's up to you to help her out! This book is filled with zero-terminated substrings, 
and you have to find the substring with the largest sum of its digits. For example, one puzzle looks like this:

"72102450111111090"

Here, there are 4 different substrings: 721, 245, 111111, and 9. The sums of their digits are 10, 11, 6, 
and 9 respectively. Therefore, the substring with the largest sum of its digits is 245, and its sum is 11.

Write a function largest_sum which takes a string and returns the maximum of the sums of the substrings. 
In the example above, your function should return 11.

Notes:
- A substring can have length 0. For example, 123004560 has three substrings, and the middle one has length 0.
- All inputs will be valid strings of digits, and the last digit will always be 0.
"""
def zero_sum(s):
    # Replace all '0's with spaces to separate substrings
    
    s = s.replace("0", " ")
    # Split the string into substrings based on spaces
    s = s.split()
    
    if len(s) == 0:
        l = 0
    else:
    # Iterate over each substring
        m = 0
        l = []
        for i in range(len(s)):
            
            # Sum the digits of the current substring
            for j in range(len(s[i])):
                m += int(s[i][j])
            # Store the sum in the list
            l.append(m)
            m = 0
        l = max(l)
    # Return the maximum sum found
    return l

if __name__ == "__main__":
    s = "72102450111111090"
    print(zero_sum(s))