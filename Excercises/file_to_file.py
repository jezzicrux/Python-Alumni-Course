from sys import argv
#Storing the file name, first file name, and second file in arguments
script, first_filename, second_filename = argv
#Opening the first file use it
first_text = open(first_filename)
print (f"You file {first_filename} has the following text:\n")
#Storing the text from the first file by reading it
appending_text = first_text.read()
#Closing the first file
first_text.close()
#Displaying the text from the first file
print (appending_text)

#Opening the second file to use it
second_text = open(second_filename)
print (f"\nYou file {second_filename} has the following text:\n")
#Storing the text from the second file by reading it
original_text = second_text.read()
#Closing the second file
second_text.close()
#Displaying the text from the second file
print (original_text)

print (f"\nWhen you add the two it now reads like this:\n")
#Opening the second file again to use it and appened the first text to the second file
second_text = open(second_filename, 'a')
#Writing the text stored in appending_text (which is the text from the first file) to the file
second_text.write(appending_text)
#Closing the second file
second_text.close()
#Opening it again to store the orginal text from the second file and the appending text from the first file
second_text = open(second_filename)
#Storing the orginal text and the appending text
full_text = second_text.read()
#Displaying the new text from the second file
print (full_text)
#Closing the second file
second_text.close()
