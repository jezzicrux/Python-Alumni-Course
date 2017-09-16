from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
indata = open(from_file, 'r').read() #LIKE THIS!!!

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w').write(indata) #Did it for write too

print("Alright, all done.")

#I noticed that there was an error when I had the close.
#I think because the file is opened and the used at the same time
#It seems that the values in the varibles are strings.
