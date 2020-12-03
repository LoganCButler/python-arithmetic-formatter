class Rectangle:
    # default constructor 
    def __init__(self, width, height): 
        self.width = width
        self.height = height

    def __str__(self):
         return f'width:{self.width} height:{self.height}'



class Square(Rectangle):
    # default constructor 
    def __init__(self, sideLength): 
        super().__init__(sideLength, sideLength)




rect = Rectangle(5, 3)
print(rect)
