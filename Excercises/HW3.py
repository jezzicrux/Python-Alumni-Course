#A mimi "magic game" The program greets the user and ask if they believe in magic.
#If they don't the game states the users favoirte color. If they believe, it goes to the guessing game.
#Then the user enters a number. The program guesses wrong and then guesses the right number.
#The program ask if they right and if the say they aren't, the program calls them a lier
from sys import argv
import time
script, name, fav_color = argv
pause = '.....'
print(f"Well hello there {name}. Welcome to wonderful magic game")
time.sleep(1) #Making pauses between the text
print(f"So can I ask you something? Do you believe in magic? Yes or No")
believer=input('>>')
if believer == 'yes' or believer == 'Yes':
    print(f"Really!? Oh I'm so glad!")
else:
    print(f"Oh really? Well I can show you some magic right now")
    time.sleep(1) #Making pauses between the text
    print(f"I know that your favoirte color is")
    """This is to make the dot appear one after another,
    but I'm still working on getting them on the same line"""
    for char in pause:
        print (char)
        time.sleep(0.3) #Making pauses between the dots
    mag_fav_color = str.upper(fav_color)
    print(f"{mag_fav_color}!")
    time.sleep(0.5)
    print(f"Cool right?")
time.sleep(1)#Making pauses between the text
print(f"But lets play a game {name}. Pick a number from 1-10. I won't look. I promise")
guess_numb=int(input('>>'))
while guess_numb <= 10:
    try:
        print(f"You picked your number? Now let me guess.")
        for char in pause:
            print (char)
            time.sleep(0.3)
        wrong_guess = guess_numb-2
        print(f"Is you number {wrong_guess}?")
        time.sleep(0.8)
        print(f"No...your number is {guess_numb}! Right?")
        honesty = input('>>')
        if str.lower(honesty) == 'yes' or str.lower(honesty) == 'yep' or str.lower(honesty) == 'yea':
            print(f"See. Told you I could do magic")
            guess_numb=11
        else:
            time.sleep(0.8)
            print(f"It's not nice to lie {name}")
            guess_numb=11
    except:
        print(f"Please enter a real number")
time.sleep(1)
print(f"Still not buying my powers? I will give you a fortune reading.")
time.sleep(1)
print(f"It takes up a lot of power so I can only do it once.")
time.sleep(1)
print(f"So what's you sign {name}?")
zodiac = input(">>")
if str.lower(zodiac) == 'aries':
    print("If you're trying to get your finances together, today might not be the best day for it.")
elif str.lower(zodiac) == 'taurus':
    print("A surprising phone call might come today from a close friend or business or romantic partner.")
elif str.lower(zodiac) == 'gemini':
    print("An unexpected development could throw you into a tailspin, but keep calm and all will be well.")
elif str.lower(zodiac) == 'cancer':
    print("Group activities could escalate almost to a frenzy, but just focus on your part.")
elif str.lower(zodiac) == 'leo':
    print("You could receive a phone call from a friend or relative you haven't seen in a long time.")
elif str.lower(zodiac) == 'virgo':
    print("News about changes in your neighborhood could throw your community for a loop. Be strong.")
elif str.lower(zodiac) == 'libra':
    print("Technology could set a personal or job-related project back for you today. \nDon't lose your temper.")
elif str.lower(zodiac) == 'scorpio':
    print("Large social gatherings, perhaps group events or festivals, \ncould put you in the middle of an agitated crowd.")
elif str.lower(zodiac) == 'sagittarius':
    print("Too many demands upon you could have you feeling a bit on edge today. \nIt's a great day to go for a workout or get out in the open if weather permits.")
elif str.lower(zodiac) == 'capricorn':
    print("A speech or lecture you hear or read could cause your way of thinking to be suddenly and drastically altered.\nConsider it objectively and you'll realize that it isn't all that drastic a change.")
elif str.lower(zodiac) == 'aquarius':
    print("Some rather shocking information could affect your current living situation and cause some upset in your household today. \nCalm everyone down and view the situation objectively.")
elif str.lower(zodiac) == 'pisces':
    print("A phone call from another state or country could bring some astounding information your way today.")
else:
    print("I guess you don't want your fortune read.")
time.sleep(1)
print(f"Well, I'm all magic out. Bye {name}. Until next time")
