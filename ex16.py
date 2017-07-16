
#1: Opens file, prints text.
#2: asks rather you want to erase the file.
#3: erases the file
#4: prompts you for 3 inputs for 3 different lines
#5: saves the 3 lines of text into the document. 

from sys import argv

script, filename = argv

print "Opening the file..."
target = open(filename, "r+")
print ">TEXT IN FILE<\n >" + target.read()

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^C)"
print "If you do want that, hit RETURN"

raw_input("?")


print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

final_output = line1 + "\n" + line2 + "\n" + line3

print "I'm going to write these to the file."

target.write(final_output)

print "And finally, we close it."
target.close()