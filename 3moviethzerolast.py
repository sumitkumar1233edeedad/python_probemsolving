n = [1, 2, 0, 4, 5, 0, 89, 0, 8]  # List containing integers, including zeros
result = []  # Initialize an empty list to store the result

# Loop through the list and append non-zero elements to the result list
for i in n:
    if i != 0:
        result.append(i)

cot = n.count(0)  # Count the number of zeros in the original list

# Append the counted number of zeros to the end of the result list
for j in range(cot):
    result.append(0)

print(result)  # Print the final list with zeros moved to the end