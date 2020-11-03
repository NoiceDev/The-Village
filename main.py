#  _____ _         __   ___ _ _
# |_   _| |_  ___  \ \ / (_) | |__ _ __ _ ___   v1.0
#   | | | ' \/ -_)  \ V /| | | / _` / _` / -_)
#   |_| |_||_\___|   \_/ |_|_|_\__,_\__, \___|
#                                   |___/

# By Noice.

#  ___          _                _   _
# | __|_ ___ __| |__ _ _ _  __ _| |_(_)___ _ _
# | _|\ \ / '_ \ / _` | ' \/ _` |  _| / _ \ ' \
# |___/_\_\ .__/_\__,_|_||_\__,_|\__|_\___/_||_|
#         |_|

# The program is a text-based Python game called "The Village" made by Noice. The program uses a tile based, function system.
# In this case... each tile being a function and heading North, South, East or West calling on another function. This program
# was planned with a small 5x5 map (excluding the mountian border and edges), the program also has a small map that prints that
# is made manually by just printing a text-version of the planned map. The map can be found in the Links section at the bottom
# of the code! Enjoy!

#  _    _ _                 _
# | |  (_) |__ _ _ __ _ _ _(_)___ ___
# | |__| | '_ \ '_/ _` | '_| / -_|_-<
# |____|_|_.__/_| \__,_|_| |_\___/__/

# Libraries that are used in the project.

import time  # The time library used for pauses, this is not needed but is a nice touch.


#  ___              _
# | _ \__ _ _ _  __| |___ _ __
# |   / _` | ' \/ _` / _ \ '  \
# |_|_\__,_|_||_\__,_\___/_|_|_|

# Just some functions I like to define so that I can keep my code looking cleaner and more organized and easily understandable.

# Prints a blank line.
def blankLine():
    print("")

# Literally does nothing. Used for some if statements so as to not cause syntax errors.
def blank():
    print()

#  ___      _   _   _
# / __| ___| |_| |_(_)_ _  __ _ ___
# \__ \/ -_)  _|  _| | ' \/ _` (_-<
# |___/\___|\__|\__|_|_||_\__, /__/
#                         |___/

# A few settings that the player gets to choose before the game starts. These are functions that are called
# later when the game begins.

mapOn = ""

def settingsMapOn(mapOn):
    while True:
        # Question.
        answer = str(input("[Do you want to have your map enabled?] [Y/N]"))

        # If statements.
        if answer.lower() == "y":
            print("[Map toggled on.]")
            mapOn = True
            break
        elif answer.lower() == "n":
            print("[Map toggle off!]")
            mapOn = False
            break
        else:
            print("[Invalid choice!]")

# Map type...
mapType = ""

def settingsMapType(mapType):
    if mapTrue == True:
        while True:
            answer = str(input("[What type of map would you like?] [1. Char] [2. Emoji]"))
            if answer.lower() == "1" or answer.lower() == "char" or answer.lower() == "character":
                mapType = "char"
                print("[Char map selected!]")
                break
            elif answer.lower() == "2" or answer.lower() == "emoj" or answer.lower() == "emoji":
                maptype = "emoj"
                print("[Emoji map selected!]")
                break
            else:
                print("[Invalid choice!]")
    else:
        blank()

# Winning screen.
def village():
    print("[You won!]")

# Compass for questions (N, W, E, S).
def compass():
    print("""
             [N]
           [W] [E]    [Directions]
             [S]
    """)

# Mountain tile.
def mountain():
    print("[Mountain]")
    blankLine()
    print("[There is a mountain in this direction.]")
    blankLine()

# Lava tile.
def lava():
    print("[Lava]")
    blankLine()
    print("[There is a lava in this direction.]")
    blankLine()

# River tile.
def river():
    time.sleep(1.5)
    print("[You fall into the river and die.]")

# Bridge tile.
def bridge():
    while True:
        time.sleep(1.5)
        print("[You are on the bridge.]")
        blankLine()
        compass()
        direction = str(input(""))
        blankLine()
        if direction == "n":
            break
        elif direction == "w":
            river()
        elif direction == "e":
            river()
        elif direction == "s":
            meadow7()
        else:
            print("[Invalid choice!]")

# Meadow 13 tile.
def meadow13():
    while True:

        # Direction.
        print("[Meadow 13]")

        blankLine()
        print("[In which direction do you want to go?]")
        blankLine()
        compass()
        direction = str(input(""))
        blankLine()

        # Movement.
        if direction.lower() == "n" or direction.lower() == "north":
            meadow10()
        elif direction.lower() == "w" or direction.lower() == "west":
            meadow12()
        elif direction.lower() == "e" or direction.lower() == "east":
            lava()
        elif direction.lower() == "s" or direction.lower() == "south":
            mountain()
        else:
            print("Invalid choice!]")
            blankLine()

# Meadow 12 tile.
def meadow12():
    while True:

        # Direction.
        print("[Meadow 12]")

        blankLine()
        print("[In which direction do you want to go?]")
        blankLine()
        compass()
        direction = str(input(""))
        blankLine()

        # Movement.
        if direction.lower() == "n" or direction.lower() == "north":
            meadow9()
        elif direction.lower() == "w" or direction.lower() == "west":
            village()
        elif direction.lower() == "e" or direction.lower() == "east":
            meadow13()
        elif direction.lower() == "s" or direction.lower() == "south":
            mountain()
        else:
            print("Invalid choice!]")
            blankLine()

# Meadow 11 tile.
def meadow11():
    while True:

        # Direction.
        print("[Meadow 11]")

        blankLine()
        print("[In which direction do you want to go?]")
        blankLine()
        compass()
        direction = str(input(""))
        blankLine()

        # Movement.
        if direction.lower() == "n" or direction.lower() == "north":
            meadow7()
        elif direction.lower() == "w" or direction.lower() == "west":
            meadow10()
        elif direction.lower() == "e" or direction.lower() == "east":
            lava()
        elif direction.lower() == "s" or direction.lower() == "south":
            lava()
        else:
            print("Invalid choice!]")
            blankLine()

# Meadow 10 tile.
def meadow10():
    while True:

        # Direction.
        print("[Meadow 10]")

        blankLine()
        print("[In which direction do you want to go?]")
        blankLine()
        compass()
        direction = str(input(""))
        blankLine()

        # Movement.
        if direction.lower() == "n" or direction.lower() == "north":
            meadow6()
        elif direction.lower() == "w" or direction.lower() == "west":
            meadow9()
        elif direction.lower() == "e" or direction.lower() == "east":
            meadow11()
        elif direction.lower() == "s" or direction.lower() == "south":
            meadow13()
        else:
            print("Invalid choice!]")
            blankLine()

# Meadow 9 tile.
def meadow9():
    while True:

        # Direction.
        print("[Meadow 9]")

        blankLine()
        print("[In which direction do you want to go?]")
        blankLine()
        compass()
        direction = str(input(""))
        blankLine()

        # Movement.
        if direction.lower() == "n" or direction.lower() == "north":
            river()
        elif direction.lower() == "w" or direction.lower() == "west":
            mountain()
        elif direction.lower() == "e" or direction.lower() == "east":
            meadow11()
        elif direction.lower() == "s" or direction.lower() == "south":
            meadow12()
        else:
            print("Invalid choice!]")
            blankLine()

# Meadow 8 tile.
def meadow8():
    while True:

        # Direction.
        print("[Meadow 8]")

        blankLine()
        print("[In which direction do you want to go?]")
        blankLine()
        compass()
        direction = str(input(""))
        blankLine()

        # Movement.
        if direction.lower() == "n" or direction.lower() == "north":
            river()
        elif direction.lower() == "w" or direction.lower() == "west":
            meadow7()
        elif direction.lower() == "e" or direction.lower() == "east":
            mountain()
        elif direction.lower() == "s" or direction.lower() == "south":
            lava()
        else:
            print("Invalid choice!]")
            blankLine()

# Meadow 7 tile.
def meadow7():
    while True:

        # Direction.
        print("[Meadow 7]")

        blankLine()
        print("[In which direction do you want to go?]")
        blankLine()
        compass()
        direction = str(input(""))
        blankLine()

        # Movement.
        if direction.lower() == "n" or direction.lower() == "north":
            bridge()
        elif direction.lower() == "w" or direction.lower() == "west":
            meadow6()
        elif direction.lower() == "e" or direction.lower() == "east":
            meadow8()
        elif direction.lower() == "s" or direction.lower() == "south":
            meadow11()
        else:
            print("Invalid choice!]")
            blankLine()

# Meadow 6 tile.
def meadow6():
    while True:

        # Direction.
        print("[Meadow 6]")

        blankLine()
        print("[In which direction do you want to go?]")
        blankLine()
        compass()
        direction = str(input(""))
        blankLine()

        # Movement.
        if direction.lower() == "n" or direction.lower() == "north":
            river()
        elif direction.lower() == "w" or direction.lower() == "west":
            river()
        elif direction.lower() == "e" or direction.lower() == "east":
            meadow7()
        elif direction.lower() == "s" or direction.lower() == "south":
            meadow11()
        else:
            print("Invalid choice!]")
            blankLine()

# Meadow 5 tile.
def meadow5():
    while True:

        # Direction.
        print("[Meadow 5]")

        blankLine()
        print("[In which direction do you want to go?]")
        blankLine()
        compass()
        direction = str(input(""))
        blankLine()

        # Movement.
        if direction.lower() == "n" or direction.lower() == "north":
            meadow1()
        elif direction.lower() == "w" or direction.lower() == "west":
            break
        elif direction.lower() == "e" or direction.lower() == "east":
            river()
        elif direction.lower() == "s" or direction.lower() == "south":
            river()
        else:
            print("Invalid choice!]")
            blankLine()

# Meadow 4 tile.
def meadow4():
    while True:

        # Direction.
        print("[Meadow 4]")

        blankLine()
        print("[In which direction do you want to go?]")
        blankLine()
        compass()
        direction = str(input(""))
        blankLine()

        # Movement.
        if direction.lower() == "n" or direction.lower() == "north":
            break
        elif direction.lower() == "w" or direction.lower() == "west":
            mountain()
        elif direction.lower() == "e" or direction.lower() == "east":
            meadow5()
        elif direction.lower() == "s" or direction.lower() == "south":
            river()
        else:
            print("Invalid choice!]")
            blankLine()

# Meadow 3 tile.
def meadow3():
    # Direction.
    print("[Meadow 3]")

    blankLine()
    print("[In which direction do you want to go?]")
    blankLine()
    compass()
    direction = str(input(""))
    blankLine()

    # Movement.
    if direction.lower() == "n" or direction.lower() == "north":
        mountain()
    elif direction.lower() == "w" or direction.lower() == "west":
        meadow2()
    elif direction.lower() == "e" or direction.lower() == "east":
        mountain()
    elif direction.lower() == "s" or direction.lower() == "south":
        bridge()
    else:
        print("Invalid choice!]")
        blankLine()

# Meadow 2 tile.
def meadow2():
    while True:

        # Direction.
        print("[Meadow 2]")
        blankLine()
        print("[In which direction do you want to go?]")
        blankLine()
        compass()
        direction = str(input(""))
        blankLine()

        # Movement.
        if direction.lower() == "n" or direction.lower() == "north":
            mountain()
        elif direction.lower() == "w" or direction.lower() == "west":
            break
        elif direction.lower() == "e" or direction.lower() == "east":
            meadow3()
        elif direction.lower() == "s" or direction.lower() == "south":
            river()
        else:
            print("Invalid choice!]")
            blankLine()

# Meadow 1 tile.
def meadow1():
    while True:

        # Direction.
        print("[Meadow 1]")
        blankLine()
        print("[In which direction do you want to go?]")
        blankLine()
        compass()
        direction = str(input(""))
        blankLine()

        # Movement.
        if direction.lower() == "n" or direction.lower() == "north":
            mountain()
        elif direction.lower() == "w" or direction.lower() == "west":
            break
        elif direction.lower() == "e" or direction.lower() == "east":
            meadow2()
        elif direction.lower() == "s" or direction.lower() == "south":
            meadow5()
        else:
            print("Invalid choice!]")
            blankLine()

# Starting tile.
def start():
    while True:

        if mapType.lower() == "1" or mapType.lower() == "char" or mapType.lower() == "character":
            print("""
            [Map] [*=You]

            [ ][M][M][M][M][M][ ]
            [M][*][1][2][3][M][M]
            [M][4][5][=][|][=][=]
            [=][=][=][6][7][8][M]
            [M][M][9][10][11][L][M]
            [M][V][12][13][L][L][M]
            [ ][M][M][M][M][M][ ]
            """)
        elif mapType.lower() == "2" or mapType.lower() == "emoj" or mapType.lower() == "emoji":
            print("""
            """)
        elif mapType.lower() == "3" or mapType.lower() == "non" or mapType.lower() == "none":
            print()

        # Direction.
        print("[In which direction do you want to go?]")
        compass()
        direction = str(input(""))
        blankLine()

        # Question
        if direction.lower() == "n" or direction.lower() == "north":
            mountain()
        elif direction.lower() == "w" or direction.lower() == "west":
            mountain()
        elif direction.lower() == "e" or direction.lower() == "east":
            meadow1()
        elif direction.lower() == "s" or direction.lower() == "south":
            meadow4()
        else:
            print("Invalid choice!]")
            blankLine()
            start()

# print('''
#     [MAP]
#      ⛰️⛰️⛰️⛰️⛰️⛰️
#   ⛰️⛰️🟩🟩😀🟩⛰️⛰️
#   ⛰️🟩🟩🌊 🌊🌫️🌊🌊🌊
#   🌊 🌊 🌊 🟩🟩🟩 ️️⛰️
#  ⛰️
#   ⛰️
#      ️⛰️⛰️⛰️⛰️⛰️⛰️
# ''')

#   ___
#  / __|__ _ _ __  ___
# | (_ / _` | '  \/ -_)
#  \___\__,_|_|_|_\___|

# The actual game, intro and settings in action themselves. Very little code in this section as most is done with funcs.

print("""
  _____ _         __   ___ _ _
 |_   _| |_  ___  \ \ / (_) | |__ _ __ _ ___   v1.0
   | | | ' \/ -_)  \ V /| | | / _` / _` / -_)
   |_| |_||_\___|   \_/ |_|_|_\__,_\__, \___|
                                   |___/

By Noice.
""")

time.sleep(1)

# Map on?
settingsMapOn(mapOn)

# Map type?
settingsMapType(mapType)

# Starts the game.
start()
