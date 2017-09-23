import math #using the math libary
import datetime #using date libary
import time #using time libary
import calendar #want to format the date nicer

def main():
    '''time_convertion()
    mile_convertion()
    temp_convertion()
    cube_roots()
    circle()
    finding_the_ex()
    vowels()
    ZA_WARUDO()
    got_any_3()'''
    what_is_today()
    #find_the_letter()


#Finding the seconds
def time_convertion():
    sec = 42 * 60 #60 seconds in 1 minute. so we have 42 minutes.
    print(f"42 minutes and 42 seconds in seconds is {sec+42}")
    print("")#Just adding space between each function

#Finding how many kilometers in a mile
def mile_convertion():
    km = 10 #We have 10 kilometers
    miles = km / 1.61 #1 mile is 1.61 kilometers. We have 10 km so we need to know how many times 1.61 goes into 10
    print(f"How many miles are there in 10 kilometers? {miles} miles.")
    print("")#Just adding space between each function

#Fahrenheit to Celsius
def temp_convertion():
    f = 83
    c = (f-32)*(5/9) #Fahrenheit it Celsius convertion formular
    print(f"83\u00B0 Fahrenheit in Celsius is {c}\u00B0")
    print("")#Just adding space between each function

#WE DOING SQUARE ROOT YA'LL!!!!
def cube_roots():
    first_numb = math.sqrt(81)
    second_numb = math.sqrt(19)
    third_numb = math.sqrt(16)
    forth_numb = math.sqrt(121)
    print(f"The square root of 81 is {first_numb}.")
    print(f"The square root of 19 is {second_numb}.")
    print(f"The square root of 16 is {third_numb}.")
    print(f"The square root of 121 is {forth_numb}.")
    print("")#Just adding space between each function

    #WE FIND SQUARE ROOTS WITH LOOPS YA'LL!!!!!
    numb_list = [81,19,16,121]
    b = 0
    for a in numb_list:
        squ_numb = math.sqrt(a)
        print(f"The square root of {numb_list[b]} is {squ_numb}.")
        b=b+1
    print("")#Just adding space between each function

#Area of a circle
def circle():
    pii = math.pi #Getting pi. Yum
    r = 9 #radius
    cir_area = pii*(r**2) #area of a circle is pi*r^squared
    print(f"The area of a circle is {cir_area}.")
    print("")#Just adding space between each function

#finding the letter x in a string
def finding_the_ex():
    phase = input("Please enter in a statement. >")
    if ('x' in str.lower(phase)):#just incase the statement is in caps
        print(f"True")
        print("")#Just adding space between each function
        return True
    else:
        print(f"False")
        print("")#Just adding space between each function
        return False

#finding the letters a, e, i, o and u in a string
def vowels():
    phase = input("Please enter in a statement. >>")
    if ('a' in str.lower(phase)) or ('e' in str.lower(phase)) or ('i' in str.lower(phase)) or ('o' in str.lower(phase)) or ('u' in str.lower(phase)):
        print(f"True")
        print("")#Just adding space between each function
        return True
    else:
        print(f"False")
        print("")#Just adding space between each function
        return False

#SPHERES!!!!!
def ZA_WARUDO(): #Jojo referance
    pii = math.pi #Getting pi. Yum
    r = 5 #radius
    ball_area = (4/3)*(pii*(r**3)) #area of a sphere is (4/3)pi*r^cubed
    print(f"The area of a sphere is {ball_area}.")
    print("")#Just adding space between each function

#boolean function that returns true if user input is divisible by 3 or return false if not
def got_any_3():
    user_numb = int(input("Enter a number to see if it's divisible by 3. >>"))
    if user_numb % 3 == 0:
        print(f"True")
        print("")#Just adding space between each function
        return True
    else:
        print(f"False")
        print("")#Just adding space between each function
        return False

#Print today's date and time
def what_is_today():
    today_date = str(datetime.datetime.now())
    calendar.TextCalendar.prmonth()
    rn_time = time.clock()
    print(f"Today is {today_date} and the time is {rn_time}.")
    print("")#Just adding space between each function

#How many times the letter a is repeated in a given word
def find_the_letter():
    user_word = input("Please enter a word. >> ")#getting the word
    a_count = list(str.lower(user_word))#putting the word into a list and removing the caps(if any)
    all_the_a = a_count.count("a")#counting how many time 'a' appears in the list
    print(f"the amount of times 'a' shows up in your word is {all_the_a}.")
    print("")#Just adding space between each function





main()
