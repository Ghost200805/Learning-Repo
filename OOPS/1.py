class Rectangle():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_area(self):
        return self.width *  self.height

obj = Rectangle(10,10,100,100).get_area()
print (obj)

class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def print(self):
        return f"X:{self.x} Y:{self.y}"

print(Vector(10,20).print())
