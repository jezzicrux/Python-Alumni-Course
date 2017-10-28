def starting_room():
    print("Welcome to the room.\nTry your best to escape.")
    front_pick()

def front_pick():
    frontwall_close()
    print ("\nWould you like to look at the 'left' wall, 'right' wall or 'back' wall?")
    choice =  input(">>")
    status = 0
    wall_switch(choice, status)

def wall_switch(choice, a):
    if choice == str.lower('left') and a == 0:
        leftwall()
    if choice == str.lower('left') and a == 1:
        leftwall_key()
    elif choice == str.lower('right') and a == 0:
        rightwall()
    elif choice == str.lower('back') and a == 0:
        backwall_picture()
    elif choice == str.lower('back') and a == 1:
        backwall_picture_open()
    elif choice == str.lower('front') and a == 0:
        front_pick()
    elif choice == str.lower('front') and a == 1:
        front_pick()

def leftpick():
#So if the button is press on backwall_picture_open() then leftwall_key() should show

def frontwall_close():
    print("""    _______________________
    |                      |
    |       _______        |
    |       |     |        |
    |       |     |        |
    |       |     |        |
    |       |     |        |
    |       |   | |        |
    |       |     |        |
    |       |     |        |
    |_______|_____|________|""")

def frontwall_open():
    print("""    _______________________
    |                      |
    |       _______        |
    |       |     |        |
    |       |     |        |
    |       |     |        |
    |       |     |        |
    |       |     |        |
    |       |     |        |
    |       |     |        |
    |_______|_____|________|""")

def rightwall():
    print("""    _______________________
    |    _________         |
    |    | | | | |         |
    |    | | | | |         |
    |    |_|_|_|_|         |
    |                      |
    |                      |
    |                      |
    |                      |
    |                      |
    |______________________|""")

def backwall_picture():
    print("""    _______________________
    |   _________          |
    |   | _____ |          |
    |   | |___| |          |
    |   |_______|          |
    |                      |
    |                      |
    |                      |
    |                      |
    |                      |
    |______________________|""")

def backwall_picture_open():
    print("""    _______________________
    |   ________           |
    |   | ____ |           |
    |   |_|__|_|           |
    |                      |
    |                      |
    |                      |
    |   _________          |
    |   | _____ |          |
    |   | |___| |          |
    |___|_______|_________|""")

def leftwall():
    print("""    _______________________
    |                      |
    |                      |
    |                      |
    |                      |
    |                      |
    |                      |
    |                      |
    |                      |
    |                      |
    |______________________|""")

def leftwall_key():
    print("""    _______________________
    |                      |
    |            _______   |
    |            | -\  |   |
    |            |___\_|   |
    |                      |
    |                      |
    |                      |
    |                      |
    |                      |
    |______________________|""")
starting_room()
