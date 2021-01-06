from sys import argv
from os.path import exists

script, from_file, to_file = argv # py ex17.py test.txt test_other.text16

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read() # this assigns the contents of the file to a variable

print(f"The input file is {len(indata)} bytes long") # len reads the amount of data in the indata file ( which in this case)

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata) # this writes the contents of indata to out_file

print("Alright, all done.")

out_file.close()
in_file.close()
