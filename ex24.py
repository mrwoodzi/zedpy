print("Let's practice everything.") #prints text
print('You\'d need to know \'bout escapes with \\ that do:')#prints test with escap' ' \
print('\n newlines and \t tabs.')#drops line and prints and has escape tabs
#the program does not run the below program chronologically as it is just a variable
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
""" # triple quotes simply prints text invarable

print("--------------")#simple print
print(poem)#is a variable that prints the poem
print("--------------")#simple print


five = 10 - 2 + 3 -6 #five is a varibale that works out a math problem
print(f"This should be five: {five}") #prints text and then prints the variable

def secret_formula(started): # this is a mini script/command let that runs
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

#remember that this is another way to format a string
print("With a starting point of: {}".format(start_point)) # line prints and then put 1000 into variable
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
