""" 
Title: Mumbling

Description:

This time no story, no theory. The examples below show you how to write the function accum:

The parameter of the function is a string, which contains only letters from a..z and A..Z like "abcd" or "RqaEzty".

The function should return a string where each character is repeated a number of times based on its position in the string (starting from 0), with the first letter capitalized and the rest lowercased, joined together with hyphens (-).

Examples:

accum("abcd")       # ➞ "A-Bb-Ccc-Dddd"
accum("RqaEzty")    # ➞ "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")       # ➞ "C-Ww-Aaa-Tttt"

"""
def convert(st):
    # Initialize an empty string to build each repeated character sequence
    re = ''
    # Convert the input string into a list of characters
    st1 = [i for i in st]
    # List to store the final formatted parts
    l = []
    # Create a list of numbers from 1 to length of the string
    number = [i+1 for i in range(len(st))]
    # Loop through each character in the string
    for j in range(len(st1)):
        # Repeat the character (j+1) times
        for i in range(len(number)):
            re += st1[j]
        # Add the repeated character sequence to the list
        l.append(re)
        # Reset the temporary string for the next character
        re = ''
    # Capitalize the first letter and lowercase the rest for each part
    l = [i.capitalize() for i in l]
        
    # Join all parts with hyphens and return the result
    return '-'.join(l)
     
             
    
if __name__ == "__main__":
    test_cases = [
        "abcd",
        "RqaEzty",
        "cwAt",
        "",                # Empty string
        "A",               # Single character
        "xyz",             # Lowercase only
        "XYZ",             # Uppercase only
        "aBcDeF",          # Mixed case
        "helloWorld",      # Longer mixed case
        "Python3",         # Contains a digit (should ideally be only letters)
        "a"*10,            # Repeated single character
    ]
    for st in test_cases:
        print(convert(st))
    