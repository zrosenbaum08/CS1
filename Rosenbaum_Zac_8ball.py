import sys #bring in the sys library for use of the exit() function
import random #bring in the random library for all random functions
import time #bring in the time library for delays
'''
Author: Zac Rosenbaum
Date: 11/13/2023
Description: Generates a random response from a list to the user's question
Challenges: Exits when you say stop, is in a loop
Bugs: None
Sources: class lectures
'''


print('''
⓼Hello, I am your magic 8-ball⓼
________________________________

''') # print hello, I am your magic 8 ball

answerlist = ["Yes", "Most certainly", "Maybe", "I'm not sure", "No", "Never", "Maybe in a year", "It is possible", "it is not possible", "This will happen soon!"]
# creates a list of possible responses
while True: # creates a loop that continuously runs the code
    while True: # creates a loop in the loop
        question = input("What is your question. Enter stop to end")
              # prompts user for a question and stores their response in a variable question  
        if question == "stop": # if user inputs 'stop', then
            exit() # exits the program
        elif "?" in question: # if the user didn't say stop check if they had a question mark, if so,
            time.sleep(1)#sets a delay for 1 second
            print(random.choice(answerlist)) # print a random choice 
            break # breaks the loop
        else: # if the input doesn't meet the previous conditionals,
            time.sleep(1)#sets a delay for 1 second
            print("not a question!") # print 'its not a question'
    while True: # creates a loop that continusly runs the code
        happy = str.lower(input("Are you happy with your answer? (yes, or no)"))
# prompts user for a question and stores their response in a variable question 
        if happy == "yes": # the user esponds yes,
            time.sleep(1)#sets a delay for 1 second
            print ("very well") #print 'very well'
            break # breaks loop
        elif happy == "no": # if user says no,
            time.sleep(1)#sets a delay for 1 second
            print ("I am sorry to hear") # print I am sorry to hear
            break # breaks loop
        else: #if the input doesn't meet the pevious conditionals,
            print("invalid")# print invalid and reasks question
            
           

