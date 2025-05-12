""" 
        Create a function which accepts one arbitrary string as an argument, and return a string of length 26.

        The objective is to set each of the 26 characters of the output string to either '1' or '0' based on the
        fact whether the Nth letter of the alphabet is present in the input (independent of its case).

        So if an 'a' or an 'A' appears anywhere in the input string (any number of times), set the first character
        of the output string to '1', otherwise to '0'. if 'b' or 'B' appears in the string, set the second character
        to '1', and so on for the rest of the alphabet.

        For instance:

        "a   **&  cZ"  =>  "10100000000000000000000001"

        "aaaaaaa79345675"  =>  "10000000000000000000000000"

        "&%#*"  =>  "00000000000000000000000000"

"""

def find(st):
    # Convert the input string to lowercase for case-insensitive comparison
    st = st.lower()
    # Create a list of all lowercase alphabet letters
    l = [chr(i) for i in range(ord('a'), ord('z')+1)]
    m = ''
    # For each letter, check if it is present in the input string
    for i in range(len(l)):
        if l[i] in st:
            m += "1"  # Letter is present
        else:
            m += '0' # Letter is absent
    
    return m

# Test the find function with a sample input string
if __name__ == "__main__":
    st = '"a   **&  cZ" '
    print(find(st))