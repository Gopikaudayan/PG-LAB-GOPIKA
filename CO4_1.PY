class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
        self.area=self.l*self.b
        self.p=2*(self.l+self.b)
    def display(self):
        print("AREA OF RECTANGLE:",self.area)
        print("PERIMETER OF RECTANGLE:",self.p)

p1=Rectangle(2,2)
p2=Rectangle(6,4)

print("RECTANGLE1")
p1.display()
print("RECTANGLE2")
p2.display()

if p1.area>p2.area:
    print("LARGEST AREA",p1.area,)
else:
    print("LARGEST",p2.area)
