""" 
Title: Isograms

📝 Description:
An isogram is a word that has no repeating letters, consecutive or non-consecutive.

Create a function that determines whether a string is an isogram.

📌 Function Signature:
python
Copy
Edit
def is_isogram(string: str) -> bool:
    pass
🧪 Examples:
python
Copy
Edit
is_isogram("Dermatoglyphics")   # ➞ True
is_isogram("aba")               # ➞ False
is_isogram("moOse")             # ➞ False  # case-insensitive
💡 Notes:
Ignore letter case (treat uppercase and lowercase as the same).

Empty string is considered an isogram.

"""


def is_isogram(string: str) -> bool:
    """
    Checks if a string is an isogram (no repeating letters, case insensitive).

    Args:
        string (str): The string to check.

    Returns:
        bool: True if the string is an isogram, False otherwise.
    """
    string = string.lower()  # Convert to lowercase for case-insensitive comparison
    str_list = [i for i in string]  # Create a list of characters
    return len(str_list) == len(set(str_list))  # Compare length with set (unique chars)
    


if __name__ == "__main__":
    print(is_isogram("Dermatoglyphics"))  # True
    print(is_isogram("aba"))              # False
    print(is_isogram("moOse"))            # False
    print(is_isogram("isogram"))          # True
    print(is_isogram(""))                 # True
    print(is_isogram("Python"))           # True
    print(is_isogram("Alphabet"))         # False
    print(is_isogram("12345"))            # True
    print(is_isogram("112233"))           # False
    print(is_isogram("No duplicates"))    # True