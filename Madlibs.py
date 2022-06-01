#Input Name of friend
friend = input("Friends Name: ")

#Input Name of Game played
game = input("Game name: ")

#Input The amount of time played in Hours
hrs = int(input("How many hours did you play: "))

#Make a story in String format an concatenate with user input
madlib = ("Yo today i went to %s's house and we played %s for %d hours." % (friend, game, hrs))

#Print MADLIB
print(madlib)