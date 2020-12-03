class Rectangle:
    # default constructor 
    def __init__(self, width, height): 
        self.width = width
        self.height = height

    def __str__(self):
         return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width
    
    def get_perimeter(self):
        return (self.height * 2) + (self.width * 2)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        pass #TODO: not implemented

    def get_amount_inside(self):
        pass #TODO: not implemented



class Square(Rectangle):
    # default constructor 
    def __init__(self, sideLength): 
        super().__init__(sideLength, sideLength)
    
    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)

    def __str__(self):
        return f'Square(side={self.width})'



rect = Rectangle(5, 3)
rect.set_width(9)
print(rect)
print(rect.get_diagonal())

print(Square(2))
