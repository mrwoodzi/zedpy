from sys import exit # from <module> import <x>

def gold_room(): 
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.") 

    if how_much < 50:
        print("Nice, you're not greedy!")
        alive()
    else:
        dead("You greedy bastard, A cave troll shows up and eats your face off.") # this <dead(why)> allows the function to assign a print statement


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ") # I have no idea how to know what the options are to remove bear, needs a help
        if choice == "help":
            print("""You can "take honey" or "taunt bear".""")
        if choice == "take honey": # this has to be worded "take honey" or it won't work
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:# has to be "taunt bear"
            print("The bear has moved from the door.")
            print("You can open the door now.") # I changed the wording of this so the user guided to what to input- "open door"
            bear_moved = True
        elif choice == "taunt bear" and bear_moved: # this is if you have already taunted bear and bear_^has_moved
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("What do you want to do?")

def cthulu_room():
    print("Here you see the great evil Cthulu.")
    print("He, It, whatever stares at you and you go insane.")
    print("Do you flee for you life or eat your head?")

    choice = input("> ")

    if "flee" in choice: #as long as "flee" is in the input it head work
        start()
    elif "head" in choice: # as long as "head" is in the input head you can write other things 
        dead("Well that was tasty!") # goes to dead function
    else:
        cthulu_room()# send you back to the top of the cthulu room

def keytar_room():
    print("You see a flock of Seagulls and a keytar.")
    print("Do you immediately decide to get a hair cut or play the keytar.")

    choice = input("> ")

    if "get a hair cut" == choice:

    elif "keytar" in choice:

    else:
        print("You get dizzy and black out.") 
        print("You feel like you were just in this room, kinda like the move Groundhog day.")
        keytar_room()


def alive(): # I added this so you can have a clear game win
    print("You Win!")
    exit(0)

def dead(why):
    print(why,"Your Dead!") # I added Your Dead! so the user knows they failed
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door  to you right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    elif choice == "tuba": # this is a cheat to win the game out right
        alive()
    elif choice == "keytar":
        keytar_room()
    else:
        dead("You stumble around the room until you starve.")
        
        
start()