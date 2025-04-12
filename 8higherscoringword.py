# Input string of words
s = 'pnxsyls xwlpy yyf gytolcdvi priwpn trfoeyjfr poqk nbjijumej bxmizjoxn rypfqmofgf zujgca jkmyjfthfl ysdojkqmw nfoy' 

# Create a dictionary to map each letter to its corresponding score (a=1, b=2, ..., z=26)
h = {chr(i): i - 96 for i in range(97, 123)}

# Split the input string into a list of words
s = s.split()

# Initialize variables
l = 0  # To keep track of cumulative score
m = []  # List to store scores of each word
 
# Calculate the score for each word
for i in s:
    p = l  # Store the previous cumulative score
    for j in i:
        l += h[j]  # Add the score of each letter in the word
    m.append(l - p)  # Append the score of the current word to the list

# Print the list of scores for debugging
print(m)

# Find the maximum score in the list
ma = max(m)

# Find the index of the word with the maximum score 
ma = next(i for i in range(len(m)) if ma == m[i])
 
print(s[ma])