import random #imports the random library to carry out all random functions
'''
Author: Zac Rosenbaum
Date: 11/13/2023
Description: Generates a random response from a list to the user's question
Challenges: func 5.5 + 8
Bugs: None
Sources: https://www.w3schools.com/python/python_howto_reverse_string.asp + lectures
'''

#function 1
def chorus(name): # defines the chorus function
    print("Happy Birthday to you,") #prints happy birthday to you
    print("Happy Birthday to you,") #prints happy birthday to you
    print(f'''Happy Birthday dear {name} 
''') #prints happy birthday to the name you enter   
def sing(name_q): #defines the sing function
    chorus(name_q)#carries out the chorus function with the name john
    chorus(name_q)#carries out the chorus function with the name john
    print("happy birthday toooooooooooooo you") #prints happy birthday toooooooooooooo you"
#function 2
def add(num1, num2):#defines the add functiona and enters the num inputs
    print(num1 + num2) #prints the sum of the inputed numbers
#function 3
def list_make(list_to_print): # defines the print list function to print the list given by the user
    for element in list_to_print: #for each element in the list given,
        print(element)#print the elements
#function 4
def contains_element(inlist, element):#defines the contains element fucntion to check if a string is in a list
    return element in inlist#returns true or false if the element is in the list
#function 5
def is_string_a_positive_number(string):#defines the function that checks if a string is a positive number
    if "-" in string:# if it has a dash/ negative
        string = string[1:]# makes the striing w/o the -
    if string.isnumeric():# gives true of false to if the string entered is a number
        return True# it reurns true
    else:# if the if doesnt work,
        return False# it reurns false
#function 5.5
def is_integer(number):#define the function that checks if an imput was an interger
    try: #tries the following
        number = int(number)# makes number into an interger
        return True # if it works it returns true
    except ValueError: # except value error if int(num) doesnt work and
        return False # it reurns false
def get_integer():#deifnes the get interger function to ask user for a number and check if interger
    while True: # makes the indented coade continusly run until broken
        number = input("Enter a number: ") # asks user for a number and stores it as an input

        if is_integer(number):#if you put number into the is_integer function
            return int(number) # returns true and breaks the while true
        else:# if the if statment is untrue, check
            print("that is not a number!")# print that is not a number 
#function 6
def rand_between():#defines the random between function 
    num1 = get_integer() # performs the get interger func to get a number
    num2 = get_integer() # performs the get interger func to get a number
    print(random.randint(num1,num2))# prints a random num between the 2 other numbers
#function 7
def replace_func(word, replace_old, replace_new):# defines replace func which replaces a strings letter with a new letter
    new_string = ""# sets a new string
    for character in word: # for/separates each letter in the word
        if character == replace_old:# if a character equals the letter repalced
            new_string += replace_new #add the new letter
        else: # if the if doesnt work
           new_string += character# new character = the old character
    return new_string #return new string
#fucntion 8
def backwards_return(return_q): # defines 
     txt = (return_q[::-1]) # creates a new interger which makes the input backwards
     print(txt)# prints the new backwards variable
#main
def main():#Creats the main function to run all functions


    #question
    while True: # sets a continous loop of code indented
        question = input("what function would you like? (1,2,3,ect.)(or end)")#asks the user what function to run and stores the input
        if question == ("1"):#if user replied '1' then
            name_q = input("What is your name?")# asks user for name for the song
            sing(name_q) # carry out the sing function
        elif question == ("2"): #if user replied '2' then
            num1 = get_integer()# runs the function to ensure the user inputs intergers
            num2 = get_integer()# runs the function to ensure the user inputs intergers
            add(num1, num2)# preforms the add func to add the two intergers together
        elif question ==("3"):#if user replied '3' then
            list_to_print = input("What is your list? Separate with commas").split(",")#asks the user fo a list and sepparates the strings with commas
            list_make(list_to_print)# carries out the 
        elif question == ("4"):#if user replied '4' then
            inlist = input("What is your list? Separate with commas").split(",")#asks the user fo a list and sepparates the strings with commas
            element = input("What would you like to check?")# asks for an element to check within the list
            print(contains_element(inlist, element))#carries out the conetains element function to check if the element is apart of the list given
        elif question == ("5"):#if user replied '5' then
            string = input("what would you like to check?")
            print(is_string_a_positive_number(string))# carries out the is string a positive number
            
        elif question == ("6"):#if user replied '6' then
            rand_between()# perform the rand between func to find a random num between the two inputs
        elif question == ("7"):#if user replied '7' then
            word = input("What is your word")# as for a word from user and stores the input
            replace_old = input("What string would you like to replace thats in the words")# Asks user what character they would like to replace in the entered word
            replace_new = input("What would you like to replace that with?")#Asks users for the character to replace and stores the input
            print(replace_func(word, replace_old, replace_new))#prints the replace func that replaces the character chosen
        elif question == ("8"):#if user replied '8' then
            return_q = input("what word would you like to reutrn backwards?")#asks user what they would like to reutrn backwards
            backwards_return(return_q)# prints the reversed word
        elif question == ("end"): #if user inputs 'end'
            break # it will stop running the question and end the program
        else:# else (if/elif don't work)
            print("goes through 8!")# tell user that past funtion 8 doesn't exist and asks them again
            

main()# runs the main function, which asks the question what funbction do you want to run
