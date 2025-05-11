"""
Write a program that, given a word, computes the scrabble score for that word.
Letter Values

You'll need these:

Letter                           Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10

There will be a preloaded dictionary dict_scores with all these values: dict_scores["E"] == 1
Examples

"cabbage" --> 14

"""
def find_score(st):
    # Convert the input string to lowercase for case-insensitive scoring
    st = st.lower()
     
    total = 0
    # Dictionary mapping each letter to its Scrabble score
    score = {
        'a' : 1,
        'b' : 3,
        'c' : 3,
        'd' : 2,
        'e' : 1,
        'f' : 4,
        'g' : 2,
        'h' : 4,
        'i' : 1,
        'j' : 8,
        'k' : 5,
        'l' : 1,
        'm' : 3,
        'n' : 1,
        'o' : 1,
        'p' : 3,
        'q' : 10,
        'r' : 1,
        's' : 1,
        't' : 1,
        'u' : 1,
        'v' : 4,
        'w' : 4,
        'x' : 8,
        'y' : 4,
        'z' : 10,
        }
    # Iterate over each key-value pair in the score dictionary
    for key, value in score.items():
        for i in st:
            # If the character matches the key, add its score to total
            if key  == i:
                total += score[key]
             
    return total

if __name__ == "__main__":
    st = "MULTIBILLIONAIRE"
    sum = find_score(st)
    print(sum)