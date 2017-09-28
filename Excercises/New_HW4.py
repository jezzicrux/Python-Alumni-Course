def main():
    numb_pick()
    print("")
    byte_size()

#This function is to ask the user to enter their number to see if its a prime number
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


#Convertion program
#Convert from kilobytes to bytes
#Convert from mega byte to byte
#Convert from terabyte to byte
#Convert from terabyte to megabyte.
def byte_size():
    print("Welcome to the Byte Size Program.")
    print("Please pick the following:\n")
    print("Press 1 to convert from Kilobyte to byte")
    print("Press 2 to convert from Megabyte to byte")
    print("Press 3 to convert from Terabyte to byte")
    print("Press 4 to convert from Terabyte to Megabyte")
    #Make a conditional for each option. Also added a try except to handle type error
    try:
        pick = int(input(">>")) #The user selection
        if pick == 1:
            print("Please enter the amount in Kilobyte:")
            kilo = int(input(">>"))
            byte_kilo = kilo * (10**3) #one kilobyte = 10^3 bytes
            print(f"{kilo} Kilobyte(s) is {byte_kilo} bytes.")
        elif pick == 2:
            print("Please enter the amount in Megabyte:")
            mega = int(input(">>"))
            byte_mega = mega * (10**6) #one megabyte = 10^6 bytes
            print(f"{mega} Megabyte(s) is {byte_mega} bytes.")
        elif pick == 3:
            print("Please enter the amount in Terabyte:")
            tera = int(input(">>"))
            byte_tera = tera * (10**12) #one terabyte = 10^12 bytes
            print(f"{tera} Terabyte(s) is {byte_tera} bytes.")
        elif pick == 4:
            print("Please enter the amount in Terabyte:")
            mtera = int(input(">>"))
            mega_mtera = mtera * (10**6) #one tera = 10^6 megabytes
            print(f"{mtera} Terabyte(s) is {mega_mtera} megabytes.")
        else:
            print("Please enter 1, 2, 3, or 4\n")
            byte_size()
    except ValueError:
        print("Please enter a numerical value.\n")
        byte_size()

main()
