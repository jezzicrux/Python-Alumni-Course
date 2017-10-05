class Point():
    def __init__(self, x, y):
        self.firstpoint = x
        self.secondpoint = y

    def point_dis(self):
        print(f"x:{self.firstpoint}\ny:{self.secondpoint}")

cord = Point(3,4)
cord.point_dis()

class rectangle:
    def __init__(self,l,w):
        self.width = l
        self.height = w

    #Making a area method to find the area
    def area(self):
        are = self.width*self.height
        print (f"The Area of your rectangle is {are}\n")

total_area = rectangle(3,7)
total_area.area()
