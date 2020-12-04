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

    # Returns a string that represents the shape using lines of "*"
    def get_picture(self):
        pictureString = ''

        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        for lineHeight in range(self.height):
            pictureString += ("*" * self.width ) + "\n"
        
        return pictureString

    # get_amount_inside
    # Returns the number of times the passed in shape could fit inside the shape (with no rotations)
    # {attemptShapInside} (Rectangle) = shape to fit inside
    def get_amount_inside(self, attemptShapInside):
        horizontalTransitions = 0
        verticalTransitions = 0

        horizontalTransitions = (self.width / attemptShapInside.width) // 1
        verticalTransitions = (self.height / attemptShapInside.height) // 1

        return int(horizontalTransitions * verticalTransitions)



class Square(Rectangle):
    # default constructor 
    def __init__(self, sideLength): 
        super().__init__(sideLength, sideLength)
    
    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)

