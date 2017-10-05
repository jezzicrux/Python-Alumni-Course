#Making a class called shapes. Using a,b,c,d as arguments the the four sides
class shapes:
    def __init__(self,l,w):
        self.base = l
        self.height = w
    #Making a perimeter method to find the perimeter
    def perimeter(self):
        perim = (2*self.base)+(2*self.height)
        print (f"The Perimeter of your shape is {perim}\n")
    #Making a area method to find the area
    def area(self):
        are = self.base*self.height
        print (f"The Area of your rectengle is {are}\n")

rectengle1 = shapes(2,3)
rectengle1.perimeter()
rectengle1.area()

rectengle2 = shapes(5,3)
rectengle2.perimeter()
rectengle2.area()

rectengle3 = shapes(1,8)
rectengle3.perimeter()
rectengle3.area()

rectengle4 = shapes(9,12)
rectengle4.perimeter()
rectengle4.area()
