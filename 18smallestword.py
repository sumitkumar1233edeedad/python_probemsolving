# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

s = "bitcoin take over the world maybe who knows perhaps"
s = s.split()
l = [len(i) for i in s]
shortest_length = min(l)  # Find the shortest length
print(shortest_length)  # Output the result

    