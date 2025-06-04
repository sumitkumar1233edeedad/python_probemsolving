''' 
Title: Find the Parity Outlier

📝 Description:
You are given an array of integers. The array is either mostly even numbers or mostly odd numbers, except for a single number called the outlier.

Your task is to return that outlier.

'''


def find_parity(numbers):
    # Separate odd and even numbers
    odd = [i for i in numbers if i % 2 != 0]
    even = [i for i in numbers if i % 2 == 0]
    # If there is only one odd number, it's the outlier
    return (odd[0] if len(odd) == 1 else(even[0] if len(even) == 1 else None))

if __name__ == "__main__":
    # Test cases
    print(find_parity([2, 4, 6, 8, 10, 3])) # 3 (only odd)
    print(find_parity([1, 3, 5, 7, 8]))     # 8 (only even)
    print(find_parity([11, 13, 15, 17, 19])) # None (all odd)
    print(find_parity([2, 4, 6, 8, 10]))     # None (all even)