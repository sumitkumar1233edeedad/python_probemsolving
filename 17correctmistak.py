# Character recognition software often makes mistakes when digitizing text.
# The task is to correct the following common mistakes in the digitized text:
# - '0' (zero) should be replaced with 'O' (uppercase letter O)
# - '1' (one) should be replaced with 'I' (uppercase letter I)
# - '5' (five) should be replaced with 'S' (uppercase letter S)

# Input string with potential errors
s = "DUBL1N"

# Convert the string into a list of characters for easy modification
s = [i for i in s]

# Iterate through the list and replace incorrect characters
for i in range(len(s)):
    if s[i] == "0":  # Replace '0' with 'O'
        s[i] = "O"
    elif s[i] == "1":  # Replace '1' with 'I'
        s[i] = "I"
    elif s[i] == "5":  # Replace '5' with 'S'
        s[i] = "S"

# Join the corrected list of characters back into a string and print the result
print(''.join(s))