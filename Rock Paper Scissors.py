# Import function that can choose randomly between choices
from random import choice

while True:
    # Function to start playing
    def play():
        
        # User input (User Chooses rock paper or scissors)
        user_obj = input("Choose between Rock 'r', Paper 'p' or Scissors 's': ")

        # Computer chooses between the 3 choices
        computer_obj = choice(['r','p','s'])

        # Assigning Strings to Characters for good display
        if user_obj == 'r':
            obj = "Rock"
        elif user_obj == 'p':
            obj = "Paper"
        elif user_obj == 's':
            obj = "Scissors"
        
        # Checking to see if valid character has been input
        else:
            print("Invalid choice. Try again")
            play()

        if computer_obj == 'r':
            cobj = "Rock"
        elif computer_obj == 'p':
            cobj = "Paper"
        elif computer_obj == 's':
            cobj = "Scissors"

        # Displaying what each competitor chose
        print("You input: %s \nComputer put: %s" % (obj, cobj))

        # Displaying results
        if user_obj == computer_obj:
            print(("Tie!"))
        
        # User only wins when (user picks rock and computer picks scissors) or (user picks paper and computer picks rock) or (user picks scissors and computer picks paper).
        elif (user_obj == 'r' and computer_obj == 's') or (user_obj == 'p' and computer_obj == 'r') or (user_obj == 's' and computer_obj == 'p'):
            print("You Win!")
        # Otherwise computer wins
        else:
            print("You Lost!")

    # Calling the Play function
    play()

