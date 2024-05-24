'''
Author: Zac Rosenbaum
Date: 11/30/2023
Description: Generates a random responce from a list to play rock paper scissors, or allow 2 people to play
Challenges: Exits when you say stop, can play a bot or user2, 
Bugs: Calls the bot player 2 instead of 'bot'
Sources: class lectures
'''
import random #bring in the random library for all random functions
import sys #bring in the sys library for use of the exit() function
user1_score = 0 # creates the variable user1 to keep track of user 1's score; sets to 0
user2_score = 0 # sets user2's score to 0
rpslist = ["rock", "paper", "scissors"] # creates a list for ramdomizing 

while True: # creates a loop that continuously runs the code
    while True: # creates a loop that continuously runs the code
        rpsplay = str.lower(input("Do you want to play rock, paper, scissors?"))# prompts user for a question and stores their response in a variable rpsplay
    
        if rpsplay == "no": # if the user answers 'no' then,
            sys.exit() #exits the program
        elif rpsplay == "yes": # if they didn't input 'no' try, 'yes', if so,
            while True: # creates a loop that continuously runs the code
                comp_or_player = str.lower(input("Do you want to play the computer or a player? "))# prompts user for a question and stores their response in a variable

                if comp_or_player not in ["computer", "player"]: # if the user doesn't input computer or player then,
                    print("Invalid") # print invalid
                else: # if it doesn't meet previous condition, then, 
                    while True: # creates a loop that continuously runs the code
                        player1_rps = str.lower(input("player 1, pick either: rock, paper, or scissors"))# prompts user for a question and stores their response in a variable

                        if player1_rps not in rpslist: # if player responce is not inside the rps list,
                            print("Invalid") # print invalid
                        else: # if it doesn't meet previous conditionals, then,
                            break # breaks the loop
                        
                    if comp_or_player == "computer": # if user answered computer then,
                        player2_rps = random.choice(rpslist) # sets the random of rpslist to be player 2
                        break #breaks loop
                    elif comp_or_player == "player": #if the user didn't say stop check if they said player, if so, 
                        while True: # creates a loop that continuously runs the code
                            player2_rps = str.lower(input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n player 2, pick either: rock, paper, or scissors" ))# prompts user for a question and stores their response in a variable and has spaces so they cant see player1's responce

                            if player2_rps not in rpslist: #if player responce is not inside the rps list,
                                print("Invalid") # print invalid
                            else: # if it doesn't meet previous conditionals, then,
                                break # breaks the loop
                        break # breaks the loop
            break # breaks the loop
        else: #if it didn't meet the precious conditionals,
            print("Invalid Responce (yes or no)") #prints 'invalid responce' and reasks the question because of the while true loop 

    while True: # creates a loop that continuously runs the code
        print("PLAYER 1:") # adds title to player score
        print(player1_rps) # print's player1's answer
        print("PLAYER 2:")  # adds title to player score
        print(player2_rps) # print's player2's answer
        
        if player1_rps == player2_rps: # if their answers are the same/equal,
            print("tie") #print tie
        elif player1_rps == "rock": #if the user didn't meet conditional, check rock, if so,
            if player2_rps == "scissors": # check if user2 said scissors if so,
                print("Player 1 wins!")# print player 2 wins
                user1_score += 1# add one point to user1 score
            elif player2_rps == "paper": #if the user2 didn't prev conditional, check paper, if so,
                print("Player 2 wins!")#print player 2 wins
                user2_score += 1 # add point to player 2
        elif player1_rps == "paper":#if the user1 didn't meet conditional, check paper, if so,
            if player2_rps == "rock": # check if player 2 said rock, if so
                print("Player 1 wins!") #print player 1 wins
                user1_score += 1 # adds point to player ones score
            elif player2_rps == "scissors": #if the user2 didn't meet conditional, check scissors, if so,
                print("Player 2 wins!")# print player 2 wins
                user2_score += 1 # add point to player 2 score
        elif player1_rps == "scissors": #if the user 1 didn't meet conditionals aboce, check scissors, if so,
            if player2_rps == "paper": # check if player 2 said paper, if so
                print("Player 1 wins!") #print player 2 wins
                user1_score += 1 #adds to player1's score
            elif player2_rps == "rock":#if the user2 didn't meet conditional, check rock, if so,
                print("Player 2 wins!") # print player2 wins
                user2_score += 1 # add point to player 2's score

        print(f"Score is Player1 - {user1_score} Player2 - {user2_score}")#prints score board
        break # breaks the loop

                


