#This is a test from the book and the student is required to debug it so it works
#The completed degugged program will be at ex26_debugged.py
#I will # problem in this file then just fix in ex26_debugged.py
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
print("How much do you weigh?", end=' ' # missing a parenthesis
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
#from sys import argv
script, filename = argv # this needs to be at top so it runs first  #should also have from

txt = open(filenme)

print("Here's your file {filename}:") # missing f" it is not just a script but a function
print(tx.read()) #missing a t in tx

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again) # we don't need this

print(txt_again_read())# this should just output txt of filename


print('Let's practice everything.')#escape is needed
print('You\'d need to know \'bout escapes
      with \\ that do \n newlines and \t tabs.')# I put this in "" to make escapes work

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------) # missing a quote
print(poem)
print(--------------") #missing a quote


five = 10 - 2 + 3 - # we are missing 6
print(f"This should be five: {five}" # we are missing a )

def secret_formula(started) #needs a colon :
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars  100 # we are missing an operator /
    return jelly_beans, jars, crates


start_point = 10000
beans, jars = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(startpoint)   # pretty sure it should be start_point????????????????????????????????????????????????????????????????????????????????????
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cates = 30 # cats is definitly spelled wrong
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!" #No parenthesis ()

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs                      # No colon :
    print("The world is dry!")


dogs += 5                          # dogs has already been given a variable

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs                    # And another :
    print("People are less than or equal to dogs.) # We forgot a quote sign


if people = dogs: # needs to be ==
    print("People are dogs.")
