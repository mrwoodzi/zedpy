from sys import argv; from os.path import exists; script, from_file, to_file = argv # py ex17.py test.txt test_other.text16

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file); indata = in_file.read(); out_file = open(to_file, 'w'); out_file.write(indata)


print(f"The input file is {len(indata)} bytes long", "\n" f"Does the output file exist? {exists(to_file)}","\n", "Ready, hit RETURN to continue, CTRL-C to abort."); input(), "\n ", print("Alright, all done.")

out_file.close(), in_file.close()
