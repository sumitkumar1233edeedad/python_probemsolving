""" 
 Count the smiley faces!

📝 Description:
Given an array of strings representing faces, count how many valid smiley faces there are.

A valid smiley face must follow these rules:

Eyes can be : or ;

Nose (optional) can be - or ~

Mouth must be ) or D

No other characters are allowed.

📌 Function Signature:
python
Copy
Edit
def count_smileys(arr: list[str]) -> int:
    pass
🧪 Examples:
python
Copy
Edit
count_smileys([])                                  # ➞ 0
count_smileys([':)', ';(', ';}', ':-D'])           # ➞ 2
count_smileys([';D', ':-(', ':-)', ';~)'])         # ➞ 3
count_smileys([';]', ':[', ';*', ':$', ';-D'])     # ➞ 1
💡 Notes:
Valid examples: :), :-), ;~D, ;D

Invalid examples: :(, :>, :o), ;-p




"""
def count_smileys(arr: list[str]) -> int:
    # Initialize counter for valid smiley faces
    count = 0
    import re
    # Regex pattern for valid smiley faces
    pattern = re.compile(r'^[:;][-~]?[)D]$')
    for face in arr:
        # Check if the face matches the valid smiley pattern
        if pattern.match(face):
            count += 1
    return count

if __name__ == "__main__":
    # Test cases
    print(count_smileys([]))                                  # ➞ 0
    print(count_smileys([':)', ';(', ';}', ':-D']))           # ➞ 2
    print(count_smileys([';D', ':-(', ':-)', ';~)']))         # ➞ 3
    print(count_smileys([';]', ':[', ';*', ':$', ';-D']))     # ➞ 1