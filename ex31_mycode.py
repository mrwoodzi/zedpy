# I added doors 3, 4 and 5 to the game.

print("""You enter a dark room with five doors.
Do you go through door 1, 2, 3, 4 or 5?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your leg off.   Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberreis.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good Job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")


elif door == "3":
    print("You see a tuba.")
    print("1. You try to play the tuba.")
    print("2. You quickly slam the door.")

    tuba = input("> ")

    if tuba == "1":
        print("You hit the brown note and crap yourself!")
        print("Congrats your constipation is finally over.")
    else:
        print("Roger Bobo and Chester Schmits show up and proceed to teach you how to circular breath.")
        print("Maybe you should have played tuba, it would help with your constipation.")

elif door == "4":
    print("You see a saxophone.")
    print("1. You try to play the saxophone.")
    print("2. You quickly slam the door because you think Kenny G might be in the room.")

    saxophone = input("> ")

    if saxophone == "1":
        print("You worst fears are realzied as you transform into Kenny G.")
        print("You then start playing Careless Whisper until you die.")
        print("Game Over")

    else:
        print("George Michael shows up and hands you a saxophone.")
        print("A life goal is then fulfilled as you play Careless Whisper on saxophone with George Michael singing.")

elif door == "5":
    print("You see a keyboard guitar.")
    print("1. You try to play the keyboard guitar.")
    print("2. You see a Flock of Seagulls.")

    keyboard = input("> ")

    if keyboard == ("1"):
        print("You then cut your hair like the guys in A Flock of Seagulls and join an 80's New Wave tribute band.")
        print("All life goals are fulfilled.")
        print("You die a happy.")
        
    else:
        print("And you raaaaaan, you ran so far aaa-waa-aaaay")
        print("Good job.")


else:
    print("You stumble around and fall on a knife and die.  Good job!")