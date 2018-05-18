# Mystery-word application #

# TO DO LIST: break when you win.

####################### IMPORTS ###########################

import random

###################### FUNCTIONS #################################

def letterguesser(guessinput):
    if guessinput in randomword:
        return True
    else:
        return False

def usedletters(updatedguess):
    if guessinput in updatedguess:
        print("Please guess a new letter")
    return usedletters

def winning(updatedguess):
    if

################# Gather Random Word ###########################

with open("/usr/share/dict/words") as wholedoc:
    wordbank = wholedoc.read().lower().splitlines()
    randomword = random.choice(wordbank)
    blankspace = "_ " * len(randomword)
print(randomword) ########### DELTE THIS WHEN COMPLETE ##############
print(blankspace)

##################### TERMS #############################
guesscounter = 8
updatedguess = []

while guesscounter > 0:
    guessinput = input("Guess a letter! ").lower()
    updatedguess += guessinput
    if letterguesser(guessinput) is True:
        for letter in randomword:
            if letter in updatedguess:
                print(letter + " ", end="")
            else:
                print("_ ", end="")
        print()
    else:
        guesscounter -= 1
        print("Incorrect, try again! ")
        print(guesscounter , "Guesses Remain")
    if guesscounter == 0:
        print("GAME OVER")
    if updatedguess == randomword:
        print("YOU WIN!")
