from sys import exit # this imports a function from a module

def gold_room(): # function for the gold_room
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.") # takes you to dead(why, ) the why
        # requires you to put in a print statement

    if how_much < 50: # is a boo to test if how_much is less than 50
        print("Nice, you're not greedy, you win!")
        exit(0) # this automatically exits the program without throwing an error
    else:
        dead("You greedy bastard!") # takes to dead function


def bear_room(): 
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ") # I have no idea how to know what the options are to remove bear, needs a help
 # the bear room uses <==> which means the users choice must exactly be <"taunt bear"> to work not just bear as with an "in"       
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
            print("I got no idea what that means.")


def cthulu_room(): #choices are different in this room and zed used <in> and not <==> so as long as part of a word is in it will work 
    print("Here you see the great evil Cthulu.")
    print("He, It, whatever stares at you and you go insane.")
    print("Do you flee for you life or eat your head?")

    choice = input("> ")

    if "flee" in choice: #as long as "flee" is in the input it head work
        start()
    elif "head" in choice: # as long as "head" is in the input it head work
        dead("Well that was tasty!")
    else:
        cthulu_room()


def dead(why):
    print(why,"\tYour Dead!" '\n"Good,job!"') # I added Your Dead! so the user knows they failed
    exit(0) # this is like a forced program end and the (0) means that no error will be thrown just a clean exit

def start():
    print("\tYou are in a dark room.")
    print("\tThere is a door  to you right and left.")
    print("\tWhich one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.") #takes you to the dead module
        
        
start()