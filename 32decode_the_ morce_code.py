""" 
        Title: Decode the Morse code

        📝 Description:
        Your task is to decode a string of Morse code into readable text.

        Each word is separated by three spaces (" ").
        Each letter is separated by one space (" ").

        You are given a dictionary (on Codewars it's called MORSE_CODE) that maps Morse code sequences to their corresponding characters.

        📌 Function Signature:
        python
        Copy
        Edit
        def decode_morse(morse_code: str) -> str:
            pass
        🧪 Examples:
        python
        Copy
        Edit
        decode_morse('.... . .-.. .-.. ---')                # ➞ "HELLO"

        decode_morse('.... . -.--   .--- ..- -.. .')        # ➞ "HEY JUDE"

        decode_morse('.-')                                  # ➞ "A"

        decode_morse('... --- ...')                         # ➞ "SOS"

        decode_morse('   ... --- ...   ')                   # ➞ "SOS"

        decode_morse('-.-. --- -.. .   .-- .- .-. ...')      # ➞ "CODE WARS"



"""

def decode_morse(st):
    # Dictionary mapping letters to Morse code
    MORSE_CODE = {
        'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
        'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
        'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
        'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
        'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',   ' ' : ' ',
    }
    # Split the input Morse code string into individual codes
    st =  st.split(' ')
    result = ''
    
    # For each Morse code, find the corresponding letter
    # Iterate through each Morse code in the split list
    for i in range(len(st)):
        # For each Morse code, find the corresponding letter in the dictionary
        for key, val in MORSE_CODE.items():
            if st[i] == val:
                result += key
        result += ''
    return result

if __name__ == "__main__":
    
    
    # Example usage: decode '.... . .-.. .-.. ---' to 'HELLO'
    print(decode_morse('.... . .-.. .-.. ---'))
    print(decode_morse('.-- --- .-. .-.. -..'))
    print(decode_morse('-- -.--   -. .- -- .'))
    print(decode_morse('.... .- ...- .   .-   --. --- --- -..   -.. .- -.--'))
    print(decode_morse('.-- .   .- .-. .   .-.. . .- .-. -. .. -. --.   .--. -.-- - .... --- -.'))
    print(decode_morse('.... . .-.. .-.. ---   .-- --- .-. .-.. -..'))
    print(decode_morse('- .... .. ...   .. ...   .-   - . ... -'))