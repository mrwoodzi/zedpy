from sys import argv

script, filename = argv # py ex16a.py test16.txt

print(f"We're going to print {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("What?")

print("You want to print!")
tuba = open(filename, 'w+') # tells to open test16.txt and the w tells what mode
# In this instance we want to read, so a w+, could also use just r is used for write and read
print("Read the file. Awesome!")
 # target - I is the text16.txt
# truncate emptys the file target is target opens text16txt then truncate erases it
print("Now I'm going to ask you for three lines.")

Line1 = input("Tuba was good while we were doing it. ")# This appears as part of the print
Line2 = input("But, gotta get out of student loan debt. ")# user hits enter 3x
line3 = input("I want to provide better for my wife. ")

print("Can I write these to the file?")
print("\n")
print("\t")
print(" Are you sure you want to do that?")


tuba.write("\t") # It did put a tab in for line 28
tuba.write('tuba time is the fun time')
tuba.write("\n")
tuba.write("\t") # It did put a tab in for line 31 : )
tuba.write("Tuba is way harder to learn than this")
tuba.write("\n")
tuba.write("\n")
tuba.write("Why did I get a degree in tuba?")
tuba.write("\n")

print("Yes let's get that door closed quick.")
tuba.close()
