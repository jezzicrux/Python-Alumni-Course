#Making a function for chesse and crackers.
#Calls the a value for cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You got {cheese_count} cheeses!")
    print(f"You got {boxes_of_crackers} boxes of crackers!")
    print("TIME TO PARTY!")
    print("GET THE DRINKS!!!.\n")

print("We can just give the function numbers directly:")
#This call the function cheese_and_crackers and "assigns" 20 to cheese_count and 30 to boxes_of_crackers
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#This call the function cheese_and_crackers and "assigns"
#amount_of_cheese (which is 10) to cheese_count and amount_of_crackers (with is 50) to boxes_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
#This call the function cheese_and_crackers and "assigns"
#The value to (10+20) to cheese_count and (5+6) to boxes_of_crackers
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
#This call the function cheese_and_crackers and "assigns" the following:
#The value of amount_of_cheese (which is 10) added by 100 is the valus of cheese_count
#The value of amount_of_crackers (with is 50) added by 20 is the valus of boxes_of_crackers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 20)
