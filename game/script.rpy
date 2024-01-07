# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("BEAST WESTERN")
define trace = Character("Trace Ebert")
#define j = character("J RIZ")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show trace mad
    
    show eileen happy
    

    # These display lines of dialogue.

    trace "You've done fucked it boy."

    trace "Once you add a sum bitches, pictures, riz, and music, you can release it to the world!"

    e "now look ill kill you bitch"
    
    # This ends the game.

    return
