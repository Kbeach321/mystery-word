# Mystery-word application #
# OBJECTIVES: # 3. 1 letter per round "Lives" # 4. Display progress on word

import random

def wholegame(guesscounter, statement):
    letter = guessinput
    if letterguesser(letter) is True:
        statement = correctguess(guessinput)
    else:
        statement = incorrectguess(guessinput)
        guesscounter -= 1
    return guesscounter, statement


def letterguesser(letter):
    if guessinput in randomword:
        return True
    else:
        return False

def incorrectguess(guessinput):
    pass
    #

def correctguess(guessinput):
    pass
    #

############# Gather Random Word ###########################

with open("/usr/share/dict/words") as wholedoc:
    wordlist = wholedoc.read().lower().splitlines()
    randomword = random.choice(wordlist)
    list(randomword)
    blankspace = "_ " * len(randomword)
print(randomword) ########### DELTE THIS WHEN COMPLETE ##############


########## TERMS ############

guesscounter = 8

while guesscounter >= 0:
    guessinput = input("Guess a letter! ")
    if guessinput in randomword:
        guesscounter += 0
        print("Your word has this many spaces: " + blankspace)

    else:
        print("Nope, guess again")
        guesscounter -= 1
    output = f"You have {guesscounter} guesses remaining"
    print(output)
