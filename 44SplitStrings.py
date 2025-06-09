'''
 🔸 Codewars 6 kyu Kata
Title: Split Strings

📝 Description:
Complete the function so that it splits the given string into pairs of two characters.
If the string contains an odd number of characters, add an underscore '_' to the final pair.

📌 Function Signature:
python
Copy
Edit
def solution(s: str) -> list[str]:
    pass
🧪 Examples:
python
Copy
Edit
solution("abc")       # ➞ ['ab', 'c_']
solution("abcdef")    # ➞ ['ab', 'cd', 'ef']
solution("a")         # ➞ ['a_']
solution("")          # ➞ []
💡 Notes:
Always return a list.

The function should work for an empty string as well.

This is often useful in text formatting or encoding tasks. solution give me
'''

def string_convert(string_c):
     # Convert the string to a list of characters
    if len(string_c)%2 != 0:
        string_c += '_'
    # range(0, len(string_c), 2) generates indices 0, 2, 4, ... up to the length of the string.
    # For each index i, string_c[i:i+2] takes a substring of two characters.
    # This splits the string into pairs of two characters.
    return [string_c[i:i+2] for i in range(0, len(string_c), 2)]
if __name__ == "__main__":
    print(string_convert('abcd'))      # ['ab', 'cd']
    print(string_convert('abc'))       # ['ab', 'c_']
    print(string_convert('abcdef'))    # ['ab', 'cd', 'ef']
    print(string_convert('a'))         # ['a_']
    print(string_convert(''))          # []
    