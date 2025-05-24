"""  
📝 Description:

You probably know the "like" system from Facebook and other social media platforms.
People can "like" blog posts, pictures, or other items.
We want to create the text that should be displayed next to such an item.

Implement the function that takes in a list of names and returns a string that describes who likes the item.
📌 Function Signature:

def likes(names: list[str]) -> str:
    pass

🧪 Examples:

likes([])                             # ➞ "no one likes this"
likes(["Peter"])                      # ➞ "Peter likes this"
likes(["Jacob", "Alex"])              # ➞ "Jacob and Alex like this"
likes(["Max", "John", "Mark"])        # ➞ "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # ➞ "Alex, Jacob and 2 others like this"

💡 Rules:

    If no one likes it → "no one likes this"

    If 1 person → "Peter likes this"

    If 2 people → "Jacob and Alex like this"

    If 3 people → "Max, John and Mark like this"

    If 4+ people → "Alex, Jacob and N others like this"
    (where N = total - 2)

"""

def likes(ar):
    if len(ar) == 1:
        return f"{ar[0]} likes this post."
    elif len(ar) > 1:
        if len(ar) == 2:
            return f"{ar[0]} and {ar[1]} like this post."
        elif len(ar) == 3:
            return f"{ar[0]}, {ar[1]} and {ar[2]} like the post."
        else:
            return f"{ar[0]}, {ar[1]} and {len(ar)-2} other like this."
    else:
        return "no one likes this"
if __name__ == "__main__":
    print(likes([]))                             # ➞ "no one likes this"
    print(likes(["Peter"]))                      # ➞ "Peter likes this"
    print(likes(["Jacob", "Alex"]))              # ➞ "Jacob and Alex like this"
    print(likes(["Max", "John", "Mark"]))        # ➞ "Max, John and Mark like this"
    print(likes(["Alex", "Jacob", "Mark", "Max"])) # ➞ "Alex, Jacob and 2 others like this"
    print(likes(["A", "B", "C", "D", "E"]))      # ➞ "A, B and 3 others like this"
    print(likes(["Sam"]))                        # ➞ "Sam likes this"
    print(likes(["Tom", "Jerry"]))               # ➞ "Tom and Jerry like this"
    print(likes(["Anna", "Elsa", "Olaf", "Kristoff", "Sven"])) # ➞ "Anna, Elsa and 3 others like this"
    print(likes(["X", "Y", "Z", "W", "V", "U"])) # ➞ "X, Y and 4 others like this"
