# this one is like your scripts with argv
def print_two(*args): #def alows us to make a function, we also name it, print_two, we tell print_ (*args) is like argv we are just creating it here not pulling it as a module
    arg1, arg2, arg3, arg4 = args # indentation attaches arguments to print_two
    print(f"arg1: {arg1}, arg2: {arg2} {arg3} {arg4}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2, arg3, arg4): # def function_name(arguments): finish it with a colon :
    print(f"arg1: {arg1}, arg2: {arg2} {arg3} {arg3} {arg4}") # added extra variables to see what would happen

#this just takes one argument
def print_one(arg1): # does def mean user define?
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin',")


print_two("Zed","Shaw", "Michael", "Woods") # the script down here gives the variables a name (which in this case we make up)
print_two_again("Michael","Woods", "Zed", "Shaw")
print_one("First!")
print_none()
