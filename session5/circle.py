class circle:
    pi = 3.141
    def __init__(self,radius,color):
        self.radius = radius
        self.color = color
    def getColor(self): #returns the color of the circle
        return (self.color)
    def getCircum(self): #returns the circumference of the circle
        return (2*self.pi*self.radius)
    
#testing below
C = circle(3,"blue")
print(C.getColor())
print(C.getCircum())
