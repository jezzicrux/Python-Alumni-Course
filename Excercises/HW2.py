#Getting the average vaules on each number set
average_number_set1=(44+64+88+53+89)/5
average_number_set2=(39+45+55+90+95+96)/6
average_number_set3=(54+(-45)+(-10)+90)/4
average_number_set4=(55+65+75+95+32)/5
#Displaying the average along with a statement using the f-string
print(f"The average of 5 given numbers is: {average_number_set1}")
print(f"The average of 6 given numbers is: {average_number_set2}")
print(f"The average of 4 given numbers is: {average_number_set3}")
print(f"The average of 5 given numbers is: {average_number_set4}")

#Finding even and odd for the following numbers: 9, 19, and 20
x = [9,19,20]
#Have a if statement run through a loop set by the list (x)
for a in range (0,3):
    if x[a]%2 == 0:
        print("even")
    else:
        print("odd")
