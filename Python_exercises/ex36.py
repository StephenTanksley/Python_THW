from sys import exit


def start_room():
    print("""\nYou awaken to the smell of clay and moisture. The air around you feels heavy and close, as if trapped. \nYou open your eyes and only darkness greets you. "Oh god. Am I blind?" You think as a feeling of panic grips you. \nSlowly, your eyes adjust to the darkness. Luminescent fungus lines the walls of what must be a cave, providing a very dim illumination. \nAhead, you see a way forward. 
          
          \nDo you move forward, or do you remain?
          """)

    choice = input("> ")

    if choice == "remain":
        die("You hung out in the cave for awhile and then you died.")
        exit(0)
    elif choice == "move forward":
        next_room()
    else:
        die("You tried to do something I didn't want you to do and snapped your neck.")


def next_room():
    print("""\nBefore you, you see two men in a room. Each man stands in front of a passageway in the rock. Unbeknownst to you, each of these men can only answer a single question - one will only lie, and the other will only tell the truth. You get the feeling that beyond the passageways that they guard will be either a way out of the cave or your doom.
          
    \nYou ask the man to the left "What would the other guard say is the way out of this cave?"
    \nThe guard answers you and says that the left passage is the way out.
    \nYou ask the man to the right the same question and he answers that the left passage is also the way out.
    
    \nWhich passage do you choose?
          """)

    choice = input("> ")

    if choice == "left":
        spike_room()
    elif choice == "right":
        escape()
    else:
        die("You tried to do something I didn't want you to do and were eaten by a grue.")


def spike_room():
    print("You crawl for what feels like an eternity through the passageway on the left.")
    die("Suddenly, the cave floor gives out beneath you. You fall into a pit of spikes and are skewered.")


def escape():
    print("You made it out of the cave and into the daylight. GGs, homie.")


def die(why):
    print(why, "Good job!")
    exit(0)


start_room()
