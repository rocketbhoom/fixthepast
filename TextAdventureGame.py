# Text adv game :D
import cmd
import textwrap
import sys
import os
import time
import random
import termcolor
import curses
import random
from random import seed
from random import randint
from termcolor import colored, cprint

screen_width = 100
seed(1)
#### Player setup (health, etc.) ####
global starter
starter = False

class player:
    def __init__(self):
        self.name = ''
        self.nickname = ''
        self.hp = 10
        self.cp = 0
        self.gen = ''
        self.loc = 'corridor'
        self.gameovr = False
        self.easy = False
        self.medium = False
        self.hard = False




myPlayer = player()
questions = 1
perfect = False
outof = 3
points = 0
line = ("")



""" Title screen selection code """

def title_screen_selections():
    potato = ['start', 'howto', 'quit']
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
Creator hack accepted.\n""")
        for character in hello:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        myPlayer.name = 'Bhoom'
        myPlayer.gen = 'male'
        time.sleep(3)
        ques_10_1()
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



    elif option.lower() not in potato:
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

    times_wrong = 2
    optionlast = input(""">""")
    os.system('clear')
    while restate not in potato:
        times_wrong += 1
        restate2 = input("> ")
        if times_wrong < 4:
            print("""

                            No, I still didn't understand that.
                            Maybe we should try something else.

                                What? You want to try again?
                                    Very well then...

                        Choose between 'start', 'howto', or 'quit'.


            """)

            if restate2.lower() == ("start"):
                start_game()  # placeholder until written
            elif restate2.lower() == ("howto"):
                howto()
            elif restate2.lower() == ("quit"):
                quitter = input("""




                                    Are you sure? (y/n)

            """)
                if quitter == ("y"):
                    print("""





                                        Well, seeya!

            """)
                    time.sleep(3)
                    sys.exit()

        if times_wrong > 4:

            os.system('clear')
            cprint("""


                        That was not a valid option! I've gone out of my way to try and
                        convince you to type in the correct answers by faking that I don't
                        understand what you said. But I actually do! THEY'RE JUST NOT ONE
                        OF THE VALID OPTIONS!

                        Why did you say that? That was not what you are supposed to say.
                        Try saying either 'start', 'howto', or 'quit', and maybe I won't
                        respond to you this way!




                """, "red", attrs=['bold'])
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

        elif times_wrong > 6:
            os.system('clear')
            cprint("""


                    Seriously, you one very stubborn person.
                    Now please.
                    Do. Not. Enter. Invalid. Commands!

                    You can choose from 'start', 'howto', and 'quit'





            """, "red", attrs=['bold', 'underline', 'blink'])
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
        myPlayer
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
                game()
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
canada_done = False
saudi_done = False
korea_done = False
ger_done = False
iran_done = False
japan_done = False
russia_done = False
india_done = False

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



visited = {'bedroom': False, 'bathroom': False, 'corridor': False,
            'stairs': False, 'kitchen': False, 'diningroom': False,
            'lab': False, 'bedroom2': False, 'bedroom3': False,
            'bathroomcorridor': False, '1stfloor': False, 'stairs1': False,
            'doorstep': False}


solved = {'china': False, 'usa': False, 'india': False, 'russia': False, 'japan': False, 'germany': False, 'iran': False, 'saudiarabia': False, 
          'korea': False, 'canada': False}




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

map_game = {
    'china': {
        name: ("China"),
    },
}

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
    'doorstep': {
        name: ("Doorstep"),
        DESCRIPTION: """
This is the doorstep. Quite dusty.
You don't dare open the door, for fear of dust.
Nothing to see here.
Go backwards to the path to the stairs.""",
        FRWRD: "",
        BCKWRD: "1stfloor",
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
To your right is the walkway to the Lab, going past both your grandparents's
rooms. To your left is a walkway to the stairs, lined with windows.
Behind you is your bedroom.


        """,
        FRWRD: "",
        BCKWRD: "bedroom",
        LEFT: "stairs",
        RIGHT: "lab",
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
        OUT: "corridor",





    },
    'bathroom': {
        name: ("The Lab's bathroom"),
        DESCRIPTION: """
Why are you in the bathroom?
There doesn't seem to anything to do here, unless you count flushing the 
toilet as interesting.

Let's go. Navigation directions : Backward (to lab), and right (Granddad's Bedroom). 
""",
        FRWRD: "",
        BCKWRD: "lab",
        LEFT: "",
        RIGHT: "bedroom3",
        UP: "",
        DOWN: "",





    },
    'stairs': {
        name: ("Stairs"),
        DESCRIPTION: """
These are the stairs leading down.
To go down, type [walk], then [down].
To walk back to the corridor type [walk], then [right].
""",
        FRWRD: "",
        BCKWRD: "stairs",
        LEFT: "",
        RIGHT: "corridor",
        UP: "",
        DOWN: "1stfloor",





    },
    '1stfloor': {
        name: ("1st Floor"),
        DESCRIPTION: """
This is the first floor.
To your right is the path to the kitchen and the dining room.
To your left is the doorstep.
Behind you are the stairs.""",
        FRWRD: "",
        BCKWRD: "stairs1",
        LEFT: "doorstep",
        RIGHT: "diningroom",
        UP: "",
        DOWN: "",





    },
    'stairs1': {
        name: ("Stairs"),
        DESCRIPTION: """
These are the stairs leading up.
To go up, type [walk], then [up].
To walk back type [walk], then [backwards].
""",
        FRWRD: "",
        BCKWRD: "1stfloor",
        LEFT: "",
        RIGHT: "",
        UP: "corridor",
        DOWN: "",





    },
    'diningroom': {
        name: ("Dining room"),
        DESCRIPTION: """
This is the dining room. All the plates on the table are upside down,
to protect from dust. A heating stove sits on the table.

There are chairs sitting around the table. All are covered with big pieces of cloth,
only the legs are visible.
There is a path to the right leading to the kitchen.
Walk backwards to go back.""",
        FRWRD: "",
        BCKWRD: "1stfloor",
        LEFT: "",
        RIGHT: "kitchen",
        UP: "",
        DOWN: "",





    },
    'kitchen': {
        name: ("Kitchen"),
        DESCRIPTION: """
This is the kitchen. A wash basin sits over to the left. There are shelves
stacked with instant noodles. A drawer labled 'Cutlery' sits near the 
wash basin.

Behind you is the path to the dining room.
In front of you is the path leading to the bathroom.""",
        FRWRD: "bathroomcorridor",
        BCKWRD: "diningroom",
        LEFT: "",
        RIGHT: "",
        UP: "",
        DOWN: "",





    },
    'bedroom2': {
        name: ("Grandma's Bedroom"),
        DESCRIPTION: """
This was your Grandma's bedroom. The room is empty and cold.
You decide to leave, as seeing her room, you can't bear to think 
about the fact that she's dead.

Leave by typing [walk], then [backward]
Move to Granddad's bedroom by walking right.""",
        FRWRD: "",
        BCKWRD: "corridor",
        LEFT: "",
        RIGHT: "bedroom3",
        UP: "",
        DOWN: "",





    },
}




##### MAP #####
"""
-----------------_______|-----------|------------|
|                |   p  |           | dining     |-------|
|                |   o  | doorstep  | room       kitchen |-------|
|  Front yard    |   r  |           |                    bathroom|
|                |   c  |-------|                        |-------|
|           -----|   h  |       |    --------------------|
|           |    --------       |    - s t a i r s -     |
|           |     Garage        |                        |
|           |                   |------------------------|
--------------------------------|

"""


def print_loc():
    if myPlayer.loc == ('bedroom3'):
        bedroom3()
    else:
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
    while myPlayer.loc != 'bedroom3':
        print_loc()
        print("""

To do something, use verbs such as 'examine' or 'inspect'
Or for movement, 'walk', then specify which direction.

Choose an option by typing it in and pressing enter.
Normal commands : 'menu', 'inv'(inventory), 'exit'
        
        
""")
        action = input("> ")
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
> """)
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
    if myPlayer.loc == 'bedroom3':
        bedroom3()



        
        
def take_things():
    global papers_taken_yes
    global inv
    warned = False
    global takeable_things
    if len(inv) < 10:
        take = ("""
What would you like to take?
Options : %s
""" % (takeable_things))
        for character in take:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        if myPlayer.loc == 'bedroom':
            bedroom_take = input("> ")
            if bedroom_take.lower() == 'book':
                book_taken = ("""
You have taken the book.\n""")
                for character in book_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'book' not in inv:
                    inv.append('book')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
            elif bedroom_take.lower() == 'picture':
                picture_taken = ("""
You have taken the picture.\n""")
                for character in picture_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'picture' not in inv:
                    inv.append('picture')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
            elif bedroom_take.lower() == 'gameboy':
                gameboy_taken = ("""
You have taken the Game Boy.\n""")
                for character in gameboy_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'gameboy' not in inv:
                    inv.append('gameboy')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
            elif bedroom_take.lower() == 'clothes':
                clothes_taken = ("""
You have taken the your clothes.\n""")
                for character in clothes_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'clothes' not in inv:
                    inv.append('clothes')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
            elif bedroom_take.lower() == 'nintendoglass':
                nintendoglass_taken = ("""
You have taken your Nintendo Glass.\n""")
                for character in book_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'nintendoglass' not in inv:
                    inv.append('nintendoglass')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
            elif bedroom_take.lower() == 'backpack':
                backpack_taken = ("""
You have taken your backpack.\n""")
                for character in backpack_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'backpack' not in inv:
                    inv.append('backpack')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
        elif myPlayer.loc == 'lab':
            lab_take = input("""> """)
            if lab_take.lower() == ('papers'):
                papers_taken = ("""
You fold the papers and put them in your pocket. I wonder, will
your Granddad get mad at you for taking his papers?\n""")
                papers_taken_yes = True
                for character in backpack_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'papers' not in inv:
                    inv.append('papers')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
            elif bedroom_take.lower() == 'acid':
                acid_taken = ("""
You carefully take the acid. Let's hope it doesn't come in contact with air, 
and activate.\n""")
                for character in acid_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'acid' not in inv:
                    inv.append('acid')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
        elif myPlayer.loc == ('kitchen'):
            kitchen_input = input("> ")
            if kitchen_input.lower() == 'instantnoodles':
                noodles_taken = ("""
You pocket a bag of instant noodles. For later.\n""")
                for character in noodles_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                if 'noodles' not in inv:
                    inv.append('noodles')
                    inv_confirm = ("""
This is your inventory:
%s\n""" % (inv))
                    for character in inv_confirm:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    time.sleep(3)
                    main_loop()
        elif myPlayer.loc == ('diningroom'):
            diningroom_in = input("""> """)
            if diningroom_in.lower() == ("plates"):
                plates_taken = ("""
You lift up the plate. Doesn't seem to fit in your pocket.\n""")
                for character in plates_taken:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                time.sleep(3)
                main_loop()



    elif len(inv) > 8:
        if warned == False:
            nearly = ("""
You may only store 10 items in your inventory. You currently have %d
items in your inventory.""" % (len(inv)))
            for character in nearly:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            warned = True
        elif warned == True:
            take_things()




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
    if destination == '':
        invalid_direction = ("""
There doesn't seem to be a pathway leading to that direction.
And you don't seem to be a Kung Fu master, so you can't 
punch through the walls.""")
        for character in invalid_direction:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(3)
        prompt()
    else:
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
        elif myPlayer.loc == 'bedroom':
            takeable_things = ['book', 'picture', 'gameboy', 'clothes', 'nintendoglass', 'backpack']
            examinable_things = ['book', 'picture', 'gameboy', 'nintendoglass']
        elif myPlayer.loc == 'bathroom':
            examinable_things = ['nothing']
        elif myPlayer.loc == 'kitchen':
            examinable_things = ['shelves', 'washbasin']
            takeable_things = ['instantnoodles']
        elif myPlayer.loc == 'diningroom':
            examinable_things = ['chair']
            takeable_things = ['plates']
        elif myPlayer.loc == 'corridor' or 'stairs' or 'bedroom2' or 'bedroom3' or '1stfloor' or 'stairs1' or 'doorstep':
            del examinable_things[:]
            del takeable_things[:]









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
    elif myPlayer.loc == 'bathroom':
        in_bathroom = input('> ')
        if in_bathroom == ("nothing"):
            hint = ("""
You have found a hint!
The hint is : What you are looking for lies in Granddad's Bedroom.

Good luck!\n""")
            for character in hint:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        while in_bathroom not in examinable_things:
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
    elif myPlayer.loc == 'kitchen':
        in_kitchen = input("""> """)
        if in_kitchen == 'shelves':
            shelves_examine = ("""
You only see stacks of instant noodles on top of each other. The shelf
itself looks quite old, but only because of the dust covering it.

The noodles seem to expire next year.\n""")
            for character in shelves_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        elif in_kitchen == 'washbasin':
            washbasin_examine = ("""
This is the wash basin.
It looks clean on the inside.
On the outside it's dusty.

The faucet dates back to 2015. It has an old-fashioned handle instead 
of turning on the moment you approach it like most faucets do.

There is a dish holder near the wash basin. It's covered with a piece of cloth.
""")
            for character in washbasin_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            time.sleep(3)
            prompt()
        while in_kitchen not in examinable_things:
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
    elif myPlayer.loc == 'diningroom':
        in_diningroom == input("> ")
        if in_diningroom == 'chair':
            chair_examine == ("""
The chair dates back to 2030.
It's a wooden chair. One of your Granddad's.

There's nothing interesting about the chair you can find.
""")
            for character in chair_examine:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
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
def bedroom3():
    global papers_taken_yes
    bedroom3_info = ("""
This is your Granddad's bedroom.
Your Granddad is currently in there.


There are pictures of famous scientists on the wall.
There is a notebook on the bedside table.




"Well, hello, %s!" your Granddad says. "What brings you here?"


[a] : "Nothing, just wanted to check on you."
[b] : "I wanted to ask you something."\n\n""" % (myPlayer.name))
    for character in bedroom3_info:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    bedroom3_in1 = input("> ")
    if bedroom3_in1 == ("a"):
        nice = ("""
"That's nice of you, %s! Well, anyways, I better get out of bed already."
Your Granddad starts to get up.

"What say we go over to the Lab and have a little chat?"

You nod in agreement.

""" % (myPlayer.name))
        for character in nice:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(3)
        moved = ("""
You have moved to lab.""")
        for character in moved:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(3)
        lab_chatting()
    elif bedroom3_in1 == 'b':
        ask = ("""
"Hmm? Well, you say you want to ask me a question? Ask away!"



[a] - "What are you working on?"
[b] - "Why do you have books on time travel?"
\n""")
        for character in ask:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        print("we got til here")
        ask_input_1 = ("> ")
        if ask_input_1.lower() == 'a':
            path2()
            print("did we get here?")

        elif ask_input_1.lower() == 'b':
            path1()



def lab_chatting():
    time_machine = colored("""handheld time machine""", "red", attrs=['bold'])
    working_on = ("""
"Do you know what I'm working on?"



[y] - Yes
[n] - No\n\n\n""")
    for character in working_on:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    working_in = input("> ")
    if working_in.lower() == ("n"):
        no = ("""
Your Granddad chuckles.

Granddad opens the shelf and takes out an object. It looks like the game-
console-looking thing.


"This is a %s." """ % (time_machine))
        for character in no:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        time.sleep(3)
        next()
        
    elif working_in.lower() == ("y"):
        yes = ("""
"Wow, really? And I thought I was being secret about it."

Your Granddad chuckles.

Granddad opens the shelf and takes out an object. It looks like the game-
console-looking thing.


"This is a %s." """ % (time_machine))
        for character in yes:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        time.sleep(3)
        next()

        






def next():
    serious = ("""
"Yes, I'm serious!"

Your Granddad laughs. 

"I've been trying this out many times. I don't anymore, though, I'm too old
to travel back through space-time again. And ever since that epidemic occured,
I don't dare exit the house to find new parts."


You have no idea what he's talking about. What epidemic?


                            [c]
                        {continue}

\n""")
    for character in serious:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    serious_in = input("> ")
    if serious_in.lower() == 'c':
        serious2 = ("""
"Ah, of course! You don't know anything about the epidemic yet.
It occured a few months after your birth. Your parents immediately
went out and filed a complaint to the plastic and meat industry."


"Why meat, Granddad? There's nothing wrong with meat, is there?"
\n

                          [c]
                      {continue}\n\n""")
        for character in serious2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        serious2_in = input("> ")
        if serious2_in == 'c':
            meat = ("""
Your Granddad looks at you.


"Meat production is extremely climate-harming." Granddad says.
"for each hamburger you eat, it requires 660 gallons of water, did you know that?
Plus, cows produce a lot of waste and methane, multiply that by 200 cows in each farm.
We're not even supposed to be eating meat. Our intestines are meant for eating plants.
Farming a lot of cows also produces sicknesses, so antibiotics are used. But that increases
the chance of creating a superbug, an antibiotic-resistant virus that could plague the world.
So, naturally, your mom and dad, who were vegans, like me, went against the meat industry.\n

                         [c]
                      {continue}
\n\n\n""")
            for character in meat:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            meat_in = input("> ")
            if meat_in == 'c':
                died = ("""
Granddad sighs.

“They both died from the disease itself, after a few months. You were hardly 1 year old at that time.”
"The environment has gotten so much worse because nobody listened at that time. And now it's so bad
that even I can't have created a gadget to help the world."\n\n
""")
                for character in died:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.08)
                time.sleep(3)
                os.system('clear')
                stringy = ("")
                if myPlayer.gen == 'boy':
                    stringy = ("m'boy")
                elif myPlayer.gen == 'girl':
                    stringy = (myPlayer.name)
                brainwave = ("""
"Why don't we go back and prevent the disease from being created by using the time machine, Granddad?"

Your Granddad looks at you. 

"I would love to do that, %s, but I'm too old to travel through time anymore. If I do, there is a 
risk that I would die along the way."



"Then why don't I do it?"


"It's too dangerous, %s. I wouldn't want to lose you too." 


""" % (myPlayer.name, myPlayer.name))
                for character in brainwave:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.07)
                time.sleep(4)
                choice_text = ("""
Make the choice.




[a] - "I can do it."
[b] - Agree, and abandon the idea.
\n""")
                for character in choice_text:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                choice_input = input("> ")
                if choice_input == 'a':
                    sure_message = ("""
"Are you sure, %s? This is very dangerous. Think carefully."


You start to have doubts.



Confirm your choice.


[y] - "Yes"
[n] - "No" """ % (myPlayer.name))
                    for character in sure_message:
                        sys.stdout.write(character)
                        sys.stdout.flush()
                        time.sleep(0.05)
                    sure_input = input("> ")
                    if sure_input == 'y':
                        go = ("""
Your Granddad looks at you and sighs.

"I guess." Granddad slowly says.\n """)
                        for character in go:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.05)
                        time.sleep(3)
                        go2 = ("""
"I don't want you to be in danger, but..."

Granddad looks stressed.
\n""")
                        for character in go2:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.08)
                        time.sleep(4)
                        go3 = ("""
"The time machine is to be handled carefully, it's very delicate."
"It can only be powered by 2 quartz crystals, and can only be 
kick-started with equipment of today, so you should mind the power. 
If you run out of power, you would be stuck in the past." 


Your Granddad reels that off and then looks at you.



"If anything happened to you, your mother would never forgive me."

Granddad chuckles. """)
                        for character in go3:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.07)
                        time.sleep(4)
                        go4 = ("""
"Press the yellow button to travel. Spin the dial to adjust the year. Those are the
basics."


Granddad puts his arm on your shoulder.

"Good luck, %s."\n\n\n""" % (myPlayer.name))
                        for character in go4:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.06)
                        time.sleep(5)
                        go5 = ("""
You set the dial for 2019.





"Come back, okay?" Granddad says.



Type in 't' to travel. """)
                        for character in go5:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.07)
                        input_time = input("> ")
                        if input_time.lower() == 't':
                            initiated = colored("""
\n\nTime travel initiated.""", "red", attrs=['bold'])
                            for character in initiated:
                                sys.stdout.write(character)
                                sys.stdout.flush()
                                time.sleep(0.05)
                            time.sleep(2)
                            cprint("""
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||    
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||""", "red", attrs=['reverse', 'bold', 'blink'])
                            time.sleep(5)
                            os.system('clear')
                            game_true()







    while serious_in.lower not in ['c']:
        hmm = ("""
Hmm, that didn't seem to be an option.\n""")
        for character in hmm:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(2)
        next()
def path1():
    bookstimetravel = ("""
"It has to do with the thing that I'm working on. Would you like to see it?"

Your Granddad says.


You nod your head.\n""")
    for character in bookstimetravel:
        sys.stdout.write(character)
        sys.stdout.write()
        time.sleep(0.05)
    time.sleep(3)
    lab_chatting()
def path2():
    lab_goto = ("""
"We can talk about this in the lab. What I'm working on is also in the
lab." \n
You nod in agreement.""")
    for character in lab_goto:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(3)
    lab_chatting()



def game_true():
    welcome_2019 = ("""
Welcome to 2019.
You are in a room.

Wait, a room? This seems to be a holo-room. There are no doors. On the screen there is a list of 10 countries.

You find a memo attached to the time-machine, saying "You will emerge in a room, but this is just a function I implimented
so that you can travel all over the world. More details are availible in the time machine. Press the green button."






                                                Press green button.

                                                       [g]
                                                                     \n""")
    for character in welcome_2019:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    input_game = input("> ")
    if input_game == ("g"):
        g_details = ("""
You press the green button.

The screen says : "loading space-time portal email system."





It's finished loading. There is a message saying:




Hey there, %s! This is the space-time portal email system. Welcome to 2019!


There is a message from Granddad.



"Dear %s,


You must be quite confused. This is a holo-room I created to make my time-traveling
easier. You see the countries on the screen? These are the countries creating the most environmental damage.
You must use your knowledge of electronics to create a machine that will help solve the problem of these countries.


This holo-room was designed so I could travel anywhere, but since you're using it, I used remote settings to 
change it from all countries to countries affecting the climate the most.



Try to stop the meat and dairy industry as well, otherwise, the disease might still be there.


Good luck." \n\n\n\n\n\n\n\n\n\n\n\n\n\n
You look at the screen.""" % (myPlayer.name, myPlayer.name))
        for character in g_details:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.07)
        time.sleep(3)
        check()
        


def prompt_game():
    check()
    if myPlayer.easy == False:
        print("""
{Time Machine Virtual Room}


{Welcome, %s! This is the Virtual Room. Your chosen countries are below.}




Countries (by most polluting first):

1. ����� - Locked
2. ��� - Locked
3. ����� - Locked
4. ������ - Locked
5. ����� - Locked
6. ������� - Locked
7. ���� - Locked
8. Saudi Arabia
9. South Korea
10. Canada


Countries are sorted with pollution by C02 emissions.


Type in the number of the country you would like to go to.
""" % (myPlayer.name))
        input_prompt_game = input("> ").lower().strip()
        if input_prompt_game == "10":
            os.system('clear')
            time.sleep(1)
            touch = ("""
You touch the little tab marked 'Canada'.



Suddenly, the room whirres.""")
            for character in touch:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.07)
            time.sleep(2)
            os.system('clear')
            time.sleep(1)
            canada()
        elif input_prompt_game == "9":
            os.system('clear')
            touch9 = ("""

You touch 'South Korea'.

The room whirres into action.""")
            for character in touch9:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.07)
            time.sleep(2)
            os.system('clear')
            time.sleep(1)
            southkorea()
        elif input_prompt_game == "8" or "eight" or "8.":
            arabia()
    elif myPlayer.easy == True and myPlayer.medium == False:
        print("""
{Time Machine Virtual Room}


{Welcome, %s! This is the Virtual Room. Your chosen countries are below.}




Countries (by most polluting first):

1. ����� - Locked
2. ��� - Locked
3. India
4. Russia
5. Japan
6. Germany
7. Iran
8. Saudi Arabia - COMPLETED
9. South Korea - COMPLETED
10. Canada - COMPLETED


Countries are sorted with pollution by C02 emissions.


Type in the number of the country you would like to go to.
""" % (myPlayer.name))



def check():
    global canada_done
    global korea_done
    global saudi_done
    global iran_done
    global ger_done
    global japan_done
    global russia_done
    global india_done
    if canada_done and korea_done and saudi_done == True:
        myPlayer.easy = True
        prompt_game()



def southkorea():
    os.system('clear')
    korea_text = ("""
You are in South Korea.


Would you like to [explore] the area, or [build] the machine to help the country?\n
""")
    for character in korea_text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    korea_input = input("""> """).lower().strip()
    if korea_input == 'explore':
        explore_korea()
    elif korea_input == 'build':
        build_korea()

def explore_korea():
    os.system('clear')
    explore_korea1 = ("""
You seem to be in Seoul.

The air is filled with sound.

It is approximately 10 am.


Would you like to examine the [air] go [back]? \n\n\n\n""")
    for character in explore_korea1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    input_explorekorea1 = input("> ")
    if input_explorekorea1 == 'air':
        air_examine_korea = ("""
The PM 2.5 micron dust levels are higher than reccommended. Wow, the air pollution is high.


Enter to go back.\n\n\n""")
        input_air = input("")
        southkorea()
    elif input_explorekorea1 == 'back':
        southkorea()
def build_korea():
    pm25 = ("""
To build a machine you must have data of the environment.""")
    for character in pm25:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(2)
    pm25in1 = input("\nEnter to continue")
    os.system('clear')
    pm252 = ("""
You must click when you see a PM 2.5 dust piece.""")
    for character in pm252:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    pm25in2 = input("\nEnter to start")
    os.system('clear')
    cprint("Game starts in 5", "red", attrs=['bold'])
    time.sleep(1)
    os.system('clear')
    cprint("Game starts in 4", "red", attrs=['bold'])
    time.sleep(1)
    os.system('clear')
    cprint("Game starts in 3", "red", attrs=['bold'])
    time.sleep(1)
    os.system('clear')
    cprint("Game starts in 2", "red", attrs=['bold'])
    time.sleep(1)
    os.system('clear')
    cprint("Game starts in 1", "red", attrs=['bold'])
    time.sleep(1)
    os.system('clear')
    cprint("Game starts in 0", "red", attrs=['bold'])
    time.sleep(1)
    cprint("Start", "red", attrs=['bold'])
    time.sleep(3)
    curses.wrapper(korea_clicker_game)


def korea_clicker_game(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    curses.mousemask(1)
    pm25_points = 0
    pm25_time = 10
    while pm25_time > 0:
        time.sleep(3)
        value = randint(0, 1)
        if value == 0:
            stdscr.addstr(9, 0, """
        ______________________________________________________
        |                                                    |
        |               Laser particle sensor                |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |              [No particles detected]               |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |____________________________________________________|

""")
            time.sleep(3)
            curses.wrapper(korea_clicker_game)
        elif value == 1:
            stdscr.addstr(9, 0, """
        ______________________________________________________
        |                                                    |
        |               Laser particle sensor                |
        |                                                    |
        |                                                    |
        |                                                    |
        |                   __________                       |
        |                  |  PM 2.5  |                      |
        |                  |          |                      |
        |                  |          |                      |
        |                  |  Alert!  |                      |
        |                  |__________|                      |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |                                                    |
        |____________________________________________________|

""")    
            key = stdscr.getch()
            if key == curses.KEY_MOUSE:
                _, x, y, _, _ = curses.getmouse()
                if y in range(9, 18) and x in range(4, 54):
                    pm25_points += 1
                    pm25_time -= 1
                    curses.wrapper(korea_clicker_game)










def canada():
    canada_text = ("""
You are in Canada.


A soft breeze hits your face.



Would you like to [explore] the area, or [build] the machine to help the country?\n
""")
    for character in canada_text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    canada_input = input("""> """).lower().strip()
    if canada_input == 'explore':
        explore_canada()
    elif canada_input == 'build':
        build_canada()

def explore_canada():
    explore_canada1 = ("""
You walk around. You seem to be in Vancouver.


A Canadian walks by.


Should you test the [water] or the [air] first?\n\n\nOr, type in [back] to return to the options screen.
""")
    for character in explore_canada1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    input_explorecanada1 = input("> ")
    if input_explorecanada1 == 'back':
        canada()
    elif input_explorecanada1 == 'water':
        how = ("""
How would you do that? You don't seem to have anything that can scan water.

You pick the handheld time machine out of your pocket.

There is a function to measure water pollution after all.


""")
        for character in how:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(3)
        water = ("""
You measure the water in a small lake.


This water is not safe.

It was probably polluted because of acid rain from oil sands.


                    [back]\n\n""")
        for character in water:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.05)
        input_water = input("""> """).lower().strip()
        if input_water == 'back':
            explore_canada()
    elif input_explorecanada1 == 'air':
        measure = ("""
There is a function to measure air in the time machine. Quite thoughtful, Granddad.

Type in 'measure' to measure.\n\n""")
        for character in measure:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        measure_input_canada = input("> ").lower().strip()
        if measure_input_canada == 'measure':
            measured = ("""
You press 'measure'.


The air pollution levels are quite high as well.

It comes from oil production, I think.


            [back]\n\n\n\n""")
            for character in measured:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.05)
            input_back = input("> ").lower().strip()
            if input_back == 'back':
                explore_canada()
def build_canada():
    intro_10 = ("""
To build a machine, you must have knowledge of climate change.\n""")
    for character in intro_10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    ques_10 = ("""
You must answer 3 questions about climate change to build a machine.

(Hint. [explore] will help you get more info.)\n""")
    for character in ques_10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(3)
    ques_start = input(colored("""Enter to continue """, "red", attrs=['bold']))
    os.system('clear')
    start = colored("""
Start.\n\n\n\n""", "red",  attrs=['bold'])
    for character in start:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(4)
    ques_10_1()













def ques_10_1():
    global perfect
    global questions
    global outof
    global points
    if questions == 1:
        ques_1_10 = ("""
QUESTION 1:


What causes most air pollution in Canada?


[a] - Transportation.
[b] - Oil production.
[c] - Factory exhaust.
[d] - All of above.

""")
        for character in ques_1_10:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        ques_1_in_10 = input("> ")
        if ques_1_in_10 == 'a':
            if points == 0:
                outof -= 1
                questions = 2
                ques_10_1()
            else:
                questions = 2
                ques_10_1()
        elif ques_1_in_10 == 'b':
            if points == 0:
                points += 1
                questions = 2
                ques_10_1()
            else:
                questions = 2
                ques_10_1()
        elif ques_1_in_10 == 'c':
            if points == 0:
                points -= 1
                questions = 2
                ques_10_1()
            else:
                questions = 2
                ques_10_1()
        elif ques_1_in_10 == 'd':
            if points == 0:
                points -= 1
                questions = 2
                ques_10_1()
            else:
                questions = 2
                ques_10_1()

    elif questions == 2:
        ques_2_10 = ("""
QUESTION 2:

What does the term 'Climate Change' mean?

[a] - The warming of the planet
[b] - The sea's acidification
[c] - More people in a room
[d] - Neighbors moving in
[e] - A and B, etc.
[f] - None of above.\n\n\n""")
        for character in ques_2_10:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        ques_2_in_10 = input("> ")
        if ques_2_in_10 == 'a':
            if points == 1:
                outof -= 1
                points -= 1
                questions = 3
                ques_10_1()
            else:
                questions = 3
                outof -= 1
                ques_10_1()
        elif ques_2_in_10 == 'b':
            if points == 3:
                points -= 1
                outof -= 1
                questions = 3
                ques_10_1()
            else:
                questions = 3
                outof -= 1
                ques_10_1()
        elif ques_2_in_10 == 'c':
            if points == 1:
                points -= 1
                outof -= 1
                questions = 3
                ques_10_1()
            else:
                questions = 3
                outof -= 1
                ques_10_1()
        elif ques_2_in_10 == 'd':
            if points == 1:
                points -= 1
                outof -= 1
                questions = 3
                ques_10_1()
            else:
                questions = 3
                outof -= 1
                ques_10_1()
        elif ques_2_in_10 == 'e':
            points += 1
            questions = 3
            ques_10_1()
        elif ques_2_in_10 == 'f':
            if points == 1:
                outof -= 1
                points -= 1
                questions = 3
                ques_10_1()
            else:
                questions = 3
                outof -= 1
                ques_10_1()
    elif questions == 3:
        ques_3_10 = ("""
QUESTION 3:


What causes the pollution of water in Canada?

[a] - Acid rain from oil sands
[b] - Dirt
[c] - Rocks
[d] - None of above\n\n\n\n\n\n\n\n""")
        for character in ques_3_10:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.02)
        ques_1_in_10 = input("> ")
        if ques_1_in_10 == 'a':
            points += 1
            questions = 4
            ques_10_1()
        elif ques_2_in_10 == 'b':
            if points > 0:
                points -= 1
                questions = 4
                ques_10_1()
            else:
                questions = 4
                ques_10_1()
        elif ques_2_in_10 == 'c':
            if points > 0:
                points -= 1
                questions = 4
                ques_10_1()
            else:
                questions = 4
                ques_10_1()
        elif ques_2_in_10 == 'd':
            if points > 0:
                points -= 1
                questions = 4
                ques_10_1()
            else:
                questions = 4
                ques_10_1()
    elif questions == 4:
        os.system('clear')
        if points == 3:
            perfect = True
            line = ("Congratulations! You won.")
        elif points == 2:
            perfect = False
            line = ("Good job.")
        elif points == 1:
            perfect = False
            line = ("You could have done better.")
        score_print = ("""

You have completed the questions.



This is your score : %d

You got %d out of 3 questions correct.

%s


Would you like to [retry] or [continue]?


""" % (points, outof, line))
        for character in score_print:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        input_score_print = input("> ")
        if input_score_print == 'retry':
            os.system('clear')
            perfect = False
            outof = 5
            points = 0
            questions = 1
            print("Restarting quiz in 5 seconds")
            time.sleep(4)
        elif input_score_print == 'continue':
            if points == 3:
                printer = ("""
You built a solar power generator magnifier design and a prototype for the 
government to reproduce. It seems they've realized what they're doing to the environment.


Good job. 9 more to go.\n\n\n""")
                for character in printer:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                time.sleep(3)
                os.system('clear')
                canada_done = True
                print("[Returning to Virtual Room...]")
                time.sleep(3)
                prompt_game()
            elif points == 2:
                printer = ("""
You built a generator powered by C02 to attach to cars, and sold the designs to the government. 

Good job. 9 more to go.\n\n\n""")
                for character in printer:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                time.sleep(3)
                os.system('clear')
                canada_done = True
                print("[Returning to Virtual Room...]")
                time.sleep(3)
                prompt_game()
            elif points == 1:
                printer = ("""
You struggled, but could not think of something to help the environment. Sorry, Granddad.

\n\n\n""")
                for character in printer:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.05)
                time.sleep(3)
                os.system('clear')
                canada_done = False
                print("[Returning to Virtual Room...]")
                time.sleep(3)
                prompt_game()








                
































title_screen()
