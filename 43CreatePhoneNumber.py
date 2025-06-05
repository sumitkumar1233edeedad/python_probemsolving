'''

Title: Create Phone Number
📝 Description:

Write a function that accepts an array of 10 integers (between 0 and 9) and returns a string of those numbers in the form of a phone number.


'''

def create_phone(number):
    return f'({number[0]}{number[1]}{number[2]}) {number[3]}{number[4]}{number[5]}-{number[6]}{number[7]}{number[8]}{number[9]}'
if __name__ == "__main__":
    print(create_phone([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    print(create_phone([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(create_phone([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
    print(create_phone([5, 5, 5, 1, 2, 3, 4, 5, 6, 7]))
    print(create_phone([2, 4, 6, 8, 0, 1, 3, 5, 7, 9]))
    print(create_phone([3, 3, 3, 4, 4, 4, 5, 5, 5, 6]))
    print(create_phone([7, 6, 5, 4, 3, 2, 1, 0, 9, 8]))
    print(create_phone([1, 1, 1, 2, 2, 2, 3, 3, 3, 4]))
    print(create_phone([0, 0, 0, 1, 1, 1, 2, 2, 2, 3]))
    print(create_phone([9, 9, 9, 8, 8, 8, 7, 7, 7, 6]))
    print(create_phone([4, 5, 6, 7, 8, 9, 0, 1, 2, 3]))
    print(create_phone([2, 3, 4, 5, 6, 7, 8, 9, 0, 1]))
    print(create_phone([8, 7, 6, 5, 4, 3, 2, 1, 0, 9]))
    print(create_phone([1, 3, 5, 7, 9, 0, 2, 4, 6, 8]))
    print(create_phone([0, 2, 4, 6, 8, 1, 3, 5, 7, 9]))
    print(create_phone([5, 4, 3, 2, 1, 0, 9, 8, 7, 6]))
    print(create_phone([6, 7, 8, 9, 0, 1, 2, 3, 4, 5]))
    print(create_phone([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))
    print(create_phone([2, 7, 1, 8, 2, 8, 1, 8, 2, 8]))
    print(create_phone([1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))