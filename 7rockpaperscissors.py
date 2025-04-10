import random

# Function to determine the result of the game
def guess(computer, user):
    # Check the result based on the rules of rock-paper-scissors
    print('Actual Your Draw!' if computer == user else (
        "You are win this game!" if computer == "rock" and user == "paper" else (
        "You are win this game!" if computer == "paper" and user == "scissors" else (
        "You are win this game!" if computer == "scissors" and user == "rock" else 
        "you are loose the game? next time try1 😊😊"))))

# Main function to run the game
if __name__ == "__main__":
    # Randomly select the computer's choice
    computer = random.choice(['rock', 'paper', 'scissors'])
    
    # Display game instructions
    print("    -:It Is Funny Game:-.\nThis Is rock_paper_scissors Game. \n1.rock, \n2.paper \n3.scissors \nHope Full You Enjoy")
    
    m = True  # Variable to control the game loop
    while m:
        # Ask the user if they want to play again
        again = input('Actual you were we playing game? yes or no :-> ')
        if again.lower() == 'yes':
            m = True  # Continue the game
            # Get the user's choice
            user = input("Enter the your choice :-> ")
            # Call the guess function to determine the result
            guess(computer, user)
        else:
            m = False  # Exit the game loop
            # Thank the user for playing
            print("-:Thankyou for coming rock_paper_scissors game!:-")