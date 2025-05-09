# Question: Count the number of divisors of a positive integer n.

# Random tests go up to n = 500000, but fixed tests go higher.

# Examples (input --> output):
# 4 --> 3 // we have 3 divisors - 1, 2 and 4
# 5 --> 2 // we have 2 divisors - 1 and 5
# 12 --> 6 // we have 6 divisors - 1, 2, 3, 4, 6 and 12
# 30 --> 8 // we have 8 divisors - 1, 2, 3, 5, 6, 10, 15 and 30

def checker(n):
    # Create a list of all divisors of n by checking divisibility for each number from 1 to n
    l = [x for x in range(1, n + 1) if n % x == 0]
    # Return the count of divisors
    
    return len(l)

if __name__ == "__main__":
    # Example input
    n = 12
    # Call the checker function and store the result
    re = checker(n)
    # Print the number of divisors
    print(re)