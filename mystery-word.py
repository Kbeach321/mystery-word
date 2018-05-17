# Mystery-word application #
# OBJECTIVES: # 3. 1 letter per round "Lives" # 4. Display progress on word

import random

def wholegame(guesscounter, statement):
    letter = guessinput
    if letterguesser(letter) is True:
        statement = correctguess(guessinput)
        guesscounter += 0
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
print(blankspace + randomword) ########### DELTE THIS WHEN COMPLETE ##############


########## TERMS ############

guesscounter = 8

while guesscounter >= 0:
    guessinput = input("Guess a letter! ")
    if guessinput in list(randomword):
        output = f"You have {guesscounter} guesses remaining"
        print(output)
