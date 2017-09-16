#We have three variables called people, cars and trucks.
#We will be using the values in these variables for or if else statements
people = 30
cars = 40
trucks = 15

#If the value in the variable cars is greater then the value in the variable people,
#display the text "We should take the cars."
#If the value in the variable cars is less then the value in the variable people,
#display the text "We should not take the cars."
#All other condition will display "We can't decide."
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

#If the value in the variable trucks is greater then the value in the variable cars,
#display the text "That's too many trucks."
#If the value in the variable trucks is less then the value in the variable cars,
#display the text "Maybe we could take the trucks."
#All other condition will display "We still can't decide."
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

#If the value in the variable people is greater then the value in the variable trucks,
#display the text "Alright, let's just take the trucks."
#All other condition will display "We still can't decide."
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

#note: We couldn't put the all in one if statement because once one condition is met,
#the other lines of code don't run.
