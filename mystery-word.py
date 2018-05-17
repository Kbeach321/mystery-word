# Mystery-word application #
# OBJECTIVES:  1. select a word from external file
# 2. Number of letters # 3. 1 letter per round "Lives"
# 4. Display progress on word # 5. 8 guesses [guess count displayed]

import random

with open("/usr/share/dict/words") as wholedoc:
    wordlist = wholedoc.read().lower().splitlines()
    randomword = random.choice(wordlist)
print(randomword)

def correctguess(letter):
    return f"{letter} is correct"

def incorrectguess(letter):
    return f"{letter} is incorrect"

################################################################

guesscounter = 8

#while guesscounter > 0:
#    print(guesscounter)
#    letterguess = input("Guess a letter! ")
#    print(computerword)
