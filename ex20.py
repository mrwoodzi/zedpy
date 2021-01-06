from sys import argv

script, input_file = argv # py ex20.py test.txt

def print_all(f): # f is an argument that gets assgined as a variable in this
    print(f.read()) # will print what is in file that will be opened in script

def rewind(f): # argument used as a variable defined
        f.seek(0) # moves the read write location to the beginning of th file

def print_a_line(line_count, f): # line_count
    print(line_count, f.readline()) # f.readline assigns the command readline to a variable
    # readline is a command to read singular lines

current_file = open(input_file) # variable for current file to be opened

print("First let's print the whole file:\n") # prints text then drops a line

print_all(current_file) # this prints the file that was opended in line 15

print("Now let's rewind, kind of like a tape.") # prints text

rewind(current_file)# function that moves read/write to beginning of file
 # we are now at line 1 of test.txt
print("Let's print three lines:") # prints line

current_line = 1 # prints line 1 then moves to line 2, the 1 will be put at from
print_a_line(current_line, current_file) # Starts printing line 1 of test.txt

current_line = current_line + 1 # prints line 2
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
