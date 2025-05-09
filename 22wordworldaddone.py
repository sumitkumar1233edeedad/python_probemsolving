#this is question
""" Given a string and a letter, return the alphabetic character after every instance of the letter (case insensitive).
        If there is a number, punctuation or underscore following the letter, it should not be returned.
        Example:
        letter = 'r'
        "are you really learning Ruby?" # => "eenu"
        "Katy Perry is on the radio!"   # => "rya"
        "Pirates say arrrrrrrrr."       # => "arrrrrrrr"
        "r8 your friend"                # => "i"

        Example usage:
        print(after_letter("are you really learning Ruby?", "r"))  # Output: "eenu"
        print(after_letter("Katy Perry is on the radio!", "r"))    # Output: "rya"
        print(after_letter("Pirates say arrrrrrrrr.", "r"))        # Output: "arrrrrrrr"
        print(after_letter("r8 your friend", "r"))                 # Output: "i" 
"""
def word(st, l):
    # Iterate through the string, checking each character
    result = ""
    for i in range(len(st) - 1):
        # If the current character matches the given letter (case-insensitive)
        # and the next character is an alphabet letter, add it to the result
        if st[i].lower() == l.lower() and st[i+1].isalpha():
            result += st[i+1]
    # Print the final result string
    print(result)

if __name__ == "__main__":
    st = "Katy Perry is on the radio!"
    l = "r"
    word(st, l)
     