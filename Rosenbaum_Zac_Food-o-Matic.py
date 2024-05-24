'''
Author: Zac Rosenbaum
Date: 3/29/2024
Discription: Creates a shakspearean insult generator that creates the amount that the user inputs
Challenges: 3 lists, insult generator, gives a rating
Bugs: None
Sources: class lectures
https://i.pinimg.com/originals/c0/70/0e/c0700ec8978d8f440dcc264e4dff4c15.jpg
'''
import time #imports time library for all time functions 
import random #imports random library for all random functions
adjectives1 = ["artless", "bawdy", "beslubbering", "bootless", "churlish", "cockered", "clouted", "craven", "currish", "dankish", "dissembling", "droning", "errant", "fawning", "fobbing", "forward", "frothy", "gleeking", "goatish", "gorbellied", "impertinent", "infectious", "jarring", "loggerheaded", "lumpish", "mammering", "mangled"]
adjectives2 = ["base-court", "bat-fowling", "beef-witted", "beetle-headed", "boil-brained", "clapper-clawed", "clay-brained", "common-kissing", "crook-pated", "dismal-dreaming", "dizzy-eyed", "doghearted", "dread-bolted", "earth-vexing", "elf-skinned", "fat-kidneyed", "fen-sucked", "flap-mouthed", "fly-bitten", "folly-fallen", "fool-born", "full-gorged", "guts-griping", "half-faced", "hasty-witted", "hedge-born", "hell-hated"]
nouns = ["apple-john", "baggage", "barnacle", "bladder", "boar-pig", "bugbear", "bum-bailey", "canker-blossom", "clack-dish", "clotpole", "coxcomb", "codpiece", "death-token", "dewberry", "flap-dragon", "flax-wench", "flirt-grill", "foot-licker", "fustilarian", "giglet", "gudgeon", "haggard", "harpy", "hedge-pig", "horn-beast", "hugger-mugger", "jointhead",]
#creates 3 different lists for the insults
adjective1_ratings = [3,4,5,1,4,2,3,5,2,3,3,1,1,2,5,3,2,5,4,3,1,5,3,2,2,3,4]
adjective2_ratings = [2,4,3,5,4,3,4,5,2,1,4,2,1,3,5,2,3,1,3,4,5,3,1,2,5,3,1]
noun_ratings = [2,3,5,1,3,4,2,5,3,3,4,5,5,4,2,3,3,5,2,4,1,5,2,5,1,3,2] 
#creates 3 more lists, giving a rating to each word apart of the insults

while True: # creates a loop that continuously runs the code
    try: # check if the following code works
        insults_question = int(input("How many insults would you like?(numbers)"))#Asks the user how many insults they would like and stores the respose as an input and intiger
        break # breaks the loop that continues to run if not
    except ValueError: #allows the code to contiue if there is a value error
        print("Enter an integer!") #prints that the input 
        
print("L")#prints 'l'
time.sleep(.5)#waits .5 seconds
print("O")#prints 'l'
time.sleep(.5)#waits .5 seconds
print("A")#prints 'l'
time.sleep(.5)#waits .5 seconds
print("D")#prints 'l'
time.sleep(.5)#waits .5 seconds
print("I")#prints 'l'
time.sleep(.5)#waits .5 seconds
print("N")#prints 'l'
time.sleep(.5)#waits .5 seconds
print("G")#prints 'l'
time.sleep(.5)#waits .5 seconds

#together this makes a loading screen :)
for insult_number in range(insults_question): #sets a for loop that repeats the amount of times the user inputs in the previous question
    adjective1 = random.choice(adjectives1) #creates a random word from the list
    adjective2 = random.choice(adjectives2) #creates a random word from the list
    noun = random.choice(nouns) #creates a random word from the list
    print(f'''
Thou {adjective1} {adjective2} {noun}
The rating for this insult is a {adjective1_ratings[adjectives1.index(adjective1)]+adjective2_ratings[adjectives2.index(adjective2)]+noun_ratings[nouns.index(noun)]}/15''') #prints a random string in each list to create an insult
# adds up the rating that is paralel to each word and adds them up from each insult to give an indivigual rating to every insult made
