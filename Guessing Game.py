#Import random library that allows random number generation.
import random

#Function that creates a random number and checks if the user input number matches the generated random number.
def guess(x):
    #Generate random number from 1 to any integer x > 0.
    random_number = random.randint(1, x)

    #Initialise guess
    guess = 0

    #check whether guess is equal to the randomly generated number.
    while guess != random_number:

        #Ask for user Input.
        guess = int(input("Guess the number: "))

        #Show the number that has been guessed.
        print("You guessed %d" % guess)

        #check if the guessed number is greater than the randomly generated numnber.
        if guess > random_number:
            print("That is the wrong number. Guess lower. ")

        #check if the guessed number is less than the randomly generated numnber.
        elif guess < random_number:
            print("That is the wrong number. Guess higher. ")
    
    #If the guessed number matches the randomly generated number then display congratulation message.
    print("Congratulations you guessed correctly, the number was: %d" % random_number)

#Call the guess function (here the upper limit is set to 10).
guess(10)
