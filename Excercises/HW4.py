def main():
    numb_pick()
    even_odd(4)
    even_odd(524)
    even_odd(56563)
    even_odd(465634)
    even_odd(3423)

def numb_pick():
    print ("Enter any number to see if it's a Prime number.")
    a = int(input(">>"))
    prime_num(a)

#This function is to see if the users number is a prime number
def prime_num(a):
    #The following does the "math" to find a prime number.
    #First it makes sure the input number is greater then 1 by divieding the input number by 2, 3, 5, 7, or 9
    #Then if the vaule is greater then 1 it makes sure the remainder isn't 0 when divied the input number by 2, 3, 5, 7, or 9
    #This is show that the user number can be divied by another number then itself
    #The reson we don't 4, 6, 8 is they are already divisible by 2
    if ((a/2) >1 and a % 2 == 0) or ((a/3) >1 and a % 3 == 0) or ((a/5) >1 and a % 5 == 0) or ((a/7) >1 and a % 7 == 0) or ((a/9) >1 and a % 9 == 0):
        print(f"{a} is not a Prime number.")
    else:
        print(f"{a} is a Prime number.")


#Finding even and odd for 5 arguments.
def even_odd(x): #X is the parameter
    if x%2 == 0:
        print("even")
    else:
        print("odd")

main()
