class Rectangle:
    def __init__(self,l,b):
        self.len=l
        self.br=b
    def setLength(self,l):
        self.len=l
    def setBreadth(self,b):
        self.br=b
    def getLength(self):
        return self.len
    def getBreadth(self):
        return self.br
    def area(self):
        return self.len*self.br
    def peri(self):
        return 2*(self.len+self.br)
r1=Rectangle(10,2) #length=10,breadth=2
print(r1.area()) #20
print(r1.peri()) #24
print(r1.setLength(12)) #length=12
print(r1.area()) #24