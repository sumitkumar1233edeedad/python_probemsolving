# Define a list with some duplicate elements
m1 = [1, 2, 2, 4, 4, 6, 7]

# Create a copy of the list using list comprehension
m = [m1[j] for j in range(len(m1))]

# Check if all elements in the list are integers or floats
if all(isinstance(x, (int, float)) for x in m1):
    # If all elements are numbers, convert the list to a set to remove duplicates
    m1 = set(m1)
    # Convert the set back to a list
    m1 = list(m1)
    # Print the unique elements
    print(m1)
else:
    # If not all elements are numbers, process the list differently
    l = []  # Initialize an empty list to store processed elements
    p = m[0]  # Set the first element as the previous element for comparison

    # Iterate through the list starting from the second element
    for i in range(1, len(m)):
        if p == m[i]:  # If the current element is the same as the previous one
            l.append(m[i])  # Add it to the list
        else:
            l.append(" ")  # Add a space to separate groups of elements
            l.append(m[i])  # Add the current element
        p = m[i]  # Update the previous element

    # Join the list into a string and split it into groups
    k = ''.join(l)
    k = k.split()

    h = ''  # Initialize an empty string to store the result
    # Iterate through the groups and take the first character of each group
    for g, item in enumerate(k):
        if len(item) > 0:
            h += item[0]
    # Print the final result
    print(h)