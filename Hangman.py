from ntpath import join
from random import choice
from word import words

def get_valid_word():
    word = choice(words)
    while ('-' in word) or (' ' in word):
        word = choice(word)
    return word
    

def hangman():
    incorrect_no = 0
    raw_word = get_valid_word()
    word = set(raw_word)
    guessed_letters = set()
    guessed_correct_letters = set()
    print("Current word is: %s" % ('- ' * len(raw_word)))

    while incorrect_no < 6 and guessed_correct_letters != word:
        
        letter = input("Enter an alphabet: ")

        if letter in guessed_letters:
            print("You've already guessed the letter %s:" % letter)

        else:
            if letter in word:
                print("Letter %s exists in the word" % letter)
                guessed_correct_letters.add(letter)
            elif letter not in word:
                print("Letter %s does not exist in word" % letter)
                incorrect_no += 1
                print("Number of tries remaining: %d" % (6 - incorrect_no))
            guessed_letters.add(letter)
        

        word_list = [letter if letter in guessed_correct_letters else '-' for letter in raw_word]
        print("Current word is: ", " ".join(word_list))

    if incorrect_no == 6:
        print("Sorry, number of tries have finished")
    elif guessed_correct_letters == word:
        print("Congratulations you have guessed the answer correctly!!!")
    print("The word was %s" % raw_word)

        
hangman()

        