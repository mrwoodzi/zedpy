import sys
script, input_encoding, error = sys.argv # run file ex23.py, utf-8, strict
  ###you can use utf-16 utf- 32for an encoding in input_encoding, I could not get it to encode in big5

def main(language_file, encoding, errors): # main is line 22 that gets things going
        line = language_file.readline() # this reads 1 line from languages.txt

        if line:  # this tests of thee is a line to read in the language_file the computer is going to test if something is true/false and then give an output
            print_line(line, encoding, errors) # this runs the cmdlt def print_line
            return main(language_file, encoding, errors)#this jumps back to top to run again, this makes it loop for a bit


def print_line(line, encoding, errors): #this prints the line 9
    next_lang = line.strip() #strip probably means strip it down
    raw_bytes = next_lang.encode(encoding, errors=errors) #this takes the stripped line and gives you the unicode in raw raw_bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors) #this decodes the raw_bytes and translates them into the real characters that are readable

    print(raw_bytes, "<===>", cooked_string) # this will print the rawbytes in the encoding that you chose with input_encoding, cooked_string is a variable that takes the raw raw_bytes
# and decodes them into real characters
languages = open("languages.txt", encoding="utf-8") #this is a variable that opens the languages.txt then it tell py that it

main(languages, input_encoding, error)
