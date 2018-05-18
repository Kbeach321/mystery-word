# Mystery-word application #
# OBJECTIVES: # 3. 1 letter per round "Lives" # 4. Display progress on word
###############################
import random
#############################

def letterguesser(guessinput):
    if guessinput in randomword:
        return True
    else:
        return False

def correctguess(guessinput):
    pass

############# Gather Random Word ###########################

with open("/usr/share/dict/words") as wholedoc:
    wordbank = wholedoc.read().lower().splitlines()
    randomword = random.choice(wordbank)
    blankspace = "_ " * len(randomword)
print(blankspace) ########### DELTE THIS WHEN COMPLETE ##############

########## TERMS ############

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
        print(guesscounter , "Guesses Remain")
    else:
        guesscounter -= 1
        print(guesscounter , "Guesses Remain")
