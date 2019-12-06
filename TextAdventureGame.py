# Text adv game :D
import cmd
import textwrap
import sys
import os
import time
import random


screen_width = 100


#### Player setup (health, etc.) ####
global starter
starter = False

class player:
    def __init__(self):
        self.name = ''
        self.hp = 10
        self.cp = 0
        self.gen = ''
        self.loc = 'corridor'
        self.gameovr = False




myPlayer = player()

""" Title screen selection code """

def title_screen_selections():
    global takeable_things
    global inv
    global optionlast
    global options_start
    options_start = ['start', 'howto', 'quit']
    option = input(""">""")
    if option.lower() == ("start"):
        start_game()  # placeholder until written
    elif option.lower() == ("howto"):
        help_menu()
    elif option.lower() == ('bhoom'):
        hello = ("""
Ah, hello, Bhoom! I'll lead you to the game straight away!\n""")
        for character in hello:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        myPlayer.name = 'Bhoom'
        myPlayer.gen = 'male'
        time.sleep(3)
        prompt()
    elif option.lower() == ("quit"):
        quitter = input("""




                        Are you sure? (y/n)

        """)
        if quitter == ("y"):
            print("""





                            Well, seeya!

        """)
        time.sleep(3)
        sys.exit()



    else:
        restate = input(""">""")
        os.system('clear')
        print("""


                    Now that's a word I've never heard of...
                        I didn't understand that.
            Could you please type in something that I actually understand?
                                Thank you.


                  Choose between 'start', 'howto', or 'quit'.



        """)

        restate = input(""">""")
        if restate.lower() == ("start"):
            start_game()  # placeholder until written
        elif restate.lower() == ("howto"):
            howto()
        elif restate.lower() == ("quit"):
            quitter = input("""




                            Are you sure? (y/n)

            """)
            if quitter == ("y"):
                print("""





                                Well, seeya!

            """)
            time.sleep(3)
            sys.exit()

    potato = ['start', 'howto', 'quit']
    times_wrong = 2
    optionlast = input(""">""")
    os.system('clear')
    while restate not in potato:
        times_wrong += 1
        if times_wrong == 4:
            break
        print("""

                        No, I still didn't understand that.
                        Maybe we should try something else.

                            What? You want to try again?
                                Very well then...

                    Choose between 'start', 'howto', or 'quit'.


        """)

        if option.lower() == ("start"):
            start_game()  # placeholder until written
        elif option.lower() == ("howto"):
            howto()
        elif option.lower() == ("quit"):
            quitter = input("""




                                Are you sure? (y/n)

        """)
            if quitter == ("y"):
                print("""





                                    Well, seeya!

        """)
                time.sleep(3)
                sys.exit()

    os.system('clear')
    print("""


                That was not a valid option! I've gone out of my way to try and
                convince you to type in the correct answers by faking that I don't
                understand what you said. But I actually do! THEY'RE JUST NOT ONE
                OF THE *VALID OPTIONS!*

                Why did you say '%s'? That was not what you are supposed to say.
                Try saying either 'start', 'howto', or 'quit', and maybe I won't
                respond to you this way!




        """ % (optionlast))
    option = input(""">""")
    if option.lower() == ("start"):
        print("""

                Finally, some sense! I'll direct you to the game right away.
                Bye bye, and try not to anger me with invalid options again!



            """)
        time.sleep(6)
        os.system('clear')
        start_game()
    elif option.lower() == ("howto"):
        print("""

                Finally, some sense! I'll direct you to the tutorial right away.
                Bye bye, and try not to anger me with invalid options again!



            """)
        time.sleep(6)
        os.system('clear')
        howto()
    elif option.lower() == ("quit"):
        os.system('clear')
        quitter = input("""




                        Seriously? After all this time bothering
                        me, you're just gonna leave without
                        saying sorry?     (y/n)

        """)
        if quitter == ("y"):
            print("""





                        ......

                        Well...

                        Just... The next time you play this game,
                        please don't make me feel bad again.

                        I'm gonna cry soon... Goodbye now...

                        [sobs]

        """)
            time.sleep(7)
            sys.exit()

    else:
        os.system('clear')
        print("""


                Seriously, you one very stubborn person.
                Now please.
                Do. Not. Enter. Invalid. Commands!

                You can choose from 'start', 'howto', and 'quit'





        """)
        option = input(""">""")
        if option.lower() == ("start"):
            os.system('clear')
            print("""

                Finally, some sense! I'll direct you to the game right away.
                Bye bye, and try not to anger me with invalid options again!



            """)
            time.sleep(6)
            start_game()
        elif option.lower() == ("howto"):
            os.system('clear')
            print("""

                Finally, some sense! I'll direct you to the tutorial right away.
                Bye bye, and try not to anger me with invalid options again!



            """)
            time.sleep(6)
            howto()
        elif option.lower() == ("quit"):
            quitter = input("""




                        Seriously? After all this time bothering
                        me, you're just gonna leave without
                        saying sorry?     (y/n)

        """)
            if quitter == ("y"):
                print("""





                        ......

                        Well...

                        Just... The next time you play this game,
                        please don't make me feel bad again.

                        I'm gonna cry soon... Goodbye now...

                        [sobs]

        """)
                time.sleep(7)
                sys.exit()



# Menu Screen

def title_screen():
    os.system('clear')
    print("""

                            ||||||||||||||||||||||||||||||
                            |............................|
                            |.       Fix the Past       .|
                            |. *a text-adventure game.* .|
                            |.                          .|
                            |.        - start -         .|
                            |.        - howto -         .|
                            |.        - quit -          .|
                            |............................|
                            ||||||||||||||||||||||||||||||

                              Copyright 2019 rocketbhoom



    """)
    title_screen_selections()

def help_menu():
    os.system('clear')
    input_1 = input("""

                        |||||||||||||||||||||||||||||||||||||
                        |...................................|
                        |.        - Instructions -         .|
                        |.    This is a text-based game.   .|
                        |.   You can navigate using the    .|
                        |.  options on screen. Type them   .|
                        |.   in to the console to choose   .|
                        |.     that particular option.     .|
                        |.                                 .|
                        |.             [next]              .|
                        |...................................|
                        |||||||||||||||||||||||||||||||||||||

                             Copyright 2019 rocketbhoom



    """)

    if input_1.lower() == ("next"):
        os.system('clear')
        input_2 = input("""

                        |||||||||||||||||||||||||||||||||||||
                        |...................................|
                        |.          - Tutorial -           .|
                        |.    You're doing it! Good job.   .|
                        |.   Now try choosing something.   .|
                        |. Type in the option you want to  .|
                        |.            choose!              .|
                        |.                                 .|
                        |. {1 cookie}         {2 cookies}  .|
                        |.    [1c]               [2c]      .|
                        |...................................|
                        |||||||||||||||||||||||||||||||||||||

                             Copyright 2019 rocketbhoom

                        Note: type in the option key in the
                        [square] brackets. The ones in the
                          {curly} brackets are the full
                                    sentence. """)
        if input_2 == '2c':
            os.system('clear')
            input_4 = input("""

                        |||||||||||||||||||||||||||||||||||||
                        |...................................|
                        |.          - Tutorial -           .|
                        |.    Ha-ha, I knew you would do   .|
                        |.   that. That's awesome though,  .|
                        |.  you now know how to play text  .|
                        |.        adventure games!         .|
                        |.                                 .|
                        |.     {Return to menu screen}     .|
                        |.            [return]             .|
                        |...................................|
                        |||||||||||||||||||||||||||||||||||||

                             Copyright 2019 rocketbhoom


                    """)
            if input_4 == ("""return"""):
                title_screen()
        if input_2 == '1c':
            os.system('clear')
            input_3 = input("""

                        |||||||||||||||||||||||||||||||||||||
                        |...................................|
                        |.          - Tutorial -           .|
                        |.   Seriously? Most people take   .|
                        |.   two. That's awesome though,   .|
                        |.  you now know how to play text  .|
                        |.        adventure games!         .|
                        |.                                 .|
                        |.     {Return to menu screen}     .|
                        |.            [return]             .|
                        |...................................|
                        |||||||||||||||||||||||||||||||||||||

                             Copyright 2019 rocketbhoom


                    """)
            if input_3 == ("return"):
                os.system('clear')
                title_screen()




# Intro



def start_game():
    global takeable_things
    global inv
    global gender_2
    global availible_options
    global starter
    starter = False
    os.system("clear")
    question1 = """
    
Name your character.\n"""
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)

    player_name = input(""">""")
    myPlayer.name = player_name
    time.sleep(2)
    os.system('clear')
    name = ("""
%s?
""" % (myPlayer.name))
    for character in name:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    strange = ("""
A strange name.
A strange name indeed.
""")
    for character in strange:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(4)
    os.system('clear')
    gender = ("""


What is your character's gender?

(male/female/unknown)


""")

    for character in gender:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    gender_in = input("> ")
    if gender_in.lower() == ("male"):
        myPlayer.gen = 'boy'
        os.system('clear')
        confirm_gen = ("""
Hey there, %s! Just to confirm, your gender is '%s', correct?

(y/n)

""" % (myPlayer.name, gender_in))
        for character in confirm_gen:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.08)
        confirm_gender = input(">")
        if confirm_gender.lower() == ("n"):
            os.system('clear')
            oopsie = ("""
Huh? Computers are usually never wrong.
It should be a human error. \n
""")
            for character in oopsie:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(3)
            oopsie2 = ("""
Or are you intentionally pranking me?
IF YOU ARE...\n
Well, anyways, you may have to re-enter your gender.
        """)
            for character in oopsie2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(5)
            gender_2 = ("""


What is your character's gender?

(male/female/unknown)\n
""")



            for character in gender_2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            gender_2_in = input("> ")
            if gender_2_in.lower() == ("male"):
                os.system('clear')
                myPlayer.gen = 'boy'
                game()
            if gender_2_in.lower() == ("female"):
                os.system("clear")
                myPlayer.gen = 'girl'
                game
            if gender_2_in.lower() == ("unknown"):
                os.system("clear")
                myPlayer.gen = 'child'
                game()
                
                
        elif confirm_gender.lower() == ("y"):
            game()
    if gender_in.lower() == ("female"):
        myPlayer.gen = 'girl'
        os.system('clear')
        confirm_gen = ("""
Hey there, %s! Just to confirm, your gender is '%s', correct?

(y/n) \n """ % (myPlayer.name, gender_in))

        for character in confirm_gen:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.08)
        confirm_gen_in_2 = ("> ")
        if confirm_gen_in_2.lower() == ("n"):
            os.system('clear')
            oopsie = ("""
Huh? Computers are usually never wrong.
It should be a human error.
""")
            for character in oopsie:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(3)
            oopsie2 = ("""
Or are you intentionally pranking me?
IF YOU ARE...
Well, anyways, you may have to re-enter your gender.
        """)
            for character in oopsie2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(5)
            gender_2 = ("""


What is your character's gender?

(male/female/unknown)\n""")



            for character in gender_2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            gender_2_in = ("> ")
            if gender_2_in.lower() == ("male"):
                os.system('clear')
                myPlayer.gen = 'boy'
                game()
            if gender_2_in.lower() == ("female"):
                os.system("clear")
                myPlayer.gen = 'girl'
                game
            if gender_2_in.lower() == ("unknown"):
                os.system("clear")
                myPlayer.gen = 'child'
                game()
                
        elif confirm_gen_in2.lower() == ("y"):
            game()
    if gender_in.lower() == ("unknown"):
        myPlayer.gen = 'child'
        os.system('clear')
        confirm_gen = ("""
Hey there, %s! Just to confirm, you chose '%s', correct?

(y/n)

""" % (myPlayer.name, gender))
        for character in confirm_gen:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.08)
        confirm_gen_in = input(">")
        if confirm_gen_in.lower() == ("n"):
            os.system('clear')
            oopsie = ("""
Huh? Computers are usually never wrong.
It should be a human error.
""")
            for character in oopsie:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(3)
            oopsie2 = ("""
Or are you intentionally pranking me?
IF YOU ARE.../n
Well, anyways, you may have to re-enter your gender.
        """)
            for character in oopsie2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.08)
            time.sleep(5)
            gender_2 = ("""


What is your character's gender?

(male/female/unknown)
\n""")
            gender_2_in = input("> ")



            for character in gender_2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            if gender_2_in.lower() == ("male"):
                os.system('clear')
                myPlayer.gen = 'boy'
                game()
            if gender_2_in.lower() == ("female"):
                os.system("clear")
                myPlayer.gen = 'girl'
                game
            if gender_2.lower() == ("unknown"):
                os.system("clear")
                myPlayer.gen = 'child'
                game()
                
                
        if confirm_gen_in2.lower() == ("y"):
            game()







#########################
#    The actual game!   #
#########################





def game():
    global takeable_things
    global inv
    global starter
    os.system('clear')
    if starter == False:
        printer = ("""

%s, you are about to go on a journey.
It will not be an easy one, but I believe in you.
You can do it""" % (myPlayer.name))
        for character in printer:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.09)

        printy2 = ("""...

        """)
        for character in printy2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.5)
        time.sleep(2)
        os.system('clear')
        starter = True
        game()
        
        
        
    elif starter == True:
        os.system("clear")
        what = ("""
...


What was that?



        """)
        for character in what:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.09)
        time.sleep(5)
        os.system("clear")
        description = ("""

You sit up in your bed.

    """)
        for character in description:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(3)
        os.system("clear")
        no_2 =  ("""
You are %s, a %s living in the year 2072. You are in your bedroom. It is 1:34 AM.
Everything seems normal. Except for the fact that you just had a weird dream.
Somebody spoke to you about a journey. And that particular person (or thing)
believes in you.


Dismissing the thought, you go back to sleep, and decide that it isn't worth thinking
about.



                        {Continue}  [c]
""" % (myPlayer.name, myPlayer.gen))
        for character in no_2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)

    
        no_input = input("""
        
        """)
        if no_input == ('c'):
            os.system('clear')
            main_loop()



        
    


##### MAP #####
"""
1st floor


-----------------_______|-----------|------------|
|                |   p  |           | dining     |-------|
|                |   o  | doorstep  | room       kitchen |
|  Front yard    |   r  |           |
|                |   c  |-------|                        |
|           -----|   h  |       |    --------------------|
|           |    --------       |    - s t a i r s -     |
|           |     Garage        |                        |
|           |                   |------------------------|
--------------------------------|



2nd floor

|                   -N-


|------------------------------------------|
| bath | Granpa's | Grandma's | Player's   |
| room | bedroom  | bedroom   | bedroom    |
|------|----      |           |            |
| LAB ROOM |      |-----------|------------|-----|
|          |------|             corridor         |
|          |         |--------|-------------     |
|                    |bathroom|      stairs      |
|--------------------|--------|------------------|



|                   -S-

"""
name = ''
DESCRIPTION = 'look'
visited = False

UP = 'up'
DOWN = 'down'
FRWRD = 'forward'
BCKWRD = 'back'
LEFT = 'left'
RIGHT = 'right'
OUT = 'out'
global inv
global inv_gone
global inv_gone2
global takeable_things
inv_gone = False
inv_gone2 = False
inv = []
takeable_things = []
examinable_things = []



visited = {'bedroom': False, 'bathroom': False, 'livingroom': False, 'corridor': False,
            'stairs': False, 'kitchen': False, 'diningroom': False, 'porch': False,
            'frontyard': False, 'lab': False, 'bedroom2': False, 'bedroom3': False,
            'bathroomcorridor': False}


"""
2nd floor:

bedroom, bedroom2 (grandmother's bedroom,
grandmother is dead, room empty), bedroom3
(grandfather's bedroom), bathroom, livingroom,
corridor2, lab

1st floor:

kitchen, diningroom (next to porch)

Outside:

porch, frontyard

"""



mappy = {
    'bedroom': {
        name: ("%s's bedroom" % (myPlayer.name)),
        DESCRIPTION: """

This is your bedroom. A rather large room, it sits on the northeast side of the house.
There is a book on the floor. It's titled 'Time Travel Science'.
There is a picture of your parents on the windowsill.
There is an ancient Game Boy Advance that your dad always kept. The label on the cartridge
reads 'Sonic The Hedgehog'.
There is a chest of drawers. Inside contains your clothes, on top there is a Nintendo Glass,
your see-through hologram video game console.
Your backpack lays in the corner of the room.
To your front is the corridor.



        """,
        FRWRD: "corridor",
        BCKWRD: "",
        LEFT: "",
        RIGHT: "",
        UP: "",
        DOWN: "",


    },
    'corridor': {
        name: ("The 2nd floor corridor"),
        DESCRIPTION: """

This is the second floor corridor.
Not much to tell here.
To your left is the walkway to the Lab, going past both your grandparents's
rooms. To your right is a walkway to the stairs, lined with windows.
Behind you is your bedroom.


        """,
        FRWRD: "",
        BCKWRD: "bedroom",
        LEFT: "lab",
        RIGHT: "stairs",
        UP: "",
        DOWN: "",



    },
    'lab': {
        name: ("Granddad's laboratory"),
        DESCRIPTION: """

This is Granddad's lab.
There are papers on the workdesk.
There seems to be something glowing on the shelf. Looks like a small handheld game console.
There is a bottle with a strange-looking liquid labeled 'Prototype 2'. There's another sticker on it
saying 'Warning : contains acid'.
There are notes with your Granddad's handwriting taped all over the desk.
The computer is on. The screen glows faintly.
There is a special navigation function here. By typing 'walk', then typing 'out', 
you will exit the lab and move to the corridor.

Navigation : [left] will lead to bathroom.
             [right] will lead to Granddad's Bedroom.



        """,
        FRWRD: "",
        BCKWRD: "",
        LEFT: "bathroom",
        RIGHT: "bedroom3",
        UP: "",
        DOWN: "",
        OUT: "corridor"





    },



}
def print_loc():
    print('\n' + ('#' * (4 + len(myPlayer.loc))))
    print('# ' + myPlayer.loc.upper() + ' #')
    print('# ' + mappy[myPlayer.loc] [DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.loc))))
    
def prompt():
    global takeable_things
    global inv_gone
    global inv_gone2
    global inv
    os.system('clear')
    print_loc()
    print("""

To do something, use verbs such as 'examine' or 'inspect'
Or for movement, 'walk', then specify which direction.

Choose an option by typing it in and pressing enter.
Normal commands : 'menu', 'inv'(inventory), 'exit'
    
    
""")
    action = input(">")
    acceptable_actions = ['examine', 'walk', 'go to', 'talk', 'take', 'inv', 'menu', 'exit', 'inspect', 'look']
    walk_commands = ['walk', 'go to']
    look_commands = ['examine', 'inspect', 'look']
    while action.lower() not in acceptable_actions:
        os.system('clear')
        print("""
Huh? That doesn't seem to be in the options list. Try typing 
something that exists in there.
        
        
        
        """)
        action = input(">")
    if action.lower() == 'exit':
        os.system('clear')
        exitplay = ("""
Are you sure? You will lose all progress on the game so far,
and your character's name will be erased from the system.

(y/n)
    
        
        """)
        for character in exitplay:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        exitplay_input = input("""
>""")
        if exitplay_input == ("n"):
            prompt()
        elif exitplay_input == ("y"):
            goodbye = ("""
Goodbye, old friend. I hope to see you again.
            
            """)
            for character in goodbye:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            time.sleep(4)
            sys.exit()
        
    elif action.lower() in walk_commands:
        player_move(action.lower())
    elif action.lower() in look_commands:
        player_examine(action.lower())
    elif action.lower() == 'take':
        take_things()
    elif action.lower() == 'menu':
        options_screen()


        
        
def take_things():
    global inv
    global takeable_things
    take = ("""
What would you like to take?
Options : %s
(if none, no items)""" % (takeable_things))
    for character in takeable_things:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    take_input = input("> ")
    if myPlayer.loc == 'bedroom':
        if take_input == 'book':
            book_taken = ("""
You have taken the book.\n""")
            if 'book' not in inv:
                inv.append('book')
            else:
                for character in book_taken:
                    sys.stdout.write(character)
                inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                for character in inv_confirm:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                time.sleep(3)
                main_loop()






#        takeable_things = ['papers', 'notes', 'acid']
#        takeable_things = ['book', 'picture', 'gameboy', 'clothes', 'nintendoglass', 'backpack']


def player_move(myAction):
    global takeable_things
    global inv_gone
    global inv_gone2
    global inv
    ask = """
    
    
Use [forward], [backward], [left], [right], [up], or [down] to navigate.\n
\n """
    for character in ask:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    ask_in = ("> ")
    dest = input(ask_in)
    if dest in ['forward']:
        destination = mappy[myPlayer.loc][FRWRD]
        movement_handler(destination)
    elif dest in ['backward']:
        destination = mappy[myPlayer.loc][BCKWRD]
        movement_handler(destination)
    elif dest in ['left']:
        destination = mappy[myPlayer.loc][LEFT]
        movement_handler(destination)
    elif dest in ['right']:
        destination = mappy[myPlayer.loc][RIGHT]
        movement_handler(destination)
    elif dest in ['up']:
        destination = mappy[myPlayer.loc][UP]
        movement_handler(destination)
    elif dest in ['down']:
        destination = mappy[myPlayer.loc][DOWN]
        movement_handler(destination)

def movement_handler(destination):
    global takeable_things
    global examinable_things
    global inv
    global inv_gone
    global inv_gone2
    if UP == "":
        no = ("""
Whoops, you can't seem to punch through the ceiling to go up. 
And there are no pathways.\n""")
        for character in no:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(3)
        prompt()
    if DOWN == "":
        nope = ("""
Whoops, you can't seem to destroy the floor to go down.\nAnd there are no pathways.\n""")
    location_player = ("""
\nYou have moved to """ + destination + ".\n")
    for character in location_player:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)
    myPlayer.loc = destination
    if myPlayer.loc == 'lab':
        takeable_things = ['papers', 'notes', 'acid']
        examinable_things = ['shelf', 'computer', 'acid', 'papers', 'notes']
    if myPlayer.loc == 'bedroom':
        takeable_things = ['book', 'picture', 'gameboy', 'clothes', 'nintendoglass', 'backpack']
        examinable_things = ['book', 'picture', 'gameboy', 'nintendoglass']



    main_loop()
def player_examine(action):
    global takeable_things
    global examinable_things
    global inv_gone
    global inv_gone2
    global inv
    question = ("""
What would you like to examine?
These are the options : %s \n""" % (examinable_things))
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    if myPlayer.loc == 'lab':
        in_lab = input("> ")
        if in_lab == ("shelf"):
            shelf_examine = ("""
You can't seem to reach the handle to open the shelf.
The handheld-game-console looking object remains a mystery.\n""")
            for character in shelf_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        elif in_lab == ("computer"):
            computer_examine = ("""
The computer screen shows a calculator app with some numbers.
Beside the calculator app is a programming application that
you seem to know. Upon closer inspection, it seems to be
your favorite code editor, Sublime Text. It shows a 
Python file with just over one hundred thousand lines.

There also seems to be a text editor window open with some
notes that you can't make any sense out of.
\n
""")
            for character in computer_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        elif in_lab == ("acid"):
            acid_examine = ("""
The liquid inside the bottle seems to glow. You wonder how corrosive this would be.

You discover that the label on the bottle can unfold. You read :

"Activates when in contact with air."

That's just about it that you can find on the bottle.\n """)
            for character in acid_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()

        elif in_lab == ("papers"):
            papers_examine = ("""
The papers have calculations and weird symbols on them. Some have
some pictures drawn on them. You're not that smart, but judging by
the line on a sheet of paper that has years written on it with arrows
pointing backwards and forwards, it has something to do with time.
\n""")
            for character in papers_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        elif in_lab == ("notes"):
            notes_examine = ("""
The notes have 'more power' and 'add return function' on them. 
There are some more, but you can't quite read them as they've been crossed out.\n""")
            for character in notes_examing:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        while in_lab not in examinable_things:
            invalid = ("""
You can't seem to spot any such thing. I wonder, how exactly did you come up
with that word? It seems supernatural. Hmm....""")
            for character in invalid:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            time.sleep(3)
            prompt()
    if myPlayer.loc == 'bedroom':
        in_pbed = input("> ")
        if in_pbed == ("book"):
            book_examine = ("""
This book used to be your Granddad's. He had finished it 10 times, 
and now occationally reads it, but otherwise, it's yours. 
""")
            for character in book_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        elif in_pbed == ("picture"):
            picture_examine = ("""
This is a picture of your parents at the park. The sky is brown with dust, but otherwise,
this picture is beautiful. 

You check the date written on the back. 2061.
""")
            for character in picture_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        elif in_pbed == ("gameboy"):
            gameboy_examine = ("""
This is an antique your father kept. It was given to him by his father, who got it 
second-hand. The screen is scratched slightly.

The cartridge inside says 'Sonic The Hedgehog'. Sonic was a character your Granddad
always liked. 
""")
            for character in gameboy_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        elif in_pbed == ("nintendoglass"):
            nintendoglass_examine = ("""
This was your Christmas present 2 years ago. The Nintendo Glass was only a tab of glass
and a game controller. When the button on the little tab was pressed, a holographic screen would appear,
the size of a 2019 home flat-screen TV. 

The CPU of the glass tab would automatically update and get new games every day.

""")
            for character in nintendoglass_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        while in_pbed not in examinable_things:
            os.system('clear')
            invalid2 = ("""
You can't seem to spot any such thing. I wonder, how exactly did you come up
with that word? It seems supernatural. Hmm....""")
            for character in invalid2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            time.sleep(3)
            prompt()



def inventory_check():
    global takeable_things
    global inv_gone
    global inv_gone2 
    global inv
    os.system('clear')
    print(inv)
    inv_return = input("""
This is your inventory. Type in 'r' to return to menu screen.\n""")
    if inv_return == ("r"):
        main_loop()
    
def main_loop():
    global takeable_things
    global inv
    while myPlayer.gameovr is False:
        prompt()
def menu():
    welcome_message = ("""
Welcome to the menu screen.\n""")
    for character in welcome_message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    menu = ("""
################################
#          [ Menu ]            #
#                              #
#                              #
#      [r] Return to game.     #
#    [inv] Check inventory.    #
#    [exit] Quit the game.     #
#   [option] Check options.    #             
#                              #
################################\n""")
    for character in menu:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.0002)
    menu_input = input("> ")
    if menu_input.lower() == ('r'):
        os.system('clear')
        prompt()
    elif menu_input.lower() == ('inv'):
        inventory_check()
    elif menu_input.lower() == ('option'):
        options_screen()
    elif menu_input.lower() == ('about'):
        about()
    elif menu_input.lower() == ('exit'):
        exitsure = ("""
Are you sure, buddy? All your progress will be lost, and your character's
name will be erased from the system. (y/n)\n""")
        for character in exitsure:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        exit_in = input("> ")
        if exit_in == ('y'):
            goodbye_menu = ("""
Well, goodbye. Hope to see you again.

Till next time!\n""")
            for character in goodbye_menu:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            sys.exit()
    



def options_screen():
    os.system('clear')
    menu_screen = ("""
         #################################
         #           [ MENU ]            #
         #                               #
         #      [r] Return to game.      #
         #    [inv] Check inventory.     #
         #  [about] About the creator.   #
         #    [exit] Quit the game.      #
         #                               #
         #                               #
         #################################\n""")
    for character in menu_screen:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.002)
    input_menu = input("""> """)
    if input_menu.lower() == ('r'):
        time.sleep(1)
        prompt()
    elif input_menu.lower() == ('inv'):
        inventory_check()
    elif input_menu.lower() == ('about'):
        about()
    elif input_menu.lower() == ('exit'):
        exitsure = ("""
Are you sure, buddy? All your progress will be lost, and your character's
name will be erased from the system. (y/n)\n""")
        for character in exitsure:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        exit_in = input("> ")
        if exit_in == ('y'):
            goodbye_menu = ("""
Well, goodbye. Hope to see you again.

Till next time!\n""")
            for character in goodbye_menu:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            sys.exit()
        elif exit_in == ('n'):
            yay = ("""
Yay! I'll lead you back to the menu right away!\n""")
            for character in yay:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            options_screen()

def about():
    about_text = ("""
Bhoom Tansirimas (aka rocketbhoom) is an 11-year-old boy who loves coding.
He only writes Python. In his spare time, he likes to read, and listen to music.


Note : All info written here is from the time of coding (Dec 2019).
       To download the latest version of this game, or to get
       more up-to-date information, go to :


       


Type in [r] to return to the menu selection screen. \n""")
    for character in about_text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    about_in = input("> ")
    if about_in == ('r'):
        options_screen()





title_screen()