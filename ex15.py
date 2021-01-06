from sys import argv

script, filename = argv # this is the py script and the text fil

txt = open(filename) # this opened the text file

print(f"Here's your file {filename}:") # this function told me the variable
print(txt.read()) # this

print("Type the filename again:")
file_again = input("> ") # this waits( real word is prompt) for the users input before running rest of script. "> " is called a prompt

txt_again = open(file_again) # reads file again

print(txt_again.read())
