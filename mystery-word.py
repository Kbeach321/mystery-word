# Mystery-word application #
# OBJECTIVES:
# 2. Number of letters # 3. 1 letter per round "Lives"
# 4. Display progress on word # 5. 8 guesses [guess count displayed]

import random

with open("/usr/share/dict/words") as wholedoc:
    wordlist = wholedoc.read().lower().splitlines()
    randomword = random.choice(wordlist)
    blankspace = "_ " * len(randomword)
print(blankspace) # CHANGE THIS TO BE _ _ _ _ #

def incorrectguess(guessinput):
    return f"{letter} is incorrect"

def correctguess(guessinput):
    return f"{letter} is correct"

def letterguesser(letter):
    if guessinput in randomword:
        return True
    else:
        return False

def wholegame(guesscounter, answer):
    letter = guessinput
    if letterguesser(letter):
        statement = correctguess(guessinput)
        guesscounter += 0
    else:
        statement = incorrectguess(guessinput)
        guesscounter -= 1
    return statement , guesscounter

#print(f"Your word contains this many letters" randomword)

################################################################

guesscounter = 8

while guesscounter > 0:
    guessinput = input("Guess a letter! ")
    answer = "YOU WIN!"
    output = f"You have {guesscounter} guesses remaining"
    guessedletter = wholegame(guesscounter, answer)
    print(output)
