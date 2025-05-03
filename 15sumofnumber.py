n = 3  # Number of terms in the series
m = 0  # Variable to store the sum of the series

# Loop through the range from 0 to n-1
for i in range(0, n):
    # Add the value of the current term in the series to m
    m += 1 / ((3 * i) + 1)
    print(m)  # Print the intermediate sum after each iteration

# Print the final sum rounded to 2 decimal places
print(f"{m:.2f}")