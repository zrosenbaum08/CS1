'''
Author: Zac Rosenbaum
Date: 5/13/2024
Description: Creates a password keeper by storing users input into a list with various modes 
Challenges: Modes 3,4,5 +add a function
Bugs: None
Sources:
'''
import random#imports the random library for all random functions
web_list = []#creates a new list with nothing in it for websites
user_list = []#creates a new list with nothing in it for usernames
pass_list = []#creates a new list with nothing in it for passwords

alphabet = list("abcdefghijklmnopqrstuvwxyz")#creates a list with the alphabet to generate a random password
special_characters = list("!@#$%^&*()_--+={}[]:;~'<>,.?/")#creates a list with special characters to generate a random password
numbers = list("1234567890")#creates a list of numebers
upper_alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")#creates a list of capital letters

def append_func(webapp, userapp, passapp):
    '''Appends inputed variables into the corresponding list
    Args:
        strings into lists
    Returns:
        No return, only adds to the lists
    Extraneous none
        description: takes in different inputs and adds them to the corresponding list'''
    web_list.append(webapp)
    user_list.append(userapp)
    pass_list.append(passapp)

while True:#sets a loop that continously runs the code til broken
    neww = input("what website would you like to add?(stop when you're done)")#asks the user what the website they would like to add is called
    if neww == ("stop"): #if the user inputed 'stop'
        break# breaks the loop
    newu = input("what is your username?")#asks for the username for the website
    newp = input("what is the password?")# asks for password(stores all variables)
    append_func(neww, newu, newp)# carries out the append func to add all the inputed elements to the lists

while True: #sets a loop that continously runs the code til broken
    mode_question = input('''
What mode would you like to use?
1.) Print Specifc
2.) Print All
3.) Add More Websties
4.) Change username/password
5.) Genrate a secure password
6.) Check if password is secure
7.) End
''')#asks user which mode they want to use and stores the input

    if mode_question == ("1"):#if user inputs 1,
        web_name = input("whats the website name?")#asks for the website they want to print
        if web_name in web_list:#if input in the list,
            i = web_list.index(web_name)#finds the index of the inputed website
            print(f'''Website:  {web_list[i]}
Username: {user_list[i]}
Password: {pass_list[i]}''')#prints the pass word and user along with password based on the index of the inputed website
        else:# if the if statement is not met,
            print("not in website names!")#print not in website names and asks again

    elif mode_question == ("2"):#if user inputs 2 to the mode question,
        for i in range(len(web_list)):#for the length of the website list
            print(f''' Website Name: {web_list[i]}
    Username: {user_list[i]}
    Password: {pass_list[i]}''')#prints all websites along with the other info based on location of the elements

    elif mode_question == ("3"):#if user inputs 3 to the mode question,
        while True:#sets a loop that continously runs the code til broken
            neww2 = input("what website would you like to add?(stop when you're done)")#asks user what website they would like to add and stores input
            if neww == ("stop"):#if user inputs 'stop'
                break#breaks the loop set
            newu2 = input("what is your username?")#asks for the username for the website
            newp2 = input("what is the password?")# asks for password(stores all variables)
            append_func(neww2, newu2, newp2)#carries out the append func to add all the inputed elements to the lists

    elif mode_question == ("4"):#if user inputs 4 to the mode question,
        while True:#sets a loop that continously runs the code til broken
            change_q = input("what website would you like to change")#ask what website user would like to change and stores the input

            if change_q in web_list:#if the input is in the list
                index = web_list.index(change_q)#sets the index of the website to a new variable
                user_list[index] = input("What is the new username?")#sets the input in the username list to the input for a new username
                pass_list[index] = input("What is the new password?")#sets the input in the password list to the input for a new password
                break#breaks the loop set
            else:#if the conditional is not met
                print("that is not a website!")#prints that the input is not a variable

    elif mode_question == ("5"):#if user inputs 5 to the mode question,
        secure_pass = ""#creates a new string with nothing in it
        rand_alph = random.randrange(5,8)#creates a random num between numbers
        rand_spec = random.randrange(3,5)#creates a random num between a set of different numbers
        for i in range(rand_alph):# for the amount in the random number,
            secure_pass += random.choice(alphabet)#adds the length of the rand num in elements to the string by randomizing the alphabet list
            secure_pass += random.choice(upper_alpha)#adds the same random amount of random uppercase letters to the string
        for i in range(rand_spec):# for the amount in the random number,
            secure_pass += random.choice(special_characters)#adds the length of the rand num in elements to the string by randomizing the special characters list
            secure_pass += random.choice(numbers)#adds the same random amount of random numbers to the string
        print(secure_pass)#prints the new string with random letters and numbers
    
    elif mode_question == ("6"):#if user inputed 6,
        check_pass_secure = input("what is your password: ")# asks user what the password they would like to check is and stores the input
        if len(check_pass_secure)<9:#if the length of the password is less than 9 characters
            print("too short")# tells the user it is too short
        if sum(char.isdigit() for char in check_pass_secure) <3:#if the amount of numbers in the password is less than 3
            print("need more numbers")# tells the user the password needs more numbers
        if sum(char in special_characters for char in check_pass_secure) <3:#if the amount of characters in the password that are in the special characters list is less than 3,
            print("need more special characters")#tells the user that the password needs more special characters
        if sum(char in upper_alpha for char in check_pass_secure) <3:#if the amount of captical letters in the password is less than 3
            print("need more uppercase letters")#tells the user that there are not enough capital letters
        if sum(char in alphabet for char in check_pass_secure) <5:#if the amount of lowercase letters in the password is less than 4
            print("need more lowervase letters")# tells the user that they need more lowercase letters
        else:
            print("password is secure")
    
    elif mode_question == ("7"):#if user inputs 6 to the mode question,
        print("BYEEEEEEEE :(")#prints bye
        break#breaks the continous loop of code

    else: #if condictionals not met,
        print("not apart of the modes!")#tells the user that they have inputed something not apart of the modes.
