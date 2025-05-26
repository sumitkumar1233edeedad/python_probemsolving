""" 
Title: Your order, please

📝 Description:
Your task is to sort a given string.
Each word in the string will contain a single number (1–9).
This number represents the position the word should be in.

Return the sorted string, based on the numbers inside the words.

If the input string is empty, return an empty string.

📌 Function Signature:
python
Copy
Edit
def order(sentence: str) -> str:
    pass
🧪 Examples:
python
Copy
Edit
order("is2 Thi1s T4est 3a")          # ➞ "Thi1s is2 3a T4est"
order("4of Fo1r pe6ople g3ood th5e the2")  # ➞ "Fo1r the2 g3ood 4of th5e pe6ople"
order("")                            # ➞ ""
💡 Notes:
Each word contains exactly one number.

Numbers range from 1 to 9.

Use the number to determine the correct word position.



"""

# Function to order words in a sentence based on the number in each word
def order(sent: str) -> str:
    # Split the sentence into words
    sent = sent.split()
    m = []
    
    # Extract the number from each word and store in m (not used later)
    for word in sent:
        for el in word:
            if el.isnumeric():
                m.append(int(el))
                
    # Prepare a list to hold words in the correct order
    p = ['' for _ in range(len(sent))]
    
    # Place each word at the correct index based on the number it contains
    for i, word in enumerate(sent):
        for el in word:
            if el.isnumeric():
                p[int(el)-1] = word
                break

    # Join the ordered words into a string and return
    return ' '.join(p)

if __name__ == "__main__":
    print(order("is2 Thi1s T4est 3a"))          # ➞ "Thi1s is2 3a T4est"
    print(order("4of Fo1r pe6ople g3ood th5e the2"))  # ➞ "Fo1r the2 g3ood 4of th5e pe6ople"
    print(order(""))                            # ➞ ""