import math
#1
class InpOut:
    def __init__(self):
        self.s=''
    def inp(self):
        self.s= input("Enter:")
    def out(self):
        print(self.s.upper())
str=InpOut()
str.inp()
str.out()



#2
class shape:
    def area(self):
        return 0
class square(shape):
    def __init__(self):
        self.lenght=int(input("Enter side lenght:"))
    def area(self):
        return self.lenght*self.lenght
square =square()
print("area: ", square.area())

#3
class rect(shape):
    def __init__(self):
        self.lenght= int(input("Enter lenght: "))
        self.witdh= int(input("Enter witdh: "))
    def area(self):
        return self.witdh*self.lenght
rect=rect()
print("Rect Area:",rect.area())

#4 if under "point" u mean => (x;y) then:
class point:
    def __init__(self):
        self.x=int(input("Enter X coordinate:"))
        self.y=int(input("Enter Y coordinate:"))
    def show(self):
        print(f"Point({self.x,self.y})")
    def move(self):
        self.addX=int(input("Change pos by X:"))
        self.addY=int(input("Change pos by Y:"))
        self.x+=self.addX
        self.y+=self.addY
        return self.x,self.y
    def dist(self):
        self.x2=int(input("Coordinate X of second point:"))
        self.y2=int(input("Coordinates Y of second point:"))
        self.distX=(self.x-self.x2)**2
        self.distY=(self.y+self.y2)**2
        return math.sqrt(self.distX+self.distY)
point=point()
point.show()
print("Ur point moved, new coordinates:", point.move())
print("Distance between ur points is: ", point.dist())

#5


