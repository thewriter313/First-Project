# Importing random library and list of english words.
from random import choice
from word import words

# Function that gets a valid word from the list.
def get_valid_word():
    word = choice(words)
    while ('-' in word) or (' ' in word):
        word = choice(word)
    return word
    
# Function that plays the hangman game.
def hangman():

    # Initialising initial condition.
    incorrect_no = 0
    raw_word = get_valid_word()
    word = set(raw_word)
    guessed_letters = set()
    guessed_correct_letters = set()
    print("Current word is: %s" % ('- ' * len(raw_word)))

    # Check to see if the number of tries has been depleted and whether the word has been guessed correctly.
    while incorrect_no < 6 and guessed_correct_letters != word:
        # Ask user for letter.
        letter = input("Enter an alphabet: ").lower()

        # Check whether input letter is actually an alphabet.
        while not letter.isalpha():
            print("Please input an alphabet.")
            letter = input("Enter an alphabet: ")

        # If letter has already been guessed then do nothing but display warning.
        if letter in guessed_letters:
            print("You've already guessed the letter %s:" % letter)
        
        # Otherwise check if the letter is in the word.
        else:

            # If letter is in word then add to correct letters guessed.
            if letter in word:
                print("Letter %s exists in the word" % letter)
                guessed_correct_letters.add(letter)

            # If letter is not in word then decrease amount of tries remaining.
            elif letter not in word:
                print("Letter %s does not exist in word" % letter)
                incorrect_no += 1
                print("Number of tries remaining: %d" % (6 - incorrect_no))
            
            # Add guessed letter to list of guessed letter regardless if the letter exists in the word or not.
            guessed_letters.add(letter)
        
        # Display which letters have been guessed correctly and display '-' for unguessed letters.
        word_list = [letter if letter in guessed_correct_letters else '-' for letter in raw_word]
        print("Current word is: ", " ".join(word_list))

    # Check to see if number of tries have depleted or if the word has been guessed correctly.
    if incorrect_no == 6:
        print("Sorry, number of tries have finished")
    elif guessed_correct_letters == word:
        print("Congratulations you have guessed the answer correctly!!!")

    # Print the word at end of game.
    print("The word was %s" % raw_word)

# Call the hangman function.    
hangman()