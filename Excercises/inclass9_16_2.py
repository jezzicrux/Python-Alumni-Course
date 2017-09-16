def main():
    pos_neg()
    divied_four()
    numb_rang()
    crazy_num(5,7)
    crazy_num(7,2)
    crazy_num(9,9)

#Letting the user know if their number is positive or negative
def pos_neg():
    #You have to add int before input because input are always strings and you need a interger
    num = int(input("Please enter a number. >"))
    if (num < 0): #less then 0
        print ("Your number is negative")
    else: # everything eles
        print ("Your number is positive")

#Letting the user know if their number is it's divisible by 4.
def divied_four():
    #You have to add int before input because input are always strings and you need a interger
    dnum = int(input("Please enter a number to see if it's divisible by 4. >"))
    #Here we use modulas to see if the number is divisible by 4 because if it is,
    #there shouldb't be a remainder and modulas looks at the remainder value.
    #If the remainder is zero then it' divisible by 4.
    if (dnum%4 == 0):
        print("You number is divisible by 4.")
    else:
        print("Sorry. Not divisible by 4.")

#Letting the user know where their number falls in the range 6 -12 or 121 - 151
def numb_rang():
    rangnum = int(input("Please enter a number to see fall in the magic zone. >"))
    if (rangnum >=6 and rangnum <=12): #This sees if the number to greater the 6 but less then 12
        print("You're in the magic zone!")
    elif (rangnum >=121 and rangnum <=151): #This sees if the number to greater the 121 but less then 151
        print("You're in the super magic zone!")
    else: #For all other numbers
        print("No magic for you. Sorry")

#Doing a crazy number program. The next function will be call 3 times
#The function will have 2 arguments.
#If the frist argument is greater the the second argument then divie the first by the second
#If the second argument is greater then the first, multiply the first by 10
def crazy_num(x,y):
    if x > y:
        print(x/y)
    elif x < y:
        print (x*10)
    else: #This is for if x and y are the smae value
        print("I don't know what to do")


main()
