# Define the input text
text = 'ninji'

# Reverse the text
text = text[::-1]

# Define the ending string to check
ending = 'ji'

# Extract the portion of the reversed text equal to the length of the ending
text = text[0:len(ending)]

# Reverse the text back to its original order
text = text[::-1]
 
# Print the extracted text and the ending
print(text, ending)

# Check if the extracted text matches the ending and print the result
print(True if text == ending else False)