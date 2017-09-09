types_of_people = 10
#Concatenating a string and the variable (types_of_people) using format
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
#Concatenating a string and the variables (binary) and (do_not) using format
y = f"Those who know {binary} and those who {do_not}."
#Displays everything in variable x
print(x)
#Displays everything in variable y
print(y)
#Concatenating a string and the variable (x) using format and displaying it
print(f"I said: {x}")
#Concatenating a string and the variable (x) using format and displaying it
print(f"I also said: '{y}'")
hilarious = False
#A string that has a empty curly brace to add whatever you want
joke_evaluation = "Isn't that joke so funny?! {}"
#Displaying everything in variable joke_evaluation and then adding the value in hilarious
print(joke_evaluation.format(hilarious)) #Format lets you add whatever you want as long as there is an empty curly brace
w = "This is the left side of..."
e = "a string with a right side."
#Displays everything in variable (w) and (e) together
print(w + e)
