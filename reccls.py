class Rectangle:
    def __init__(self,len,brd):
        self.l = len
        self.b = brd
        
    def area(self):
        return self.l * self.b
    def peri(self):
        return 2 * (self.l + self.b)
    
x = Rectangle (10,5)
y = Rectangle (12,4)

if x.area() == y.area():
    print ("Both are Equal")
else:
    print ("Not Equal")
        