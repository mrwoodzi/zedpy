#I don't know what started is in line 2???
def secret_formula(started): # this is a mini script/command let that runs
    jelly_beans = started * 500
    glass_jars = jelly_beans / 1000
    crates = glass_jars / 100
    return jelly_beans, glass_jars, crates

five = 10 - 2 + 3 -6 #five is a varibale that works out a math problem
start_point = 10000
beans, jars, crates = secret_formula(start_point)
start_point = start_point / 10 #This is a variable that takes the start_point and divides it by 10
formula = secret_formula(start_point)
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
""" # triple quotes simply prints text invarable

print("Let's practice everything.") #prints text
print('You\'d need to know \'bout escapes with \\ that do:')#prints test with escap' ' \
print('\n newlines and \t tabs.')#drops line and prints and has escape tabs
#the program does not run the below program chronologically as it is just a variable

print("--------------")#simple print
print(poem)#is a variable that prints the poem
print("--------------")#simple print

print(f"This should be five: {five}") #prints text and then prints the variable
#remember that this is another way to format a string
print("With a starting point of: {}".format(start_point)) # line prints and then put 1000 into variable
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.") #How does it no beans = jelly_beans??????

print("We can also do that this way:")
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula)) #Not sure how py recognizes {}{} with out them turning different color
#tHIS line I guess you could just use
