from sys import argv #this gave a command(to run something in powershell)#is this part of a port?

# read the WYSS section for how to run this
script, first, second, third = argv # as the programmer you have to know that there are 4 values/variables to fill, the script and
# then 3 values the user fills in
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
