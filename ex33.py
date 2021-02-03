i = 0 # 0 is i 
numbers = [] # [] means we get to define the numbers

while i < 6: # run this scipt while i remains lesson the 6
    print(f"At the top i is {i}")
    numbers.append(i) #append starts adding numbers to [] which is a list
# the variable i is changed to add + 1 each time the program is run through
    i = i + 1 # py remembers the number from the last run through of the program
    print("Numbers now: ", numbers) # numbers keep getting added to 
    print(f"At the bottom i is {i}") # i also gets added each time

# i is now greater than 6 so the while loop is ended and moves down here
print("The numbers: ")

for num in numbers:
    print(num)


