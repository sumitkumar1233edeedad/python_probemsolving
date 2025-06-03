'''  
Title: Counting Duplicates

📝 Description:
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string.




'''

def duplicate_count(text: str) -> int:
    # Convert each character to lowercase and include it in the list if it appears more than once in the text
    text1 = [i.lower() for i in text]
    # Return the number of unique characters that appear more than once
    text1 = [i for i in text1 if text1.count(i) > 1]
    return len(set(text1)), text1
    

if __name__ == "__main__":
    # Test cases to demonstrate the function
    print(duplicate_count("abcde"))             # Output: 0
    print(duplicate_count("aabbcde"))           # Output: 2 ('a' and 'b')
    print(duplicate_count("aabBcde"))           # Output: 2 ('a' and 'b', case-insensitive)
    print(duplicate_count("aA11"))              # Output: 2 ('a' and '1')
    print(duplicate_count("ABBA"))              # Output: 2 ('a' and 'b', case-insensitive)