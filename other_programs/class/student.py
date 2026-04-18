class Student :
    def __init__(self,r,n,s):
        self.rollNum=r
        self.name=n
        self.stream=s

    def setMarks(self,m):
        self.marksList=m

    def getStream(self):
        return self.stream
    
    def percentage(self):
        sum_marks=0
        for i in self.marksList:
            sum_marks+=i
        self.perc=round(sum_marks*0.2,2)
        return self.perc
    
    def gradeGen(self):
        grade=[]
        for i in self.marksList:
            if i>=90:
                grade.append('A')
            elif i>=80:
                grade.append('B')
            elif i>=65:
                grade.append('C')
            elif i>=40:
                grade.append('D')
            else:
                grade.append('E')
        return grade

    def division(self):
        if self.perc>=60:
            return 'I'
        elif self.perc>=50:
            return 'II'
        else:
            return 'III'

s=Student(12,'Alice','S')
print(s.setMarks([90,89,97,95,98]))
print(s.getStream())
print(s.percentage())
print(s.gradeGen())
print(s.division())