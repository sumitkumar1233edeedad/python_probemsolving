'''
Title: Stop gninnipS My sdroW!

📝 Description:
Write a function that takes in a string of one or more words and returns the same string,
but with all words with five or more letters reversed.

Words with fewer than five letters should remain unchanged.
Punctuation should be treated as part of the word.



'''


def spin_words(sentence: str) -> str:
    cot1 = sentence.split()
    convert = [i[::-1] if len(i) >= 5 else i for i in cot1]
    return ' '.join(convert)
 
if __name__ == "__main__":
    print(spin_words("Hey fellow warriors"))         # ➞ "Hey wollef sroirraw"
    print(spin_words("This is a test"))              # ➞ "This is a test"
    print(spin_words("This is another test"))        # ➞ "This is rehtona test"
    print(spin_words("Welcome"))                     # ➞ "emocleW"