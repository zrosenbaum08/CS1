print ('''
Zac Rosenbaum's Morning Rutine!
_____________________________________________________________________
''')

print ("⏰Alarm!⏰")

while True:
    snooze = str.lower(input("Snooze?"))

    if snooze == "yes":
        print ('''
go back to sleep for 5 minutes
''')
    elif snooze == "no":
        print ('''
Wake up!
⠀⠀⠀⠀⠀⠀⣀⣠⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⡿⠋⠉⠉⠻⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⣿⡄⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣷⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⢸⣿⣿⡿⠿⠿⠟⠛⠛⠻⢿⣿⣶⣄⠀⠀⠀
⠀⠀⠀⠀⠀⢈⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⠀⠈⠻⣿⣇⠀⠀
⠀⠀⠀⠀⢀⣾⡏⠀⠀⠀⠀⠀⠀⠀⣴⡿⠋⠉⠀⠀⠀⠀⠀⠀⠀⢹⡿⠀⠀
⠀⠀⣀⣤⣼⣿⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣷⣄⠀
⢠⣾⠟⠋⠉⠋⠀⠀⠀⠀⠀⠀⠀⠈⣿⣦⣀⣀⣀⣤⣤⣶⣶⠿⠋⠁⢹
⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⢉⣿⠋⠉⠉⠉⠁⠀⠀⠀⠀⢸⣿⠀
⢸⣿⠀⠀⠀⠀⠀⢀⣀⣀⣤⣴⠿⠋⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⢀⣴⣿⠏⠀
⢸⣿⡄⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⣸⣿⢶⣤⣤⣴⡶⠿⠛⠙⣿⠀
⠈⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⠀
⠀⠘⣿⣆⠀⠀⠀⠀⣠⣤⡀⠀⠀⠀⠀⠈⠻⣧⣀⡀⠀⠀⠀⣀⣠⣴⡿⠀
⠀⠀⠘⢿⣿⣦⣤⣴⡿⠻⠿⣷⣦⣤⣤⣤⣴⣾⣿⡿⠿⠿⠿⠟⠛⠀⠀⠀
⠀⠀⠀⠀⠉⢉⣉⠉⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')
        break
    else:
        print ('''
INVALID RESPONCE! (yes or no)
''')

while True:

    phone = str.lower(input("Go on your phone?"))
    
    if phone == "yes":
        print ('''
Addict
''')
        break
    elif phone == "no":
        print ('''

    Good decision
    ''')
        break
    else:
        print ('''
INVALID RESPONCE! (yes or no)
''')

print ('''

Take a shower :)
''')
while True:
    music = str.lower(input("listen to music?"))

    if music == "yes":
        print ('''
way to start your day!♪♪
''')
        break
    elif music == "no":
        print ('''
you okay? :(
''')
        break
    else:
        print ('''
INVALID RESPONCE! (yes or no)
''')

if music == "yes":
    while True:
            mtype = str.lower(input ("what kind of music? reggae, hip hop, or something else?♪♪"))
            
            if mtype == "reggae":
                print ('''
        ♪♪Jah man!♪♪
        ''')
                break
            elif mtype == "hip hop":
                print ('''
        ♪♪Nice!♪♪
        ''')
                break
            if mtype == "something else":
                print ('''
        ♪♪Good choice!♪♪
        ''')
                break
            else:
                print ('''
        INVALID RESPONCE! (reggae, hip hop, or something else)


    ''')
        
print ('''

Get dressed!!

''')
while True:
    breakfast = str.lower(input("Are you going to eat breakfast? Do you want eggs or cereal? both?"))

    if breakfast == "cereal":
        print ('''
Not bad
''')
        break
    elif breakfast == "eggs":
        print ('''
Healthy start!
''')
        break
    if breakfast == "both":
        print ('''
Thats a big breakfast!
''')
        break
    else:
        print ('''
INVALID RESPONCE! (cereal, eggs, or both)

''')

print ('''
Now brush your teeth
''')

while True:
    time = str.lower(input ("Check the time?"))

    if time == "yes":
        print ('''

Oh no!, your late, its time to get to school
''')
        break
    elif time == "no":
        
            timesure = str.lower(input ("Are you sure?"))

            if timesure == "yes":
                print ('''
You are going to miss your first class!
''')
                break
            elif timesure == "no":
                print ('''

Good choice, but you might be late to advisory!
''')
                break
            else:
                print ("INVALID RESPONCE! (yes or no)")

print ('''


Now get to school! Good Luck!

''')




        

