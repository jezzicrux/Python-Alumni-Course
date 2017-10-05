import time

def main():
    #wordcounter()
    #da_count()
    #even_odd()
    #wordcount_no_len()
    letter_shows()

#Assignment 14. This function will count a users input
def wordcounter():
    print("Welcome to the word counter game")
    print("Please enter a word and we'll count it")
    da_word = input(">>")
    print (f"The lenght of {da_word} is {len(da_word)}.\n")

#Assignment 15. Count down
def da_count():
    print ("Hello there. I am the Count and I love to count.\nLet's count down from 20\n")
    a = 20
    time.sleep(2)
    while a >=0:
        print(a)
        a = a-1
        time.sleep(1)

#Assignment 16. Even and Odd
def even_odd(): #X is the parameter
    print ("Please enter a number to see if it's even or odd")
    x = int(input(">>"))
    if x%2 == 0:
        print("even")
    else:
        print("odd")

#Assignment 17. Count word WITHOUT len
def wordcount_no_len():
    print("Welcome to the word counter game. AGAIN!!!")
    print("Please enter a word and we'll count it")
    a_word = input(">>")
    a=0
    for letters in a_word:
        a = a+1
    print(f"The number of charters of {a_word} is {a}.")

#Assignment 18. count the letters
def letter_shows():
    print("Welcome to the Letter Show!!!")
    print("Please enter a word and we'll show each letter")
    word = input(">>")
    a=0
    for letters in word:
        print (word[a])
        a = a+1

main()
