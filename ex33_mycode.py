# As an exercise Zed says to turn while loop into function
# Made my head explode
# I way over thought this one and had to look it up how to turn into a function
# 

def not_fun_code(started):
    i = 0 # 0 is i 
    numbers = [] # [] means we get to define the numbers

    while i < 6: # run this scipt while i remains lesson the 6
        print(f"At the top i is {i}")
        numbers.append(i) #append starts adding numbers to [] which is a list
# the variable i is changed to add + 1 each time the program is run through
        i = i + 1 # py remembers the number from the last run through of the program
        print("Numbers now: ", numbers) # numbers keep getting added to 
        print(f"At the bottom i is {i}") # i also gets added each time back at top

# i is now greater than 6 so the while loop is ended and moves down here
    print("The numbers: ")

    for num in numbers:
        print(num)



print(f"{not_fun_code}")

