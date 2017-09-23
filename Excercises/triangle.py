def main():
    print(f"Welcome to the triangle finder program")
    print(f"Please enter 3 values for each side.")
    print(f"Enter in value for side 1")
    side1 = int(input(">> "))
    print(f"Enter in value for side 2")
    side2 = int(input(">> "))
    print(f"Enter in value for side 3")
    side3 = int(input(">> "))
    triangle_check(side1,side2,side3)

def triangle_check(a,b,c):
    if (a+b > c) and (a+c > b) and (b+c > a) and (((a**2) + (b**2)) == (c**2)):
        print(f"All your sides can make a triangle! ALRIGHT!!!! Get it?")
    elif (a+b > c) and (a+c > b) and (b+c > a) and (((a**2) + (b**2)) > (c**2)):
        print(f"Look at your triangle. It's a cutie")
    elif (a+b > c) and (a+c > b) and (b+c > a) and (((a**2) + (b**2)) < (c**2)):
        print(f"Your triangle is so obtuse")
    elif (a+b == c) or (a+c == b) or (c+b == a):
        print("YOUR TRIANGLE IS OUT OF CONTROL. IT'S A REAL DEGENERATE!!")
    else:
        print("You aint got nutin' son!")


main()
