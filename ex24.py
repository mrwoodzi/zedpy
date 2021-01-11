print("\tLet's practice everything.") #prints text
print('\tYou\'d need to know \'bout escapes with \\ that do:')#prints test with escap' ' \
print('\n \tnewlines and \t tabs.')#drops line and prints and has escape tabs
#the program does not run the below program chronologically as it is just a variable
poem = """
\t\tThe lovely world
\twith logic so firmly planted
\tcannot discern \n \tthe needs of love
\tnor comprehend passion from intuition
\tand requires an explanation
\n\t\twhere there is none.
""" # triple quotes simply prints text invarable

print("\t\t--------------")#simple print
print(poem)#is a variable that prints the poem
print("\t\t--------------")#simple print


five = 10 - 2 + 3 -6 #five is a varibale that works out a math problem
print(f"\tThis should be five: {five}") #prints text and then prints the variable

def secret_formula(started): # this is a mini script/command let that runs
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

#remember that this is another way to format a string
print("\tWith a starting point of: {}".format(start_point)) # line prints and then put 1000 into variable
# it's just like with an f"" string
print(f"\tWe'd have {beans} beans, {jars} jars, and {crates} crates.") #How does it no beans = jelly_beans??????

start_point = start_point / 10

print("\tWe can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("\tWe'd have {} beans, {} jars, and {} crates.".format(*formula))
