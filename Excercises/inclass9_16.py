#Making a function the adds three number and divdes by 3. (Pretty much average)
#This the function to get the average of the three numbers
avg = 0
def average(x,y,z):
    avg=(x+y+z)/3
    print(f"The average the three numbers is {avg}.")

def getting_numbs():
    print ("Please enter your first number")
    x = int(input(">>"))
    print ("Please enter your second number")
    y = int(input(">>"))
    print ("Please enter your third number")
    z = int(input(">>"))
    average(x,y,z)

getting_numbs()
