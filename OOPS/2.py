# Inheritance 

class Shapes():
    def __init__(self,color):
        self.color = color


class Rectangle(Shapes):
    def __init__(self,x,y,width,height,color):
        super().__init__(color)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_area(self):
        return self.width *  self.height # Abstraction - User doesnt know what formula or whatever is happening , he is just getting his area...

obj = Rectangle(10,10,100,100).get_area()
print (obj)