# Mystery-word application #
# OBJECTIVES:
# 2. Number of letters # 3. 1 letter per round "Lives"
# 4. Display progress on word # 5. 8 guesses [guess count displayed]

import random

with open("/usr/share/dict/words") as wholedoc:
    wordlist = wholedoc.read().lower().splitlines()
    randomword = random.choice(wordlist)
print(randomword)

def wholegame(guesscounter, answer):
    if correctguess():
        statement = "That letter is correct "
        guesscounter += 0
    else:
        statement = "That letter is incorrect "
        guesscounter -= 1
    return statement , guesscounter

#print(f"Your word contains this many letters" randomword)

#def correctguess(letter):
#    return f"{letter} is correct"

#def incorrectguess(letter):
#    return f"{letter} is incorrect"

################################################################

guesscounter = 8

while guesscounter > 0:
    guessinput = input("Guess a letter! ")
    output = f"You have {guesscounter} guesses remaining"

    print(output)
